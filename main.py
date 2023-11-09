import tkinter as tk

def button_click(button_number):
    print(f"Button {button_number} clicked!")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Four Buttons Example")

# Set the window size
window.geometry("400x100")

def front():
    def File():
        button_click(1)

    def Edit():
        button_click(2)

    def View():
        button_click(3)

    def More():
        button_click(4)

    # Create buttons outside the inner functions
    button1 = tk.Button(window, text="Button 1", command=File)
    button1.grid(row=0, column=0, padx=20)

    button2 = tk.Button(window, text="Button 2", command=Edit)
    button2.grid(row=0, column=1, padx=10)

    button3 = tk.Button(window, text="Button 3", command=View)
    button3.grid(row=0, column=2, padx=10)

    button4 = tk.Button(window, text="Button 4", command=More)
    button4.grid(row=0, column=3, padx=10)

# Call the front function
front()

# Run the Tkinter event loop
window.mainloop()
