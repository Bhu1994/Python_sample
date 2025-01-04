import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x380")

        # Entry widget to display the current expression
        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.input_field = tk.Entry(input_frame, font=('Helvetica', 18), textvariable=self.input_text, justify=tk.RIGHT, bd=10, insertwidth=2)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(fill=tk.BOTH, padx=5, pady=5)

        # Button Frame
        button_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        button_frame.pack(side=tk.TOP)

        # Buttons
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]

        row = 0
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(button_frame, text=button, font=('Helvetica', 16), command=action, width=5, height=2).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Keyboard Bindings
        self.root.bind("<Key>", self.on_key_press)

    def on_button_click(self, button):
        if button == 'C':
            self.clear()
        elif button == '=':
            self.calculate()
        else:
            self.expression += button
            self.input_text.set(self.expression)

    def on_key_press(self, event):
        key = event.char
        if key.isdigit() or key in ['+', '-', '*', '/']:
            self.expression += key
            self.input_text.set(self.expression)
        elif key == '\r':  # Enter key
            self.calculate()
        elif key == '\x08':  # Backspace key
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.input_text.set(result)
            self.expression = str(result)
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
