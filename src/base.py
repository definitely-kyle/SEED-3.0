# Library to contain some useful functions to reduce clutter in main SEED file
# Created 28/10/2020 by Kyle Kean

# Import packages
try:
    import numpy as np
    import csv
    import matplotlib.pyplot as plt
    import tkinter as tk
    import sys
    import tkinter as tk # tkinter is the GUI module used for this project
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter import filedialog as fd
    from math import ceil
    import os
except ImportError as mod: # If the user didn't install the required modules beore trying to run SEED 2.0
    print("Install the required modules before starting:\n" + str(mod))
    messagebox.showerror(title="Module Import Error", message="Install the required modules before starting:\n" + str(mod))
    sys.exit()
except Exception as err: # Any other exception that should occur (nothing else should happen, hence generalising all other exceptions)
    print("Error while importing:\n" + str(err))
    sys.exit()

bgc = "lightgray" # GUI background colour

## Begin function library
# Switch function for diff method
def switch(arg):
    if (arg == "finite_difference"):
        return 0
    elif (arg == "savitzky_golay"):
        return 1
    elif (arg == "spectral"):
        return 2
    elif (arg == "spline"):
        return 3
    elif (arg == "trend_filtered"):
        return 4
    else:
        return 0 # Default to Finite Difference if anything else

# Takes an array with headers and separates into time series (left column) and data, and calculates dt
# Returns time, dt, data and a list of variable names (if present)
def clean_contents(contents):
    # Separate the input file into data points, time series and variable names
    variable_names = contents[0][1:] # Obtain the system variable names from the data
    del contents[0] # Remove the system variable names from the data matrix
    time_series = np.array([float(val[0]) for val in contents]) # From the first column of the data file, obtain the time series data for the data
    dt = float(time_series[1])-float(time_series[0]) # From the time series data, obtain dt

    contents = [val[1:] for val in contents] # Remove the time series data from the data matrix
    contents = np.array([[float(val) for val in item] for item in contents]) # Turn the list of lists into a numpy array as this is what the PySINDy model expects as an input
    return time_series, dt, contents, variable_names

