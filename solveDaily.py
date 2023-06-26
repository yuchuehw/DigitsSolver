from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from solver import DigitSolver
from collections import defaultdict

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

def close_help_button_click():
    click_element('close-help', "close help button doesn't work!")

def next_puzzle_button_click():
    click_element('next-puzzle-button', "next puzzle button doesn't work!")

def number_button_click(button_id, error_message):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        ).click()
    except:
        input(f"I am stuck, {error_message}")

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
    driver.get('https://www.nytimes.com/games/digits')  # Replace with the actual URL of the game

    play_button_click()
    close_help_button_click()

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
            input("Press Enter to exit the program")
            continue

        next_puzzle_button_click()

    driver.quit()

if __name__ == "__main__":
    main()
