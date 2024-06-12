

# Calculator
<img width="151" alt="image" src="https://github.com/Yash-Epte/Calculator/assets/121223452/9e9aaca2-bb8c-417e-b098-491888dbc638">


A simple calculator application built using Python and Tkinter.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Supports the use of parentheses for grouping.
- Includes a backspace function to correct input mistakes.
- Clear function to reset the calculation.
- User-friendly graphical interface.

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/your-username/Calculator.git
   ```

3. Navigate to the project directory:
   ```bash
   cd Calculator
   ```

4. Run the calculator:
   ```bash
   python main.py
   ```

## Usage

1. The calculator GUI will open.
2. Use the buttons to input numbers and operators.
3. Click `=` to evaluate the expression.
4. Use `C` to clear the input field and start a new calculation.
5. Use `←` to delete the last entered character.

## Code Overview

The main code for the calculator is contained in `calculator.py`. Here's a brief overview of the key functions:

- `add_to_calculation(symbol)`: Adds the given symbol to the current calculation. Handles backspace for correction.
- `evaluate_calculation()`: Evaluates the current calculation and displays the result. Shows an error message if the evaluation fails.
- `clear_field()`: Clears the current calculation and resets the input field.

## GUI Layout

- A text field at the top displays the current calculation and results.
- Buttons for digits (0-9), operations (`+`, `-`, `*`, `/`), and special characters (`(`, `)`).
- Clear (`C`), backspace (`←`), and equals (`=`) buttons for additional functionality.

## Contributing

Feel free to fork this repository and submit pull requests. Any contributions, whether they're bug fixes, new features, or documentation improvements, are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue in this repository or contact me at [your-email@example.com](mailto:your-email@example.com).

---

Replace the placeholder email and GitHub repository URL with your actual details.
