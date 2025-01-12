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
!pip install autogalaxy==2024.11.13.2
!pip install numba

"""
Project Setup: Repository Clone
===============================

The code below retrieves the project files from the GitHub repository.
"""
!git clone https://github.com/Jammy2211/BSc_Galaxies_Project

"""
Task: Colours
=============

Galaxies appear differently at different wavelengths, making the study of galaxy colors crucial for understanding their formation and evolution.  

Linking a galaxy's color to its formation history requires understanding star formation and how stars emit across wavelengths:  

- **Bluer wavelengths** trace more massive, recently formed stars, revealing the galaxy’s recent history, such as periods of sustained star formation.  
- **Redder wavelengths** trace lower-mass stars that formed earlier, providing insights into the galaxy's long-term history and formation.  

This also means that certain structures, such as star-forming knots or spiral arms, are more prominent in bluer wavelengths.    

Understanding how galaxy observations vary with wavelength is essential. For this task, the James Webb Space Telescope provides data in two filters:  

- `F115W`: Observations in the near-infrared at 1.15 microns.
- `F444W`: Observations in the mid-infrared at 4.44 microns. 

__Overview__

We will begin by using light profile fitting tools on simulated galaxies, where the appearance of the simulated
galaxies vary over wavelength. 

Next, we will apply these tools to James Webb Space Telescope (JWST) images of real galaxies to make our own
inference on how a galaxy's appearance changes over wavelength.

The research project concludes with you writing a report, that includes a literature review on an aspect of galaxy
colours and presents some of the results of your JWST image analysis.

__Task 1: Simulations__

In this task, we fit simulated images of galaxies, to verify that your light profile fitting analysis works, before
applying it to real James Webb Space Telescope images of galaxies in task 3.

To investigate how a galaxy's appearance changes over wavelength, we fit light profiles to images of galaxies
observed at different wavelengths.

**Task Instructions:**

1. Navigate to the folder `dataset/task_2_colours`, where you will find the 
simulated datasets `F115W` and `F444W`.

2. Use the light profile fitting tools to fit a Sersic light profile to each dataset.

3. Verify that the fitting results demonstrate a trend where the `effective_radius` increases with wavelength. 
   Specifically, the `effective_radius` should be lowest in the F115W data and highest in the F444W data.
"""
# INSERT YOUR CODE HERE

"""
__Task 2: Morphological Features__

As discussed earlier, the appearance of galaxies at different wavelengths can reveal different morphological features.

Before we perform light profile fitting of the JWST images, this task therefore involves visually inspecting the
JWST images of each galaxy and noting any morphological features that are visible at different wavelengths.

In the folder `dataset/task_2_colours/jwst`, you will find 10 images of real galaxies observed with the James Webb
Space Telescope (JWST), all observed at the two wavelengths `F115W` and `F444W`. 

You should therefore first familiarize yourself with common features observed in galaxies, in particular spiral
arms, bars, bulges, disks and knots of star formation. Then, you should visually inspect the JWST images
and makes notes of where you think you see these featurs in the data.

These features are difficult to fit with light profiles using the tools you learned in the previous tutorial,
therefore noting down their presence will be important for the next task.
"""
# INSERT YOUR CODE HERE

"""
__Task 3: Real Galaxies__

Now that you have visually inspected the JWST images of galaxies, your objective is to fit the different wavelength
data with light profiles and compare how the results vary with wavelength. 

For 3 galaxies of your choice, use the light profile fitting tools to fit each galaxy at each wavelength of data
and make a plot where wavelength is on the x axis and `effective_radius` is on the y axis. How do these galaxies
change their size over wavelength?

Once you are content with the results, read below on task 4 on the report you will write. This report should include 
JWST analysis results specific to the aspect of galaxy colours you choose to write about. Therefore you will
need to tailor your JWST analysis to the specific subject matter you choose to write about and this analyse a
larger sample of galaxies than just the 3 you chose above.

__Residuals__

Keep in mind that real galaxies are inherently complex, exhibiting the structural features you noted in task 2, that
may not be perfectly captured by a simple light profile. As a result, the fits will likely show significantly
larger residuals compared to those from simulated galaxies.
"""
# INSERT YOUR CODE HERE

"""
__Task 4: Report__

The final task involves writing a report, combining a literature review with an analysis of the JWST images.

**Literature Review:**

The report should include a concise literature review focusing on a specific topic related to how the appearance of 
galaxies changes over wavelength.

You are free to choose your focus, but here are some suggested topics and questions to consider:

- Familiarize yourself with what a galaxy redshift is, and consider how the redshift of a galaxy can affect its
  appearance depending on which wavelengths you observe it at.
  
- Research how the wavelength at which stars emit light depends on the properties of the stars, and relate this
  to how it affects the appearance of galaxies at different wavelengths.

- Do more reading on the types of morphological features that are visible in galaxies at different wavelengths,
  and consider why these features are more visible at certain wavelengths.
  
**JWST Analysis:**

The report should also include figures and results from your analysis of JWST images, directly linked to the aspect of
the literature you choose to write about. 

You are expected to build on the analysis you performed in Task 3, for example reporting different aspects of the 
results and expanding it to more than 3 galaxies.

You should link these results to the topics discussed in your literature review, providing a coherent connection 
between your discussion and the practical JWST analysis and results.
"""