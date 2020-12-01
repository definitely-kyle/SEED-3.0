# Library to contain some useful functions to reduce clutter in main SEED file
# Created 28/10/2020 by Kyle Kean

# Import packages
import numpy as np
import csv
import matplotlib.pyplot as plt

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
        to_read = "./src/data/" + selection

    with open(to_read, newline='') as csvfile:
        data = list(csv.reader(csvfile))  

    return data

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
