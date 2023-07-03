"""
The `solver.solver` module provides functionality to solve the Digits game.

The Digits game is a numerical puzzle where the objective is to reach a target digit by
combining a set of starting digits using basic arithmetic operations.

The module includes a `DigitSolver` class that can be used to solve the game
and find the solutions.

Usage:
    from solver.solver import DigitSolver

    # Create a DigitSolver object
    solver = DigitSolver(starting_digits, target_digit)

    # Solve the game and get the solutions
    solutions = solver.solve()

    # Print solution count
    print(f"{solutions} solution(s) found")

Author: Yu-Chueh Wang
Version: 1.7.0
"""

from itertools import combinations
import time
import warnings
from typing import List, Callable, Iterable


OPERATIONS = {
    "+": lambda i, j: i + j,
    "−": lambda i, j: i - j if i >= j else None,
    "×": lambda i, j: i * j,
    "÷": lambda i, j: i // j if j != 0 and i // j == i / j else None,
}


class TimeOutManager:
    """
    A class to manage timeouts.

    Attributes:
        end_time (float): The timestamp when the timeout period ends.

    Methods:
        has_time_out: Checks if the timeout period has elapsed.

    Example usage:
        timeout_manager = TimeOutManager(time_out_in=5)
        if timeout_manager.has_time_out():
            print("Timeout occurred!")
    """

    def __init__(self, time_out_in: int = 5):
        """
        Initializes the TimeOutManager object with a timeout duration.

        Args:
            time_out_in (int, optional): The timeout duration in seconds. Defaults to 5.

        Returns:
            None
        """
        self.end_time = time.time() + time_out_in

    def has_time_out(self) -> bool:
        """
        Checks if the timeout period has elapsed.

        Returns:
            bool: True if the timeout period has not elapsed, False otherwise.
        """
        return time.time() - self.end_time > 0

    def time_remain(self) -> int:
        """
        Checks if the time remains before timeout

        Returns:
            int: time left in second
        """
        return time.time() - self.end_time

