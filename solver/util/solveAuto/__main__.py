from solveAuto import play_button_click
from solveAuto import close_help_button_click
from solveAuto import read_problem
from solveAuto import combine_numbers
from solveAuto import next_puzzle_button_click
from solveAuto import back_to_puzzles_button_click

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from collections import defaultdict
from datetime import datetime
import argparse
import time
import os
import sys

## temporary implementation ##
path = os.path.abspath(__file__).split("/")
path.pop()
timeshiftpath = "/".join(path) + "/TimeShift.js"
path.pop()
path.pop()
path.pop()
sys.path.append("/".join(path))
## temporary implementation ##

from solver.solver import DigitSolver

LEVEL_0_TIME = 1680998400000
ONE_DAY = 86400000


def dailyPuzzleInfo() -> int:
    """
    return today's puzzle level
    """
    now = time.time()
    level = (now * 1000 - LEVEL_0_TIME) // ONE_DAY
    return int(level)


def puzzleLevelToTime(level: int) -> int:
    return LEVEL_0_TIME + level * ONE_DAY


def getDate(time_: int) -> str:
    """
    time in millisecond to a formatted date string.
    """
    return datetime.fromtimestamp(time_ // 1000).strftime("%B %d, %Y")


def init_parser() -> argparse:
    usage = "%(prog)s [-h] [[-start S] [-level L] | [-d]]"
    parser = argparse.ArgumentParser(description="Automatic Digits solver", usage=usage)

    parser.add_argument(
        "-start",
        "--startLevel",
        nargs=1,
        type=int,
        metavar="S",
        dest="start",
        help="starting level(int)",
    )
    parser.add_argument(
        "-level",
        "--levelToPlay",
        nargs=1,
        type=int,
        metavar="L",
        dest="level",
        help="total level to play(int)",
    )
    parser.add_argument(
        "-daily",
        "--dailyOnly",
        dest="daily",
        action="store_true",
        help="solve daily puzzle only",
    )
    return parser


def automation(start_level, level_to_play, click_close: bool = False):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    # Read TimeShift.js
    inject = ""
    with open(timeshiftpath, "r") as f:
        inject = f.read()

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": inject})
    level = start_level
    time_ = puzzleLevelToTime(start_level)

    for level_played in range(level_to_play):
        puzzle_date = getDate(time_)
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
            solver.printer_setter(lambda x: solution.append(x))
            solver.solve(True)
            print(list(buttons), target)

            for step in solution[0]:
                print(step)
                step_list = step.split(" ")
                combine_numbers(driver, step_list, buttons)

            if question == 4:
                back_to_puzzles_button_click(driver)
                time_ += 86400000
                level += 1
                continue

            next_puzzle_button_click(driver)

    driver.quit()
    print("done")


def main():
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
        start_level = dailyPuzzleInfo()
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
    error: argument -start and -level must be use simultaneously"""
        print(warning)


if __name__ == "__main__":
    main()
