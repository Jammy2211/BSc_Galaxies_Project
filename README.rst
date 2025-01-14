BSc Galaxy Morphology Project
=============================

This repository contains the Jupyter Notebooks and data for the BSc project on galaxy morphology.

This research project uses the Astronomy software package **PyAutoGalaxy** to analysis images of galaxies and study their morphology and structure.

It is recommended to run **PyAutoGalaxy** and undertake the project you use Google Colab, following the instructions described in section 1.4.1 of the project handbook. Google Colab runs **PyAutoGalaxy** via a web browser on a web server, making installation and setup of the software much simpler and providing cloud-based CPU resources to run the project.

However, as described in section 1.4.2 of the project handbook, you may choose to run **PyAutoGalaxy** and undertake the project on your own computer. This requires you to install the software and its dependencies, which can be a more complex process, and is only recommended if you are experienced with Python and software installation and confident in your ability to troubleshoot any issues that may arise. Instructions for how to do this are provided at the bottom of this GitHub page.

Project Structure
-----------------

The project consists of a Jupyter notebook called ``tutorial.ipynb`` which is comprised of four sections describing different aspects of galaxy morphology analysis:

- ``section_1_grids_and_galaxies``: How grids of (y,x) coordinates are used to create images of galaxies that ultimately quantify their morphology.
- ``section_2_data``: Simulating and inspecting telescope imaging data of a galaxy, for example from the Hubble Space Telescope.
- ``section_3_fitting``: How to fit imaging data of a galaxy and quantify whether a fit is good or bad.
- ``section_4_non_linear_searches``: Performing model-fitting via a non-linear search to find the best-fit models describing a galaxy's morphology.

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

This version of the workspace is built and tested for using **PyAutoGalaxy v2024.11.13.2**.

Local Installation (pip)
------------------------

Installation instructions below follow those provided on the **PyAutoGalaxy** documentation website:

`Installation using pip <https://pyautogalaxy.readthedocs.io/en/latest/installation/pip.html>`_:

We strongly recommend that you install **PyAutoGalaxy** in a
`Python virtual environment <https://www.geeksforgeeks.org/python-virtual-environment/>`_, with the link attached
describing what a virtual environment is and how to create one.

We upgrade pip to ensure certain libraries install:

.. code-block:: bash

    pip install --upgrade pip

The latest version of **PyAutoGalaxy** is installed via pip as follows (specifying the version as shown below ensures
the installation has clean dependencies):

.. code-block:: bash

    pip install autogalaxy==2024.11.13.2
    pip install numba

**PyAutoGalaxy** should now be installed and you should be able to successfully run the ``tutorial.ipynb`` Jupyter notebook.

Local Installation (conda)
--------------------------

Installation instructions below follow those provided on the **PyAutoGalaxy** documentation website:

`Installation using conda <https://pyautogalaxy.readthedocs.io/en/latest/installation/conda.html>`_


Installation via a conda environment circumvents compatibility issues when installing certain libraries. This guide
assumes you have a working installation of `conda <https://conda.io/miniconda.html>`_.

First, update conda:

.. code-block:: bash

    conda update -n base -c defaults conda

Next, create a conda environment (we name this ``autogalaxy`` to signify it is for the **PyAutoGalaxy** install):

The command below creates this environment with Python 3.11, the most recent supported version of Python:

.. code-block:: bash

    conda create -n autogalaxy python=3.11

Activate the conda environment (you will have to do this every time you want to run **PyAutoGalaxy**):

.. code-block:: bash

    conda activate autogalaxy

We upgrade pip to ensure certain libraries install:

.. code-block:: bash

    pip install --upgrade pip

The latest version of **PyAutoGalaxy** is installed via pip as follows (the command ``--no-cache-dir`` prevents
caching issues impacting the installation):

.. code-block:: bash

    pip install autogalaxy==2024.11.13.2 --no-cache-dir
    pip install numba

**PyAutoGalaxy** should now be installed and you should be able to successfully run the ``tutorial.ipynb`` Jupyter notebook.