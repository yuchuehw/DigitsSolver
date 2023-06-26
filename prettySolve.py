from solver import DigitSolver
import concurrent.futures
import os

Executor = concurrent.futures.ThreadPoolExecutor


def main():
    os.system('clear')
    holding_list = []

    def mf(step: list) -> None:
        holding_list.append(step)

    def alternative_input(prompt: str = ""):
        try:
            input_ = input(prompt)
        except KeyboardInterrupt:
            print()
            print("Program exited!")
            exit()
        return input_

    def get_integer_list_input(prompt: str) -> list:
        while True:
            input_str = alternative_input(prompt)
            number_list = input_str.split()
            valid_numbers = []
            for num in number_list:
                try:
                    valid_numbers.append(int(num))
                except ValueError:
                    print(f"Invalid input: {num}. Please enter integers separated by spaces.")
                    break
            if len(valid_numbers) == len(number_list):
                return valid_numbers

    def get_integer_input(prompt: str) -> int:
        while True:
            input_str = alternative_input(prompt)
            try:
                return int(input_str)
            except ValueError:
                print(f"Invalid input: {input_str}. Please enter an integer.")

    number_list = []
    while not number_list:
        number_list = get_integer_list_input("Enter numbers allowed separated by space: ")
        if not number_list:
            print("Invalid input. Please enter at least one valid integer.")

    os.system('clear')
    target = get_integer_input("Enter the target number: ")
    os.system('clear')

    solver = DigitSolver(number_list, target)
    solver.printer_setter(mf)

    with Executor() as executor:
        future = executor.submit(solver.solve)
        print("Use the enter key to loop through possible solutions. Press <Ctrl>+C to exit.")
        while True:
            try:
                input()
                os.system('clear')
            except KeyboardInterrupt:
                print("Program end.")
                break
            if holding_list:
                holding_list.sort(key=lambda o: len(o))
                print("Possible solution:")
                print(*holding_list.pop(0), sep="\n")
            elif future.done():
                print("Computation has stopped.")
                print(f"{future.result()} solutions found.")
                break
            else:
                print("Calculating, please wait...")


if __name__ == "__main__":
    main()
