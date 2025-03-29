import tkinter as tk
from tkinter import ttk

class NameAddressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Name and Address")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.info_label = ttk.Label(
            self.main_frame,
            text="Click the button to show the name and address",
            wraplength=250,
            justify=tk.CENTER
        )
        self.info_label.pack(pady=20)
        
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)
        
        self.show_button = ttk.Button(
            self.button_frame,
            text="Show Info",
            command=self.show_info
        )
        self.show_button.pack(side=tk.LEFT, padx=5)
        
        self.quit_button = ttk.Button(
            self.button_frame,
            text="Quit",
            command=self.root.destroy
        )
        self.quit_button.pack(side=tk.LEFT, padx=5)
    
    def show_info(self):
        name_address = "Steven Marcus\n274 Baily Drive\nWaynesville, NC 27999"
        self.info_label.config(text=name_address)

if __name__ == "__main__":
    root = tk.Tk()
    app = NameAddressApp(root)
    root.mainloop()