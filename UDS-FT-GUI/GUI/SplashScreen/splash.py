import tkinter as tk
import GUI.gui as gui
import time
import FOP.FileOp as fop

def callMainWindow():
    splash_screen.destroy()
    gui.show_main_window()

def showSS():
    global splash_screen
    splash_screen = tk.Tk()
    splash_screen.title("Splash Screen")

    relative_path = "NASH_logo.png"
    image_path = fop.get_image_path(relative_path=relative_path)
    # Load splash image
    splash_image = tk.PhotoImage(file=image_path)

    # Set the size of the splash screen
    splash_width = 400
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
    