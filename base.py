# Library to contain some useful functions to reduce clutter in main SEED file
# Created 28/10/2020 by Kyle Kean

# Import packages


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

