"""
Digits Automation

This script automates the solving of the Digits game on The New York Times website using
Selenium WebDriver. It interacts with the game interface, reads the puzzle information,
applies the Digits solver algorithm, and progresses through the levels automatically.

The automation process involves launching a web browser (Google Chrome) using Selenium
WebDriver, navigating to the Digits game page on The New York Times website, and
simulating user actions to solve each puzzle. The script utilizes the `solve_auto`
module for various actions, such as clicking buttons, reading the puzzle, combining
numbers, and progressing to the next puzzle.

The script supports different modes of operation:
- Automatic play from a specified starting level to a given number of levels.
- Automatic play of the daily puzzle only.
- Interactive mode for manually specifying the starting level and the number of levels
to play.

To use the script, the following dependencies are required:
- Selenium WebDriver: Install using `pip install selenium`.
- ChromeDriver: Download the appropriate ChromeDriver executable for your Chrome browser
version and place it in the system's PATH.

Module Dependencies:
- `solve_auto`: Provides functions for interacting with the Digits game interface.

Usage:
Run the script with the desired command-line options to automate the Digits game solving process.

Command-Line Options:
- `-start`, `--startLevel S`: Specifies the starting level (integer).
- `-level`, `--levelToPlay L`: Specifies the total number of levels to play (integer).
- `-daily`, `--dailyOnly`: Solves the daily puzzle only.


Author: Yu-Chueh Wang
Version: 1.7.0
"""

from collections import defaultdict
from datetime import datetime
import argparse
import time
import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from solve_auto import (play_button_click,
                        close_help_button_click,
                        read_problem,
                        combine_numbers,
                        next_puzzle_button_click,
                        back_to_puzzles_button_click)

## temporary implementation ##
path = os.path.abspath(__file__).split("/")
path.pop()
TIMESHIFTPATH = "/".join(path) + "/TimeShift.js"
path.pop()
path.pop()
path.pop()
sys.path.append("/".join(path))
from solver.solver import DigitSolver
## temporary implementation ##

LEVEL_0_TIME = 1680998400000
ONE_DAY = 86400000


def daily_puzzle_info() -> int:
    """
    Returns the level of today's puzzle.

    Returns:
        int: The level of today's puzzle.
    """
    now = time.time()
    level = (now * 1000 - LEVEL_0_TIME) // ONE_DAY
    return int(level)


def puzzle_level_to_time(level: int) -> int:
    """
    Converts a puzzle level to a time value in milliseconds.

    Args:
        level (int): The puzzle level.

    Returns:
        int: The corresponding time value in milliseconds.
    """
    return LEVEL_0_TIME + level * ONE_DAY


def get_date(time_: int) -> str:
    """
    Converts a time value in milliseconds to a formatted date string.

    Args:
        time_ (int): The time value in milliseconds.

    Returns:
        str: The formatted date string.
    """
    return datetime.fromtimestamp(time_ // 1000).strftime("%B %d, %Y")


def init_parser() -> argparse.ArgumentParser:
    """
    Initializes the command-line argument parser.

    Returns:
        argparse.ArgumentParser: The initialized argument parser.
    """
    usage = "%(prog)s [-h] [[-start S] [-level L] | [-d]]"
    parser = argparse.ArgumentParser(description="Automatic Digits solver", usage=usage)

    parser.add_argument(
        "-start",
        "--startLevel",
        nargs=1,
        type=int,
        metavar="S",
        dest="start",
        help="starting level (int)",
    )
    parser.add_argument(
        "-level",
        "--levelToPlay",
        nargs=1,
        type=int,
        metavar="L",
        dest="level",
        help="total level to play (int)",
    )
    parser.add_argument(
        "-daily",
        "--dailyOnly",
        dest="daily",
        action="store_true",
        help="solve daily puzzle only",
    )
    return parser


def automate_puzzle(driver: webdriver.Chrome, level: int, time_: int, click_close: bool) -> None:
    """
    Automates the solving of a single puzzle.

    Args:
        driver (webdriver.Chrome): The Chrome WebDriver.
        level (int): The level of the puzzle.
        time_ (int): The time value of the puzzle.
        click_close (bool): Whether to click the "Close Help" button.
    """
    puzzle_date = get_date(time_)
    print(f"Now solving puzzle #{level} ({puzzle_date})")

    driver.get("https://www.nytimes.com/games/digits")
    driver.execute_script(f"Date = TimeShift.Date;TimeShift.setTime({time_});")

    play_button_click(driver)

    if click_close:
        close_help_button_click(driver)

    for question in range(5):
        buttons = defaultdict(list)
        solution = []

        target = read_problem(driver, buttons)

        solver = DigitSolver([int(x) for x in buttons], int(target))
        solver.printer = solution.append
        solver.solve(True)
        print(list(buttons), target)

        for step in solution[0]:
            print(step)
            step_list = step.split(" ")
            combine_numbers(driver, step_list, buttons)

        if question == 4:
            back_to_puzzles_button_click(driver)
            time_ += ONE_DAY
            level += 1
            continue

        next_puzzle_button_click(driver)


def automation(start_level: int, level_to_play: int, click_close: bool = False) -> None:
    """
    Automates the Digits game solving process.

    Args:
        start_level (int): The starting level.
        level_to_play (int): The total number of levels to play.
        click_close (bool, optional): Whether to click the "Close Help" button. Defaults to False.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    # Read TimeShift.js
    inject = ""
    with open(TIMESHIFTPATH, "r", encoding="utf-8") as time_shift_js:
        inject = time_shift_js.read()

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": inject})
    level = start_level
    time_ = puzzle_level_to_time(start_level)

    for _ in range(level_to_play):
        automate_puzzle(driver, level, time_, click_close)

    driver.quit()
    print("done")


def main() -> None:
    """
    The main function for running the Digits solver.
    """
    parser = init_parser()
    args = parser.parse_args()

    start_level = 1
    level_to_play = 20

    if not args.start and not args.level and not args.daily:
        automation(start_level, level_to_play)
    elif (args.start and args.daily) or (args.level and args.daily):
        warning = f"""usage: {sys.argv[0]} [-h] [[-start S] [-level L] | [-d]]
    error: argument -start and -level: not allowed with argument -daily"""
        print(warning)

    elif args.daily:
        start_level = daily_puzzle_info()
        level_to_play = 1
        automation(start_level, level_to_play, True)
    elif args.start and args.level:
        start_level, level_to_play = args.start[0], args.level[0]
        if start_level <= 0:
            print("warning: start level is less than 1. setting it to 1.")
            start_level = 1
        automation(start_level, level_to_play, True)
    else:
        warning = f"""usage: {sys.argv[0]} [-h] [[-start S] [-level L] | [-d]]
    error: argument -start and -level must be used simultaneously"""
        print(warning)


if __name__ == "__main__":
    main()
