"""
The solver package provides functionality to solve the Digits game.

Modules:
- solver.py: Contains the DigitSolver class for solving the Digits game.
- __main__.py: Provides a command-line interface to run the Digits game solver.
- util module: Contains utility functions that complimant the DigitSOlver claass

To solve the Digits game, use the DigitSolver class from the solver module.
The solver.py module provides the necessary methods and logic to solve the
game by combining a set of starting digits using basic arithmetic operations.

The __main__.py module provides a convenient command-line interface to
interactively run the Digits game solver. It allows specifying the starting
digits and target digit as command-line arguments, and provides options to
find all solutions or only one solution.

The util module contains utility functions used by the solver,
such as input validation and solving via automation program.

Usage:
    # Import the DigitSolver class from the solver module
    from solver.solver import DigitSolver

    # Create a DigitSolver object and solve the game
    solver = DigitSolver(starting_digits, target_digit)
    solutions = solver.solve()

    # Run the solver as a standalone application
    python solver [starting_digits] [target_digit] [-os, --onesolution]

Author: Yu-Chueh Wang
Version: 1.7.0
"""