class DigitSolver:
    """
    A class for solving the Digits game.

    Attributes:
        starting_digits (List[int]): A list of starting digits for the game.
        target_digit (int): The target digit of the puzzle.

    Methods:
        solve: Solves the Digits game and returns the solutions found.
        printer: Get or set the printer function used for pretty printing.

    Example usage:
        solver = DigitSolver([4, 8, 9, 12, 15, 18], 453)
        solutions = solver.solve()
    """

    def __init__(self, starting_digits: Iterable[int], target_digit: int):
        """
        Create a DigitSolver object to solve the Digits game.

        Args:
            starting_digits (Iterable[int]): An iterable containing the starting-
            digits of the game (preferably a list).

            target_digit (int): The target digit of the puzzle.

        Raises:
            ValueError: If the target_digit is not a positive integer.

            TypeError: If the starting_digits cannot be sorted using the
            `sorted` function.

            ValueError: If the starting_digits are not integers or
            if they are not in a 1-dimensional format.
        """
        if not isinstance(target_digit, int) or target_digit < 0:
            raise ValueError(
                "Invalid target_digit value. It must be a positive integer."
            )

        try:
            starting_digits = sorted(starting_digits)
        except TypeError as sorting_error:
            raise TypeError(
                "starting_digits must be an iterable and applicable to sorted()"
            ) from sorting_error

        if not all(isinstance(digit, int) for digit in starting_digits):
            raise ValueError("members of starting_digits must be integers")

        self._starting_digits: List[int] = starting_digits
        self._target_digit: int = target_digit
        self._printer: Callable[[List[str]], None] = lambda x: print(
            "solution found:", *x, "", sep="\n"
        )
        self._has_no_solution: bool = False
        self._already_solved: bool = False
        self._no_solution_check()
        self._already_solved_check()

    def _no_solution_check(self) -> None:
        """
        Checks if there is no solution for the puzzle.

        Raises a warning if there is no solution.
        """
        total_product: int = 1
        has_non_one_digit: bool = False

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
        """
        Checks if the puzzle is already solved.

        Raises a warning if the puzzle is already solved.
        """
        if self._target_digit in self._starting_digits:
            self._already_solved = True
            warnings.warn("Puzzle is already Solved. (Target in starting_digit)")

    @property
    def printer(self) -> Callable[[List[str]], None]:
        """
        Get the printer function used for pretty printing.

        Returns:
            Callable[[List[str]], None]: The current printer function.
        """
        return self._printer

    @printer.setter
    def printer(self, function: Callable[[List[str]], None]) -> None:
        """
        Set a custom printer function for pretty printing.

        The DigitSolver class always calls this function with one argument, `steps`,
        which is a list of steps to solve the problem.

        Args:
            function (callable): A callable function to set as the pretty print function.

        Raises:
            TypeError: If the provided function is not callable.
        """
        if not callable(function):
            raise TypeError("function must be a callable object")
        self._printer = function

    def _step_str(
        self, operator_: str, num1: int, num2: int, combined_num:int
    ) -> List[str]:
        """
        Generates a step strin by formatting the
        provided operator and numbers.

        Args:
            operator_ (str): The operator string.
            num1 (int): The first number.
            num2 (int): The second number.
            combined_num(int): the result of the operation

        Returns:
            List[str]: The new step list.
        """
        return f"{num1} {operator_} {num2} = {combined_num}"

    def _check_n_print(self, solutions: List[List[frozenset]], step: List[str]) -> bool:
        """
        Detects if the solution is solved inefficiently by comparing it to
        previously computed solutions.
        Calls the pretty print function if the solution is efficient.

        Args:
            solutions (List[List[frozenset]]): A 2d list of found solutions
            (set version of steps).
            step (List[str]): A list of all steps to reach the solution.

        Returns:
            bool: True if the solution is efficient, False if it is inefficient.
        """
        frozen_step = frozenset(step)
        for solution_length in range(len(step) - 1):
            for solution_ in solutions[solution_length]:
                if solution_.issubset(frozen_step):
                    return False
        solutions[len(step) - 1].append(frozen_step)
        self._printer(step)
        return True

    def _calc_answer(
        self,
        numbers: List[int],
        step: List[str],
        discovered: set,
        solutions: List[List[frozenset]],
    ) -> List[tuple]:
        """
               Calculates the answer by combining numbers using operations.

               Args:
                   numbers (List[int]): The list of numbers to combine.
                   step (List[str]): The current step to reach the solution.
                   discovered (set): The set of previously discovered solutions.
                   solutions (List[List[frozenset]]): A 2d list of found solutions

        (set version of steps).

               Returns:
                   List[tuple]: A list of tasks to be processed.
        """
        tasks = []
        for num1, num2 in combinations(range(len(numbers)), 2):
            templist = numbers[:]
            num1, num2 = templist.pop(num2), templist.pop(num1)
            for operator_, operation_ in OPERATIONS.items():
                combined_num = operation_(num1, num2)
                if combined_num == self._target_digit:
                    combined_num = int(combined_num)
                    new_step = step + [self._step_str(operator_,
                                                      num1,
                                                      num2,
                                                      self._target_digit)]
                    self._check_n_print(solutions, new_step)
                elif combined_num:
                    new_numbers = sorted(templist + [combined_num])
                    if len(new_numbers) == 1:
                        continue
                    if tuple(new_numbers) in discovered:
                        continue
                    discovered.add(tuple(new_numbers))
                    new_step = step + [self._step_str(operator_,
                                                      num1,
                                                      num2,
                                                      self._target_digit)]
                    next_gen = (new_numbers, new_step, discovered, solutions)
                    tasks.append(next_gen)
        return tasks

    def solve(self, one_solution: bool = False) -> int:
        """
        Solves the Digits game and returns the number of solutions found.

        Args:
            one_solution (bool, optional): If True, stops after finding one
            solution. Defaults to False.

        Returns:
            int: The number of solutions found.
        """
        if self._has_no_solution:
            return 0
        if self._already_solved:
            if self._printer:
                self._printer([self._target_digit])
            return 1

        solutions = [[] for _ in range(len(self._starting_digits) - 1)]
        step = []
        discovered = set()
        even_generation = []
        odd_generation = []

        tasks = self._calc_answer(
            self._starting_digits,
            step,
            discovered,
            solutions,
        )
        odd_generation.extend(tasks)
        gen = 1

        time_out_manager = TimeOutManager()

        while not time_out_manager.has_time_out():
            solution_count = sum(len(x) for x in solutions)
            if one_solution and solution_count == 1:
                break
            if gen % 2 == 0:
                processing = even_generation
                storing = odd_generation
            else:
                processing = odd_generation
                storing = even_generation
            if processing:
                tasks = processing.pop()
                storing.extend(self._calc_answer(*tasks))
            elif not processing and not storing:
                break
            else:
                gen += 1
        solution_count = sum(len(x) for x in solutions)
        return solution_count
