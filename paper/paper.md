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
date: 23 April 2021
bibliography: paper.bib
---

# Summary

Scientific discovery in the present day has moved increasingly in the direction of machine learning and data-driven methods due to an abundance of options for collecting data, as well as the unrelenting growth of computation. While scientists routinely collect vast amounts of data, finding a system's governing equations is a manual and laborious process.

`SEED` is an intuitive and comprehensive Graphical User Interface (GUI) for the Python package PySINDy [@deSilva2020], which allows for the extraction of governing differential equations from data. The GUI provides researchers in various fields with access to PySINDy's functionality without any need for prior programming knowledge.

# Statement of Need

Data-driven methods and sparsity algorithms lead current research in system identification. One such method is the Sparse Identification of Non-linear Dynamics (SINDy) [@Brunton3932]. SINDy is implemented as the python package PySINDy and, while effective, requires considerable knowledge in Python programming to utilise the tools to their full extent. `SEED` remedies this barrier by providing a Graphical User Interface (GUI) with access to all facets of PySINDy while remaining approachable and easy to use.

`SEED` maintains the modular approach core to the PySINDy model and generates the GUI from the package's source code, allowing for future developments to PySINDy to be automatically captured without the need for manual addition to the codebase. Users can select the numerical differentiation methods, optimiser methods and custom libraries and change any options within these categories, with typical default values provided. Upon computation, SEED then creates a SINDy model, and the user can display and save the output equations and model parameters.  The software also shows coefficient tables and plots displaying the predicted model versus the input data in separate windows.  Moreover, SEED provides the functionality of SINDy with Control (SINDYc) [@BRUNTON2016710] to allow the user to identify dynamical systems with forcing inputs and control.

We illustrate SEED's functionality with two extensively studied examples, the Lorenz System [@lorenz1963] and the Lotka-Volterra (Predator-Prey) System [@lotka1910]. We use the Lorenz system to demonstrate `SEED` with no forcing function or other control. In contrast, the Lotka-Volterra System is an unforced system without using SINDYc, and a forced system with SINDYc analysis enabled.

# Acknowledgements

The Institute for Data Science, Durham University, generously supported this research.

# References
