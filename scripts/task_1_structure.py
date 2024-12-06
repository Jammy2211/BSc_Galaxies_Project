"""
Project Setup
=============

At the beginning of the `tutorial.ipynb` notebook, steps were performed to ensure auto-saving of progress,
installation of the Python libraries used by the project and downloading of the GitHub repository.

These steps are now repeated in this task notebook, make sure you run them before proceeding with the task!

Project Setup: Colab Setup
==========================

To set up Google Colab for the research project, follow these steps to ensure your progress is saved. These
instructions are also detailed in the accompanying document, which includes images for guidance.

First, connect Google Colab to your Google account and Google Drive. This setup ensures your work is autosaved and
preserved even if you close your browser tab or window. Next, open the tutorial notebook in Colab, click on
the "File" tab in the top-left corner, and select "Save a copy in Drive." This action will create a duplicate of the
notebook and open it in a new tab titled "Copy of task_filename.ipynb."

In the new tab, rename the notebook by clicking on its title in the top-left corner. Change it
from "Copy of task_filename.ipynb" to "YOUR_NAME_task_filename.ipynb," replacing "YOUR_NAME" with your actual name.
With these steps complete, the notebook will now autosave your changes to your Google Drive, ensuring your
progress is retained.

Project Setup: Software Installation
====================================

Next, install the Python software libraries required for this research project. In Google Colab, this can be done
easily by running the cell below in the Jupyter Notebook.

If prompted to restart the session after installation, do so and then rerun the cell to ensure all libraries are
properly installed.
"""
!pip install autogalaxy
!pip install numba

"""
Project Setup: Repository Clone
===============================

The code below retrieves the project files from the GitHub repository.
"""
!git clone https://github.com/Jammy2211/BSc_Galaxies_Project

"""
Task 1: Structure
=================

Galaxy structure refers to the fundamental characteristics of galaxies, which are generally grouped into three main
structural categories:

- **Ellipticals:** Galaxies with a smooth, featureless light profile, where stellar orbits are randomly oriented and "velocity dispersion supported."

- **Disk galaxies:** Galaxies with a more intricate light profile, characterized by stellar orbits predominantly in a rotating disk, making them "rotationally supported."

- **Irregulars:** Galaxies that do not fit into the first two categories, often displaying complex or asymmetric light profiles, such as those resulting from merger events.

We will begin by using light profile fitting tools on simulated galaxies to distinguish between elliptical and disk
galaxies, employing one of the methods astronomers use for galaxy classification. We will not consider irregular
galaxies in this project, which are difficult to fit with light profiles due to their complex structure.

Next, we will apply these tools to James Webb Space Telescope (JWST) images of real galaxies to classify a small sample
into elliptical and disk categories.

The research project concludes with an open-ended task: to explore this classification further by reading more on the
division between elliptical and disk galaxies and writing a short report on the subject.

__Task 1: Structural Decomposition__

To classify galaxies as elliptical or disk galaxies, the following light profile fitting method is applied:

- **Elliptical galaxies**: These typically exhibit a Sersic light profile with a `sersic_index` ranging from 2.5 to 4.0. Thus, if a Sersic profile fitted to a galaxy results in an inferred `sersic_index` above 2.5, the galaxy is likely elliptical.

- **Disk galaxies**: These generally have a Sersic light profile with a `sersic_index` of 1.0. Therefore, if a Sersic profile fitted to a galaxy yields an inferred `sersic_index` below 2.5, the galaxy is likely a disk galaxy.

**Task Instructions:**

1. Navigate to the folder `dataset/task_1_structure`, where you will find two simulated galaxy datasets: `disk` and `elliptical`.

2. Use the light profile fitting tools to fit a Sersic light profile to each dataset.

3. Verify that the fitting results align with the true `sersic_index` values:

   - The galaxy dataset named `disk` has a true `sersic_index` of **1.0**.
   - The galaxy dataset named `elliptical` has a true `sersic_index` of **4.0**.

By successfully fitting the Sersic profile and recovering these values, you will confirm the accuracy of your light profile fitting tools.
"""
# INSERT YOUR CODE HERE

"""
__Task 2: Model Comparison__

Certain Sersic profiles have specific names when their `sersic_index` takes particular values:

- A Sersic profile with a **`sersic_index` of 4.0** is called a **De Vaucouleurs profile**. In **PyAutoGalaxy**, it can be fitted using the `ag.lp.DevVaucouleurs` class.
- A Sersic profile with a **`sersic_index` of 1.0** is called an **Exponential profile**. In **PyAutoGalaxy**, it can be fitted using the `ag.lp.Exponential` class.

These classes allow you to model the light profiles of galaxies with predefined Sersic indices, using the same Python code introduced in previous tutorials.

**Task Instructions:**

1. Fit the `De Vaucouleurs` profile (`ag.lp.DevVaucouleurs`) to the **`elliptical`** galaxy dataset and 
   the `Exponential` profile (`ag.lp.Exponential`) to the **`disk`** galaxy dataset, and confirm that the fits are 
   successful.

2. Fit both the `De Vaucouleurs` and `Exponential` profiles to the other dataset (`elliptical` and `disk`) and verify
   that the fits are unsuccessful using the `log_likelihood` values.

By completing this task, you will confirm that the `De Vaucouleurs` and `Exponential` profiles accurately capture the
structure of elliptical and disk galaxies, respectively, using **PyAutoGalaxy**'s specialized light profile fitting tools.
"""
# INSERT YOUR CODE HERE

"""
__Task 3: Real Galaxies__

In the folder `dataset/task_1_structure/jwst`, you will find 10 images of real galaxies observed with the James Webb
Space Telescope (JWST). Your objective is to classify each galaxy as either elliptical or disk-shaped using light profile fitting tools.

You can achieve this by applying either of the methods discussed earlier or by combining them for a more robust
classification.

Keep in mind that real galaxies are inherently complex, often exhibiting additional emission and structural features
that may not be perfectly captured by a simple light profile. As a result, the fits will likely show significantly
larger residuals compared to those from simulated galaxies.

Analyzing these residuals can offer further insights into whether a galaxy is elliptical or disk-shaped and reveal
properties that these residuals might represent.
"""
# INSERT YOUR CODE HERE

"""
__Task 4: Report__

For the final task, you are required to write a short report on the division between elliptical and disk galaxies.

The subject matter is open ended, but you may wish to consider the following points:

- How does the division of galaxy structures into elliptical and disk galaxies relate to the original clclassification
  scheme proposed by Edwin Hubble?
  
- What are the key differences between elliptical and disk galaxies in terms of their stellar dynamics?

- What are the key differences between elliptical and disk galaxies in terms of their current star formation activity
  and star formation histories?
"""