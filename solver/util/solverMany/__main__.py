from runme import play_button_click
from runme import read_problem
from runme import combine_numbers
from runme import next_puzzle_button_click
from runme import back_to_puzzles_button_click

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import defaultdict
from datetime import datetime
import os
import sys

## temporary implementation ##
path = os.path.abspath(__file__).split("/")
path.pop()
path.pop()
path.pop()
path.pop()
sys.path.append("/".join(path))
## temporary implementation ##

from solver.solver import DigitSolver

def main():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=chrome_options)
    # Read TimeShift.js
    inject = ""
    with open("TimeShift.js", "r") as f:
        inject = f.read()

    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': inject})

    LEVEL_0_TIME = 1681084800000
    start_level = 0
    time_ = LEVEL_0_TIME + start_level * 86400000
    level = start_level

    while True:
        puzzle_date = datetime.fromtimestamp(time_ // 1000).strftime("%B %d, %Y")
        print(f"Now solving puzzle #{level} ({puzzle_date})")

        driver.get('https://www.nytimes.com/games/digits')
        driver.execute_script(f"Date = TimeShift.Date;TimeShift.setTime({time_});")

        play_button_click(driver)

        for question in range(5):
            buttons = defaultdict(list)
            solution = []

            target = read_problem(driver, buttons)

            solver = DigitSolver([int(x) for x in buttons], int(target))
            solver.printer_setter(lambda x: solution.append(x))
            solver.solve(True)
            print(list(buttons), target)

            for step in solution[0]:
                print(step)
                step_list = step.split(' ')
                combine_numbers(driver, step_list, buttons)

            if question == 4:
                back_to_puzzles_button_click(driver)
                time_ += 86400000
                level += 1
                continue

            next_puzzle_button_click(driver)

    driver.quit()

if __name__ == "__main__":
    main()
