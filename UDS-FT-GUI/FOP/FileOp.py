import tkinter as tk
from tkinter import filedialog

def check_format():
    print("Checking format...\n")
    
def check_address():
    print("Checking start address...\n")

def browse():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_path = file_path.replace("/","//")
    
        return file_path
        # file_path_var.set(file_path)