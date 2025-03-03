# Import the tkinter library for GUI
import tkinter as tk

#Function to handle button clicks
def click(event):
    """
    This function is triggered when a button is clicked.
    It handles the logic for updating the display and performing calculations.
    """

# Get the text from the clicked button
text = event.widget.cget("text")

# if the "=" button is clicked, evaluate the expression
if text == "="
    try:
        # Evaluate the expression in the display and set the result
        result = str(eval(screen.get()))
        screen.set(result)
    except Exception as e:
        # If there's an error(e.g., invalid expression), display "Error"
        screen.set("Error")
    # If the "c" button is clicked, clear the display
elif text == "C":
    screen.set("")
# Otherwisw , append the button's text to the display
else:
    screen.set(screen.get() + text)

# Create the main application window
root = tk.Tk()
root.title ("Simple Calculator") #set the window title
root.geometry ("300 x 400") #Set the window size

#Create  a StringVar to store the input and result
screen = tk.StringVar()

#Create an Entry widget to display the input and result
entry = tk.Entry(root, textvar=screen, font = "Arial 20 bold", justify ="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10. padx=10)

#Define the buttons for the calculator
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]
# Create a  frame to hold the buttons
frame = tk.Frame*(root)
frame.pack()

#Loop through the buttons and create them
for i, button in enumerate(buttons):
    # Create a button with the specified text
    b = tk.Button(frame, text=button, font="Arial 15 bold", padx=20, pady=20)
    #Place the button in a grid layout
    b.grid(row=i // 4, column=i % 4, sticky="nsew")
    ##Bind the button to the click function
    b.bind("<Button-1>", click)

#Adjust the grid layout to make the buttons expand evenly
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    frame.grid_rowconfigure(i, weight=1)

#Start the main event loop
root.mainloop()