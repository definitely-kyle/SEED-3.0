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

class TestLorenz(object):
    def test_default_lorenz_coefficients(self):
        contents = read_file("data_Lorenz3d.csv", "")
        time_series, dt, contents, variable_names = clean_contents(contents)
        model = ps.SINDy(feature_names = variable_names)
        model.fit(contents, t=dt)

        actual_co = model.coefficients()
        actual_score = model.score(contents, t = time_series)

        expected_co = [[0.0, -10.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 28.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, -2.666, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]]
        expected_score = 1.0

        assert (pytest.approx(actual_co, 0.1) == expected_co)
        assert (pytest.approx(actual_score, 0.1) == expected_score)

    @pytest.mark.mpl_image_compare
    def test_default_lorenz_plot(self):
        contents = read_file("data_Lorenz3d.csv", "")
        time_series, dt, contents, variable_names = clean_contents(contents)
        model = ps.SINDy(feature_names = variable_names)
        model.fit(contents, t=dt)

        coefs = model.coefficients()
        feats = model.get_feature_names() # Get the feature names from the obtained model
        score = model.score(contents, t=time_series) # Obtain the model score for the system

        conds = np.array([float(val) for val in contents[0]]) # Convert the system's initial conditions into a numpy array of float values as this is what is expected by the model.simulate() function
        sim_data = model.simulate(conds,time_series) # Create the forward simulated data. This uses the original initial conditions evolved with the model output equations to obtain new data
        

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

        return fig

        


