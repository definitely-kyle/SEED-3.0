---
title: 'SEED: Software for the Extraction of Equations from Data'
tags:
  - Python
  - graphical user interface
  - dynamical systems
  - model discovery
  - system identification
authors:
  - name: Kyle Kean
    affiliation: 1
  - name: Michael Vause
    affiliation: "1, 2"
  - name: Rui Carvalho
    orcid: 0000-0002-3279-4218
    affiliation: "1, 2"
affiliations:
  - name: Department of Engineering, Durham University, South Road, Durham, DH1 3LE, UK
    index: 1
  - name: Institute for Data Science, Durham University, South Road, Durham, DH1 3LE, UK
    index: 2
date: 02 March 2021
bibliography: paper.bib
---

# Summary

Scientific discovery in the present day has moved increasingly in the direction of machine learning and data-driven methods. This is due to in part to an abundance of measurement options for collecting data from a system, as well as the unrelenting growth of computational power. However, while a huge amount of data which is relevant to a system's behaviour can be collected, the key governing equations are sparse in the space of basis functions. 

`SEED` is an intuitive and comprehensive Graphical User Interface (GUI) for the Python package PySINDy [@deSilva2020] which allows for the extraction of governing differential equations from data. The GUI provides the cutting-edge data-driven methods to researchers in a wide variety fields without any need for prior programming knowledge. 

# Statement of Need

Research in system identification in the Modern Era is primarily led by data-driven methods, such as Sparse Identification of Non-linear Dynamics (SINDy), Dynamic Mode Decomposition (DMD), Koopman Operator. SINDy has been implemented as the python package PySINDy and, while effective, requires considerable knowledge in Python programming to utilise the tools to their full extent. `SEED` remedies this barrier by providing a Graphical User Interface (GUI) with access to all facets of PySINDy while remaining approachable and easy to use.

`SEED` maintains the modular approach core to the PySINDy object and generates the GUI from the source code of the PySINDy package. The allows for the future developments to PySINDy to be automatically captured without need for manual addition to the codebase. One may choose from a selection of numerical differentiation methods, optimiser methods and custom libraries and can change any options within these categories, with typical default values provided. Upon computation `SEED` then creates the SINDy model and provides the output equations and model parameters, which can then be saved for use. Coefficient tables and plots displaying the predicted model versus the input data are also presented in separate windows. `SINDy with Control` (SINDYc) [@BRUNTON2016710] functionality is also provided to allow the user to identify dynamical systems with forcing inputs and control. 

These methods are explained using two key examples, the Lorenz System [@lorenz1963] and the Lotka-Volterra (Predator-Prey) System [@lotka1910]. These two examples have been extensively studied and are very useful as examples for this reason. The Lorenz System is used to demonstrate SEED in standard cases with no forcing function or other control. The Lotka-Volterra System is analysed as an unforced system without using SINDYc, and as a forced system with SINDYc analysis enabled.

# Acknowledgements

The Institute for Data Science, Durham University, generously supported this research.

# References