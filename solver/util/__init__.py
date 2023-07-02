"""
solver.util

This module provides utility functions and classes used in the Digits solver 
application. It consists of two submodules: `solve_auto` and `pretty_solve`.

- `solve_auto`: Contains functions for automating the interaction with the Digits
game interface using Selenium WebDriver. It includes functions for clicking buttons,
reading puzzle information, combining numbers, and progressing through the puzzles
automatically.

- `pretty_solve`: Contains functions for displaying the solutions in a formatted and
visually appealing manner. It includes a function to print the steps of the solution
in a human-readable format.

Dependencies:
- Selenium WebDriver: Required for the `solve_auto` submodule.
- ChromeDriver: Required for the `solve_auto` submodule.

Note: Make sure to have the necessary dependencies installed and the ChromeDriver
executable in the system's PATH before using the `solve_auto` submodule.

Author: [Your Name]
Version 1.7.1
"""

