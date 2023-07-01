from pylint.lint import Run
from pylint.reporters.text import TextReporter
from pybadges import badge
import os
grade = 0
color = ""

abs = "/home/runner/work/DigitsSolver/DigitsSolver/"

with open(abs+"pylint.out", "w+") as f:
    reporter = TextReporter(f)
    Run([abs+"solver"], reporter=reporter, exit=False)

with open(abs+"pylint.out","r") as f:
    f=f.read()
    target = "Your code has been rated at "
    f = f[f.index(target)+len(target):]
    f = f[:f.index("/")]
grade = float(f)
if grade <= 1.2:
    color = '#e7241d'
elif grade <= 3.6:
    color = '#ef832c'  
elif grade <= 6.0:
    color  = '#fffd46'
elif grade <= 8.4:
    color = '#9cfa40'
else:
    color = '#60f83d'

s = badge(left_text='pylint score', right_text=str(grade), right_color=color)

with open(abs+"pylint_badge.svg", "w+") as f:
    f.write(s)
