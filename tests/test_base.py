import pytest
import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

try:
    from base import switch, clean_contents, read_file
except ImportError as mod: # If the user didn't install the required modules beore trying to run SEED 2.0
    print("Install the required modules before starting:\n" + str(mod))
except Exception as err: # Any other exception that should occur (nothing else should happen, hence generalising all other exceptions)
    print("Error while importing:\n" + str(err))

class TestSwitch(object):
    def test_switch_with_correct_input(self):
        actual = [switch("finite_difference"), switch("savitzky_golay"), switch("spectral"), switch("spline"), switch("trend_filtered")]
        expected = [0, 1, 2, 3, 4]

        assert actual == expected

    def test_switch_with_bad_input(self):
        assert switch(200) == 0

class TestReadData(object):
    def test_default_lorenz(self):
        ts, dt, cont, vars = clean_contents(read_file("data_Lorenz3d.csv", ""))
        ts = ts[0:4]
        cont = cont[0:4]

        expected_ts = [0., 0.002, 0.004, 0.006]
        expected_dt = 0.002
        expected_cont = [   [-8,8,27], 
                            [-7.683508382,7.966250523,26.73151873], 
                            [-7.373984577,7.92929174,26.46998112], 
                            [-7.071350036,7.889537629,26.21523996]
                            ]
        expected_vars = ["x", "y", "z"]

        assert np.all(ts == expected_ts)
        assert np.all(dt == expected_dt)
        assert np.all(cont == expected_cont)
        assert np.all(vars == expected_vars)

    def test_random_5d(self):
        ts, dt, cont, vars = clean_contents(read_file("random_5d.csv", ""))
        ts = ts[0:4]
        cont = cont[0:4]

        expected_ts = [0., 0.001, 0.002, 0.003]
        expected_dt = 0.001
        expected_cont = [   [3.216510998,9.914181513,3.866592635,0.746334938,4.606170334],
                            [0.650685986,4.486606167,5.84805047,1.991102499,5.211598163], 
                            [1.318906913,8.869120427,2.594125945,9.226401504,2.357597024],
                            [8.26282217,2.762088665,1.941167642,5.280758711,4.70049113]
                            ]
        expected_vars = ["a", "b", "c", "d", "e"]

        assert np.all(ts == expected_ts)
        assert np.all(dt == expected_dt)
        assert np.all(cont == expected_cont)
        assert np.all(vars == expected_vars)
