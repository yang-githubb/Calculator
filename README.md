# Python Calculator (Core Logic)

A simple, testable calculator core written in Python. It includes basic arithmetic operations and a set of runnable tests in the `__main__` block. Ideal foundation for adding a GUI later (e.g., with tkinter) or integrating into other apps.

## Current Features

- Basic operations: addition, subtraction, multiplication, division
- Decimal input handling (prevents multiple `.`)
- Delete/backspace support
- Division-by-zero protection (clears state)
- Runnable tests with clear PASS/FAIL output

## Requirements

- Python 3.8+
- No third-party packages required

## How to Run

Run the built-in tests:
```bash
python calculator.py
```
You should see PASS/FAIL messages for each test and a final "All tests completed." line when successful.

## File Overview

- `calculator.py`: The `Calculator` class (core logic) and a set of runnable tests in the `__main__` block
- `requirements.txt`: Placeholder (no extra deps needed)
- `.gitignore`: Standard Python/git ignores

## Example (What the tests do)

- 5 + 3 = 8
- 10 - 4 = 6
- 6 * 7 = 42
- 15 / 3 = 5
- 3.5 + 1.2 = 4.7
- Prevents multiple decimals (e.g., `.` then `.` then `5` ⇒ `0.5`)
- Delete behavior (123 → 12 → 1 → 0)
- Division by zero clears the calculator state

## Next Steps (Choose Your Path)

- Add a GUI with tkinter
  - Create a window, display label, and 4x5 button grid
  - Wire buttons to `Calculator` methods
  - Optional: keyboard shortcuts, styling

- Or add automated tests with pytest
  - Create `tests/test_calculator.py`
  - Port each main-block test into pytest functions
  - Run with `pytest -q`

## Suggested Git Workflow

- Commit core logic:
```bash
git add calculator.py README.md
git commit -m "Implement calculator core logic and add runnable tests"
```
- Create a feature branch for GUI or pytest:
```bash
git checkout -b feature/gui   # or feature/pytest
```

## License

This project is open source and free to use for any purpose.
