# Library to contain some useful functions to reduce clutter in main SEED file
# Created 28/10/2020 by Kyle Kean

# Import packages
import numpy as np
import csv

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

    return(data)