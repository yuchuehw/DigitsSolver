<p align="center">
    <picture>
      <img 
        src="https://raw.githubusercontent.com/yuchuehw/DigitsSolver/main/new_logo.png" 
        alt="Digits Solver icon"
        width="500"
       />
    </picture>
<p>

English
 • [繁體中文](readme/README_zh-TW.md)
 • [简体中文](readme/README_zh-CN.md)
 • [日本語](readme/README_ja.md)
 • [Español](readme/README_es.md)
 • [Français](readme/README_fr.md)
 • [Italiano](readme/README_it.md)
 • [Deutsche](readme/README_de.md)
 • [Русский](readme/README_ru.md)

Welcome to Digits Solver, the ultimate Python companion for conquering the mind-bending [Digits](https://www.nytimes.com/games/digits) puzzle game, developed by The New York Times. Dive into a captivating world of numerical challenges and master the art of strategic manipulation. With Digits Solver, you'll strategically manipulate a set of starting digits using mathematical operations to reach the elusive target digit. Its powerful algorithm and meticulous analysis empower you to swiftly unravel each puzzle, delivering step-by-step solutions with unwavering precision. Elevate your puzzle-solving prowess and unlock the secrets hidden within the digits. Get ready for an exciting journey to become a Digits master!

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
See the algorithm in action by clicking the green run button after being redirected:

[![Replit](https://img.shields.io/badge/DEMO-REPL.IT-purple.svg?style=flat&logo=replit)](https://replit.com/@yuchuehw/DigitsSolver)

You can also watch this speed run that uses

 the Digits Solver algorithm:

[![Replit](https://img.shields.io/badge/DEMO-YOUTUBE-purple.svg?style=flat&logo=youtube)](https://www.youtube.com/watch?v=se2OdZnEHHA)

*Note: The demo showcases the [solve_auto](readme/solveAuto.md) feature. Continue reading for more information.*

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Alternative Usage](#alternative-usage)
- [Util Modules](#util-modules)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

You can obtain a copy of the Digits Solver program using one of the following methods:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yuchuehw/DigitsSolver.git
   ```

2. **Download the Zip File**:
   - Go to the [Release](https://github.com/yuchuehw/DigitsSolver/releases) tab on the GitHub repository.
   - Download the latest release zip file.
   - Extract the contents of the zip file to your desired location.

After obtaining the program, you can proceed to the [Usage](#usage) section to run the Digits Solver program.

## Usage

To run the Digits Solver program, open the terminal and navigate to the directory where you have downloaded or cloned the DigitsSolver repository. Once you are in the appropriate directory, execute the following command in the terminal (replace values in angle brackets with your input; see examples section for more details):

```bash
python solver <starting_digits> <target_digit> [-os] [-h]
```

- `<starting_digits>`: A space-separated list of integers representing the starting digits.
- `<target_digit>`: The target digit that needs to be obtained.
- `-os` or `--onesolution` (optional): If specified, the program will find only one solution. Otherwise, it will find all possible solutions.
- `-h` or `--help` (optional): If used, the help menu will be displayed.

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
Solution found:
15 + 3 = 18
23 × 18 = 414
414 + 25 = 439

We found 1 solution(s)
```

## Alternative Usage

The Digits Solver can also be imported as a Python module and used programmatically. You are free to add more functionality than what we have provided. Here's a minimal example of how to use it as an import:

```python
from solver.solver import DigitSolver

solver = DigitSolver([3, 12, 15, 20, 23, 25], 439)
solution_count = solver.solve(False)
print(f"We found {solution_count} solution(s)")
```

## Util Modules

We have also included a few additional Python programs that complement the solver program. They are located inside the solver/util folder. You can read more about how to use them here:

- [How to Use pretty_solve.py](readme/prettySolve.md): Provides a visually enhanced version of the solver program.
- [How to Use solve_auto.py](readme/solveAuto.md): Fully automatic Digits solver with Selenium

Feel free to explore these files and utilize them for specific use cases or scenarios.

*Appendix folder includes 450 problems used in the NYT Games. Feel free to use those problems for program testing.*

## Contributing

Contributions to the Digits Solver program are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

When contributing, please ensure that you follow best practices, maintain code quality, and provide clear descriptions of your changes.

## License

The Digits Solver program is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). You are free to use, modify, and distribute this program for personal or commercial purposes. Please see the [LICENSE](LICENSE.md) file for more details.

## Acknowledgements

Special thanks to the author of [timeshift.js](https://github.com/plaa/TimeShift-js) for their contribution to this project. Portions of their code have been utilized in the implementation of the solver.util module.
