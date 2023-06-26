# Digits Solver Automation

This script automates the solving of puzzles in the Digits game on the New York Times website using Selenium and a custom solver.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Selenium library
- Chrome WebDriver
- solver.py
- solveDaily.py or solverMany.py + TimeShift.js

## Getting Started

1. Clone the repository or download the script.
2. Install the required dependencies using pip:

   ```shell
   pip install selenium
   ```

3. Download the Chrome WebDriver executable and add its location to your system's PATH environment variable.

## Usage

1. Open the `digits_solver.py` script in a text editor.

2. Update the `inject` variable with the path to the `TimeShift.js` file. This file is used to manipulate the game's time.

3. Run the script:

   ```shell
   python solveDaily.py
   ```
   or
   ```shell
   python solveMany.py
   ```

   The script will launch a Chrome browser and start solving the puzzles automatically.

## Functionality

The script automates the following actions:

1. Navigating to the Digits game on the New York Times website.

2. Manipulating the game's time using the `TimeShift.js` script.(solveMany.py only)

3. Clicking the "Play" button to start a puzzle.

4. Solving each puzzle by performing the necessary clicks on the number buttons and operators.

5. Handling cases where the script gets stuck, such as when buttons or elements are not clickable.

6. Advancing to the next puzzle or returning to the puzzle selection screen when a puzzle set is completed.

7. Printing the current puzzle number and date for reference.(solveMany.py only)

## Customization

If you want to modify or extend the script's functionality, you can explore the following functions:

- `click_element(element_id, error_message)`: Handles clicking on an element identified by its ID. If the element is not clickable, it prompts the user for input.

- `combine_numbers(step_list, buttons)`: Handles combining numbers by performing the necessary clicks on the number buttons and updating the buttons' state.

- `next_puzzle_button_click()`: Handles clicking the "Next Puzzle" button to proceed to the next puzzle.

- `back_to_puzzles_button_click()`: Handles clicking the "Back to Puzzles" button when a puzzle set is completed.

Feel free to modify the code according to your specific requirements.

## License

This script is provided under the [MIT License](LICENSE).

Please note that the documentation assumes you have already set up the necessary environment and dependencies as mentioned in the "Prerequisites" section. Make sure to replace `digits_solver.py` with the actual filename if you have named the file differently.
