try:
    import pytest
    import matplotlib.pyplot as plt
    import pysindy as ps
    import numpy as np
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

    from base import read_file, clean_contents
except ImportError as mod: # If the user didn't install the required modules beore trying to run SEED 2.0
    print("Install the required modules before starting:\n" + str(mod))
except Exception as err: # Any other exception that should occur (nothing else should happen, hence generalising all other exceptions)
    print("Error while importing:\n" + str(err))

class TestPlots(object):
    def test_default_lorenz(self):
        contents = read_file("data_Lorenz3d.csv", "")
        time_series, dt, contents, variable_names = clean_contents(contents)
        model = ps.SINDy(feature_names = variable_names)
        model.fit(contents, t=dt)
        actual = model.coefficients()

        expected = [[0.0, -10.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 28.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, -2.666, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]]

        assert (pytest.approx(actual, 0.1) == expected)
