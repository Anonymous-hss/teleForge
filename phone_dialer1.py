import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os

class PhoneDialerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Phone Dialer')
        
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)

        # Create frames for tabs
        self.pending_frame = ttk.Frame(self.notebook)
        self.completed_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.pending_frame, text='Pending Calls')
        self.notebook.add(self.completed_frame, text='Completed Calls')

        # Create UI elements for Pending Calls
        self.phone_list = []
        self.pending_listbox = tk.Listbox(self.pending_frame, selectmode=tk.MULTIPLE, width=50, height=15)
        self.pending_listbox.pack(pady=10)

        self.call_button = tk.Button(self.pending_frame, text='Call Selected', command=self.call_selected)
        self.call_button.pack(pady=5)

        self.mark_done_button = tk.Button(self.pending_frame, text='Mark as Done', command=self.mark_as_done)
        self.mark_done_button.pack(pady=5)

        self.import_button = tk.Button(self.pending_frame, text='Import from Excel', command=self.import_numbers)
        self.import_button.pack(pady=5)

        # Create UI elements for Completed Calls
        self.completed_listbox = tk.Listbox(self.completed_frame, width=50, height=15)
        self.completed_listbox.pack(pady=10)

    def import_numbers(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            try:
                df = pd.read_excel(file_path, header=0)  # Use the first row as header
                df.columns = df.columns.str.strip()  # Strip any whitespace from column names
                self.phone_list = list(zip(df['Name'], df['Phone Number']))  # Use the correct column names
                self.update_pending_listbox()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import numbers: {e}")

    def update_pending_listbox(self):
        self.pending_listbox.delete(0, tk.END)  # Clear existing entries
        for name, number in self.phone_list:
            self.pending_listbox.insert(tk.END, f"{name}: {number}")

    def call_selected(self):
        selected_indices = self.pending_listbox.curselection()
        for index in selected_indices:
            number = self.phone_list[index][1]
            os.system(f'start tel:{number}')  # Open default dialer

    def mark_as_done(self):
        selected_indices = self.pending_listbox.curselection()
        for index in reversed(selected_indices):
            name, number = self.phone_list.pop(index)  # Remove from pending list
            self.completed_listbox.insert(tk.END, f"{name}: {number}")  # Add to completed list
        self.update_pending_listbox()  # Refresh pending listbox

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneDialerApp(root)
    root.mainloop()