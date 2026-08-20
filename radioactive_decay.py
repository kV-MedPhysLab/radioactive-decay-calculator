import tkinter as tk
from tkinter import ttk


class RadioactiveDecayCalculator:
    def __init__(self, root):
        self.root = root

        self.root.title("Radioactive Decay Calculator")
        self.root.geometry("800x700")
        self.root.minsize(700, 600)

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = ttk.Label(
            self.root,
            text="Radioactive Decay Calculator",
            font=("Segoe UI", 22, "bold")
        )
        title.pack(pady=(20, 5))

        subtitle = ttk.Label(
            self.root,
            text="Calculate radioactive decay quantities from the values you know."
        )
        subtitle.pack(pady=(0, 20))


def main():
    root = tk.Tk()
    app = RadioactiveDecayCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
