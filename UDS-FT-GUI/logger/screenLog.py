import tkinter as tk


def log_message(message,log_area):
    log_area.config(state=tk.NORMAL)  # Enable editing
    log_area.insert(tk.END, message + "\n")  # Append message
    log_area.config(state=tk.DISABLED)  # Disable editing