# Read selected file (from "Example/Own Data" dropdown) and return an array containing its data
def read_file(selection, to_open):
    if(selection == "Own Data"):
        to_read = to_open      
    else:
        to_read = str(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data/")) + selection

    with open(to_read, newline='') as csvfile:
        data = list(csv.reader(csvfile))  

    return data

# Creates a figure and set of axes to store plots
# Returns fig and axs handle
def create_plot(time_series, contents, variable_names, coefs, feats, sim_data):
    # Create a figure with the correct number of subplots
    fig, axs = plt.subplots(contents.shape[1], 2, sharex=False, sharey=False, figsize=(11, 2*len(variable_names)))

    # Plot the data on the subplots
    for i in range(contents.shape[1]): # For every row of subplots
        if(len(variable_names) == 1): # This is needed to enable the plotting of one dimensional systems
            dim = (1)
        else:
            dim = (i, 1)

        # Plot the input data and the forward simulated data obtained after creating the model
        axs[dim].plot(time_series, contents[:, i], 'k', label='input data')
        axs[dim].plot(time_series, sim_data[:, i], 'r--', label='model simulation')
        if(i == 0):
            axs[dim].legend()
        axs[dim].set(xlabel='t', ylabel=variable_names[i].format(i))

        # Loop through the coefficient matrix to extract the non zero values
        coef_plt = [] # List of non zero coefficients (coefficient values)
        desc_plt = [] # List of descriptors for the non zero variables
        row = coefs[i]
        for item in range(len(coefs[0])):
            val = row[item]
            des = feats[item]
            if val != 0:
                coef_plt.append(val)
                desc_plt.append(des)

        if(len(variable_names) == 1): # This is needed to enable the plotting of one dimensional systems
            dim = (0)
        else:
            dim = (i, 0)

        # Plot the non zero coefficient values as a bar plot
        axs[dim].bar(desc_plt,coef_plt)
        axs[dim].axhline(y=0, color='k')
        axs[dim].set_title("d" + str(variable_names[i]) + "/dt",size=10)

        # If the number of output coefficients is greater than 6, change the font size to 8
        if len(coef_plt) > 6:
            size = 8
        else:
            size = 10
        plot_label = axs[dim].get_xticklabels() # Get all of the font label objects for the subplot
        [each_label.set_fontsize(size) for each_label in plot_label] # Set the font size of the specific subplot

    fig.subplots_adjust(hspace=0.3) # Add vertical space in between each row of subplots so they don't overlap
    fig.tight_layout() # Remove excess whitespace from the top and bottom of the figure
    return fig, axs

# Lorenz system for generation - This is taken from the PySINDy feature overview file
def lorenz(z, t):
    return [
        10 * (z[1] - z[0]),
        z[0] * (28 - z[2]) - z[1],
        z[0] * z[1] - (8 / 3) * z[2]
    ]

# Create Lorenz generation window
def show_lorenz():
    lorenz_window = tk.Tk() # Create the Lorenz generation popup window
    lorenz_window.title("Lorenz Data Generation")
    lorenz_window.config(bg=bgc)

    # Create widgets for dt input
    dt_label = tk.Label(lorenz_window,text="dt",font=("Times",15,"bold"),bg=bgc)
    dt_label.grid(row=0,column=0,sticky="E")
    dt_entry = tk.Entry(lorenz_window,font=("Times",15),highlightbackground=bgc,width=10)
    dt_entry.grid(row=0,column=1,columnspan=2,sticky="EW")
    dt_entry.insert(0,"0.002")
    
    # Create widgets for start and end times
    time_label = tk.Label(lorenz_window,text="Times",font=("Times",15,"bold"),bg=bgc)
    time_label.grid(row=1,column=0,sticky="E")
    time_entry1 = tk.Entry(lorenz_window,font=("Times",15),highlightbackground=bgc,width=5)
    time_entry1.grid(row=1,column=1)
    time_entry1.insert(0,"0")
    time_entry2 = tk.Entry(lorenz_window,font=("Times",15),highlightbackground=bgc,width=5)
    time_entry2.grid(row=1,column=2)
    time_entry2.insert(0,"10")

    # Create widgets for the initial conditions
    conds_label = tk.Label(lorenz_window,text="Initial Conditions x,y,z",font=("Times",15,"bold"),bg=bgc)
    conds_label.grid(row=2,column=0,sticky="E")
    conds_entry = tk.Entry(lorenz_window,font=("Times",15),highlightbackground=bgc,width=10)
    conds_entry.grid(row=2,column=1,columnspan=2,sticky="EW")
    conds_entry.insert(0,"-8,8,27")

    # Create widgets to display the number of generated points
    number = ceil((float(time_entry2.get())-float(time_entry1.get()))/float(dt_entry.get()))
    points_label = tk.Label(lorenz_window,text="Number of Points: " + str(number),font=("Times",15,"bold"),bg=bgc)
    points_label.grid(row=3,column=0,columnspan=2,sticky="W")

    # Create the button that continues onto generating the system from the input conditions
    cont_button = tk.Button(lorenz_window,text="Continue",font=("Times",15),width=10,highlightbackground=bgc,command=lambda: lorenz_window.quit())
    cont_button.grid(row=3,column=2,sticky="EW")

    # Bind any key press (within the popup window) with updating the number of generated points
    lorenz_window.bind('<Key>', lambda event: update_number(event, dt_entry, time_entry1, time_entry2, points_label))
    lorenz_window.mainloop()

    # Before destroying the popup window, grab the input conditions
    dt = dt_entry.get()
    t_min = time_entry1.get()
    t_max = time_entry2.get()
    conds = conds_entry.get()

    lorenz_window.destroy() # Destroy the window

    return dt, t_min, t_max, conds

# Update number of points display on generate Lorenz window
def update_number(event, dt_entry, time_entry1, time_entry2, points_label):
    try: 
        number = (float(time_entry2.get())-float(time_entry1.get()))/float(dt_entry.get()) # Calculate the number of points based on the input values
        points_label.configure(text = "Number of Points: " + str(ceil(number)))
    except ZeroDivisionError: # If one of the numbers is equal to 0
        points_label.configure(text = "Number of Points: ")
    except ValueError: # If one of the input values are non numeric
        points_label.configure(text = "Number of Points: ")
    except Exception as e: # Any other exception. This shouldn't happen
        print("Error!\n" + str(e))

def clean_contents_control(contents):
    # Separate the input file into data points, time series and variable names
    numcols = len(contents[0])
    if ((contents[0][numcols-1]) == "u"):
        variable_names = contents[0][1:] # Obtain the system variable names from the data
        del contents[0] # Remove the system variable names from the data matrix
        u = np.array([row[-1] for row in contents]) # Forcing function data
        contents = [row[:-1] for row in contents] # Remove forcing function data from contents
        time_series = np.array([float(val[0]) for val in contents]) # From the first column of the data file, obtain the time series data for the data
        dt = float(time_series[1])-float(time_series[0]) # From the time series data, obtain dt

        contents = [val[1:] for val in contents] # Remove the time series data from the data matrix
        contents = np.array([[float(val) for val in item] for item in contents]) # Turn the list of lists into a numpy array as this is what the PySINDy model expects as an input
        return time_series, dt, contents, u, variable_names
    else:
        raise Exception('Invalid format: contents must be in order of t, [data], u')