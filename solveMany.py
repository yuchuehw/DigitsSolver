from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from solver import DigitSolver
from collections import defaultdict
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

def click_element(element_id, error_message):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, element_id))
        ).click()
    except:
        input(f"I am stuck, {error_message}")

def play_button_click():
    click_element('play-button', "play button doesn't work!")

def number_button_click(button_id, error_message):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        ).click()
    except:
        input(f"I am stuck, {error_message}")

def next_puzzle_button_click():
    click_element('next-puzzle-button', "next puzzle button doesn't work!")

def back_to_puzzles_button_click():
    click_element('back-to-puzzles-button', "back to puzzles button doesn't work!")

def combine_numbers(step_list, buttons):
    i1, i2 = buttons[step_list[0]].pop(), buttons[step_list[2]].pop()

    number_button_click(f'number-pos-{i1}', "I can't click the first number")
    number_button_click(step_list[1], "I can't click the operator")
    number_button_click(f'number-pos-{i2}', "I can't click the second number")

    buttons[step_list[4]].append(i2)

    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, f'number-pos-{i2}'), step_list[4])
        )
    except:
        input("I am stuck, the number doesn't seem to combine!")



def main():
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

        play_button_click()

        for question in range(5):
            buttons = defaultdict(list)
            solution = []

            for x in range(6):
                button_id = f'number-pos-{x}'
                button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, button_id))
                )
                buttons[button.get_attribute('innerHTML')].append(x)

            target = driver.find_element(
                By.ID,
                'target'
            ).get_attribute('innerHTML')

            solver = DigitSolver([int(x) for x in buttons], int(target))
            solver.printer_setter(lambda x: solution.append(x))
            solver.solve(True)
            print(list(buttons), target)

            for step in solution[0]:
                print(step)
                step_list = step.split(' ')
                combine_numbers(step_list, buttons)

            if question == 4:
                back_to_puzzles_button_click()
                time_ += 86400000
                level += 1
                continue

            next_puzzle_button_click()

    driver.quit()

if __name__ == "__main__":
    main()
