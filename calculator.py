class Calculator:
    """
    A calculator class that handles basic arithmetic operations.
    """
    
    def __init__(self):
        """
        Initialize the calculator with default values.
        """
        self.current_value = "0"
        self.previous_value = ""
        self.operation = None
        self.should_reset_screen = False
        
    
    def clear(self):
        """

        Clear all values and reset the calculator to initial state.
        """
        self.current_value = "0"
        self.previous_value = ""
        self.operation = None
        self.should_reset_screen = False
    
    def append_number(self, number):
        if self.should_reset_screen:
            self.current_value = number
            self.should_reset_screen = False
            return  # important: avoid appending again

        if number == "." and "." in self.current_value:
            return

        if self.current_value == "0" and number != ".":
            self.current_value = number
            return

        self.current_value += number

    def choose_operation(self, operation):
        """
        Choose an arithmetic operation.
        Args:
            operation (str): The operation symbol ("+", "-", "*", "/")
        """
        if self.previous_value:
            self.compute()
        self.operation = operation
        self.previous_value = self.current_value
        self.should_reset_screen = True
    
    def compute(self):
        """
        Perform the actual calculation.
        """
        if self.operation and self.previous_value:
            if self.operation == "+":
                self.current_value = str(float(self.previous_value) + float(self.current_value))
            elif self.operation == "-":
                self.current_value = str(float(self.previous_value) - float(self.current_value))
            elif self.operation == "*":
                self.current_value = str(float(self.previous_value) * float(self.current_value))
            elif self.operation == "/":
                if float(self.current_value) == 0:
                    print("Error: Cannot divide by zero!")
                    self.clear()
                    return
                self.current_value = str(float(self.previous_value) / float(self.current_value))

            # Clean up after calculation
            self.operation = None
            self.previous_value = ""
            self.should_reset_screen = True

    def delete(self):
        """
        Delete the last digit from current display.
        """
        if self.current_value == "0":
            return
        if len(self.current_value) == 1:
            self.current_value = "0"
        else:
            self.current_value = self.current_value[:-1]
    
    def get_display_value(self):
        """
        Get the current display value.
        Returns:
            str: The current value to display
        """
        return self.current_value


# Test your calculator here!
if __name__ == "__main__":
    print("=== Testing Your Calculator ===")
    
    # Create calculator instance
    calc = Calculator()

    def assert_close(actual_str, expected_number, desc):
        actual = float(actual_str)
        ok = abs(actual - expected_number) < 1e-9
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {desc} -> got {actual_str}, expected {expected_number}")
        assert ok

    # Test 1: Addition 5 + 3 = 8
    calc.clear()
    calc.append_number("5")
    calc.choose_operation("+")
    calc.append_number("3")
    calc.compute()
    assert_close(calc.get_display_value(), 8, "5 + 3")

    # Test 2: Subtraction 10 - 4 = 6
    calc.clear()
    calc.append_number("10")
    calc.choose_operation("-")
    calc.append_number("4")
    calc.compute()
    assert_close(calc.get_display_value(), 6, "10 - 4")

    # Test 3: Multiplication 6 * 7 = 42
    calc.clear()
    calc.append_number("6")
    calc.choose_operation("*")
    calc.append_number("7")
    calc.compute()
    assert_close(calc.get_display_value(), 42, "6 * 7")

    # Test 4: Division 15 / 3 = 5
    calc.clear()
    calc.append_number("15")
    calc.choose_operation("/")
    calc.append_number("3")
    calc.compute()
    assert_close(calc.get_display_value(), 5, "15 / 3")

    # Test 5: Decimals 3.5 + 1.2 = 4.7
    calc.clear()
    calc.append_number("3")
    calc.append_number(".")
    calc.append_number("5")
    calc.choose_operation("+")
    calc.append_number("1")
    calc.append_number(".")
    calc.append_number("2")
    calc.compute()
    assert_close(calc.get_display_value(), 4.7, "3.5 + 1.2")

    # Test 6: Prevent multiple decimals -> '0.' then '.' ignored then '5' => 0.5
    calc.clear()
    calc.append_number(".")
    calc.append_number(".")
    calc.append_number("5")
    assert_close(calc.get_display_value(), 0.5, "prevent multiple decimals")

    # Test 7: Delete behavior -> 123 -> del -> 12 -> del -> 1 -> del -> 0
    calc.clear()
    calc.append_number("1")
    calc.append_number("2")
    calc.append_number("3")
    calc.delete()
    assert_close(calc.get_display_value(), 12, "delete once")
    calc.delete()
    assert_close(calc.get_display_value(), 1, "delete twice")
    calc.delete()
    assert_close(calc.get_display_value(), 0, "delete to zero")

    # Test 8: Division by zero clears calculator
    calc.clear()
    calc.append_number("5")
    calc.choose_operation("/")
    calc.append_number("0")
    calc.compute()
    # After divide-by-zero, clear() sets current_value to "0"
    assert_close(calc.get_display_value(), 0, "division by zero -> clear")

    print("\nAll tests completed.")