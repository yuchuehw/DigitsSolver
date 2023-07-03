<p align="center">
    <picture>
      <img 
        src="new_logo.png" 
        alt="Digits Solver icon"
        width="500"
       />
    </picture>
<p>

[English](README.md)
 • [繁體中文](README_zh-TW.md)
 • [简体中文](README_zh-CN.md)
 • [日本語](README_ja.md)
 • [Español](README_es.md)
 • [Français](README_fr.md)
 • [Italiano](README_it.md)
 • [Deutsche](README_de.md)
 • [Русский](README_ru.md)

Digits Solver is a Python program that solves a digits puzzle game by finding mathematical operations that can be applied to a set of starting digits to obtain a target digit.

[![Python application](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/python-app.yml)
[![CodeQL](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/yuchuehw/DigitsSolver/actions/workflows/github-code-scanning/codeql)
[![PyLint Score](https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/pylint_badge.svg)](pylint.out)
<br>
[![python badge](https://img.shields.io/badge/Python-3776AB?style=flat&for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-grey.svg?style=flat&logo=selenium)](https://www.selenium.dev/)
[![TimeShift](https://img.shields.io/badge/TimeShift.js-grey.svg?style=flat&logo=javascript)](https://github.com/plaa/TimeShift-js)
![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&color=pink)
[![License](https://img.shields.io/github/license/yuchuehw/DigitsSolver?style=flat&color=yellow)](LICENSE.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![HitCount](https://hits.dwyl.com/yuchuehw/DigitsSolver.svg?style=flat)

## Demo
You can see the algorithm in action here(click the green run button after redirected.):

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

You could also watch this speed run that uses this algorithm:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*note: the demo uses the solveAuto features continue reading for more info*
## Table of Contents
- [Usage](#usage)
- [Examples](#examples)
- [Alternative Usage](#alternative-usage)
- [Contributing](#contributing)
- [License](#license)


## Usage

To run the Digits Solver program, execute the following command:

```bash
git clone https://github.com/yuchuehw/DigitsSolver
cd ./DigitSolver
python solver <starting_digits> <target_digit> [-os] [-h]
```

- `<starting_digits>`: A space-separated list of integers representing the starting digits.
- `<target_digit>`: The target digit that needs to be obtained.
- `-os` or `--onesolution` (optional): If specified, the program will find only one solution. Otherwise, it will find all possible solutions.
- -`h` or `--help` (optional): If used, the help menu would be shown.

## Examples

1. Find all solutions for the digits puzzle:
   ```bash
   python solver 3 12 15 20 23 25 439
   ```

2. Find only one solution for the digits puzzle:
   ```bash
   python solver 3 12 15 20 23 25 439 -os
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
```python
from solver.solver import DigitSolver
solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
solution_count = solver.solve(False)
print(f"we found {solution_count} solution(s)")
```
## Other Files

I have also included a few additional Python programs that complement the solver program. You can find detailed instructions on how to use each of these programs below:

- [How to Use pretty_solve.py](reference/prettySolve.md): Provides a visually enhanced version of the solver program.
- [How to Use solve_auto.py](reference/solveAuto.md): Fully automatic Digits solver with Selenium

Feel free to explore these files and utilize them for specific use cases or scenarios.

*apendix folder included 450 problems used in the NYT Games. Feel free to use those problem for program testing*

## Contributing

Contributions to the Digits Solver program are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

When contributing, please ensure that you follow best practices, maintain code quality, and provide clear descriptions of your changes.


## License

The Digits Solver program is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). You are free to use, modify, and distribute this program for personal or commercial purposes. Please see the [LICENSE](LICENSE.md) file for more details.

## Acknowledgements

Special thanks to the author of [timeshift.js](https://github.com/plaa/TimeShift-js) for their contribution to this project. Portions of their code have been utilized in the implementation of the solver.util module
