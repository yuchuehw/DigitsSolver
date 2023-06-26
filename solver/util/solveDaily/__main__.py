from runme import play_button_click
from runme import close_help_button_click
from runme import read_problem
from runme import combine_numbers
from runme import next_puzzle_button_click

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import defaultdict
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
    driver.get('https://www.nytimes.com/games/digits')  # Replace with the actual URL of the game

    play_button_click(driver)
    close_help_button_click(driver)

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
            combine_numbers(driver,step_list, buttons)

        if question == 4:
            input("Press Enter to exit the program")
            continue

        next_puzzle_button_click(driver)

    driver.quit()

if __name__ == "__main__":
    main()
