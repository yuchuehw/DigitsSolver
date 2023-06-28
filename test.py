def test_solve_single_solution():
    solver = DigitSolver([8, 11, 13, 18, 23, 24], 407)
    solver.solve()
    # Assert that at least one solution is found
    assert(solution_found > 0)

def test_solve_multiple_solutions(self):
    solver = DigitSolver([2, 4, 6, 8], 12)
    solver.solve()
    # Assert that multiple solutions are found
    assert(solution_count > 1)

def test_solve_no_solution(self):
    solver = DigitSolver([1, 2, 3, 4], 100)
    solver.solve()
    # Assert that no solution is found
    assert(solution_found <= 0)
