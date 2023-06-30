from itertools import combinations
import operator
import time
import warnings

OPERATIONS = {
    "+": operator.add,
    "−": operator.sub,
    "×": operator.mul,
    "÷": operator.truediv,
}


class DigitSolver:
    def __init__(self, starting_digits: iter, target_digit: int):
        """
        Create a DigitSolver object to solve the Digits game.

        Args:
            starting_digits (iterable): An iterable containing the starting digits of the game (preferably a list).
            target_digit (int): The target digit of the puzzle.

        Returns:
            DigitSolver object: An instance of the DigitSolver class.

        Warnings:
            - Throws a warning if there is no solution or if the game is already solved.

        Raises:
            - TypeError: If the starting_digits cannot be sorted using the `sorted` function.
            - ValueError: If the starting_digits are not integers or if they are not in a 1-dimensional format.
            - ValueError: If the target_digit is not an integer or if it is smaller than 0.
        """

        if not isinstance(target_digit, int) or target_digit < 0:
            raise ValueError(
                "Invalid target_digit value. It must be a positive integer."
            )

        try:
            starting_digits = sorted(starting_digits)
        except Exception:
            raise TypeError("starting_digits must be a iter and applied to sorted()")

        if not all(isinstance(digit, int) for digit in starting_digits):
            raise ValueError("members of starting_digits must be integers")

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
            warnings.warn("No Solution Warning. (Target too big!)")

    def _already_solved_check(self) -> None:
        if self._target_digit in self._starting_digits:
            self._already_solved = True
            warnings.warn("Puzzle is already Solved. (Target in starting_digit)")

    def printer_setter(self, function: callable) -> None:
        """
        Customizes and replaces the pretty print function with the specified function. The DigitSolver class always calls this function with one argument, steps, which is a list of steps to solve the problem.

        Args:
        function (callable): A callable function to set as the pretty print function.

        Returns:
        None: Sets the pretty print function to the specified function.

        Raises:
        TypeError: If the provided function is not callable.
        """
        if not collable(function):
            raise TypeError("function must be a callable object")
        self._printer = function
        return

    def _calc_answer(
        self,
        numbers: list,
        target: int,
        step: list,
        discovered: set,
        solutions: list,
        tasks: list,
    ) -> None:
        """
        Calculates the solution for the Digits game and prints the steps.

        Args:
        numbers (list): A sorted list of usable numbers at each position.
        target (int): The target number to reach.
        steps (list): A list of previous steps to reach the current position (empty initially).
        discovered (set): A set of discovered position(sorted tuples).
        solutions (list): A 2d list of found solutions(set version of steps).
        sorted by solution length(eg:one step->0 two->1 ...).
        tasks (list): A queue for tree search.

        Returns:
        None: Prints the steps of the solution if found.
        (or run the self._printer if set.)

        Raises:
        None: No explicit exceptions are raised.
        """

        def que_recursive_call(
            numbers: list,
            target: int,
            step: list,
        ) -> None:
            """
            Stores the parameters for the next depth in a tuple and appends it to a list.

            Args:
            numbers (list): A sorted list of usable numbers at the next position.
            target (int): The target number to reach.
            steps (list): A list of previous steps to reach this newly discovered position.

            Returns:
            None: Stores the values to a list.

            Raises:
            None: No explicit exceptions are raised.
            """
            # if there's only one number left there's no need to find any further.
            if len(numbers) == 1:
                return

            tupled_numbers = tuple(numbers)
            if tupled_numbers in discovered:
                return
            discovered.add(tupled_numbers)
            tasks.append(
                (
                    numbers,
                    target,
                    step,
                    discovered,
                    solutions,
                )
            )

        def check_n_print(step: tuple) -> bool:
            """
            Detects if the solution is solved inefficiently by comparing it to previously computed solutions. Calls the pretty print function if the solution is efficient.

            Args:
            steps (list): A list of all steps to reach the solution.

            Returns:
            bool: True if the solution is efficient, False if it is inefficient.

            Raises:
            None: No explicit exceptions are raised.
            """
            frozen_step = frozenset(step)
            for x in range(len(step) - 1):
                for o in solutions[x]:
                    if o.issubset(frozen_step):
                        return False
            solutions[len(step) - 1].append(frozen_step)
            pretty_print(step)
            return True

        def pretty_print(step) -> None:
            """
            format the solution it found.

            Args:
            steps (list): A list of all steps to reach the solution.

            Returns:Prints the steps of the solution.
            (or run the self._printer if set.)

            Raises:
            None: No explicit exceptions are raised.
            """
            if not self._printer:
                print("solution found:", *step, "", sep="\n")
            else:
                self._printer(step)
            return

        def generate_new_step(step: list, op: str, num1: int, num2: int) -> tuple:
            """
            Generates a new step by appending the current step with the provided operator and numbers.

            Args:
            op (str): The operator string.
            num1 (int): The first number.
            num2 (int): The second number.

            Returns:
            list: The new step list.

            Raises:
            None: No explicit exceptions are raised.
            """
            return step + [f"{num1} {op} {num2} = {self._target_digit}"]

        # use combinations to generate two index.
        for i1, i2 in combinations(range(len(numbers)), 2):
            templist = numbers[:]
            # pop the index in the back first.
            num1, num2 = templist.pop(i2), templist.pop(i1)
            for op in OPERATIONS:
                # check for division by 0
                if op == "÷" and num2 == 0:
                    continue
                combined_num = OPERATIONS[op](num1, num2)
                if combined_num == target:
                    combined_num = int(combined_num)
                    new_step = generate_new_step(step, op, num1, num2)
                    check_n_print(new_step)

                elif combined_num >= 0 and int(combined_num) == combined_num:
                    combined_num = int(combined_num)
                    new_numbers = sorted(templist + [combined_num])
                    new_step = generate_new_step(step, op, num1, num2)
                    que_recursive_call(new_numbers, target, new_step)

    def solve(self, one_solution: bool = False) -> int:
        """
        Calls this function to start solving the puzzle.

        Args:
            one_solution (optional) (bool): If set to True, find only one solution.

        Returns:
            solutions_found (int): Number of solutions found.

        Raises:
            None: No explicit exceptions are raised.
        """
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
            discovered,
            solutions,
            odd_generation,
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

        return sum(len(x) for x in solutions)
