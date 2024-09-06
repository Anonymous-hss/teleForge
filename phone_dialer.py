import tkinter as tk
import os  # For executing system commands
from bleak import BleakClient

# Sample phone numbers
phone_numbers = ['+919527022111','+916280936040']

# Function to dial number
def dial_number(number):
    # This command will depend on your operating system and setup.
    # For example, on Windows, you might use:
    os.system(f'start tel:{number}')  # This will open the default dialer

# Create the main window
def create_app():
    root = tk.Tk()
    root.title('Phone Dialer')

    # Create a list to hold phone numbers
    for number in phone_numbers:
        frame = tk.Frame(root)
        frame.pack(pady=5)

        label = tk.Label(frame, text=number)
        label.pack(side=tk.LEFT)

        call_button = tk.Button(frame, text='Call', command=lambda n=number: dial_number(n))
        call_button.pack(side=tk.RIGHT)

    root.mainloop()

# Run the application
if __name__ == "__main__":
    create_app()