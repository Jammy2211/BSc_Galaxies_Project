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
Task: Sizes
===========

The sizes of galaxies are a fundamental property that offer key insights into their formation and evolutionary history.  

As galaxies evolve, they typically grow in size through two main processes: the formation of new stars and mergers 
with other galaxies. These processes gradually build up a galaxy's mass and structure over time. Consequently, 
larger galaxies are generally older, as they have had more time to undergo these growth mechanisms.  

By studying the sizes of large samples of galaxies, astronomers can piece together a coherent picture of how 
galaxies have evolved over the 13.7 billion years of the Universe's history. Such studies also reveal trends in 
galaxy growth rates across different epochs, helping us understand the role of star formation, mergers, and 
environmental factors in shaping the diversity of galaxies we observe today.  

__Overview__

We will begin by using light profile fitting tools on simulated galaxies to verify that you are able to measure
the sizes of galaxies using light profile fitting successfully.

Next, we will apply these tools to James Webb Space Telescope (JWST) images of real galaxies to make quantitative
statements about their sizes.

The research project concludes with you writing a report, that includes a literature review on an aspect of galaxy
sizes and presents some of the results of your JWST image analysis.

__Task 1: Simulations__

In this task, we fit simulated images of galaxies, to verify that your light profile fitting analysis works, before
applying it to real James Webb Space Telescope images of galaxies in task 3.

**Task Instructions:**

1. Navigate to the folder `dataset/task_4_sizes`, where you will find two simulated datasets, `small` and `large`.

2. Use the light profile fitting tools to fit a Sersic light profile to each dataset.

3. Verify that the `effective_radius` inferred by the fit for the `small` dataset is 0.5" and for the `large` dataset is 2.0".
"""
# INSERT YOUR CODE HERE

"""
__Task 2: Quantifying Size__

The `effective_radius` defines the size of a galaxy as the radius containing half its luminous emission.

Use the function `galaxy.image_2d_from()` to create 2D images of the simulated galaxies you fitted above and verify 
that 50% of the luminosity is contained within the `effective_radius` values you measured above.
"""
# INSERT YOUR CODE HERE

"""
__Task 3: Real Galaxies__

In the folder `dataset/task_4_sizes/jwst`, you will find 10 images of real galaxies observed with the James Webb
Space Telescope (JWST). 

For 3 galaxies of your choice, use the light profile fitting tools to measure the sizes of three galaxies in the 
dataset. 

You should then make plots comparing the measured sizes on the x axis with other measured galaxy properties, 
such as `intensity` and `sersic_index`. 

Once you are content with the results, read below on task 4 on the report you will write. This report should include 
JWST analysis results specific to the aspect of galaxy sizes you choose to write about. Therefore you will
need to tailor your JWST analysis to the specific subject matter you choose to write about and this analyse a
larger sample of galaxies than just the 3 you chose above.

__Residuals__

Keep in mind that real galaxies are inherently complex, often exhibiting additional emission and structural features
that may not be perfectly captured by a simple light profile. As a result, the fits will likely show significantly
larger residuals compared to those from simulated galaxies.
"""
# INSERT YOUR CODE HERE

"""
__Task 4: Report__

The final task involves writing a report, combining a literature review with an analysis of the JWST images.

**Literature Review:**

You are free to choose your focus, but here are some suggested topics and questions to consider:

- Read up on the "fundamental plane" of elliptical galaxies. What is it and how does it relate to the sizes of galaxies?

- Read up on the Tully-Fisher relation. What is it and how does it relate to the sizes of galaxies?

- The `effective_radius` defines the size of a galaxy as the radius containing half its luminous emission. What other
ways could a galaxy's size be defined and how would they compare to the `effective_radius`?
  
**JWST Analysis:**

The report should also include figures and results from your analysis of JWST images, directly linked to the aspect of
the literature you choose to write about. 

You are expected to build on the analysis you performed in Task 3, for example reporting different aspects of the 
results and expanding it to more than 3 galaxies.

You should link these results to the topics discussed in your literature review, providing a coherent connection 
between your discussion and the practical JWST analysis and results.
"""