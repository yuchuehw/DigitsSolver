from itertools import combinations
import operator
import time
import warnings
import argparse
import sys

OPERATIONS = {
    "+": operator.add,
    "−": operator.sub,
    "×": operator.mul,
    "÷": operator.truediv,
}


class DigitSolver:
    def __init__(self, starting_digits: iter, target_digit: int):
        if not isinstance(target_digit, int) or target_digit < 0:
            raise TypeError(
              "Invalid target_digit value. It must be a positive integer."
            )

        try:
            starting_digits = sorted(starting_digits)
        except Exception:
            raise TypeError(
              "starting_digits must be a iter and applied to sorted()"
            )

        if not all(isinstance(digit, int) for digit in starting_digits):
            raise TypeError(
              "members of starting_digits must be integers"
            )

        self._starting_digits = starting_digits
        self._target_digit = target_digit
        self._printer = None
        self._has_no_solution = False
        self._already_solved = False
        self._no_solution_check()
        self._already_solved_check()

    def _no_solution_check(self) -> None:
        total_product = 1
        has_non_one_digit = False

        for digit in self._starting_digits:
            if digit > 1:
                total_product *= digit
                has_non_one_digit = True
            elif digit == 1:
                total_product += 1

        if not has_non_one_digit:
            total_product -= 1

        if total_product < self._target_digit:
            self._has_no_solution = True
            warnings.warn(
              "No Solution Warning. (Target too big!)"
            )

    def _already_solved_check(self) -> None:
        if self._target_digit in self._starting_digits:
            self._already_solved = True
            warnings.warn(
              "Puzzle is already Solved. (Target in starting_digit)"
            )

    def printer_setter(self, function: callable) -> None:
        self._printer = function

    def _calc_answer(
        self,
        numbers: list,
        target: int,
        step: list,
        counter_list: list,
        discovered: set,
        solutions: list,
        tasks: list
    ) -> None:
        def make_recursive_call(
            base_list: list,
            new_num: int,
            target_num: int,
            step: list,
            op: str,
            old_num1: int,
            old_num2: int
        ) -> None:
            new_num = int(new_num)
            next_base_list = base_list + [new_num]
            next_base_list.sort()
            temp = tuple(next_base_list)
            if temp in discovered:
                return
            discovered.add(temp)
            tasks.append((
                next_base_list,
                target_num,
                step + [f"{old_num1} {op} {old_num2} = {new_num}"],
                counter_list,
                discovered,
                solutions
            ))

        def pretty_print(step: list, op: str, num1: int, num2: int) -> None:
            step = step + [f"{num1} {op} {num2} = {self._target_digit}"]
            frozen_step = frozenset(step)
            for x in range(len(step) - 1):
                for o in solutions[x]:
                    if o.issubset(frozen_step):
                        return
            counter_list[0] += 1
            solutions[len(step) - 1].append(frozen_step)
            if not self._printer:
                print("solution found:", *step, "", sep="\n")
            else:
                self._printer(step)

        if len(numbers) == 1:
            return

        for i1, i2 in combinations(range(len(numbers)), 2):
            templist = numbers[:]
            num1, num2 = templist.pop(i2), templist.pop(i1)
            for op in OPERATIONS:
                if op == '÷' and num2 == 0:
                    continue
                combined_num = OPERATIONS[op](num1, num2)
                if combined_num == target:
                    pretty_print(step, op, num1, num2)
                elif combined_num >= 0 and int(combined_num) == combined_num:
                    make_recursive_call(
                        templist, combined_num, target, step, op, num1, num2
                    )

    def solve(self, one_solution: bool = False):
        if self._has_no_solution:
            return 0
        elif self._already_solved:
            if self._printer:
                self._printer(self._target_digit)
            else:
                print(f"solution found:\n{self._target_digit}")
            return 1

        counter_list = [0]
        solutions = [[] for x in range(len(self._starting_digits) - 1)]
        step = []
        discovered = set()
        even_generation = []
        odd_generation = []
        self._calc_answer(
            self._starting_digits,
            self._target_digit,
            step,
            counter_list,
            discovered,
            solutions,
            odd_generation
        )
        gen = 1
        # Wait for all tasks to complete with a timeout
        timeout = 5  # Timeout in seconds
        start_time = time.time()
        end_time = start_time + timeout
        remaining_time = end_time - time.time()
        while remaining_time > 0:
            # end early if one solution is found and only need one solution.
            if one_solution and counter_list[0] == 1:
                break
            # generation were broken into even or odd
            # you process either even or odd and store the next generation
            # in the oposite list.
            if gen % 2 == 0:
                processing = even_generation
                storing = odd_generation
            else:
                processing = odd_generation
                storing = even_generation
            if processing:
                self._calc_answer(*processing.pop(), storing)
            elif not processing and not storing:
                if not self._printer:
                  print("done:)")
                break
            else:
                gen += 1
            remaining_time = end_time - time.time()

        return counter_list[0]


def main():
    parser = argparse.ArgumentParser(
      description="New York Times' Digits solver")
    parser.add_argument('starting_digits', metavar='N', type=int, nargs='+',
                        help='numbers(int) allowed in the game')
    parser.add_argument('target_digit', metavar='n', type=int, nargs=1,
                        help='target number(int)')
    parser.add_argument('-os', "--onesolution", dest='one_solution',
                        action='store_true',
                        help='find only 1 solution (default:find all solution)'
                        )

    starting_digits = [3, 12, 15, 20, 23, 25]
    target_digit = 439
    one_solution = False
    if sys.argv[1:]:
        args = parser.parse_args()
        starting_digits = args.starting_digits
        target_digit = args.target_digit[0]
        one_solution = args.one_solution
    else:
        print("this is a demo of using solver.py as import")
        print("""here's the full code:

  from solver import DigitSolver
  solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
  solution_count = solver.solve(False)
  print(f"we found {solution_count} solution(s)")

here's the result:
        """)
    solver = DigitSolver(starting_digits, target_digit)
    solution_count = solver.solve(one_solution)
    print(f"we found {solution_count} solution(s)")
    if not sys.argv[1:]:
        print("we also support console mode use [-h] to learn more.")


if __name__ == "__main__":
    main()
