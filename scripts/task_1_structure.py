"""
Project Setup
=============

At the beginning of the `tutorial.ipynb` notebook, steps were performed to ensure auto-saving of progress,
installation of the Python libraries used by the project, downloading of the GitHub repository and setting up the
working directory and configuration files.

These steps are now repeated in this task notebook, make sure you run them before proceeding with the task!

Project Setup: Colab Setup
==========================

To set up Google Colab for the research project, follow these steps to ensure your progress is saved. These
instructions are also detailed in the accompanying document, which includes images for guidance.

First, connect Google Colab to your Google account and Google Drive. This setup ensures your work is autosaved and
preserved even if you close your browser tab or window. Next, open the tutorial notebook in Colab, click on
the "File" tab in the top-left corner, and select "Save a copy in Drive." This action will create a duplicate of the
notebook and open it in a new tab titled "Copy of tutorial.ipynb."

In the new tab, rename the notebook by clicking on its title in the top-left corner. Change it
from "Copy of tutorial.ipynb" to "YOUR_NAME_tutorial.ipynb," replacing "YOUR_NAME" with your actual name.
With these steps complete, the notebook will now autosave your changes to your Google Drive, ensuring your
progress is retained.

Project Setup: Software Installation
====================================

Next, install the Python software libraries required for this research project. In Google Colab, this can be done
easily by running the cell below in the Jupyter Notebook.
"""
!pip install autoconf==2025.12.21.1 autofit==2025.12.21.1 autoarray==2025.12.21.1 autogalaxy==2025.12.21.1 pyvis==0.3.2 dill==0.4.0 jaxnnls dynesty==2.1.4 emcee==3.1.6 nautilus-sampler==1.0.4 timeout_decorator==0.5.0 anesthetic==2.8.14 --no-deps

"""
Project Setup: Repository Clone
===============================

The code below downloads the project files from the GitHub repository and stores them in your Google Colab
directory.
"""
!git clone https://github.com/Jammy2211/BSc_Galaxies_Project

"""
Project Setup: Working Directory
================================

On the left hand side of your Google Collab window, you will see a file explorer. Click on the folder icon. This will
open the file explorer. 

The screenshot below shows what should be displayed, for now you do not need to worry about the contents
of this folder but later you will use it to inspect the output of the code you run:

![ColabGolder](https://github.com/Jammy2211/BSc_Galaxies_Project/blob/master/Colab_Example_Folder.png?raw=true)

The `content` folder is the root directory of your Google Colab environment, within which is a folder 
named `BSc_Galaxies_Project`. This folder contains all the files and scripts for the project, which were downloaded 
by the repository clone command above.

The Python working directory defines where Python looks for data files and scripts to load. To ensure the working
directory is correctly set to the `BSc_Galaxies_Project` folder, run the cell below. This cell also updates
configuration file paths to ensure they point to the correct directories.
"""
import os
from autoconf import conf

os.chdir("/content/BSc_Galaxies_Project")

conf.instance.push(
    new_path="/content/BSc_Galaxies_Project/config",
    output_path="/content/BSc_Galaxies_Project/output",
)

"""
__Reminder: Permanently Saving Results__

At the end of the starting tutorial, you were shown how to save the results of your model-fitting to your hard-disk
or Google Drive. This is important, as it ensures the results are not lost when the Google Colab virtual machine
shuts down. The Jupyter Notebook description of how to do this and required code is shown again below, to remind
you to do this after you begin performing model-fits.

Until you have run model-fits and generated results, the code below will not work and raise exceptions regarding
there not being an `output` directory. This is expected, and you should run the code below after you have performed
model-fits.

__Permanently Saving Results__

A Google Colab is a temporary server that is erased after 90 minutes, meaning your output folder will be
erased and you will lose the results of any model-fitting you performed.

There are two ways to permanently save the results of a model-fit, and you can use either or both of them.

**Save to Google Drive**: If you have a Google Drive, you can save the results to it. This is handled by the
code below, which every time you run it will save the results in the `output` folder of your Google Drive
in a folder named `BSc_Galaxies_Project`.

If you navigate to this folder in your Google Drive you will find the results of all model-fits you have
performed. As new runs are performed and results are saved, they will be added to this folder ever time you
run the code below.
"""
from google.colab import drive
drive.mount("/content/drive")

!cp -r /content/BSc_Galaxies_Project/output /content/drive/MyDrive/BSc_Galaxies_Project

