try:
    import pytest
    import matplotlib.pyplot as plt
    import pysindy as ps
    import numpy as np
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

    from base import read_file, clean_contents, create_plot
except ImportError as mod: # If the user didn't install the required modules beore trying to run SEED 2.0
    print("Install the required modules before starting:\n" + str(mod))
except Exception as err: # Any other exception that should occur (nothing else should happen, hence generalising all other exceptions)
    print("Error while importing:\n" + str(err))

class TestLorenz(object):
    def test_default_lorenz_model(self):
        contents = read_file("data_Lorenz3d.csv", "")
        time_series, dt, contents, variable_names = clean_contents(contents)
        model = ps.SINDy(feature_names = variable_names)
        model.fit(contents, t=dt)

        actual_co = model.coefficients()
        actual_score = model.score(contents, t = time_series)

        expected_co = [[0.0, -10.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 28.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, -2.666, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]]
        expected_score = 1.0

        assert (pytest.approx(actual_co, 0.1) == expected_co)
        assert (pytest.approx(actual_score, 0.01) == expected_score)

    @pytest.mark.mpl_image_compare
    def test_default_lorenz_plot(self):
        contents = read_file("data_Lorenz3d.csv", "")
        time_series, dt, contents, variable_names = clean_contents(contents)
        model = ps.SINDy(feature_names = variable_names)
        model.fit(contents, t=dt)

        coefs = model.coefficients()
        feats = model.get_feature_names() # Get the feature names from the obtained model

        conds = np.array([float(val) for val in contents[0]]) # Convert the system's initial conditions into a numpy array of float values as this is what is expected by the model.simulate() function
        sim_data = model.simulate(conds,time_series) # Create the forward simulated data. This uses the original initial conditions evolved with the model output equations to obtain new data
        

        fig, _ = create_plot(time_series, contents, variable_names, coefs, feats, sim_data)

        return fig

class TestRandom5d(object):  
    def test_default_5d_model(self):
        contents = read_file("random_5d.csv", "")
        time_series, dt, contents, variable_names = clean_contents(contents)
        model = ps.SINDy(feature_names = variable_names)
        model.fit(contents, t=dt)

        _ = model.coefficients()
        actual_score = model.score(contents, t = time_series)

        # expected_coefficients should be incomprehensible
        expected_score_max = 0.1 # model is expected to fail 

        # assert (pytest.approx(actual_co, 0.1) == expected_co)
        assert actual_score < expected_score_max # model is expected to score poorly (less than 0.1)


