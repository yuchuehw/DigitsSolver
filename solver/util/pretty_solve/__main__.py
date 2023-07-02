"""
Digits Game Solver

This module provides a command-line interface to solve the Digits game. The Digits game is a mathematical
puzzle where the goal is to reach a target number by performing arithmetic operations on a list of given numbers.
The module uses the concurrent.futures module to execute the solver in a separate thread, allowing for real-time
interaction with the solutions.

Usage:
    1. Run the script from the command line.
    2. Enter the numbers allowed, separated by spaces.
    3. Enter the target number.
    4. Use the Enter key to loop through possible solutions.
    5. Press Ctrl+C to exit the program.

Note: The module requires the 'solver' package to be installed, which contains the 'solver' module with the
implementation of the DigitSolver class.

Author: Yu-Chueh Wang
Version: 1.7.1

"""

import concurrent.futures
import os
import sys

## temporary implementation ##
path = os.path.abspath(__file__).split("/")
path.pop()
path.pop()
path.pop()
path.pop()
sys.path.append("/".join(path))
## temporary implementation ##

from solver.solver import DigitSolver

Executor = concurrent.futures.ThreadPoolExecutor


def main() -> None:
    """
    Main function to run the Digits game solver.

    This function prompts the user for inputs, initializes the DigitSolver,
    and starts the solver process. It allows the user to loop through possible solutions
    by pressing the enter key and exits the program on Ctrl+C.

    Returns:
        None
    """
    os.system("clear")
    holding_list = []

    def mf(step: list) -> None:
        """
        Custom printer function to store steps in the holding list.

        Args:
            step (list): A list of steps to solve the Digits game.

        Returns:
            None
        """
        holding_list.append(step)

    def alternative_input(prompt: str = "") -> str:
        """
        Function to handle user input with KeyboardInterrupt support.

        Args:
            prompt (str, optional): The input prompt. Defaults to "".

        Returns:
            str: The user's input string.
        """
        try:
            input_ = input(prompt)
        except KeyboardInterrupt:
            print()
            print("Program exited!")
            exit()
        return input_

    def get_integer_list_input(prompt: str) -> list:
        """
        Function to get a list of integers from user input.

        Args:
            prompt (str): The input prompt.

        Returns:
            list: A list of integers entered by the user.
        """
        while True:
            input_str = alternative_input(prompt)
            number_list = input_str.split()
            valid_numbers = []
            for num in number_list:
                try:
                    valid_numbers.append(int(num))
                except ValueError:
                    print(
                        f"Invalid input: {num}. Please enter integers separated by spaces."
                    )
                    break
            if len(valid_numbers) == len(number_list):
                return valid_numbers

    def get_integer_input(prompt: str) -> int:
        """
        Function to get an integer from user input.

        Args:
            prompt (str): The input prompt.

        Returns:
            int: The integer entered by the user.
        """
        while True:
            input_str = alternative_input(prompt)
            try:
                return int(input_str)
            except ValueError:
                print(f"Invalid input: {input_str}. Please enter an integer.")

    number_list = []
    while not number_list:
        number_list = get_integer_list_input(
            "Enter numbers allowed separated by space: "
        )
        if not number_list:
            print("Invalid input. Please enter at least one valid integer.")

    os.system("clear")
    target = get_integer_input("Enter the target number: ")
    os.system("clear")

    solver = DigitSolver(number_list, target)
    solver.printer = mf

    with Executor() as executor:
        future = executor.submit(solver.solve)
        print(
            "Use the enter key to loop through possible solutions. Press <Ctrl>+C to exit."
        )
        while True:
            try:
                input()
                os.system("clear")
            except KeyboardInterrupt:
                print("Program end.")
                break
            if holding_list:
                holding_list.sort(key=lambda o: len(o))
                print("Possible solution:")
                print(*holding_list.pop(0), sep="\n")
            elif future.done():
                print("Computation has stopped.")
                print(f"{future.result()} solutions found.")
                break
            else:
                print("Calculating, please wait...")


if __name__ == "__main__":
    main()
