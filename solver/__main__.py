"""
This module provides a command-line interface for solving the New York Times' 
Digits game using the DigitSolver class.

Usage:
    python solver [starting_digits] [target_digit] [-os]

Arguments:
    starting_digits (int): Numbers allowed in the game.
    Must be provided as separate integer values.
    target_digit (int): Target number that needs to be achieved.
    -os, --onesolution: Optional flag to find only one solution.
    By default, all solutions are found.

Example:
    python main.py 3 12 15 20 23 25 439

    This command runs the DigitSolver with starting digits [3, 12, 15, 20, 23, 25]
    and target digit 439,
    finding all solutions to the game.

Console Mode:
    If no command-line arguments are provided,
    a demo of using the DigitSolver class as an import will be displayed.

    Here's the full code:

    ```
    from solver import DigitSolver

    solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
    solution_count = solver.solve(False)
    print(f"we found {solution_count} solution(s)")
    ```

    The result will be printed, showing the number of solutions found.
"""

import argparse
import sys
from solver import DigitSolver


def main():
    """
    Main function for running the Digits game solver.

    This function parses the command-line arguments,
    creates an instance of the DigitSolver class,
    and prints the number of solutions found for the game.

    Command-line Arguments:
        - starting_digits (int): Numbers allowed in the game.
        - target_digit (int): Target number that needs to be achieved.
        - -os, --onesolution: Optional flag to find only one solution.
        By default, all solutions are found.

    Returns:
        None

    Raises:
        None
    """
    parser = argparse.ArgumentParser(description="New York Times' Digits solver")
    parser.add_argument(
        "starting_digits",
        metavar="N",
        type=int,
        nargs="+",
        help="numbers(int) allowed in the game",
    )
    parser.add_argument(
        "target_digit", metavar="n", type=int, nargs=1, help="target number(int)"
    )
    parser.add_argument(
        "-os",
        "--onesolution",
        dest="one_solution",
        action="store_true",
        help="find only 1 solution (default:find all solution)",
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
        print(
            """here's the full code:

  from solver import DigitSolver
  solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
  solution_count = solver.solve(False)
  print(f"we found {solution_count} solution(s)")

here's the result:
        """
        )
    solver = DigitSolver(starting_digits, target_digit)
    solution_count = solver.solve(one_solution)
    print(f"we found {solution_count} solution(s)")
    if not sys.argv[1:]:
        print("we also support CLI mode use [-h] to learn more.")


if __name__ == "__main__":
    main()
