import tkinter as TK
from tkinter import *
from PIL import Image, ImageTk

# Create a window
root = Tk()

# Load the image file
img = Image.open('product.jpg')

# Create a PhotoImage object from the image file
photo = ImageTk.PhotoImage(img)

# Display the image in a label widget
label = Label(root, image=photo)
label.pack()

# Run the GUI loop
root.mainloop()