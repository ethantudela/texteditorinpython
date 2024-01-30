import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(expand=True, fill='both')
        self.setup_menu()
        self.setup_search_bar()

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)
        menubar.add_cascade(label="File", menu=file_menu)
        
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menubar)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

    def exit_editor(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def setup_search_bar(self):
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack(fill='x')
        self.search_entry.bind("<Return>", self.search_text)  # Bind Enter key to search
        search_button = tk.Button(self.root, text="Search", command=self.search_text)
        search_button.pack()
    
    def search_text(self, event=None):
        search_query = self.search_entry.get()
        if search_query:
            start_index = "1.0"
            while True:
                start_index = self.text_area.search(search_query, start_index, stopindex="end", nocase=True, regexp=True)
                if not start_index:
                    messagebox.showinfo("Search", "No more matches found.")
                    break
                end_index = f"{start_index}+{len(search_query)}c"
                self.text_area.tag_add("search", start_index, end_index)
                start_index = end_index
            self.text_area.tag_config("search", background="yellow")

def main():
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()