"""
**Download to Hard-disc**: You can download the `output` folder to your PC or laptop by running the code below. 

You have to .zip the output folder first in order to download it, and you may therefore need to also unzip it
locally once downloaded. 

As you perform more runs, this .zip file will include them, ensuring all results of model fitting are retained.
"""
from google.colab import files

!zip -r output.zip /content/BSc_Galaxies_Project/output
files.download("output.zip")


"""
Task: Structure
===============

Galaxy structure refers to the fundamental characteristics of galaxies, which are generally grouped into three main
structural categories:

- **Ellipticals:** Galaxies with a smooth, featureless light profile, where stellar orbits are randomly oriented and "velocity dispersion supported."

- **Disk galaxies:** Galaxies with a more intricate light profile, characterized by stellar orbits predominantly in a rotating disk, making them "rotationally supported."

- **Irregulars:** Galaxies that do not fit into the first two categories, often displaying complex or asymmetric light profiles, such as those resulting from merger events.

__Overview__

We will begin by using light profile fitting tools on simulated galaxies to distinguish between elliptical and disk
galaxies, employing one of the methods astronomers use for galaxy classification. We will not consider irregular
galaxies in this project, which are difficult to fit with light profiles due to their complex structure.

Next, we will apply these tools to James Webb Space Telescope (JWST) images of real galaxies to classify a small sample
into elliptical and disk categories.

The research project concludes with you writing a report, that includes a literature review on an aspect of galaxy 
structure and presents some of the results of your JWST image analysis.

__Pixel Scale__

In the `tutorial.ipynb` notebook, we introduced the concept of pixel scale, which is the conversion factor between
arc-seconds and pixels in an image. For the example simulated images, the pixel scale was **0.1 arc-seconds per pixel**.

For the example simulated images and JWST images in this task, the pixel scale is **0.06 arc-seconds per pixel**. You 
will need to account for this difference when analyzing the JWST images.

__Task 1: Simulations__

In this task, we fit simulated images of galaxies, to verify that your light profile fitting analysis works, before
applying it to real James Webb Space Telescope images of galaxies in task 3.

To classify galaxies as elliptical or disk galaxies, the following light profile fitting method is applied:

- **Elliptical galaxies**: These typically exhibit a Sersic light profile with a `sersic_index` ranging from 2.5 to 5.0. Thus, if a Sersic profile fitted to a galaxy results in an inferred `sersic_index` above 2.5, the galaxy is likely elliptical.

- **Disk galaxies**: These generally have a Sersic light profile with a `sersic_index` near 1.0. Therefore, if a Sersic profile fitted to a galaxy yields an inferred `sersic_index` below 2.5, the galaxy is likely a disk galaxy.

**Task Instructions:**

1. Navigate to the folder `dataset/task_1a_structure` or `dataset/task_1b_structure`, depending on which you were assigned. You will find two simulated galaxy datasets: `disk` and `elliptical`.

2. Use the light profile fitting tools to fit a Sersic light profile to each dataset.

3. Verify that the fitting results align with the true `sersic_index` values:

   - The galaxy dataset named `disk` infers a `sersic_index` value close to **1.0**.
   - The galaxy dataset named `elliptical` infers a `sersic_index` value close to **4.0**.

By successfully fitting the Sersic profile and recovering these values, you have therefore confirmed your light profile fitting code is working correctly.
"""
# INSERT YOUR CODE HERE

"""
__Task 2: Model Comparison__

Certain Sersic profiles have specific names when their `sersic_index` takes particular values:

- A Sersic profile with a `sersic_index` of 4.0 is called a **De Vaucouleurs profile**. In **PyAutoGalaxy**, it can be fitted using the `ag.lp.DevVaucouleurs` class.
- A Sersic profile with a `sersic_index` of 1.0 is called an **Exponential profile**. In **PyAutoGalaxy**, it can be fitted using the `ag.lp.Exponential` class.

These classes allow you to model the light profiles of galaxies with predefined Sersic indices, using the same Python code introduced in previous tutorials.

By comparing the quality of fits using different profiles, we can identify the model that best matches the data, 
helping to determine whether a galaxy is more likely to be an elliptical or a disk.

**Task Instructions:**

1. Fit the `De Vaucouleurs` profile (`ag.lp.DevVaucouleurs`) to the `elliptical` galaxy dataset and 
   the `Exponential` profile (`ag.lp.Exponential`) to the `disk` galaxy dataset, and confirm that the fits are 
   accurate.

2. Fit both the `De Vaucouleurs` and `Exponential` profiles to the other dataset (`elliptical` and `disk`) and verify
   that the fits are worse, produce visible residuals and have lower `log_likelihood` values.

By completing this task, you will confirm that the `De Vaucouleurs` and `Exponential` profiles accurately capture the
structure of elliptical and disk galaxies, respectively, using **PyAutoGalaxy**'s specialized light profile fitting tools.
"""
# INSERT YOUR CODE HERE

