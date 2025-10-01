# Python Calculator

A beautiful, modern calculator application built with Python and tkinter. Features a sleek dark-themed GUI with smooth interactions and full keyboard support.

## Features

- 🎨 Modern dark-themed user interface
- 🔢 Basic arithmetic operations (+, -, ×, ÷)
- 💯 Percentage calculations
- ⌨️ Full keyboard support
- 🖱️ Mouse/touch interface with hover effects
- 📊 Number formatting with commas for readability
- ⚡ Fast and responsive
- 🛡️ Error handling (division by zero, invalid operations)

## Requirements

- Python 3.6 or higher
- tkinter (comes built-in with Python)

## Installation

1. Make sure you have Python installed on your system
2. Clone or download this repository
3. No additional packages needed - tkinter is included with Python!

## How to Run

Simply run the calculator script:

```bash
python calculator.py
```

Or on some systems:

```bash
python3 calculator.py
```

## Usage

### Mouse Controls

- Click number buttons (0-9) to input numbers
- Click operator buttons (+, -, ×, ÷) to perform operations
- Click `=` to calculate the result
- Click `AC` to clear all
- Click `DEL` to delete the last digit
- Click `%` to convert the current number to a percentage
- Click `.` for decimal point

### Keyboard Shortcuts

- **Numbers**: Type 0-9 to input numbers
- **Decimal**: Press `.` for decimal point
- **Operators**: Press `+`, `-`, `*`, `/` for operations
- **Equals**: Press `Enter` to calculate
- **Clear**: Press `Escape` to clear all
- **Delete**: Press `Backspace` to delete last digit
- **Percentage**: Press `%` for percentage

## Features Explained

### Dark Modern UI
The calculator features a sleek dark theme with carefully chosen colors:
- Dark background for reduced eye strain
- Color-coded buttons (operations in red, equals in teal)
- Smooth hover effects

### Number Formatting
Large numbers are automatically formatted with commas for better readability (e.g., 1,000,000).

### Smart Calculations
- Prevents division by zero with error messages
- Rounds floating point results to avoid precision errors
- Chains multiple operations seamlessly
- Automatic decimal optimization (removes .0 from whole numbers)

### Responsive Design
- Fixed size for consistency
- Large, easy-to-click buttons
- Clear, readable display

## File Structure

```
Calculator/
├── calculator.py       # Main calculator application
├── requirements.txt    # Python dependencies (minimal)
└── README.md          # This file
```

## Creating an Executable (Optional)

If you want to create a standalone executable:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Create the executable:
   ```bash
   pyinstaller --onefile --windowed calculator.py
   ```

3. The executable will be in the `dist` folder

## Customization

You can easily customize the calculator by modifying `calculator.py`:

- **Colors**: Change the `bg_color`, `hover_color`, and `fg_color` values in the `create_button` method
- **Fonts**: Modify the font tuples (e.g., `("Segoe UI", 48, "bold")`)
- **Size**: Adjust the geometry in `self.root.geometry("400x600")`
- **Button Layout**: Modify the `buttons` list in the `create_buttons` method

## Troubleshooting

### tkinter not found

If you get an error that tkinter is not installed:

- **Windows**: Reinstall Python and make sure to check "tcl/tk and IDLE" during installation
- **macOS**: tkinter should be included with Python
- **Linux**: Install tkinter with:
  ```bash
  sudo apt-get install python3-tk  # Ubuntu/Debian
  sudo yum install python3-tkinter  # Fedora/CentOS
  ```

## License

This project is open source and free to use for any purpose.

## Contributing

Feel free to fork this project and add your own features! Some ideas:
- Scientific calculator functions (sin, cos, tan, etc.)
- Memory functions (M+, M-, MR, MC)
- History of calculations
- Themes (light mode, custom colors)
- Keyboard shortcuts customization

Enjoy calculating! 🎉
