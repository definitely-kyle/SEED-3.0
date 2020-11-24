# PySEED

**PySEED**: **Py**thon **S**oftware for the **E**xtraction of **E**quations from **D**ata

**TO DO**
* Unit Testing
* Adding Optimisers (LASSO etc.)
* Analyse Noise Rejection
* General Tidying and Moving to Base Library and Main

## Table of contents
* [Introduction](#introduction)
* [Getting Started](#getting-started)
	* [Installing](#installing)
* [Usage](#usage)
	* [Running SEED 2.X](#running-SEED)
	* [Examples](#examples)
	* [Using your own data](#using-your-own-data)
* [Model Output](#model-output)
* [Future developments](#future-developments)
* [License](#license)

## Introduction
PySEED is a package written in Python that allows for the extraction of governing differential equations from data. It has been written with use of the [PySINDy](https://github.com/dynamicslab/pysindy) package, written by Brian de Silva et al.

PySEED has a simple and intuitive Graphical User Interface (GUI) so that researchers in a wide variety of fields, without needing to know any programming, can analyse their data using these cutting edge methods.

## Getting Started

### Installing
Currently, PySEED has only been tested on Windows. Although it may be able to run on other operating systems, results may vary. For previous iterations which have been tested on Mac, please refer to SEED 2.0, created by Michael Vause.

First, download the files from the PySEED GitHub page. Press the green _Code_ button on the top left and download zip. When downloaded, unzip the downloaded files. After downloading these source files, save them in the same folder anywhere you would like.

* Python:

In order to run PySEED, the user must have a current Python installation, that can be downloaded from the [Python website](https://www.python.org/downloads/). If running PySEED on a Windows system, ensure to select the add python to path option during installation.

As well as the base Python installation, it is vital to install the Python modules needed for the programme to run. You can do this by running these commands in the terminal or command line:

* Windows - command line:

> _python -m pip install matplotlib pysindy pandas_

## Usage

### Running PySEED

To run PySEED from its files, open the Python IDE (included with the Python download) and open the file _SEED2\_0.py_. Click _Run > Run Module_ on the toolbar to run the software.

The GUI will start up and will look like this:

* Mac:

![GUI mac](images/GUI_mac.png)

* Windows:

![GUI win](images/GUI_win.png)

After launching, you can then select your data file and press the _Compute_ button to obtain your output equations.

Check the [PySINDy](https://github.com/dynamicslab/pysindy) GitHub repository for details on the optimization, differentiation and feature library options.

### Examples
There are two datasets that come with the download.

The first, called _data\_Lorenz3d.csv_, contains the data for a three dimensional lorenz system, generated from the [feature overview](https://github.com/dynamicslab/pysindy/blob/master/examples/1_feature_overview.ipynb) example file from the [PySINDy](https://github.com/dynamicslab/pysindy) GitHub repository. 

The second, called _random\_5d.csv_, contains five variables of randomly generated data. This is to show an example of the output of SEED 2.X when a system with no underlying relationship is tested. It is clear that the SINDy algorithm can't settle on sparse coefficients to represent the model.

The ability to generate your own dataset is also built into the program. Just select the _Generate Lorenz Data_ option in the _Example/ Own Data_ dropdown menu. After pressing compute, a window will pop up containing the inital Lorenz conditions of the _data\_Lorenz3d.csv_ data. You can then edit the conditions to generate your own system. After pressing _Continue_, PySEED will generate the system, and compute its output.

### Using your own data
In order to use your own data with PySEED, you must save the data as a _.csv_ file with one column of time series data, and further columns containing the data for each recorded variable. The first row of your _.csv_ file must be the names of each variable.  
An example of a three variable system is shown below:

![own data](images/Own_Data.png)

There are two ways to run the program with your own data files.

The first is to select _Own Data_ in the _Example/Own Data_ dropdown selection box on the main panel of the GUI, then using the file browser, you can then select the file containing your data.

You can also save the data file in the data folder containing the example data files that came with the SEED 2.X download, then select it in the dropdown after running SEED 2.X.

## Model Output
After pressing compute, SEED 2.X uses the selections on the main GUI window to make a PySINDy model using the selected data. The first output window displays the output sparse coefficients in a table, and automatically forms the output equations. It also calculates and displays the model score, an inbuilt feature to PySINDy. An example of this window, on MacOS, can be seen below:

![output window 1](images/window1.png)

The second output window displays two sets of plots. The first set shows the coefficients for each output equation in bar plots to easily visualise which terms in each equation are more important. The second set of plots shows the selected input data plotted against simulated data, created using the input data's initial conditions, evolved using the model's output equations. This can be seen below:

![output window 2](images/window2.png)

Pressing the save button on this window saves both a _.png_ of the output plots and a _.csv_ of the output coefficient matrix to the filepath selected.

Both example output windows are the MacOS versions.

## Future Developments
As well as the current features of PySINDy integrated into SEED 2.X, there are a number of features currently in development to be released in the near future. This includes but is not limited to:

* Integration of the Lasso method for system optimization
* Loading a previous model from the saved .csv file
* The ability to use a custom feature library
* The ability to combine feature librarys
* Integrating SINDy with control
* The usage of different forms of input data, as shown on the PySINDy [feature overview](https://github.com/dynamicslab/pysindy/blob/master/examples/1_feature_overview.ipynb)
* Adding tooltips explaining each of the options
