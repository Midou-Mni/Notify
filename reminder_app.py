import time
import threading
import pyttsx3
import tkinter as tk
from plyer import notification

def notify_every_x_minutes(interval, title, message, speak_enabled):
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 is for male, 1 is for female (on many systems)

    while True:
        print(f"Waiting for {interval * 60} seconds...")
        time.sleep(interval * 60)

        notification.notify(
            title=title,
            message=message,
            timeout=20
        )

        if speak_enabled:
            engine.say(f"{title}: {message}")
            engine.runAndWait()

def start_reminder():
    try:
        interval = float(interval_entry.get())
        title = title_entry.get()
        message = message_entry.get()
        speak_enabled = speak_var.get()

        root.withdraw()

        reminder_thread = threading.Thread(target=notify_every_x_minutes, args=(interval, title, message, speak_enabled))
        reminder_thread.daemon = True
        reminder_thread.start()
    except ValueError:
        error_label.config(text="Please enter a valid number for the interval.")

def stop_reminder():
    root.quit()
def clear_interval_field():
    interval_entry.delete(0, tk.END)
def clear_title_field():
    title_entry.delete(0, tk.END)
def clear_message_field():
    message_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Reminder Settings")

default_interval = 0.1
default_title = "تدكير"
default_message = "صلي على رسول الله"

tk.Label(root, text="Reminder Interval (minutes):").grid(row=0, column=0, padx=10, pady=5)
interval_entry = tk.Entry(root)
interval_entry.grid(row=0, column=1, padx=10, pady=5)
interval_entry.insert(0, default_interval)
clear_interval_button = tk.Button(root, text="X", command=clear_interval_field)
clear_interval_button.grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Reminder Title:").grid(row=1, column=0, padx=10, pady=5)
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1, padx=10, pady=5)
title_entry.insert(0, default_title)
clear_title_button = tk.Button(root, text="X", command=clear_title_field)
clear_title_button.grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Reminder Message:").grid(row=2, column=0, padx=10, pady=5)
message_entry = tk.Entry(root)
message_entry.grid(row=2, column=1, padx=10, pady=5)
message_entry.insert(0, default_message)
clear_message_button = tk.Button(root, text="X", command=clear_message_field)
clear_message_button.grid(row=2, column=2, padx=5, pady=5)

speak_var = tk.BooleanVar(value=True)
speak_checkbox = tk.Checkbutton(root, text="Enable Speaking", variable=speak_var)
speak_checkbox.grid(row=3, column=1, pady=10)

start_button = tk.Button(root, text="Start Reminder", command=start_reminder)
start_button.grid(row=4, column=1, columnspan=2, pady=10)

stop_button = tk.Button(root, text="Stop Reminder", command=stop_reminder)
stop_button.grid(row=4, column=0, columnspan=1, pady=10)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()