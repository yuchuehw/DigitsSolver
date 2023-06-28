from solver import DigitSolver
import argparse
import sys


def main():
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
        print("we also support console mode use [-h] to learn more.")


if __name__ == "__main__":
    main()
