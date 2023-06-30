"""
This module provides helper functions for interacting with the Digits game using Selenium WebDriver.

The functions in this module assist in reading the problem statement, clicking elements on the page,
combining numbers, and navigating through the game.

Note: This code assumes the usage of Selenium WebDriver for browser automation.

Requires:
    - selenium (Python library for browser automation)
    - WebDriver (e.g., ChromeDriver) compatible with the browser version

Author: Yu-Chueh Wang
Version: 1.7.0
"""

from typing import Dict, List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


def read_problem(driver: WebDriver, buttons: Dict[str, List[int]]) -> str:
    """
    Reads the problem statement from the Digits game and returns the target number.

    Args:
        driver (WebDriver): The Selenium WebDriver object.
        buttons (Dict[str, List[int]]): A dictionary to store the
        positions of the available numbers.

    Returns:
        str: The target number as a string.
    """
    for button_index in range(6):
        button_id = f"number-pos-{button_index}"
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        buttons[button.get_attribute("innerHTML")].append(button_index)

    target = driver.find_element(By.ID, "target").get_attribute("innerHTML")
    return target


def click_element(driver: WebDriver, element_id: str, error_message: str) -> None:
    """
    Clicks an element with the given ID on the page.

    Args:
        driver (WebDriver): The Selenium WebDriver object.
        element_id (str): The ID of the element to be clicked.
        error_message (str): The error message to display if the element is not clickable.
    """
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, element_id))
        ).click()
    except:
        input(f"I am stuck, {error_message}")


def play_button_click(driver: WebDriver) -> None:
    """
    Clicks the "Play" button on the page.

    Args:
        driver (WebDriver): The Selenium WebDriver object.
    """
    click_element(driver, "play-button", "play button doesn't work!")


def close_help_button_click(driver: WebDriver) -> None:
    """
    Clicks the "Close Help" button on the page.

    Args:
        driver (WebDriver): The Selenium WebDriver object.
    """
    click_element(driver, "close-help", "close help button doesn't work!")


def next_puzzle_button_click(driver: WebDriver) -> None:
    """
    Clicks the "Next Puzzle" button on the page.

    Args:
        driver (WebDriver): The Selenium WebDriver object.
    """
    click_element(driver, "next-puzzle-button", "next puzzle button doesn't work!")


def number_button_click(driver: WebDriver, button_id: str, error_message: str) -> None:
    """
    Clicks a number button with the given ID on the page.

    Args:
        driver (WebDriver): The Selenium WebDriver object.
        button_id (str): The ID of the number button to be clicked.
        error_message (str): The error message to display if the element is not clickable.
    """
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        ).click()
    except:
        input(f"I am stuck, {error_message}")


def wait_til_combine(driver: WebDriver, button_id: str, expect_value: str) -> None:
    """
    Waits until the number button with the given ID displays the expected value.

    Args:
        driver (WebDriver): The Selenium WebDriver object.
        button_id (str): The ID of the number button to check for the expected value.
        expect_value (str): The expected value of the number button.
    """
    try:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, button_id), expect_value)
        )
    except:
        input("I am stuck, the number doesn't seem to combine!")


def combine_numbers(driver: WebDriver, step_list: List[str], buttons: Dict[str, List[int]]) -> None:
    """
    Combines two numbers based on the given step list.

    Args:
        driver (WebDriver): The Selenium WebDriver object.
        step_list (List[str]): A list containing the operator and
        numbers to be combined.
        buttons (Dict[str, List[int]]): A dictionary to store the
        positions of the available numbers.
    """
    i, j = buttons[step_list[0]].pop(), buttons[step_list[2]].pop()

    number_button_click(driver, f"number-pos-{i}", "I can't click the first number")
    number_button_click(driver, step_list[1], "I can't click the operator")
    number_button_click(driver, f"number-pos-{j}", "I can't click the second number")

    buttons[step_list[4]].append(j)

    wait_til_combine(driver, f"number-pos-{j}", step_list[4])


def back_to_puzzles_button_click(driver: WebDriver) -> None:
    """
    Clicks the "Back to Puzzles" button on the page.

    Args:
        driver (WebDriver): The Selenium WebDriver object.
    """
    click_element(driver, "back-to-puzzles-button", "back to puzzles button doesn't work!")
