BSc Galaxy Morphology Project
=============================

This repository contains the Jupyter Notebooks and data for the BSc project on galaxy morphology.

The project can be completed at an online web server by following the link below:

https://mybinder.org/v2/gh/Jammy2211/BSc_Galaxies_Project/HEAD

Project Structure
-----------------

The project consists of a Jupyter notebook called ‘`tutorial.ipynb‘` which is comprised of four sections describing different aspects of galaxy morphology analysis:

- ``section_1_grids_and_galaxies.ipynb``: How grids of (y,x) coordinates are used to create images of galaxies that ultimately quantify their morphology.
- ``section_2_data.ipynb``: Simulating and inspecting telescope imaging data of a galaxy, for example from the Hubble Space Telescope.
- ``section_3_fitting.ipynb``: How to fit imaging data of a galaxy and quantify whether a fit is good or bad.
- ``section_4_non_linear_searches.ipynb``: Performing model-fitting via a non-linear search to find the best-fit models describing a galaxy's morphology.

You will then complete a task which uses what you learned in the tutorials to analyse James Webb Space Telescope imaging data of real galaxies.

There are 6 six tasks in total, you should have been assigned one of the following:

- ``task_1_structure.ipynb``: Investigate the structural classification of a sample of galaxies compared to where they should appear on the Hubble Tuning Fork diagram.
- ``task_2_colours.ipynb``: Investigate how galaxies change their appearance when they are observed at different wavelengths.
- ``task_3_mergers.ipynb``: Perform analysis of imaging data containing two merging galaxies and estimate quantities describing the properties of the merger.
- ``task_4_sizes.ipynb``: Estimate the sizes of a sample of galaxies and consider different ways that the size of galaxies can be measured.
- ``task_5_ellipticity.ipynb``: Quantify how elliptical galaxies appear in projection and consider how that relates to three-dimensional stellar distribution.
- ``task_6_bars.ipynb``: Analyse a sample of galaxies which contain a morphological structure called a bar.

The workspace includes the following additional directories:

- ``scripts``: **PyAutoLens** examples written as Python scripts.
- ``dataset``: Where data is stored, including example datasets distributed.

Workspace Version
-----------------

This version of the workspace is built and tested for using **PyAutoGalaxy v2024.11.6.1**.
