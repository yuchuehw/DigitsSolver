"""
Digits Game Solver

This module provides a command-line interface to solve the Digits game. 
The Digits game is a mathematical puzzle where the goal is to reach a target number
by performing arithmetic operations on a list of given numbers.
The module uses the concurrent.futures module to execute the solver in a separate
thread, allowing for real-time interaction with the solutions.

Usage:
    1. Run the script from the command line.
    2. Enter the numbers allowed, separated by spaces.
    3. Enter the target number.
    4. Use the Enter key to loop through possible solutions.
    5. Press Ctrl+C to exit the program.

Note: The module requires the 'solver' package to be installed, 
which contains the 'solver' module with the
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
    and starts the solver process.
    It allows the user to loop through possible solutions
    by pressing the enter key and exits the program on Ctrl+C.

    Returns:
        None
    """
    os.system("clear")
    holding_list = []
    number_list = get_number_list_from_user()
    target = get_target_from_user()

    solver = initialize_solver(number_list, target)
    solver.printer = holding_list.append

    with Executor() as executor:
        future = executor.submit(solver.solve)
        print_instructions()
        while True:
            try:
                input()
                os.system("clear")
            except KeyboardInterrupt:
                print("Program end.")
                break
            if holding_list:
                print_solution(holding_list)
            elif future.done():
                print_computation_result(future)
                break
            else:
                print("Calculating, please wait...")


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
        sys.exit()
    return input_


def get_number_list_from_user() -> list:
    """
    Function to get a list of integers from user input.

    Returns:
        list: A list of integers entered by the user.
    """
    while True:
        input_str = alternative_input("Enter numbers allowed separated by space: ")
        number_list = input_str.split()
        valid_numbers = []
        for num in number_list:
            try:
                valid_numbers.append(int(num))
            except ValueError:
                print(f"Invalid input: {num}. Please enter integers separated by spaces.")
                break
        if len(valid_numbers) == len(number_list):
            return valid_numbers

        print("Invalid input. Please enter at least one valid integer.")


def get_target_from_user() -> int:
    """
    Function to get the target number from user input.

    Returns:
        int: The target number entered by the user.
    """
    while True:
        input_str = alternative_input("Enter the target number: ")
        try:
            return int(input_str)
        except ValueError:
            print(f"Invalid input: {input_str}. Please enter an integer.")


def initialize_solver(number_list: list, target: int) -> DigitSolver:
    """
    Function to initialize the DigitSolver with user inputs.

    Args:
        number_list (list): The list of numbers allowed.
        target (int): The target number.

    Returns:
        DigitSolver: An instance of the DigitSolver initialized with the user inputs.
    """
    return DigitSolver(number_list, target)


def print_instructions() -> None:
    """
    Function to print the instructions for using the solver.

    Returns:
        None
    """
    print("Use the enter key to loop through possible solutions.")
    print("Press <Ctrl>+C to exit.")


def print_solution(holding_list: list) -> None:
    """
    Function to print a possible solution from the holding list.

    Args:
        holding_list (list): The list of possible solutions.

    Returns:
        None
    """
    print("Possible solution:")
    print(*holding_list.pop(0), sep="\n")


def print_computation_result(future: concurrent.futures.Future) -> None:
    """
    Function to print the computation result from the future object.

    Args:
        future (concurrent.futures.Future): The future object representing the computation.

    Returns:
        None
    """
    print("Computation has stopped.")
    print(f"{future.result()} solutions found.")


if __name__ == "__main__":
    main()
