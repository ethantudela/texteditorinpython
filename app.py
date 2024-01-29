import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Python Text Editor")

        self.text_area = tk.Text(self.window, wrap=tk.WORD)
        self.text_area.pack(expand=tk.YES, fill=tk.BOTH)

        self.create_menu()

        self.window.mainloop()

    def create_menu(self):
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)

if __name__ == "__main__":
    text_editor = TextEditor()