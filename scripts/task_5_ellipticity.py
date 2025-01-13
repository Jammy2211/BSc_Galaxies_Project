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
Task: Ellipticity
=================

The ellipticity of galaxies is a fundamental property that describes their shape.  

It quantifies a galaxy’s shape as the ellipse that best matches its observed light distribution, with ellipticity
defined as the ratio of the difference between the major and minor axes to their sum, reflecting how elongated a galaxy appears.  

Ellipticity provides insights into a galaxy's formation and evolution. Galaxies with low axis ratios (high ellipticity) 
are typically elliptical galaxies in Edwin Hubble's classification, characterized by spheroidal shapes, random stellar 
orbits, and little star formation.  

In contrast, disk galaxies, with higher axis ratios (lower ellipticity), have flat, rotating disks and often show 
spiral arms or other features of ongoing star formation. Their lower ellipticity reflects their rotational symmetry 
and flattened structure.  

Ellipticity also relates to a galaxy’s 3D shape. The observed ellipticity changes with a galaxy's inclination. 
When viewed edge-on, a galaxy appears more elongated, leading to higher ellipticity, while a face-on view shows a 
more circular shape with lower ellipticity. Thus, ellipticity is a projection of the galaxy's true 3D structure, and 
accounting for inclination helps astronomers infer whether a galaxy is spheroidal or disk-like.

__Overview__

We will begin by using light profile fitting tools on simulated galaxies, where the appearance of the simulated
galaxies vary over wavelength. 

Next, we will apply these tools to James Webb Space Telescope (JWST) images of real galaxies to make our own
inference on the ellipticities of galaxies.

The research project concludes with you writing a report, that includes a literature review on an aspect of galaxy
colours and presents some of the results of your JWST image analysis.

__Pixel Scale__

In the `tutorial.ipynb` notebook, we introduced the concept of pixel scale, which is the conversion factor between
arc-seconds and pixels in an image. For the example simulated images, the pixel scale was **0.1 arc-seconds per pixel**.

For the example simulated images and JWST images in this task, the pixel scale is **0.06 arc-seconds per pixel**. You 
will need to account for this difference when analyzing the JWST images.

__Task 1: Simulations__

In this task, we fit simulated images of galaxies, to verify that your light profile fitting analysis works, before
applying it to real James Webb Space Telescope images of galaxies in task 3.

**Task Instructions:**

1. Navigate to the folder `dataset/task_5_ellipticity`, where you will find two simulated datasets, `round` and `flat`.

2. Use the light profile fitting tools to fit a Sersic light profile to each dataset.

3. Verify that the `axis_ratio` inferred by the fit for the `round` dataset is 0.9 and for the `flat` dataset is 0.5.
"""
# INSERT YOUR CODE HERE

"""
__Task 2: Three Dimensions__

The `axis_ratio` quantifies the ellipticity of a galaxy in 2D and is defined as the ratio of the galaxy's minor axis (b) to its major axis (a), giving a value of `b/a`. However, the true shape of a galaxy is 3D, and there are three possible shapes that an ellipse generalizes to in 3D:

- **Oblate**: A shape where the galaxy is flattened along one axis, like a squished sphere. In this case, the minor axis (b) is shorter than the other two axes, with the galaxy's major axis (a) and the third axis (c) being longer. This creates a disk-like or lenticular shape, with a shape resembling a flattened spheroid.

- **Prolate**: A shape where the galaxy is elongated along one axis, resembling a rugby ball. In this case, the major axis (a) is longer than the other two axes, and the third axis (c) is also longer than the minor axis (b), forming an elongated, cigar-like shape.

- **Triaxial**: A more complex shape where all three axes are different lengths. The axes (a), (b), and (c) are distinct, leading to an asymmetrical shape that doesn't exhibit simple symmetry along any axis. This results in a more irregular, elongated shape in 3D. 

For this task, write Python code below which converts the 3D shape of a galaxy (\(a\), \(b\), and \(c\)) into its 
observed 2D axes (\(a_{obs}\) and \(b_{obs}\)) based on a given inclination angle. The inclination angle is the angle 
between the galaxy's rotation axis and the observer’s line of sight. As the galaxy becomes more edge-on, the observed 
minor axis \(b_{obs}\) decreases, while the major axis \(a_{obs}\) remains unchanged.

By applying projection formulas, you will learn how a galaxy's 3D shape influences its 2D appearance, which is 
important for accurate galaxy shape classification and analysis.
"""
# INSERT YOUR CODE HERE

"""
__Task 3: Real Galaxies__

In the folder `dataset/task_4_ellipticities/jwst`, you will find 10 images of real galaxies observed with the James Webb
Space Telescope (JWST). 

For 3 galaxies of your choice, use the light profile fitting tools to measure the ellipticities of three galaxies in 
the dataset. 

You should then make plots comparing the measured ellipticities on the x axis with other measured galaxy properties, 
such as `effective_radius` and `sersic_index`. 

Once you are content with the results, read below on task 4 on the report you will write. This report should include 
JWST analysis results specific to the aspect of galaxy ellipticities you choose to write about. Therefore you will
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

- Galaxies are classified as elliptical or disk-shaped based on their ellipticity. Research these galaxy types and 
  understand how ellipticity measurements relate to their structure.

- A galaxy's ellipticity is linked to the dynamics and orbits of its stars. Investigate stellar dynamics and their 
  connection to galaxy ellipticity.

- Astronomers observe galaxies in 2D but must infer their 3D shapes. Explore methods for this and determine how many 
  observations are needed to fully understand a galaxy's 3D structure.
  
**JWST Analysis:**

The report should also include figures and results from your analysis of JWST images, directly linked to the aspect of
the literature you choose to write about. 

You are expected to build on the analysis you performed in Task 3, for example reporting different aspects of the 
results and expanding it to more than 3 galaxies.

You should link these results to the topics discussed in your literature review, providing a coherent connection 
between your discussion and the practical JWST analysis and results.
"""