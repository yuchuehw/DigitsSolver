from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_problem(driver, buttons):
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
    return target

def click_element(driver, element_id, error_message):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, element_id))
        ).click()
    except:
        input(f"I am stuck, {error_message}")

def play_button_click(driver):
    click_element(driver, 'play-button', "play button doesn't work!")

def close_help_button_click(driver):
    click_element(driver, 'close-help', "close help button doesn't work!")

def next_puzzle_button_click(driver):
    click_element(driver, 'next-puzzle-button', "next puzzle button doesn't work!")

def number_button_click(driver, button_id, error_message):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        ).click()
    except:
        input(f"I am stuck, {error_message}")

def wait_til_combine(driver, button_id, expect_value):
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, button_id), expect_value)
        )
    except:
        input("I am stuck, the number doesn't seem to combine!")


def combine_numbers(driver, step_list, buttons):
    i1, i2 = buttons[step_list[0]].pop(), buttons[step_list[2]].pop()

    number_button_click(driver, f'number-pos-{i1}', "I can't click the first number")
    number_button_click(driver, step_list[1], "I can't click the operator")
    number_button_click(driver, f'number-pos-{i2}', "I can't click the second number")

    buttons[step_list[4]].append(i2)

    wait_til_combine(driver, f'number-pos-{i2}', step_list[4])
