"""
This is a test file that is used to test the functionality of the `DigitSolver` class in `solver.py`.
It contains multiple test cases to validate different scenarios of solving digit puzzles. The main usage
of this file is to run the tests using pytest by executing `pytest test.py`.

Note:
-----
1. Additional test cases can be added to this file to further test the `DigitSolver` class.
2. Do not relocate or move this file, as it is being used by the workflow.

Example Usage:
--------------
To run the tests using pytest, execute the following command in the terminal:
    pytest test.py

"""

from solver.solver import DigitSolver


def test_solve_single_solution():
    """
    Test case to validate the solving of a puzzle with a single solution.

    The test creates a `DigitSolver` object with the provided digits and target value.
    It then calls the `solve()` method and asserts that at least one solution is found.

    """
    solver = DigitSolver([8, 11, 13, 18, 23, 24], 407)
    solution_found = solver.solve()
    # Assert that at least one solution is found
    assert solution_found > 0


def test_solve_multiple_solutions():
    """
    Test case to validate the solving of a puzzle with multiple solutions.

    The test creates a `DigitSolver` object with the provided digits and target value.
    It then calls the `solve()` method and asserts that multiple solutions are found.

    """
    solver = DigitSolver([2, 4, 6, 8], 12)
    solution_found = solver.solve()
    # Assert that multiple solutions are found
    assert solution_found > 1


def test_solve_no_solution():
    """
    Test case to validate the handling of a puzzle with no solution.

    The test creates a `DigitSolver` object with the provided digits and target value.
    It then calls the `solve()` method and asserts that no solution is found.

    """
    solver = DigitSolver([1, 2, 3, 4], 100)
    solution_found = solver.solve()
    # Assert that no solution is found
    assert solution_found == 0
