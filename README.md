# Digits Solver

Digits Solver is a Python program that solves a digits puzzle game by finding mathematical operations that can be applied to a set of starting digits to obtain a target digit.

## Table of Contents
- [Usage](#usage)
- [Examples](#examples)
- [Alternative Usage](#alternative-usage)
- [Contributing](#contributing)
- [License](#license)


## Usage

To run the Digits Solver program, execute the following command:

```bash
python solver.py <starting_digits> <target_digit> [-os]
```

- `<starting_digits>`: A space-separated list of integers representing the starting digits.
- `<target_digit>`: The target digit that needs to be obtained.
- `-os` or `--onesolution` (optional): If specified, the program will find only one solution. Otherwise, it will find all possible solutions.

## Examples

1. Find all solutions for the digits puzzle:
   ```bash
   python solver.py 3 12 15 20 23 25 439
   ```

2. Find only one solution for the digits puzzle:
   ```bash
   python solver.py 3 12 15 20 23 25 439 -os
   ```

## Output

The program will output the number of solutions found and display each solution in the following format:

```
solution found:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

we found 1 solution(s)
```

## Alternative Usage
The Digits Solver can also be imported as a Python module and used programmatically. Here's an example:
```
from solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
solution_count = solver.solve(False)
print(f"we found {solution_count} solution(s)")
```

## Contributing

Contributions to the Digits Solver program are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

When contributing, please ensure that you follow best practices, maintain code quality, and provide clear descriptions of your changes.


## License

The Digits Solver program is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this program for personal or commercial purposes. Please see the [LICENSE](LICENSE) file for more details.
