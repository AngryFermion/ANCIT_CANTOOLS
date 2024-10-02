import tkinter as tk
from tkinter import filedialog
import os
import sys
import time
# Function to create the full path to the image
def get_image_path(relative_path):
    # Get the current directory of the script
    # current_directory = os.path.dirname(__file__)
    # Create the relative path to the image
    try:
        # PyInstaller creates a temporary folder and stores paths in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        print("loading absolute path....")
        time.sleep(2)
        base_path = os.path.abspath(".")
    # image_path = os.path.join(current_directory, 'img', image_name)
    image_path = os.path.join(base_path, relative_path)
    image_path = image_path.replace("/","//")
    return image_path


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