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
Task: Mergers
=============

Galaxy mergers are a fundamental aspect of galaxy evolution, occurring when two or more galaxies collide and merge, 
ultimately forming a single galaxy. These events can significantly alter the structure and appearance of galaxies.  

Mergers are commonly observed in large galaxy samples and are now considered a key process in the formation of all 
galaxies in the Universe, with nearly every nearby galaxy predicted to have experienced tens or hundreds of mergers.  

During or after a merger, galaxies exhibit distinct morphological features, such as tidal tails, streams, and 
asymmetries. These features create irregularities in a galaxy's appearance, helping astronomers identify ongoing 
or recent mergers.  

__Overview__

We will begin by using light profile fitting tools on simulated merging galaxies to verify that you are able to
apply the tools to merging galaxies successfully.

Next, we will apply these tools to James Webb Space Telescope (JWST) images of real merging galaxies to make 
quantitative statements about the properties of galaxy mergers.

The research project concludes with you writing a report, that includes a literature review on an aspect of galaxy
mergers and presents some of the results of your JWST image analysis.

__Task 1: Simulations__

In this task, we fit simulated images of galaxies, to verify that your light profile fitting analysis works, before
applying it to real James Webb Space Telescope images of galaxies in task 3.

**Task Instructions:**

1. Navigate to the folder `dataset/task_3_mergers`, where you will find two simulated datasets, `merger_1` and `merger_2`.

2. Use the light profile fitting tools to fit a Sersic light profile to each galaxy in both datasets. You can choose to 
   fit each galaxy individually or attempt to fit the Sersic profile to both galaxies simultaneously.

3. Verify that in the `merger_1` dataset, the ratio of the `intensity` of one galaxy to the other is 2:1, and in the `merger_2` dataset, the ratio is 5:1.
"""
# INSERT YOUR CODE HERE

"""
__Task 2: Morphological Features__

As discussed earlier, galaxies undergoing a merger or after a merger can reveal different morphological features.

Before we perform light profile fitting of the JWST images, this task therefore involves visually inspecting the
JWST images of the galaxies and noting any morphological features that are visible at different wavelengths.

In the folder `dataset/task_3_mergers/jwst`, you will find 10 images of real merging galaxies observed with the James Webb
Space Telescope (JWST).

You should therefore first familiarize yourself with common features observed in merging galaxies, for example 
tidal tails, streams, shells, and asymmetries in the light profile. Then, you should visually  inspect the JWST images 
and makes notes of where you think you see these features in the data.

These features are difficult to fit with light profiles using the tools you learned in the previous tutorial,
therefore noting down their presence will be important for the next task.
"""
# INSERT YOUR CODE HERE

"""
__Task 3: Real Galaxies__

Now that you have visually inspected the JWST images of galaxies, your objective is to fit the data with light profiles 
and make quantitative statements about the properties of the merging galaxies.

For 3 merging galaxies of your choice, use the light profile fitting tools to measure the `intensity` ratio of
the mergers (as performed in task 1 above). What is the range of intensity ratios you infer?

Once you are content with the results, read below on task 4 on the report you will write. This report should include 
JWST analysis results specific to the aspect of galaxy mergers you choose to write about. Therefore you will
need to tailor your JWST analysis to the specific subject matter you choose to write about and this analyse a
larger sample of galaxies than just the 3 you chose above.

__Residuals__

Keep in mind that merging galaxies are inherently complex, often exhibiting additional emission and structural features
that may not be perfectly captured by a simple light profile. As a result, the fits will likely show significantly
larger residuals compared to those from simulated galaxies.

Analyzing these residuals can offer further insights into galaxy mergers.
"""
# INSERT YOUR CODE HERE

"""
__Task 4: Report__

The final task involves writing a report, combining a literature review with an analysis of the JWST images.

**Literature Review:**

You are free to choose your focus, but here are some suggested topics and questions to consider:

- Read up on the terms major merger and minor merger and consider how they can be related to the intensity ratios
  you measured.
  
- Another quantity measured is the separation between the merging galaxies, what can this tell you about the
  properties of the merger of galaxies?
  
- The images analysed in this task were two galaxies under going a merger, how long would you expect it to take
  for the galaxies to merger and become a single galaxy?

**JWST Analysis:**

The report should also include figures and results from your analysis of JWST images, directly linked to the aspect of
the literature you choose to write about. 

You are expected to build on the analysis you performed in Task 3, for example reporting different aspects of the 
results and expanding it to more than 3 galaxies.

You should link these results to the topics discussed in your literature review, providing a coherent connection 
between your discussion and the practical JWST analysis and results.
"""