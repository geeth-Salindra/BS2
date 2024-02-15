import tkinter as tk
import pyautogui
import time

# Global variable to track if the typing process should continue
typing = False

def type_message():
    global typing
    typing = True
    # Retrieve message and number of times from entry widgets
    message = message_entry.get()
    num_times = int(num_times_entry.get())

    # Give the user a few seconds to click on the text field
    status_label.config(text="Please click on the text field")
    time.sleep(5)

    # Loop for typing the message 'num_times' times
    for _ in range(num_times):
        if not typing:  # Check if the typing process should stop
            break
        pyautogui.typewrite(message)
        pyautogui.press('enter')

def stop_typing():
    global typing
    typing = False
    status_label.config(text="Typing process stopped")

def validate_integer(new_value):
    if new_value.isdigit() or new_value == "":
        return True
    else:
        return False

# Create main window
root = tk.Tk()
root.title("Boost String")
root.geometry("250x120")  # Set width and height
root.resizable(False, False)  # Make the window non-resizable

# Create message entry
message_label = tk.Label(root, text="Enter the message:")
message_label.pack()
message_entry = tk.Entry(root)
message_entry.pack()

# Create number of times entry with validation
num_times_label = tk.Label(root, text="Enter the number of times:")
num_times_label.pack()
validate_cmd = root.register(validate_integer)
num_times_entry = tk.Entry(root, validate="key", validatecommand=(validate_cmd, "%P"))
num_times_entry.pack()

# Create frame to contain buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create button to trigger typing
type_button = tk.Button(button_frame, text="Type Message", command=type_message)
type_button.pack(side=tk.LEFT)

# Create button to stop typing
stop_button = tk.Button(button_frame, text="Stop Typing", command=stop_typing)
stop_button.pack(side=tk.LEFT)

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
