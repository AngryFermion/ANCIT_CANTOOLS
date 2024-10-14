import tkinter as tk
import GUI.gui as gui
import time
import FOP.FileOp as fop

def callMainWindow():
    splash_screen.destroy()
    gui.show_main_window(img_path=image_path_logo,img_ico=image_path_ico)

def showSS():
    global splash_screen
    splash_screen = tk.Tk()
    splash_screen.title("Splash Screen")

    relative_path_ss = "Ancit_logo.png" #"NASH_logo.png"
    relative_path_logo = "Ancit_logo.jpeg"
    relative_path_ico = "Ancit_logo.ico"
    global image_path_ss, image_path_logo, image_path_ico
    image_path_ss = fop.get_image_path(relative_path=relative_path_ss)
    image_path_logo = fop.get_image_path(relative_path=relative_path_logo)
    image_path_ico = fop.get_image_path(relative_path=relative_path_ico)
    # Load splash image
    splash_image = tk.PhotoImage(file=image_path_ss)

    # Set the size of the splash screen
    splash_width = 250
    splash_height = 200

    # Center the splash screen on the screen
    screen_width = splash_screen.winfo_screenwidth()
    screen_height = splash_screen.winfo_screenheight()
    x = (screen_width // 2) - (splash_width // 2)
    y = (screen_height // 2) - (splash_height // 2)
    splash_screen.geometry(f"{splash_width}x{splash_height}+{x}+{y}")
    splash_screen.overrideredirect(True)  # Remove window decorations

    splash_label = tk.Label(splash_screen, image=splash_image)
    splash_label.pack(expand=True)
    
    
    splash_screen.after(3000, callMainWindow)
    splash_screen.mainloop()
    