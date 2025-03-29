import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Celsius to Fahrenheit Converter")
        self.root.geometry("350x200")
        self.root.resizable(False, False)
        
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.celsius_frame = ttk.Frame(self.main_frame)
        self.celsius_frame.pack(fill=tk.X, pady=10)
        
        self.celsius_label = ttk.Label(
            self.celsius_frame,
            text="Celsius Temperature:",
            width=20
        )
        self.celsius_label.pack(side=tk.LEFT, padx=5)
        
        self.celsius_entry = ttk.Entry(self.celsius_frame, width=10)
        self.celsius_entry.pack(side=tk.LEFT, padx=5)
        
        self.result_frame = ttk.Frame(self.main_frame)
        self.result_frame.pack(fill=tk.X, pady=10)
        
        self.result_label = ttk.Label(
            self.result_frame,
            text="Fahrenheit Temperature:",
            width=20
        )
        self.result_label.pack(side=tk.LEFT, padx=5)
        
        self.fahrenheit_label = ttk.Label(
            self.result_frame,
            text="",
            width=10
        )
        self.fahrenheit_label.pack(side=tk.LEFT, padx=5)
        
        self.convert_button = ttk.Button(
            self.main_frame,
            text="Convert",
            command=self.convert
        )
        self.convert_button.pack(pady=20)
    
    def convert(self):
        try:
            celsius = float(self.celsius_entry.get())
            fahrenheit = (9/5) * celsius + 32
            self.fahrenheit_label.config(text=f"{fahrenheit:.2f}")
        except ValueError:
            self.fahrenheit_label.config(text="Invalid input")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()