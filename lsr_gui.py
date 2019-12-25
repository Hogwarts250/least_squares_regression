import ast
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import ttk

from least_squares_regression import calc_lsr, calc_stnd_deviation
from mpl_lsr import plot_coordinates

def calculate(*args):
    try:
        input_coordinates = ast.literal_eval(coordinates.get())

    except ValueError:
        input_coordinates = None
    
    if input_coordinates:
        slope, y_intercept = calc_lsr(input_coordinates)
        plot_coordinates(input_coordinates, slope, y_intercept)

        stnd_deviation.set(calc_stnd_deviation(slope, y_intercept, input_coordinates))

        update_image()

def update_image():
    img2 = PhotoImage(file = "lsr.png")
    graph.configure(image = img2)
    graph.image = img2

    
root = Tk()
root.title("Least Squares Regression")

img = PhotoImage(file = "lsr.png")
coordinates = StringVar()
stnd_deviation = StringVar()

mainframe = ttk.Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

coordinate_entry = ttk.Entry(mainframe, textvariable = coordinates)
coordinate_entry.grid(column = 0, row = 0, sticky = (N, W, E, S))

graph = ttk.Label(mainframe, image = img)
graph.grid(column = 0, row = 1, columnspan = 2, sticky = (N, S))

ttk.Button(mainframe, text = "Enter", command = calculate).grid(column = 1, row = 0, sticky = (N, W, E, S))
ttk.Label(mainframe, textvariable = stnd_deviation).grid(column = 0, row = 2, columnspan = 2, sticky = (N, S))

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
mainframe.columnconfigure(0, weight = 3)
mainframe.columnconfigure(1, weight = 1)
mainframe.rowconfigure(1, weight = 1)
mainframe.rowconfigure(2, weight = 1)

for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

coordinate_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()