"""
__Task 3: Real Galaxies__

In the folder `dataset/task_1a_structure/jwst` or `dataset/task_1b_structure/jwst`, you will find 10 images of real 
galaxies observed with the James Webb Space Telescope (JWST). 

For 3 galaxies of your choice, use the light profile fitting tools to classify each galaxy as either elliptical or 
disk-shaped using light profile fitting tools. You can achieve this by applying either of the methods discussed 
earlier or by combining them for a more robust classification.

Once you are content with the results, read below on task 4 on the report you will write. This report should include 
JWST analysis results specific to the aspect of galaxy structure you choose to write about. Therefore you will
need to tailor your JWST analysis to the specific subject matter you choose to write about and analyse a
larger sample of galaxies than just the 3 you chose above.

__Residuals__

Keep in mind that real galaxies are inherently complex, often exhibiting additional emission and structural features
that may not be perfectly captured by a simple light profile. As a result, the fits will likely show significantly
larger residuals compared to those from simulated galaxies.

Analyzing these residuals can offer further insights into whether a galaxy is elliptical or disk-shaped and reveal
properties that these residuals might represent.
"""
# INSERT YOUR CODE HERE

"""
__Task 4: Report__

The final task involves writing a report, combining a literature review with an analysis of the JWST images.

**Literature Review:**

The report should include a concise literature review focusing on a specific topic related to galaxy structure and 
the classification of galaxies into elliptical and disk types.

You are free to choose your focus, but here are some suggested topics and questions to consider:

- How does the division between elliptical and disk galaxies relate to Edwin Hubble's original classification scheme?

- What are the key differences between elliptical and disk galaxies in terms of their stellar dynamics?

- What are the key differences between elliptical and disk galaxies in terms of their current star formation activity and star formation histories?
  
**JWST Analysis:**

The report should also include figures and results from your analysis of JWST images, directly linked to the aspect of
the literature you choose to write about. 

You are expected to build on the analysis you performed in Task 3, for example reporting different aspects of the 
results and expanding it to more than 3 galaxies.

You should link these results to the topics discussed in your literature review, providing a coherent connection 
between your discussion and the practical JWST analysis and results.

**Recommended Reading:**

NASA's Astrophysics Data System (ADS) is a widely used digital library portal for accessing astronomical and astrophysical literature. Researchers and students use NASA ADS to find scientific papers, references, and citations in the field of astronomy, astrophysics, and related disciplines. You can access NASA ADS at the following link: [NASA ADS](https://ui.adsabs.harvard.edu/).

For an excellent overview of galaxy morphology and structure, particularly for the use of the Sérsic index, the following papers are a good starting point:

1. **"A Revised Parallel-Sequence Morphological Classification of Galaxies" by John Kormendy (2012)**  
   - This paper provides a comprehensive summary of galaxy morphology, offering insights into the classification of galaxies and the structural differences between ellipticals, lenticulars, and spirals. It also introduces the concept of a revised parallel-sequence classification.  
   [Link to paper on ADS](https://ui.adsabs.harvard.edu/abs/2012ApJS..198....2K/abstract)

2. **"On the estimation of galaxy structural parameters: the Sérsic model" by I. Trujillo & A. Graham (2001)**  
   - This paper explains the Sérsic index and its application in characterizing galaxy light profiles, from elliptical galaxies to bulges of spirals. It also discusses the relationship between the Sérsic index and other structural parameters like galaxy concentration and total luminosity.  
   [Link to paper on ADS](https://ui.adsabs.harvard.edu/abs/2001MNRAS.326..869T/abstract)

3. **"Elliptical and Disk Galaxy Structure and Modern Scaling Laws" by A. Graham (2013)**  
   - This paper discusses the Sérsic model's role in describing the light profiles of galaxies and examines how the Sérsic index correlates with various structural parameters, providing insights into galaxy morphology and scaling relations. 
   [Link to paper on ADS](https://ui.adsabs.harvard.edu/abs/2013pss6.book...91G/abstract)

These papers provide a well-rounded foundation for understanding galaxy morphology and the use of the Sérsic index in structural analysis. For beginners or non-specialists, starting with Kormendy's 2012 paper is highly recommended.
"""