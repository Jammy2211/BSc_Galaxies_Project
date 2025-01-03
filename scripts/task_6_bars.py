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
Task: Bars
==========

Bars are an important structural component that can be observed in galaxies.  

A galaxy bar is a linear structure composed of stars, gas, and dust that extends from the central bulge and usually 
aligns with the galaxy's major axis. Bars are most commonly found in spiral galaxies, where they act as a conduit 
for material, helping channel gas and dust into the central regions, potentially triggering star formation.  

Bars are thought to form through gravitational instabilities in the galaxy’s disk, often becoming more pronounced 
as a galaxy evolves. They play a key role in the dynamics of a galaxy, influencing its star formation activity, 
gas distribution, and the overall morphology. The presence and characteristics of a bar can provide important clues 
about the galaxy’s age, dynamical state, and history.  

Bars are relatively common in galaxies, particularly in barred spiral galaxies, where they are seen in 
about 30-50% of spirals. However, it remains unclear whether bars are a permanent feature or a transient phenomenon 
in a galaxy's evolution. Some studies suggest that bars may dissolve over time, while others propose that they 
evolve and change in strength, leading to varying lifespans and possible transitions to other forms of galaxy structure.

__Overview__

We will begin by using light profile fitting tools on simulated galaxies, where the appearance of the simulated
galaxies vary over wavelength. 

Next, we will apply these tools to James Webb Space Telescope (JWST) images of real galaxies to make our own
quantitative measurement of whether a bar is present in a galaxy.

The research project concludes with you writing a report, that includes a literature review on an aspect of galaxy
colours and presents some of the results of your JWST image analysis.

__Task 1: Simulations__

In this task, we fit simulated images of galaxies to verify the accuracy of your light profile fitting analysis before 
applying it to real James Webb Space Telescope images in Task 3.

To identify a bar within a galaxy, we need to include it as an additional light profile in our galaxy model. While 
there are different profiles used by astronomers to represent a bar, a common choice is a **Sersic** profile with 
a **sersic_index** of 0.5, which is much lower than the typical values we used in the previous tutorial.

This bar profile should be fitted on top of the regular **Sersic** profile used in the previous task, which accounts 
for the majority of the galaxy's emission. As a result, the model will include two separate **Sersic** profiles: one 
for the bar and one for the remaining galaxy emission.

**Task Instructions:**

1. Navigate to the folder `dataset/task_6_bars`, where you will find the simulated datasets `bar_0` and `bar_1`. 
   Visually inspect the images, you should note there is a elongated central bar shaped emission, at 45 degree from 
   the x-axis over the top of the surrounding rounder emission. This is the bar.

2. Use the light profile fitting tools to fit a model composed of two Sersic light profiles, where one Sersic light 
   profile has its `sersic_index` fixed to a value of 0.5, to each dataset.

3. Verify that the `effective_radius` inferred for the fit to `bar_0` is 0.3 and that for `bar_1` is 0.8.
"""
# INSERT YOUR CODE HERE

"""
__Task 2: Model Comparison__

For the simulated datasets, we knew they contained a bar because they were specifically simulated with one. However, 
for real datasets, we lack this information, so we need a quantitative method to determine if a galaxy has a bar.

Model comparison enables us to achieve this by fitting two models: one without a bar (e.g., a single `Sersic` 
profile) and one with a bar (e.g., a `Sersic` profile plus a second `Sersic` with a `sersic_index=0.5` for the bar).

By comparing the quality of the fits from these different models, we can identify which one better matches the data, 
helping to determine whether a galaxy is more likely to have a bar.

**Task Instructions:**

1. Fit a single `Sersic` model to the `bar_0` and `bar_1` galaxy datasets.

2. Verify that the single `Sersic` fits are worse than the fits performed in Task 1 by comparing the `log_likelihood` values.

3. Load the `no_bar` dataset from the `dataset` folder, fit it with both the single `Sersic` model and the model 
   including a bar (i.e., a second `Sersic` with a `sersic_index=0.5`), and verify that the `log_likelihood` values 
   do not improve when a bar is included.

By completing this task, you will confirm that there is a quantitative method to determine whether a galaxy has a bar.
"""
# INSERT YOUR CODE HERE

"""
__Task 3: Real Galaxies__

In the folder `dataset/task_6_bars/jwst`, you will find 10 images of real galaxies observed with the James Webb
Space Telescope (JWST). 

For 3 galaxies of your choice, use the light profile fitting tools to determine if you think they possess a bar
or not.

Quantitatively inferring whether a galaxy has a bar in real galaxy images is highly challenging. It's possible to be 
visually confident that a galaxy contains a bar, but the model comparison results may not support this, or vice versa. 
Therefore, it is important to pair your quantitative model comparison analysis with a visual inspection of each galaxy. 
Be prepared to make a judgment about whether a galaxy has a bar, regardless of the model comparison results.

Once you are content with the results, read below on task 4 on the report you will write. This report should include 
JWST analysis results specific to the aspect of galaxy bars you choose to write about. Therefore you will
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

- Research how bars affect the stellar dynamics of galaxies and their formation processes.

- There is debate about whether bars are transient phenomena that form and disappear, or if they persist once formed. 
  Investigate this topic and consider how light profile fitting could help address this question.

- You used model comparison to determine if galaxies contain a bar, but this process may not have worked perfectly 
  for the JWST images. Discuss possible reasons for imperfections and suggest ways to improve the method.
  
**JWST Analysis:**

The report should also include figures and results from your analysis of JWST images, directly linked to the aspect of
the literature you choose to write about. 

You are expected to build on the analysis you performed in Task 3, for example reporting different aspects of the 
results and expanding it to more than 3 galaxies.

You should link these results to the topics discussed in your literature review, providing a coherent connection 
between your discussion and the practical JWST analysis and results.
"""