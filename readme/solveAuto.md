# Digits Solver Automation

This script automates the solving of puzzles in the Digits game on the New York Times website using Selenium and a custom solver.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Selenium library
- Chrome WebDriver
- solver folder

## Getting Started

1. Clone the repository or download the script.
2. Install the required dependencies using pip:

   ```shell
   pip install selenium
   ```

3. Download the Chrome WebDriver executable and add its location to your system's PATH environment variable.

Sure! Here's the documentation for the command-line interface:


## Usage

```plaintext
solveAuto [-h] [[-start S] [-level L] | [-daily]]
```

### Optional Arguments

- `-h, --help`: Show the help message and exit.

- `-start S, --startLevel S`: Specify the starting level to begin solving the puzzles. The value should be an integer.

- `-level L, --levelToPlay L`: Specify the total number of levels to play. The value should be an integer.

- `-daily, --dailyOnly`: Solve daily puzzles only. If this flag is provided, the tool will ignore the `--startLevel` and `--levelToPlay` options and solve only the daily puzzle.

## Examples


1. Solve 10 levels starting from level 5:
   ```plaintext
   python solver/util/solveAuto --startLevel 5 --levelToPlay 10
   ```

2. Solve daily puzzles only:
   ```plaintext
   python solver/util/solveAuto --dailyOnly
   ```

Note: If no arguments are provided, the tool will use default settings (start from level 1 to level 20).


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

This script is provided under the [MIT License](LICENSE.md).

Please note that the documentation assumes you have already set up the necessary environment and dependencies as mentioned in the "Prerequisites" section.
