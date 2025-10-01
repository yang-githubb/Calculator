"""
Modern Calculator Application
A beautiful GUI calculator built with Python and tkinter
"""

import tkinter as tk
from tkinter import font
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")
        
        # Calculator state
        self.current_value = "0"
        self.previous_value = ""
        self.operation = None
        self.should_reset_screen = False
        
        # Create UI
        self.create_display()
        self.create_buttons()
        
        # Bind keyboard events
        self.root.bind("<Key>", self.handle_keypress)
        
    def create_display(self):
        """Create the calculator display"""
        display_frame = tk.Frame(self.root, bg="#2b2b2b", pady=20)
        display_frame.pack(fill=tk.BOTH)
        
        # Previous operand display
        self.previous_label = tk.Label(
            display_frame,
            text="",
            font=("Segoe UI", 14),
            bg="#2b2b2b",
            fg="#888888",
            anchor="e",
            padx=20
        )
        self.previous_label.pack(fill=tk.BOTH)
        
        # Current operand display
        self.display = tk.Label(
            display_frame,
            text="0",
            font=("Segoe UI", 48, "bold"),
            bg="#2b2b2b",
            fg="white",
            anchor="e",
            padx=20
        )
        self.display.pack(fill=tk.BOTH)
        
    def create_buttons(self):
        """Create calculator buttons"""
        buttons_frame = tk.Frame(self.root, bg="#2b2b2b")
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button layout
        buttons = [
            ['AC', 'DEL', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        
        # Create buttons
        for row_idx, row in enumerate(buttons):
            for col_idx, button_text in enumerate(row):
                if button_text == '0':
                    # Zero button spans 2 columns
                    btn = self.create_button(
                        buttons_frame, 
                        button_text, 
                        row_idx, 
                        col_idx, 
                        columnspan=2
                    )
                elif button_text == '=':
                    # Equals button spans 2 columns
                    btn = self.create_button(
                        buttons_frame, 
                        button_text, 
                        row_idx, 
                        2, 
                        columnspan=2
                    )
                else:
                    btn = self.create_button(
                        buttons_frame, 
                        button_text, 
                        row_idx, 
                        col_idx
                    )
    
    def create_button(self, parent, text, row, col, columnspan=1):
        """Create a single button with appropriate styling"""
        # Determine button color based on type
        if text in ['AC', 'DEL', '%']:
            bg_color = "#505050"
            hover_color = "#606060"
            fg_color = "white"
        elif text in ['÷', '×', '-', '+']:
            bg_color = "#ff6b6b"
            hover_color = "#ff7979"
            fg_color = "white"
        elif text == '=':
            bg_color = "#4ecdc4"
            hover_color = "#5fd9cf"
            fg_color = "white"
        else:
            bg_color = "#3b3b3b"
            hover_color = "#4b4b4b"
            fg_color = "white"
        
        btn = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 20, "bold"),
            bg=bg_color,
            fg=fg_color,
            activebackground=hover_color,
            activeforeground=fg_color,
            relief=tk.FLAT,
            cursor="hand2",
            command=lambda: self.handle_button_click(text)
        )
        
        # Add hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))
        
        btn.grid(row=row, column=col, columnspan=columnspan, 
                 sticky="nsew", padx=5, pady=5)
        
        return btn
    
    def handle_button_click(self, text):
        """Handle button clicks"""
        if text.isdigit() or text == '.':
            self.append_number(text)
        elif text in ['÷', '×', '-', '+']:
            self.choose_operation(text)
        elif text == '=':
            self.compute()
        elif text == 'AC':
            self.clear()
        elif text == 'DEL':
            self.delete()
        elif text == '%':
            self.calculate_percentage()
        
        self.update_display()
    
    def handle_keypress(self, event):
        """Handle keyboard input"""
        key = event.char
        
        if key.isdigit() or key == '.':
            self.append_number(key)
        elif key in ['+', '-']:
            self.choose_operation(key)
        elif key == '*':
            self.choose_operation('×')
        elif key == '/':
            self.choose_operation('÷')
        elif key == '%':
            self.calculate_percentage()
        elif key == '\r':  # Enter key
            self.compute()
        elif event.keysym == 'BackSpace':
            self.delete()
        elif event.keysym == 'Escape':
            self.clear()
        
        self.update_display()
    
    def append_number(self, number):
        """Append a number to the display"""
        if self.should_reset_screen:
            self.current_value = "0"
            self.should_reset_screen = False
        
        if number == '.' and '.' in self.current_value:
            return
        
        if self.current_value == '0' and number != '.':
            self.current_value = number
        else:
            self.current_value += number
    
    def choose_operation(self, operation):
        """Choose an arithmetic operation"""
        if self.current_value == '':
            return
        
        if self.previous_value != '':
            self.compute()
        
        self.operation = operation
        self.previous_value = self.current_value
        self.should_reset_screen = True
    
    def compute(self):
        """Perform the calculation"""
        if self.operation is None or self.previous_value == '':
            return
        
        try:
            prev = float(self.previous_value)
            current = float(self.current_value)
            
            if self.operation == '+':
                result = prev + current
            elif self.operation == '-':
                result = prev - current
            elif self.operation == '×':
                result = prev * current
            elif self.operation == '÷':
                if current == 0:
                    self.display.config(text="Error: Div by 0")
                    self.current_value = "0"
                    self.previous_value = ""
                    self.operation = None
                    return
                result = prev / current
            
            # Round to avoid floating point errors
            result = round(result, 10)
            
            # Remove unnecessary decimals
            if result == int(result):
                result = int(result)
            
            self.current_value = str(result)
            self.operation = None
            self.previous_value = ""
            self.should_reset_screen = True
            
        except (ValueError, ZeroDivisionError) as e:
            self.display.config(text="Error")
            self.current_value = "0"
            self.previous_value = ""
            self.operation = None
    
    def clear(self):
        """Clear the calculator"""
        self.current_value = "0"
        self.previous_value = ""
        self.operation = None
        self.should_reset_screen = False
    
    def delete(self):
        """Delete the last digit"""
        if self.current_value == "0":
            return
        
        if len(self.current_value) == 1:
            self.current_value = "0"
        else:
            self.current_value = self.current_value[:-1]
    
    def calculate_percentage(self):
        """Convert current value to percentage"""
        try:
            current = float(self.current_value)
            self.current_value = str(current / 100)
        except ValueError:
            pass
    
    def format_number(self, number_str):
        """Format number for display"""
        try:
            number = float(number_str)
            if number == int(number):
                return f"{int(number):,}"
            else:
                # Format with commas and preserve decimals
                parts = number_str.split('.')
                integer_part = int(parts[0])
                decimal_part = parts[1] if len(parts) > 1 else ""
                if decimal_part:
                    return f"{integer_part:,}.{decimal_part}"
                else:
                    return f"{integer_part:,}"
        except (ValueError, IndexError):
            return number_str
    
    def update_display(self):
        """Update the calculator display"""
        # Update current operand
        display_text = self.format_number(self.current_value)
        
        # Limit display length
        if len(display_text) > 15:
            display_text = display_text[:15]
        
        self.display.config(text=display_text)
        
        # Update previous operand
        if self.operation and self.previous_value:
            prev_text = f"{self.format_number(self.previous_value)} {self.operation}"
            self.previous_label.config(text=prev_text)
        else:
            self.previous_label.config(text="")


def main():
    """Main function to run the calculator"""
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()

