# Crypto Swap Calculator

This is a simple tool to calculate some basic variables of a crypto swap. The program takes user input for various parameters and performs calculations to determine the amount and minimum amount of a second token received in a swap, based on the given inputs.

## Features

- **User Input**: Collects user inputs for token names, current prices, amount to swap, swap fee, and slippage.
- **Calculations**: Computes the price ratio, amount to receive, and minimum amount to receive.
- **Results Display**: Displays the results in a new window.
- **Exit Mechanism**: Allows the user to exit the program by pressing 'q' in the results window.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)
- Selenium WebDriver (optional, if planning to extend the functionality for web-based interactions)

## Installation

1. Ensure Python 3.x is installed on your system.
2. Clone this repository to your local machine.
3. Install any required packages (Tkinter should be included with Python).

## Usage

1. Run the program using Python:

    ```sh
    python crypto_swap_calculator.py
    ```

2. A window will appear prompting you to enter the following information:
    - Name of the currency to swap (Token A)
    - Name of the currency to swap to (Token B)
    - Current price of Token A (in $)
    - Current price of Token B (in $)
    - Amount of Token A to swap
    - Swap fee
    - Slippage percentage

3. After entering the required information, click the "Calculate" button.

4. A new window will display the results of the calculations, including:
    - Price ratio (Token A to Token B)
    - Amount of Token B to receive
    - Minimum amount of Token B to receive

5. Press 'q' in the results window to exit the program.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
