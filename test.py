from solver.solver import DigitSolver
def test_solve_single_solution():
    solver = DigitSolver([8, 11, 13, 18, 23, 24], 407)
    solution_found = solver.solve()
    # Assert that at least one solution is found
    assert(solution_found > 0)

def test_solve_multiple_solutions():
    solver = DigitSolver([2, 4, 6, 8], 12)
    solution_found = solver.solve()
    # Assert that multiple solutions are found
    assert(solution_found > 1)

def test_solve_no_solution():
    solver = DigitSolver([1, 2, 3, 4], 100)
    solution_found = solver.solve()
    # Assert that no solution is found
    assert(solution_found == 0)
