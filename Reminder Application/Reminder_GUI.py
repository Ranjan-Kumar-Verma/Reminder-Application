# Note: To make executable file from .py use pyinstaller --onefile Reminder_GUI.py --hidden-import plyer.platforms.linux.notification (and --hidden-import plyer.platforms.win.notification for window machine )


from tkinter import *
from plyer import notification
import time
from sys import exit
root = Tk()

# Variables and constants
WIDTH = 500
HEIGHT = 400
INPUT_WIDTH = 45
reminder_title = StringVar()
reminder_message = StringVar()
# reminder_time = IntVar
X_PADDING = 5
Y_PADDING = 10
FONT = "ubuntu"



# Functions
# Function to show that reminder is saved
def Reminder_saved():
    TIME = float(reminder_time_str.get())
    notification.notify(
        title='Reminder saved',
        message=f'I will remind you after {TIME} minutes',
        timeout=4
    )

# Function to set reminder
def reminder(Reminder_title, Reminder_message):
    notification.notify(
        title=Reminder_title,
        message=Reminder_message,
        timeout=5
    )

# Main function to call other functions
def set_reminder(reminder_title, reminder_message):
    TIME = float(reminder_time_str.get())
    Reminder_saved()
    root.withdraw()
    time.sleep(TIME*60)
    reminder(reminder_title, reminder_message)
    exit()


# Geometry of the root window
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Verma Desktop Reminder")
# root.configure(background="white")


# Heading frame
frame = Frame(root)
frame.pack()

#Heading in frame
Label(frame, text="Verma Desktop Reminder", font=(
    f"{FONT} 25 bold")).pack(padx=15, pady=30)

# Frame 2 (for all inputs)
input_frame = Frame(root)
input_frame.pack()

# Input title from user
# Title
Label(input_frame, text="Title to notify: ", font=(f"{FONT} 15")).grid(
    row=0, column=0, sticky='w', padx=X_PADDING, pady=Y_PADDING)
Entry(input_frame, width=INPUT_WIDTH, textvariable=reminder_title).grid(
    row=0, column=1,columnspan=2, sticky='w', padx=X_PADDING, pady=Y_PADDING)

# Message
Label(input_frame, text="Display Message: ", font=(f"{FONT} 15")).grid(
    row=1, column=0, sticky='w', padx=X_PADDING, pady=Y_PADDING)
Entry(input_frame, width=INPUT_WIDTH, textvariable=reminder_message).grid(
    row=1, column=1,columnspan=2, sticky='w', padx=X_PADDING, pady=Y_PADDING)

# Time
Label(input_frame, text="Set Time: ", font=(f"{FONT} 15")).grid(
    row=2, column=0, sticky='w', padx=X_PADDING, pady=Y_PADDING)
reminder_time_str = StringVar()
Entry(input_frame, width=15, textvariable=reminder_time_str).grid(
    row=2, column=1, sticky='ew',padx=X_PADDING, pady=Y_PADDING)
Label(input_frame, text="minutes", font=(f"{FONT} 15")).grid(
    row=2, column=2, sticky='w', pady=Y_PADDING)
# frame.grid_columnconfigure(1, weight=1)


# Set notification button
set_reminder_btn = Button(root, text="Set Reminder", command=lambda: set_reminder(
    reminder_title.get(), reminder_message.get()), font=(f"{FONT} 15"))
set_reminder_btn.pack(padx=X_PADDING, pady=Y_PADDING, ipady=Y_PADDING//2)


root.mainloop()
