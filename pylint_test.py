"""
This script is used to generate a Pylint badge based on the Pylint score of the `solver` module.
It runs Pylint on the module and writes the Pylint score to a file named `pylint.out`. Then, it
extracts the score from the file, determines the appropriate color for the badge based on the score,
and generates an SVG badge using the `pybadges` library. The generated badge is saved as `pylint_badge.svg`.

Usage:
------
To generate the Pylint badge, execute the following command in the terminal:
    python pylint_test.py

Note:
-----
1. Do not relocate or move this file, as it is being used to generate the Pylint badge in the workflow.

"""

from pylint.lint import Run
from pylint.reporters.text import TextReporter
from pybadges import badge
import random
import string

def randomword(length):
    """
    Generate a random word of the specified length.

    Parameters:
    length (int): Length of the random word to generate.

    Returns:
    str: Randomly generated word.

    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

if __name__ == "__main__":
    run_id = randomword(10)
    grade = None
    color = None
    abs = "/home/runner/work/DigitsSolver/DigitsSolver/"

    with open(abs + "pylint.out", "w+") as f:
        f.write(f"runid:{run_id}\n")
        reporter = TextReporter(f)
        Run([abs + "solver"], reporter=reporter, exit=False)

    with open(abs + "pylint.out", "r") as f:
        content = f.read()
        target = "Your code has been rated at "
        if target in content:
            content = content[content.index(target) + len(target):]
            content = content[:content.index("/")]
        else:
            content = ""
        if content:
            grade = float(content)

    if not grade or grade <= 1.2:
        color = '#e7241d'
    elif grade <= 3.6:
        color = '#ef832c'
    elif grade <= 6.0:
        color = '#fffd46'
    elif grade <= 8.4:
        color = '#9cfa40'
    else:
        color = '#60f83d'

    if not grade:
        grade = "fatal"

    badge_text = badge(left_text='pylint score', right_text=str(grade), right_color=color)

    with open(abs + "pylint_badge.svg", "w+") as f:
        f.write(f"<!-- runid:{run_id} -->\n")
        f.write(badge_text)
