import tkinter as tk
from tkinter import filedialog, scrolledtext
import logger.screenLog as sl
import FOP.FileOp as fp
import OS.threadMaster as task

def browse_file():
    global file_path
    file_path = fp.browse()
    if file_path == "BAD_EXT":
        print("Bad extension")
    elif file_path == "BAD_ADDR":
        print("Start Address incorrect")
    else:
        file_path_var.set(file_path)
        button1.config(state=tk.NORMAL)
        


def on_button1_click():
    # sl.log_message("Button 1 clicked.",log_area=log_area)
    task.startTask(log_area,file_path=file_path)



def show_main_window():
    # Destroy the splash screen and show the main window
    # obj_ss.destroy()
    
    # Create the main application window
    global root
    root = tk.Tk()
    root.title("NASH FLASH TOOL")

    # Set the size of the main window
    main_width = 400
    main_height = 400
    root.geometry(f"{main_width}x{main_height}")

    # Center the main window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (main_width // 2)
    y = (screen_height // 2) - (main_height // 2)
    root.geometry(f"{main_width}x{main_height}+{x}+{y}")

    # Frame for the file path and browse button
    top_frame = tk.Frame(root)
    top_frame.pack(pady=10, padx=10, fill=tk.X)

    # Variable to hold the file path
    global file_path_var
    file_path_var = tk.StringVar()

    # Entry to display the file path
    file_path_entry = tk.Entry(top_frame, textvariable=file_path_var, width=40)
    file_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    # Browse button
    browse_button = tk.Button(top_frame, text="Browse", command=browse_file)
    browse_button.pack(side=tk.RIGHT)

    # Frame for log area
    log_frame = tk.Frame(root)
    log_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Scrolled text area for logs
    global log_area
    
    log_area = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, height=10, state=tk.DISABLED)
    log_area.pack(fill=tk.BOTH, expand=True)

    # Frame for buttons at the bottom
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Two buttons in the bottom area
    # 
    global button1
    button1 = tk.Button(button_frame, text="FLASH", command=on_button1_click,state=tk.DISABLED)
    button1.pack(side=tk.LEFT, padx=5)


    # button2 = tk.Button(button_frame, text="Button 2", command=on_button2_click)
    # button2.pack(side=tk.LEFT, padx=5)

    # Run the application
    root.mainloop()

