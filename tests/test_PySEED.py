try:
    import pytest
    import matplotlib.pyplot as plt
    import pysindy as ps
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

    from PySEED import *  
except ImportError as mod: # If the user didn't install the required modules beore trying to run SEED 2.0
    print("Install the required modules before starting:\n" + str(mod))
except Exception as err: # Any other exception that should occur (nothing else should happen, hence generalising all other exceptions)
    print("Error while importing:\n" + str(err))

class TestPlots(object):

    @pytest.mark.mpl_image_compare
    def test_default_lorenz(self):
        contents = read_file("data_Lorenz3d.csv")
        time_series, dt, contents, variable_names = clean_contents(contents)

        

        