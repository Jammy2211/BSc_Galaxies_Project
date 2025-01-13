"""
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

You will be prompted to restart the session, with a message that states:

```
Restart session
WARNING: The following packages were previously imported in this runtime:
  [psutil]
You must restart the runtime in order to use newly installed versions.

Restarting will lose all runtime state, including local variables.
```

When this pop-up appears, click "Restart session", let the Google colab webpage reload and rerun the cell and
continue with the notebook.
"""
!pip install autogalaxy==2024.11.13.2
!pip install numba

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
BSc Galaxies Project: Introduction
==================================

Nearly a century ago, Edwin Hubble famously classified galaxies into three distinct groups: ellipticals, spirals and
irregulars. He produced a diagram of these galaxies, called the Hubble Tuning Fork, which is shown below and still
used by astronomers in the modern day:

![HubbleTuning](https://github.com/Jammy2211/autogalaxy_workspace/blob/main/scripts/howtogalaxy/chapter_1_introduction/HubbleTuningFork.jpg?raw=true)

To make his diagram, Hubble looked at images of each galaxy in his sample, and subjectively judged by eye how to
classify them. Today, Astronomers use computer software, statistical algorithms and image processing techniques to
perform this task in a more quantifiable and objective way.

These tutorials will teach you how to perform this analysis yourself, using the open-source software
package **PyAutoGalaxy**. By the end, you’ll be able to take an image of a galaxy and study its morphology and
structure using the same techniques that professional astronomers use today.

Tutorial 1: Grids And Galaxies
==============================

In this tutorial, we will introduce the fundamental concepts and quantities used to study galaxy morphology.
These concepts will enable us to create images of galaxies and analyze how their light is distributed across space.
Additionally, we will explore how adjusting various properties of galaxies can alter their appearance. For instance,
we can change the size of a galaxy, rotate it, or modify its brightness.

To create these images, we first need to define 2D grids of $(y, x)$ coordinates. We will shift and rotate these
grids to manipulate the appearance of the galaxy in the generated images. The grid will serve as the input for light
profiles, which are analytic functions that describe the distribution of a galaxy's light. By evaluating these light
profiles on the grid, we can effectively generate images that represent the structure and characteristics of galaxies.

Here is an overview of what we'll cover in this tutorial:

- **Grids**: Create a uniform grid of $(y,x)$ coordinates and show how it can be used to measure the light of a galaxy.
- **Geometry**: How to shift and rotate a grid, and convert it to elliptical coordinates.
- **Light Profiles**: Using light profiles, analytic functions that describe how a galaxy's light is distributed.
- **Galaxies**: Creating galaxies containing light profiles and computing the image of a galaxy.
- **Units**: Converting the units of a galaxy's image to physical units like kiloparsecs.

The imports below are required to run the tutorials in a Jupyter notebook. They also import the
`autogalaxy` package and the `autogalaxy.plot` module which are used throughout the tutorials.
"""
import numpy as np

import autogalaxy as ag
import autogalaxy.plot as aplt

"""
__Grids__

A `Grid2D` is a set of two-dimensional $(y,x)$ coordinates that represent points in space where we evaluate the 
light emitted by a galaxy.

Each coordinate on the grid is referred to as a 'pixel'. This is because we use the grid to create the image of a
galaxy at each of these coordinates, meaning that each coordinate maps to the centre of each pixel in this image.

Grids are defined in units of 'arc-seconds' ("). An arc-second is a unit of angular measurement used by astronomers to 
describe the apparent size of objects in the sky.

The `pixel_scales` parameter sets how many arc-seconds each pixel represents. For example, if `pixel_scales=0.1`, 
then each pixel covers 0.1" of the sky.

Below, we create a uniform 2D grid of 101 x 101 pixels with a pixel scale of 0.1", corresponding to an area 
of 10.1" x 10.1", spanning from -5.05" to 5.05" in both the y and x directions.
"""
grid = ag.Grid2D.uniform(
    shape_native=(
        101,
        101,
    ),  # The dimensions of the grid, which here is 101 x 101 pixels.
    pixel_scales=0.1,  # The conversion factor between pixel units and arc-seconds.
)

"""
We can visualize this grid as a uniform grid of dots, each representing a coordinate where the light is measured.
"""
grid_plotter = aplt.Grid2DPlotter(grid=grid)
grid_plotter.set_title("Uniform Grid of Coordinates")
grid_plotter.figure_2d()

"""
Each coordinate in the grid corresponds to an arc-second position. Below, we print a few of these coordinates to see 
the values.

To print these values, we use the `native` attribute of the grid, which returns the grid as a 2D NumPy array of
shape [total_y_pixels, total_x_pixels, 2].

The `native` attribute is used to access many properties of numpy arrays through this tutorial.
"""
print("(y,x) pixel 0:")
print(grid.native[0, 0])  # The coordinate of the first pixel.
print("(y,x) pixel 1:")
print(grid.native[0, 1])  # The coordinate of the second pixel.
print("(y,x) pixel 2:")
print(grid.native[0, 2])  # The coordinate of the third pixel.
print("(y,x) pixel 100:")
print(grid.native[1, 0])  # The coordinate of the 100th pixel.
print("...")

"""
We can also check the `shape_native` of the `Grid2D` object.
"""
print(grid.native.shape)

"""
For these tutorials, you should use whatever format is most intuitive for the task you are performing.

*Exercise: Try creating grids with different `shape_native` and `pixel_scales` using the `ag.Grid2D.uniform()` function above.  Print the grid (y,x) coordinates and observe how they change when you adjust `shape_native` and `pixel_scales`.*

__Geometry__

The above grid is centered on the origin $(0.0", 0.0")$. Sometimes, we need to shift the grid to be centered on a 
specific point, like the center of a galaxy.

We can shift the grid to a new center, $(y_c, x_c)$, by subtracting this center from each coordinate.
"""
centre = (0.3, 0.5)  # Shifting the grid to be centered at y=1.0", x=2.0".

grid_shifted = grid
grid_shifted[:, 0] = grid_shifted[:, 0] - centre[0]  # Shift in y-direction.
grid_shifted[:, 1] = grid_shifted[:, 1] - centre[1]  # Shift in x-direction.

print("(y,x) pixel 0 After Shift:")
print(grid_shifted.native[0, 0])  # The coordinate of the first pixel after shifting.

"""
The grid is now centered around $(0.3", 0.5")$. We can plot the shifted grid to see this change.

*Exercise: Try shifting the grid to a different center, for example $(0.0", 0.0")$ or $(2.0", 3.0")$. Observe how the center of the grid changes when you adjust the `centre` variable.*
"""
grid_plotter = aplt.Grid2DPlotter(grid=grid_shifted)
grid_plotter.set_title("Grid Centered Around (0.3, 0.5)")
grid_plotter.figure_2d()

"""
Next, we can rotate the grid by an angle `phi` (in degrees). The rotation is counter-clockwise from the positive x-axis.

To rotate the grid:

1. Calculate the distance `radius` of each coordinate from the origin using $r = \sqrt{y^2 + x^2}$.
2. Determine the angle `theta` counter clockwise from the positive x-axis using $\theta = \arctan(y / x)$.
3. Adjust `theta` by the rotation angle and convert back to Cartesian coordinates via $y_r = r \sin(\theta)$ and $x_r = r \cos(\theta)$.
"""
angle_degrees = 60.0

y = grid_shifted[:, 0]
x = grid_shifted[:, 1]

radius = np.sqrt(y**2 + x**2)
theta = np.arctan2(y, x) - np.radians(angle_degrees)

grid_rotated = grid_shifted
grid_rotated[:, 0] = radius * np.sin(theta)
grid_rotated[:, 1] = radius * np.cos(theta)

print("(y,x) pixel 0 After Rotation:")
print(grid_rotated.native[0, 0])  # The coordinate of the first pixel after rotation.

"""
The grid has now been rotated 60 degrees counter-clockwise. We can plot it to see the change.

*Exercise: Try rotating the grid by a different angle, for example 30 degrees or 90 degrees. Observe how the grid changes when you adjust the `angle_degrees` variable.*
"""
grid_plotter = aplt.Grid2DPlotter(grid=grid_rotated)
grid_plotter.set_title("Grid Rotated 60 Degrees")
grid_plotter.figure_2d()

"""
Next, we convert the rotated grid to elliptical coordinates using:

$\eta = \sqrt{(x_r)^2 + (y_r)^2/q^2}$

Where `q` is the axis-ratio of the ellipse and $(x_r, y_r)$ are the rotated coordinates. 

Elliptical coordinates are a system used to describe positions in relation to an ellipse rather than a circle. They 
are particularly useful in astronomy when dealing with objects like galaxies, which often have elliptical shapes 
due to their inclination or intrinsic shape.

*Exercise: Try converting the grid to elliptical coordinates using a different axis-ratio, for example 0.3 or 0.8. What happens to the grid when you adjust the `axis_ratio` variable?*
"""
axis_ratio = 0.5
eta = np.sqrt((grid_rotated[:, 0]) ** 2 + (grid_rotated[:, 1]) ** 2 / axis_ratio**2)

print("First Ten Elliptical Coordinates:")
print(eta[:10])

"""
Above, the angle $\phi$ (in degrees) was used to rotate the grid, and the axis-ratio $q$ was used to convert the grid 
to elliptical coordinates.

From now on, we'll describe ellipticity using "elliptical components" $\epsilon_{1}$ and $\epsilon_{2}$, calculated 
from $\phi$ and $q$:

$\epsilon_{1} = \frac{1 - q}{1 + q} \sin(2\phi)$  
$\epsilon_{2} = \frac{1 - q}{1 + q} \cos(2\phi)$

We'll refer to these as `ell_comps` in the code for brevity.

*Exercise*: Try computing the elliptical components from the axis-ratio and angle above. What happens to the elliptical
components when you adjust the `axis_ratio` and `angle_degrees` variables?
"""
fac = (1 - axis_ratio) / (1 + axis_ratio)
epsilon_y = fac * np.sin(2 * np.radians(angle_degrees))
epsilon_x = fac * np.cos(2 * np.radians(angle_degrees))

ell_comps = (epsilon_y, epsilon_x)

print("Elliptical Components:")
print(ell_comps)


"""
__Light Profiles__

Galaxies are collections of stars, gas, dust, and other astronomical objects that emit light. Astronomers study this 
light to understand various properties of galaxies.

To model the light of a galaxy, we use light profiles, which are mathematical functions that describe how a galaxy's 
light is distributed across space. By applying these light profiles to 2D grids of $(y, x)$ coordinates, we can 
create images that represent a galaxy's luminous emission.

A commonly used light profile is the `Sersic` profile, which is widely adopted in astronomy for representing galaxy 
light. The `Sersic` profile is defined by the equation:

$I_{\rm Ser} (\eta_{\rm l}) = I \exp \left\{ -k \left[ \left( \frac{\eta}{R} \right)^{\frac{1}{n}} - 1 \right] \right\}$

In this equation:

 - $\eta$ represents the elliptical coordinates of the profile in arc-seconds (refer to earlier sections for elliptical coordinates).
 - $I$ is the intensity normalization of the profile, given in arbitrary units, which controls the overall brightness of the Sersic profile.
 - $R$ is the effective radius in arc-seconds, which determines the size of the profile.
 - $n$ is the Sersic index, which defines how 'steep' the profile is, influencing the concentration of light.
 - $k$ is a constant that ensures half the light of the profile lies within the radius $R$, where $k = 2n - \frac{1}{3}$.

We can evaluate this function using values for $(\eta, I, R, n)$ to calculate the intensity of the profile at 
a particular elliptical coordinate.
"""
elliptical_coordinate = (
    0.5  # The elliptical coordinate where we compute the intensity, in arc-seconds.
)
intensity = 1.0  # Intensity normalization of the profile in arbitrary units.
effective_radius = 2.0  # Effective radius of the profile in arc-seconds.
sersic_index = 1.0  # Sersic index of the profile.
k = 2 * sersic_index - (
    1.0 / 3.0
)  # Calculating the constant k, note that this is an approximation.

# Calculate the intensity of the Sersic profile at a specific elliptical coordinate.
sersic_value = np.exp(
    -k * ((elliptical_coordinate / effective_radius) ** (1.0 / sersic_index) - 1.0)
)

print("Intensity of Sersic Light Profile at Elliptical Coordinate 0.5:")
print(sersic_value)

"""
The calculation above gives the intensity of the Sersic profile at an elliptical coordinate of 0.5.

To create a complete image of the Sersic profile, we can evaluate the intensity at every point in our grid of 
elliptical coordinates.
"""
sersic_image = np.exp(-k * ((eta / effective_radius) ** (1.0 / sersic_index) - 1.0))

"""
When we plot the resulting image, we can see how the properties of the grid affect its appearance:

 - The peak intensity is at the position $(0.3", 0.5")$, where we shifted the grid.
 - The image is elongated along a 60° counter-clockwise angle, corresponding to the rotation of the grid.
 - The image has an elliptical shape, consistent with the axis ratio of 0.5.

This demonstrates how the geometry of the grid directly influences the appearance of the light profile.

*Exercise: Try changing the values of `centre`, `ell_comps`, `effective_radius`, and `sersic_index` above. Observe how these adjustments change the Sersic profile image.*
"""
array_plotter = aplt.Array2DPlotter(
    array=ag.Array2D(
        values=sersic_image, mask=grid.mask
    ),  # The `Array2D` object is discussed below.
)
array_plotter.set_title("Sersic Image")
array_plotter.figure_2d()

"""
Instead of manually handling these transformations, we can use `LightProfile` objects from the `light_profile` 
module (`lp`) for faster and more efficient calculations.

Below, we define a `Sersic` light profile using the `Sersic` object. We can print the profile to display its parameters.
"""
sersic_light_profile = ag.lp.Sersic(
    centre=(0.0, 0.0),
    ell_comps=(0.0, 0.1),
    intensity=1.0,
    effective_radius=2.0,
    sersic_index=1.0,
)

print(sersic_light_profile)

"""
With this `Sersic` light profile, we can create an image by passing a grid to its `image_2d_from` method.

The calculation will internally handle all the coordinate transformations and intensity evaluations we performed 
manually earlier, making it much simpler.

The `Sersic` profile we created just above is different from the one we used to manually compute the image,
so the image will look different. However, the process is the same.
"""
image = sersic_light_profile.image_2d_from(grid=grid)

array_plotter = aplt.Array2DPlotter(
    array=image,
)
array_plotter.set_title("Sersic Image via Light Profile")
array_plotter.figure_2d()

"""
The `image` is returned as an `Array2D` object. 

Similar to a `Grid2D`, it is accessed via the `native` attribute. which is a 2D NumPy array of shape [total_y_pixels, total_x_pixels].
"""
print("Intensity of pixel 0:")
print(image.native[0, 0])

"""
To visualize the light profile's image, we use a `LightProfilePlotter`.

We provide it with the light profile and the grid, which are used to create and plot the image.
"""
light_profile_plotter = aplt.LightProfilePlotter(
    light_profile=sersic_light_profile, grid=grid
)
light_profile_plotter.set_title("Image via LightProfilePlotter")
light_profile_plotter.figures_2d(image=True)

"""
The `LightProfilePlotter` also has methods to plot the 1D radial profile of the light profile. This profile shows
how the intensity of the light changes as a function of distance from the profile's center. This is a more informative
way to visualize the light profile's distribution.

The 1D plot below is a `semilogy` plot, meaning that the x-axis (showing the radial distance in arc-seconds) is linear,
while the y-axis (showing the intensity) is log10. This is a common way to visualize light profiles, as it highlights
the fainter outer regions of the profile. A log x-axis is also a common choice.

*Exercise: Try plotting the 1D radial profile of Sersic profiles with different effective radii and Sersic indices. Does the 1D representation show more clearly how the light distribution changes with these parameters?*
"""
light_profile_plotter = aplt.LightProfilePlotter(
    light_profile=sersic_light_profile, grid=grid
)
light_profile_plotter.set_title("Sersic 1D Radial Profile")
light_profile_plotter.figures_1d(image=True)

"""
Since galaxy light distributions often cover a wide range of values, they are typically better visualized on a log10 
scale. This approach helps highlight details in the faint outskirts of a light profile.

The `MatPlot2D` object has a `use_log10` option that applies this transformation automatically. Below, you can see 
that the image plotted in log10 space reveals more details.
"""
light_profile_plotter = aplt.LightProfilePlotter(
    light_profile=sersic_light_profile,
    grid=grid,
    mat_plot_2d=aplt.MatPlot2D(use_log10=True),
)
light_profile_plotter.set_title("Sersic Image")
light_profile_plotter.figures_2d(image=True)

"""
__Galaxies__

Now, let's introduce `Galaxy` objects, which are key components in **PyAutoGalaxy**.

A light profile represents a single feature of a galaxy, such as its bulge or disk. To model a complete galaxy, 
we combine multiple `LightProfiles` into a `Galaxy` object. This allows us to create images that include different 
components of a galaxy.

In addition to light profiles, a `Galaxy` has a `redshift`, which indicates how far away it is from Earth. The redshift 
is essential for performing unit conversions using cosmological calculations, such as converting arc-seconds into 
kiloparsecs (kpc, a kiloparsec is a distance unit in astronomy, equal to about 3.26 million light-years.)

Let's start by creating a galaxy with two `Sersic` light profiles, which notationally we will consider to represent
a bulge and disk component of the galaxy, the two most important structures seen in galaxies which drive the
Hubble tuning fork classification shown at the beginning of this tutorial.
"""
bulge = ag.lp.Sersic(
    centre=(0.0, 0.0),
    ell_comps=(0.0, 0.111111),
    intensity=1.0,
    effective_radius=1.0,
    sersic_index=2.5,
)

disk = ag.lp.Sersic(
    centre=(0.0, 0.0),
    ell_comps=(0.0, 0.3),
    intensity=0.3,
    effective_radius=3.0,
    sersic_index=1.0,
)

galaxy = ag.Galaxy(redshift=0.5, bulge=bulge, disk=disk)

print(galaxy)

"""
We can pass a 2D grid to a light profile to compute its image using the `image_2d_from` method. 

The same approach works for a `Galaxy` object:
"""
image = galaxy.image_2d_from(grid=grid)

print("Intensity of `Grid2D` pixel 0:")
print(image.native[0, 0])
print("Intensity of `Grid2D` pixel 1:")
print(image.native[0, 1])
print("Intensity of `Grid2D` pixel 2:")
print(image.native[0, 2])
print("...")

array_plotter = aplt.Array2DPlotter(
    array=image,
)
array_plotter.set_title("Bulge+Disk Image via Galaxy")
array_plotter.figure_2d()

"""
We can use a `GalaxyPlotter` to plot the galaxy's image, just like how we used `LightProfilePlotter` for a light 
profile.
"""
galaxy_plotter = aplt.GalaxyPlotter(galaxy=galaxy, grid=grid)
galaxy_plotter.set_title("Galaxy Bulge+Disk Image")
galaxy_plotter.figures_2d(image=True)

"""
The bulge dominates the center of the image, and is pretty much the only luminous emission we see can see on a linear
scale. The disk's emission is present, but it is much fainter and spread over a larger area.

We can confirm this using the `subplot_of_light_profiles` method, which plots each individual light profile separately.
"""
galaxy_plotter.set_title("Galaxy Bulge+Disk Subplot")
galaxy_plotter.subplot_of_light_profiles(image=True)

"""
Because galaxy light distributions often follow a log10 pattern, plotting in log10 space helps reveal details in the 
outskirts of the light profile, in this case the emission of the disk.

This is especially helpful to separate the bulge and disk profiles, which have different intensities and sizes.
"""
galaxy_plotter = aplt.GalaxyPlotter(
    galaxy=galaxy, grid=grid, mat_plot_2d=aplt.MatPlot2D(use_log10=True)
)
galaxy_plotter.set_title("Galaxy Bulge+Disk Image")
galaxy_plotter.figures_2d(image=True)

"""
The `figures_1d_decomposed` method allows us to visualize each light profile's contribution in 1D.

1D plots show the intensity of the light profile as a function of distance from the profile’s center. The bulge
and disk profiles share the same `centre`, meaning that plotting them together shows how they overlap. If the
`centre` of the profiles were different, they would still be plotted on top of each other, but as a user you
would need to remember that the profiles are not aligned in 2D.
"""
galaxy_plotter.set_title("Bulge+Disk 1D Decomposed")
galaxy_plotter.figures_1d_decomposed(image=True)

"""
We can group multiple galaxies at the same redshift into a `Galaxies` object, which is created from a list of 
individual galaxies.

Below, we create an additional galaxy and combine it with the original galaxy into a `Galaxies` object. This could
represent two galaxies merging or interacting with each other, which is commonly seen in studies of galaxy evolution.
"""
extra_galaxy = ag.Galaxy(
    redshift=0.5,
    bulge=ag.lp.Sersic(
        centre=(0.2, 0.3),
        ell_comps=(0.0, 0.111111),
        intensity=1.0,
        effective_radius=1.0,
        sersic_index=2.5,
    ),
)

galaxies = ag.Galaxies(galaxies=[galaxy, extra_galaxy])

"""
The `Galaxies` object has similar methods as those for light profiles and individual galaxies.

For example, `image_2d_from` sums the images of all the galaxies.
"""
image = galaxies.image_2d_from(grid=grid)

"""
We can plot the combined image using a `GalaxiesPlotter`, just like with other plotters.
"""
galaxies_plotter = aplt.GalaxiesPlotter(galaxies=galaxies, grid=grid)
galaxies_plotter.figures_2d(image=True)

"""
A subplot of each individual galaxy image can also be created.
"""
galaxies_plotter.subplot_galaxy_images()

"""
Because galaxy light distributions often follow a log10 pattern, plotting in log10 space helps reveal details in the 
outskirts of the light profile.

This is especially helpful when visualizing how multiple galaxies overlap.
"""
galaxies_plotter = aplt.GalaxiesPlotter(
    galaxies=galaxies, grid=grid, mat_plot_2d=aplt.MatPlot2D(use_log10=True)
)
galaxies_plotter.figures_2d(image=True)

"""
__Unit Conversion__

Earlier, we mentioned that a galaxy’s `redshift` allows us to convert between arcseconds and kiloparsecs.

A redshift measures how much a galaxy's light is stretched by the Universe's expansion. A higher redshift means the 
galaxy is further away, and its light has been stretched more. By knowing a galaxy’s redshift, we can convert angular 
distances (like arcseconds) to physical distances (like kiloparsecs).

To perform this conversion, we use a cosmological model that describes the Universe's expansion. Below, we use 
the `Planck15` cosmology, which is based on observations from the Planck satellite.
"""
cosmology = ag.cosmo.Planck15()

kpc_per_arcsec = cosmology.kpc_per_arcsec_from(redshift=galaxy.redshift)

print("Kiloparsecs per Arcsecond:")
print(kpc_per_arcsec)


"""
This `kpc_per_arcsec` can be used as a conversion factor between arcseconds and kiloparsecs when plotting images of
galaxies.

We compute this value and plot the image in converted units of kiloparsecs.

This passes the plotting modules `Units` object a `ticks_convert_factor` and manually specified the new units of the
plot ticks.
"""
units = aplt.Units(ticks_convert_factor=kpc_per_arcsec, ticks_label=" kpc")

mat_plot = aplt.MatPlot2D(units=units)

galaxy_plotter = aplt.GalaxyPlotter(galaxy=galaxy, grid=grid, mat_plot_2d=mat_plot)
galaxy_plotter.figures_2d(image=True)

"""
__Wrap Up__

You've learnt the basic quantities used to study galaxy morphology. 

Lets summarize what we've learnt:

- **Grids**: WA grid is a set of 2D coordinates that represent the positions where we measure the light of a galaxy. 

- **Geometry**: How to shift, rotate, and convert grids to elliptical coordinates.

- **Light Profiles**: Mathematical functions that describe how a galaxy's light is distributed in space. We've used 
  the `Sersic` profile to create images of galaxies.

- **Galaxies**: Galaxies are collections of light profiles that represent a galaxy's light. We've created galaxies with 
  multiple light profiles and visualized their images.

- **Unit Conversion**: By assuming redshifts for galaxies we can convert their quantities from arcseconds to kiloparsecs.

Tutorial 2: Data
================

In the previous tutorial, we used light profiles to create images of galaxies. However, those images don't accurately
represent what we would observe through a telescope.

Real telescope images, like those taken with the Charge Coupled Device (CCD) imaging detectors on the Hubble Space
Telescope (HST), include several factors that affect what we see:

**Telescope Optics:** The optical components of the telescope can blur the light, influencing the image's sharpness.

**Exposure Time:** The time the detector collects light, affecting the clarity of the image. Longer exposure times
gather more light, improving the signal-to-noise ratio and creating a clearer image.

**Background Sky:** Light from a background sky, such as distant stars or zodiacal light, adds noise to the image.

In this tutorial, we'll simulate a galaxy image by applying these real-world effects to the light profiles and images
we created earlier.

Here is an overview of what we'll cover in this tutorial:

- **Optics Blurring:** Simulating how the telescope optics blur the galaxy's light, making the image appear blurred.
- **Poisson Noise:** Adding Poisson noise to the image, simulating the randomness in the photon-to-electron conversion process on the CCD.
- **Background Sky:** Adding a background sky to the image, simulating the light from the sky that adds noise to the image.
- **Simulator:** Using the `SimulatorImaging` object to simulate imaging data that includes all these effects.
- **Output:** Saving the simulated data to `.fits` files for use in future tutorials, where .fits is the standard image format used by astronomers.
"""
import numpy as np
from os import path
import autogalaxy as ag
import autogalaxy.plot as aplt

"""
__Initial Setup__

To create our simulated galaxy image, we first need a 2D grid. This grid will represent the coordinate space over 
which we will simulate the galaxy's light distribution.
"""
grid = ag.Grid2D.uniform(
    shape_native=(
        101,
        101,
    ),  # The dimensions of the grid, which here is 101 x 101 pixels.
    pixel_scales=0.1,  # The conversion factor between pixel units and arc-seconds.
)

"""
Next, we define the properties of our galaxy. In this tutorial, we’ll represent the galaxy with a bulge using a 
Sersic light profile.

In the previous tutorial, the units of `intensity` were arbitrary. However, for this tutorial, where we simulate 
realistic imaging data, the intensity must have specific units. We’ll use units of electrons per second per pixel 
($e- pix^-1 s^-1$), which is standard for CCD imaging data.
"""
galaxy = ag.Galaxy(
    redshift=0.5,
    bulge=ag.lp.Sersic(
        centre=(0.0, 0.0),
        ell_comps=(0.0, 0.111111),
        intensity=1.0,  # in units of e- pix^-1 s^-1
        effective_radius=1.0,
        sersic_index=2.5,
    ),
)

galaxies = ag.Galaxies(galaxies=[galaxy])

"""
To visualize the galaxy’s image, which we will use as the starting point for the simulations, we use the following code:
"""
galaxies_plotter = aplt.GalaxiesPlotter(galaxies=galaxies, grid=grid)
galaxies_plotter.set_title("Galaxy Image Before Simulating")
galaxies_plotter.figures_2d(image=True)

"""
__Optics Blurring__

All images captured using CCDs (like those on the Hubble Space Telescope) experience some level of blurring 
due to the optics of the telescope. This blurring occurs because the optical system spreads out the light from each 
point source (e.g., a star or a part of a galaxy).

The Point Spread Function (PSF) describes how the telescope blurs the image. It can be thought of as a 2D representation 
of how a single point of light would appear in the image, spread out by the optics. In practice, the PSF is a 2D 
convolution kernel that we apply to the image to simulate this blurring effect.
"""
psf = ag.Kernel2D.from_gaussian(
    shape_native=(11, 11),  # The size of the PSF kernel, represented as an 11x11 grid.
    sigma=0.1,  # Controls the width of the Gaussian PSF, which determines the level of blurring.
    pixel_scales=grid.pixel_scales,  # Maintains consistency with the scale of the image grid.
    normalize=True,  # Normalizes the PSF kernel so that its values sum to 1.
)

"""
We can visualize the PSF to better understand how it will blur the galaxy's image. The PSF is essentially a small 
image that represents the spreading out of light from a single point source. This kernel will be used to blur the 
entire galaxy image when we perform the convolution.
"""
array_plotter = aplt.Array2DPlotter(array=psf)
array_plotter.set_title("PSF 2D Kernel")
array_plotter.figure_2d()

"""
The PSF is often more informative when plotted on a log10 scale. This approach allows us to clearly observe values 
in its tail, which are much smaller than the central peak yet critical for many scientific analyses. The tail 
values may significantly affect the spread and detail captured in the data.
"""
array_plotter = aplt.Array2DPlotter(array=psf, mat_plot_2d=aplt.MatPlot2D(use_log10=True))
array_plotter.set_title("PSF 2D Kernel")
array_plotter.figure_2d()

"""
Next, we'll manually perform a 2D convolution of the PSF with the image of the galaxy. This convolution simulates the 
blurring that occurs when the telescope optics spread out the galaxy's light.

1. **Padding the Image**: Before convolution, we add padding (extra space with zero values) around the edges of the 
   image. This prevents unwanted edge effects when we perform the convolution, ensuring that the image's edges don't 
   become artificially altered by the process.

2. **Convolution**: Using the `Kernel2D` object's `convolve` method, we apply the 2D PSF convolution to the padded 
   image. This step combines the PSF with the galaxy's light, simulating how the telescope spreads out the light.

3. **Trimming the Image**: After convolution, we trim the padded areas back to their original size, obtaining a 
   convolved (blurred) image that matches the dimensions of the initial galaxy image.
"""
image = galaxies.image_2d_from(grid=grid)  # The original unblurred image of the galaxy.
padded_image = galaxies.padded_image_2d_from(
    grid=grid, psf_shape_2d=psf.shape_native  # Adding padding based on the PSF size.
)
convolved_image = psf.convolved_array_from(
    array=padded_image
)  # Applying the PSF convolution.
blurred_image = convolved_image.trimmed_after_convolution_from(
    kernel_shape=psf.shape_native
)  # Trimming back to the original size.

"""
We can now plot the original and the blurred images side by side. This allows us to clearly see how the PSF 
convolution affects the appearance of the galaxy, making the image appear softer and less sharp.
"""
array_plotter = aplt.Array2DPlotter(array=image)
array_plotter.set_title("Galaxy Image Before PSF")
array_plotter.figure_2d()

array_plotter.set_title("Galaxy Image After PSF")
array_plotter = aplt.Array2DPlotter(array=blurred_image)
array_plotter.figure_2d()


"""
__Poisson Noise__

In addition to the blurring caused by telescope optics, we also need to consider Poisson noise when simulating imaging 
data.

When a telescope captures an image of a galaxy, photons from the galaxy are collected by the telescope's mirror and 
directed onto a CCD (Charge-Coupled Device). The CCD is made up of a silicon lattice (or another material) that 
converts incoming photons into electrons. These electrons are then gathered into discrete squares, which form the 
pixels of the final image.

The process of converting photons into electrons is inherently random, following a Poisson distribution. This randomness 
means that the number of electrons in each pixel can vary, even if the same number of photons hits the CCD. Therefore, 
the electron count per pixel becomes a Poisson random variable. For our simulation, this means that the recorded 
number of photons in each pixel will differ slightly from the true number due to this randomness.

To replicate this effect in our simulation, we can add Poisson noise to the galaxy image using NumPy’s random module, 
which generates values from a Poisson distribution.

It's important to note that the blurring caused by the telescope optics occurs before the photons reach the CCD. 
Therefore, we need to add the Poisson noise after blurring the galaxy image.

We also need to consider the units of our image data. Let’s assume that the galaxy image is measured in units of 
electrons per second ($e^- s^{-1}$), which is standard for CCD imaging data. To simulate the number of electrons 
actually detected in each pixel, we multiply the image by the observation’s exposure time. This conversion changes t
he units to the total number of electrons collected per pixel over the entire exposure time.

Once the image is converted, we add Poisson noise, simulating the randomness in the photon-to-electron conversion 
process. After adding the noise, we convert the image back to units of electrons per second for analysis, as 
this is the preferred unit for astronomers when studying their data.
"""
exposure_time = 300.0  # Units of seconds
blurred_image_counts = (
    blurred_image * exposure_time
)  # Convert to total electrons detected over the exposure time.
blurred_image_with_poisson_noise = (
    np.random.poisson(blurred_image_counts, blurred_image_counts.shape) / exposure_time
)  # Add Poisson noise and convert back to electrons per second.

"""
Here is what the blurred image with Poisson noise looks like.
"""
array_plotter = aplt.Array2DPlotter(
    array=ag.Array2D(values=blurred_image_with_poisson_noise, mask=grid.mask),
)
array_plotter.set_title("Image With Poisson Noise")
array_plotter.figure_2d()

"""
It is challenging to see the Poisson noise directly in the image above, as it is often subtle. To make the noise more 
visible, we can subtract the blurred image without Poisson noise from the one with noise.

This subtraction yields the "Poisson noise realization" which highlights the variation in each pixel due to the Poisson 
distribution of photons hitting the CCD. It represents the noise values that were added to each pixel. We call
it the realization because it is one possible outcome of the Poisson process, and the noise will be different each time
we simulate the image.
"""
poisson_noise_realization = blurred_image_with_poisson_noise - blurred_image

array_plotter = aplt.Array2DPlotter(
    array=ag.Array2D(values=poisson_noise_realization, mask=grid.mask)
)
array_plotter.set_title("Poisson Noise Realization")
array_plotter.figure_2d()

"""
__Background Sky__

The final effect we will consider when simulating imaging data is the background sky.

In addition to light from the galaxy, the telescope also picks up light from the sky. This background sky light is 
primarily due to two sources: zodiacal light, which is light scattered by interplanetary dust in the solar system, 
and the unresolved emission from distant stars and galaxies.

For our simulation, we'll assume that the background sky has a uniform brightness across the image, measured at 
0.1 electrons per second per pixel. The background sky is added to the image before applying the PSF convolution 
and adding Poisson noise. This is important because it means that the background contributes additional noise to the 
image.

The background sky introduces noise throughout the entire image, including areas where the galaxy is not present. 
This is why CCD images often appear noisy, especially in regions far from where the galaxy signal is detected. 
The sky noise can make it more challenging to observe faint details of the galaxy.

To simulate this, we add a constant background sky to the galaxy image and then apply Poisson noise to create the 
final simulated image as it would appear through a telescope.
"""
background_sky_level = 0.1

# Add background sky to the blurred galaxy image.
blurred_image_with_sky = blurred_image + background_sky_level
blurred_image_with_sky_counts = blurred_image_with_sky * exposure_time

# Apply Poisson noise to the image with the background sky.
blurred_image_with_sky_poisson_noise = (
    np.random.poisson(
        blurred_image_with_sky_counts, blurred_image_with_sky_counts.shape
    )
    / exposure_time
)

# Visualize the image with background sky and Poisson noise.
array_plotter = aplt.Array2DPlotter(
    array=ag.Array2D(values=blurred_image_with_sky_poisson_noise, mask=grid.mask),
)
array_plotter.set_title("Image With Background Sky")
array_plotter.figure_2d()

# Create a noise map showing the differences between the blurred image with and without noise.
poisson_noise_realization = (
    blurred_image_with_sky_poisson_noise - blurred_image_with_sky
)

array_plotter = aplt.Array2DPlotter(
    array=ag.Array2D(values=poisson_noise_realization, mask=grid.mask)
)
array_plotter.set_title("Poisson Noise Realization")
array_plotter.figure_2d()

"""
__Simulator__

The `SimulatorImaging` object lets us create simulated imaging data while including the effects of PSF blurring, 
Poisson noise, and background sky all at once:
"""
simulator = ag.SimulatorImaging(
    exposure_time=300.0, psf=psf, background_sky_level=0.1, add_poisson_noise=True
)

dataset = simulator.via_galaxies_from(galaxies=galaxies, grid=grid)

"""
By plotting the `data` from the dataset, we can see that it matches the image we simulated earlier. It includes 
the effects of PSF blurring, Poisson noise, and noise from the background sky. This image is a realistic 
approximation of what a telescope like the Hubble Space Telescope would capture.
"""
dataset_plotter = aplt.Array2DPlotter(array=dataset.data)
dataset_plotter.set_title("Simulated Imaging Data")
dataset_plotter.figure_2d()

"""
The dataset also includes the `psf` (Point Spread Function) used to blur the galaxy image.

For actual telescope data, the PSF is determined during data processing and is provided along with the observations. 
It's crucial for accurately deconvolving the PSF from the galaxy image, allowing us to recover the true properties 
of the galaxy. We'll explore this further in the next tutorial.
"""
array_plotter = aplt.Array2DPlotter(array=dataset.psf, mat_plot_2d=aplt.MatPlot2D(use_log10=True))
array_plotter.set_title("Simulated PSF")
array_plotter.figure_2d()

"""
The dataset includes a `noise_map`, which represents the Root Mean Square (RMS) standard deviation of the noise 
estimated for each pixel in the image. Higher noise values mean that the measurements in those pixels are 
less certain, so those pixels are given less weight when analyzing the data.

This `noise_map` is different from the Poisson noise arrays we plotted earlier. The Poisson noise arrays show the 
actual noise added to the image due to the random nature of photon-to-electron conversion on the CCD, as calculated 
using the numpy random module. These noise values are theoretical and cannot be directly measured in real telescope data.

In contrast, the `noise_map` is our best estimate of the noise present in the image, derived from the data itself 
and used in the fitting process.
"""
array_plotter = aplt.Array2DPlotter(array=dataset.noise_map)
array_plotter.set_title("Simulated Noise Map")
array_plotter.figure_2d()

"""
The `signal-to-noise_map` shows the ratio of the signal in each pixel to the noise level in that pixel. It is 
calculated by dividing the `data` by the `noise_map`.

This ratio helps us understand how much of the observed signal is reliable compared to the noise, allowing us to 
see where we can trust the detected signal from the galaxy and where the noise is more significant.

In general, a signal-to-noise ratio greater than 3 indicates that the signal is likely real and not overwhelmed by 
noise. For our datasets, the signal-to-noise ratio peaks at ~70, meaning we can trust the signal detected in the
image.
"""
array_plotter = aplt.Array2DPlotter(
    array=dataset.signal_to_noise_map,
)
array_plotter.set_title("Signal-To-Noise Map")
array_plotter.figure_2d()

"""
The `ImagingPlotter` object can display all of these components together, making it a powerful tool for visualizing 
simulated imaging data.

It also shows the Data and PSF on a logarithmic (log10) scale, which helps highlight the faint details in these 
components.

The "Over Sampling" plots on the bottom of the figures display advanced features that can be ignored for now.
"""
imaging_plotter = aplt.ImagingPlotter(dataset=dataset)
imaging_plotter.set_title(
    None
)  # Disable input title so subplot uses correct title for each sub-figure.
imaging_plotter.subplot_dataset()

"""
__Output__

We will now save these simulated data to `.fits` files, the standard format used by astronomers for storing images.
Most imaging data from telescopes like the Hubble Space Telescope (HST) are stored in this format.

The `dataset_path` specifies where the data will be saved, in this case, in the directory 
`autogalaxy_workspace/dataset/imaging/simple_example/`, which contains many example images distributed with 
the `autogalaxy_workspace`.

The files are named `data.fits`, `noise_map.fits`, and `psf.fits`, and will be used in the next tutorial.
"""
dataset_path = path.join("dataset", "imaging", "simple_example")
print("Dataset Path: ", dataset_path)

dataset.output_to_fits(
    data_path=path.join(dataset_path, "data.fits"),
    noise_map_path=path.join(dataset_path, "noise_map.fits"),
    psf_path=path.join(dataset_path, "psf.fits"),
    overwrite=True,
)

"""
__Wrap Up__

In this tutorial, you learned how CCD imaging data of a galaxy is collected using real telescopes like the 
Hubble Space Telescope, and how to simulate this data using the `SimulatorImaging` object.

Let's summarize what we've covered:

- **Optics Blurring**: The optics of a telescope blur the light from galaxies, reducing the clarity and sharpness of 
the images.

- **Poisson Noise**: The process of converting photons to electrons on a CCD introduces Poisson noise, which is random 
variability in the number of electrons collected in each pixel.

- **Background Sky**: Light from the sky is captured along with light from the galaxy, adding a layer of noise across 
the entire image.

- **Simulator**: The `SimulatorImaging` object enables us to simulate realistic imaging data by including all of 
these effects together and contains the `data`, `psf`, and `noise_map` components.

- **Output**: We saved the simulated data to `.fits` files, the standard format used by astronomers for storing images.

Tutorial 3: Fitting
===================

In previous tutorials, we used light profiles to create simulated images of galaxies and visualized how these images
would appear when captured by a CCD detector on a telescope like the Hubble Space Telescope.

However, this simulation process is the reverse of what astronomers typically do when analyzing real data. Usually,
astronomers start with an observation—an actual image of a galaxy—and aim to infer detailed information about the
galaxy’s properties, such as its shape, structure, formation, and evolutionary history.

To achieve this, we must fit the observed image data with a model, identifying the combination of light profiles that
best matches the galaxy's appearance in the image. In this tutorial, we'll illustrate this process using the imaging
data simulated in the previous tutorial. Our goal is to demonstrate how we can recover the parameters of the light
profiles that we used to create the original simulation, as a proof of concept for the fitting procedure.

The process of fitting data introduces essential statistical concepts like the `model`, `residual_map`, `chi-squared`,
`likelihood`, and `noise_map`. These terms are crucial for understanding how fitting works, not only in astronomy but
also in any scientific field that involves data modeling. This tutorial will provide a detailed introduction to these
concepts and show how they are applied in practice to analyze astronomical data.

Here is an overview of what we'll cover in this tutorial:

- **Dataset**: Load the imaging dataset that we previously simulated, consisting of the image, noise map, and PSF.
- **Mask**: Apply a mask to the data, excluding regions with low signal-to-noise ratios from the analysis.
- **Masked Grid**: Create a masked grid, which contains only the coordinates of unmasked pixels, to evaluate the
  galaxy's light profile in only unmasked regions.
- **Fitting**: Fit the data with a galaxy model, computing key quantities like the model image, residuals,
  chi-squared, and log likelihood to assess the quality of the fit.
- **Bad Fits**: Demonstrate how even small deviations from the true parameters can significantly impact the fit.
- **Model Fitting**: Perform a basic model fit on a simple dataset, adjusting the model parameters to improve the
  fit quality.
"""
import numpy as np
from os import path
import autogalaxy as ag
import autogalaxy.plot as aplt

"""
__Dataset__

We begin by loading the imaging dataset that we will use for fitting in this tutorial. This dataset is identical to the 
one we simulated in the previous tutorial, representing how a galaxy would appear if captured by a CCD camera.

In the previous tutorial, we saved this dataset as .fits files in the `autogalaxy_workspace/dataset/imaging/simple_example` 
folder. The `.fits` format is commonly used in astronomy for storing image data along with metadata, making it a
standard for CCD imaging.

The `dataset_path` below specifies where these files are located: `autogalaxy_workspace/dataset/imaging/simple_example/`.
"""
dataset_path = path.join("dataset", "imaging", "simple_example")

dataset = ag.Imaging.from_fits(
    data_path=path.join(dataset_path, "data.fits"),
    noise_map_path=path.join(dataset_path, "noise_map.fits"),
    psf_path=path.join(dataset_path, "psf.fits"),
    pixel_scales=0.1,
)

"""
The `Imaging` object contains three key components: `data`, `noise_map`, and `psf`:

- `data`: The actual image of the galaxy, which we will analyze.

- `noise_map`: A map indicating the uncertainty or noise level in each pixel of the image, reflecting how much the 
  observed signal in each pixel might fluctuate due to instrumental or background noise.
  
- `psf`: The Point Spread Function, which describes how a point source of light is spread out in the image by the 
  telescope's optics. It characterizes the blurring effect introduced by the instrument.

Let's print some values from these components and plot a summary of the dataset to refresh our understanding of the 
imaging data.
"""
print("Value of first pixel in imaging data:")
print(dataset.data.native[0, 0])
print("Value of first pixel in noise map:")
print(dataset.noise_map.native[0, 0])
print("Value of first pixel in PSF:")
print(dataset.psf.native[0, 0])

dataset_plotter = aplt.ImagingPlotter(dataset=dataset)
dataset_plotter.subplot_dataset()

"""
__Mask__

The signal-to-noise map of the image highlights areas where the signal (light from the galaxy) is detected above the 
background noise. Values above 3.0 indicate regions where the galaxy's light is detected with a signal-to-noise ratio
of at least 3, while values below 3.0 are dominated by noise, where the galaxy's light is not clearly distinguishable.

To ensure the fitting process focuses only on meaningful data, we typically mask out regions with low signal-to-noise 
ratios, removing areas dominated by noise from the analysis. This allows the fitting process to concentrate on the 
regions where the galaxy is clearly detected.

Here, we create a `Mask2D` to exclude certain regions of the image from the analysis. The mask defines which parts of 
the image will be used during the fitting process.

For our simulated image, a circular 3" mask centered at the center of the image is appropriate, since the simulated 
galaxy was positioned at the center.
"""
mask = ag.Mask2D.circular(
    shape_native=dataset.shape_native,
    pixel_scales=dataset.pixel_scales,
    radius=3.0,  # The circular mask's radius in arc-seconds
    centre=(0.0, 0.0),  # center of the image which is also the center of the galaxy
)

print(mask)  # 1 = True, meaning the pixel is masked. Edge pixels are indeed masked.
print(mask[48:53, 48:53])  # Central pixels are `False` and therefore unmasked.

"""
We can visualize the mask over the galaxy image using an `ImagingPlotter`, which helps us adjust the mask as needed. 
This is useful to ensure that the mask appropriately covers the galaxy's light and does not exclude important regions.

To overlay objects like a mask onto a figure, we use the `Visuals2D` object. This tool allows us to add custom 
visuals to any plot, providing flexibility in creating tailored visual representations.
"""
visuals = aplt.Visuals2D(mask=mask)

dataset_plotter = aplt.ImagingPlotter(dataset=dataset, visuals_2d=visuals)
dataset_plotter.set_title("Imaging Data With Mask")
dataset_plotter.figures_2d(data=True)

"""
Once we are satisfied with the mask, we apply it to the imaging data using the `apply_mask()` method. This ensures 
that only the unmasked regions are considered during the analysis.
"""
dataset = dataset.apply_mask(mask=mask)

"""
When we plot the masked imaging data again, the mask is now automatically included in the plot, even though we did 
not explicitly pass it using the `Visuals2D` object. The plot also zooms into the unmasked area, showing only the 
region where we will focus our analysis. This is particularly helpful when working with large images, as it centers 
the view on the regions where the galaxy's signal is detected.
"""
dataset_plotter = aplt.ImagingPlotter(dataset=dataset)
dataset_plotter.set_title("Masked Imaging Data")
dataset_plotter.figures_2d(data=True)

"""
The mask is now stored as an additional attribute of the `Imaging` object, meaning it remains attached to the 
dataset. This makes it readily available when we pass the dataset to a `FitImaging` object for the fitting process.
"""
print("Mask2D:")
print(dataset.mask)

"""
After applying the mask, the `native` representation of the data changes slighty.

The 2D array keeps its original shape, [total_y_pixels, total_x_pixels], but masked pixels (those where the mask is True) are set to 0.0.

Let's verify this by checking the `shape_native` of the data and printing a value at the edge which will have been
set to 0.0 and a value near the center which will be unchanged.
"""
print("Shape of the masked data:")
print(dataset.data.shape_native)

print("Example masked pixel in the image's native representation at its edge:")
print(dataset.data.native[0, 0])
print("Example unmasked pixel in the image's native representation at its center:")
print(dataset.data.native[50, 50])

"""
The `mask` object also has a `pixels_in_mask` attribute, which gives the number of unmasked pixels.
"""
print(dataset.data.mask.pixels_in_mask)

"""
__Masked Grid__

In tutorial 1, we emphasized that the `Grid2D` object is crucial for evaluating a galaxy's light profile. This grid 
contains (y, x) coordinates for each pixel in the image and is used to map out the positions where the galaxy's 
light is calculated.

From a `Mask2D`, we derive a `masked_grid`, which consists only of the coordinates of unmasked pixels. This ensures 
that light profile calculations focus exclusively on regions where the galaxy's light is detected, saving computational 
time and improving efficiency.

Below, we plot the masked grid:
"""
masked_grid = mask.derive_grid.unmasked

grid_plotter = aplt.Grid2DPlotter(grid=masked_grid)
grid_plotter.set_title("Masked Grid2D")
grid_plotter.figure_2d()

"""
By plotting this masked grid over the galaxy image, we can see that the grid aligns with the unmasked pixels of the 
image.

This alignment **is crucial** for accurate fitting because it ensures that when we evaluate a galaxy's light profile, 
the calculations occur only at positions where we have real data from.
"""
visuals = aplt.Visuals2D(grid=masked_grid)
imaging_plotter = aplt.ImagingPlotter(dataset=dataset, visuals_2d=visuals)
imaging_plotter.set_title("Image Data With 2D Grid Overlaid")
imaging_plotter.figures_2d(data=True)

"""
__Fitting__

Now that our data is masked, we are ready to proceed with the fitting process.

Fitting the data is done using the `Galaxy` and `Galaxies objects that we introduced in tutorial 2. We will start by 
setting up a `Galaxies`` object, using the same galaxy configuration that we previously used to simulate the 
imaging data. This setup will give us what is known as a 'perfect' fit, as the simulated and fitted models are identical.
"""
galaxy = ag.Galaxy(
    redshift=0.5,
    bulge=ag.lp.Sersic(
        centre=(0.0, 0.0),
        ell_comps=(0.0, 0.111111),
        intensity=1.0,  # in units of e- pix^-1 s^-1
        effective_radius=1.0,
        sersic_index=2.5,
    ),
)

galaxies = ag.Galaxies(galaxies=[galaxy])

"""
Next, let's plot the image of the galaxies. This should look familiar, as it is the same image we saw in 
previous tutorials. The difference now is that we use the dataset's `grid`, which corresponds to the `masked_grid` 
we defined earlier. This means that the galaxy image is only evaluated in the unmasked region, skipping calculations 
in masked regions.
"""
galaxies_plotter = aplt.GalaxiesPlotter(galaxies=galaxies, grid=dataset.grid)
galaxies_plotter.set_title("Galaxy Image To Be Fitted")
galaxies_plotter.figures_2d(image=True)

"""
Now, we proceed to fit the image by passing both the `Imaging` and `Galaxies` objects to a `FitImaging` object. 
This object will compute key quantities that describe the fit’s quality:

`image`: Creates an image of the galaxies using their image_2d_from() method.
`model_data`: Convolves the galaxy image with the data's PSF to account for the effects of telescope optics.
`residual_map`: The difference between the model data and observed data.
`normalized_residual_map`: Residuals divided by noise values, giving units of noise.
`chi_squared_map`: Squares the normalized residuals.
`chi_squared` and `log_likelihood`: Sums the chi-squared values to compute chi_squared, and converts this into 
a log_likelihood, which measures how well the model fits the data (higher values indicate a better fit).

Let's create the fit and inspect each of these attributes:
"""
fit = ag.FitImaging(dataset=dataset, galaxies=galaxies)
fit_imaging_plotter = aplt.FitImagingPlotter(fit=fit)

"""
The `model_data` represents the galaxy's image after accounting for effects like PSF convolution. 

An important technical note is that when we mask data, we discussed above how the image of the galaxy is not evaluated
outside the mask and is set to zero. This is a problem for PSF convolution, as the PSF blurs light from these regions
outside the mask but at its edge into the mask. They must be correctly evaluated to ensure the model image accurately
represents the image data.

The `FitImaging` object handles this internally, but evaluating the model image in the additional regions outside the mask
that are close enough to the mask edge to be blurred into the mask. 
"""
print("Central model image pixel:")
print(fit.model_data.native[50, 50])
fit_imaging_plotter.figures_2d(model_image=True)

"""
Even before computing other fit quantities, we can normally assess if the fit is going to be good by visually comparing
the `data` and `model_data` and assessing if they look similar.

In this example, the galaxies used to fit the data are the same as the galaxies used to simulate it, so the two
look very similar (the only difference is the noise in the image).
"""
fit_imaging_plotter.figures_2d(data=True)
fit_imaging_plotter.figures_2d(model_image=True)

"""
The `residual_map` is the different between the observed image and model image, showing where in the image the fit is
good (e.g. low residuals) and where it is bad (e.g. high residuals).

The expression for the residual map is simply:

`residual_map` = (`data` - `model_data`)

The residual-map is plotted below, noting that all values are very close to zero because the fit is near perfect.
The only non-zero residuals are due to noise in the image.
"""
residual_map = dataset.data - fit.model_data
print("Central residual-map pixel:")
print(residual_map.native[50, 50])

print("Central residual-map pixel via fit:")
print(fit.residual_map.native[50, 50])

fit_imaging_plotter.figures_2d(residual_map=True)

"""
Are these residuals indicative of a good fit to the data? Without considering the noise in the data, it's difficult 
to ascertain. That is, its hard to ascenrtain if a residual value is large or small because this depends on the
amount of noise in that pixel.

The `normalized_residual_map` divides the residual-map by the noise-map, giving the residual in units of the noise.
Its expression is:

 `normalized_residual_map` = `residual_map` / `noise_map` = (`data` - `model_data`) / `noise_map`

If you're familiar with the concept of standard deviations (sigma) in statistics, the normalized residual map represents 
how many standard deviations the residual is from zero. For instance, a normalized residual of 2.0 (corresponding 
to a 95% confidence interval) means that the probability of the model underestimating the data by that amount is only 5%.
"""
normalized_residual_map = residual_map / dataset.noise_map

print("Central normalized residual-map pixel:")
print(normalized_residual_map.native[50, 50])

print("Central normalized residual-map pixel via fit:")
print(fit.normalized_residual_map.native[50, 50])

fit_imaging_plotter.figures_2d(normalized_residual_map=True)

"""
Next, we define the `chi_squared_map`, which is obtained by squaring the `normalized_residual_map` and serves as a 
measure of goodness of fit.

The chi-squared map is calculated as:

`chi_squared_map` = (`normalized_residuals`) ** 2.0 = ((`data` - `model_data`)**2.0)/(`variances`)

Squaring the normalized residual map ensures all values are positive. For instance, both a normalized residual of -0.2 
and 0.2 would square to 0.04, indicating the same quality of fit in terms of `chi_squared`.

As seen from the normalized residual map, it's evident that the model provides a good fit to the data, in this
case because the chi-squared values are close to zero.
"""
chi_squared_map = (normalized_residual_map) ** 2
print("Central chi-squared pixel:")
print(chi_squared_map.native[50, 50])

print("Central chi-squared pixel via fit:")
print(fit.chi_squared_map.native[50, 50])

fit_imaging_plotter.figures_2d(chi_squared_map=True)

"""
Now, we consolidate all the information in our `chi_squared_map` into a single measure of goodness-of-fit 
called `chi_squared`. 

It is defined as the sum of all values in the `chi_squared_map` and is computed as:

`chi_squared` = sum(`chi_squared_map`)

This is algebraically written as:

$\chi^2 = \sum \left(\frac{\text{data} - \text{model\_data}}{\text{noise\_map}}\right)^2$

This summing process highlights why ensuring all values in the chi-squared map are positive is crucial. If we 
didn't square the values (making them positive), positive and negative residuals would cancel each other out, 
leading to an inaccurate assessment of the model's fit to the data.

The lower the `chi_squared`, the fewer residuals exist between the model's fit and the data, indicating a better 
overall fit!
"""
chi_squared = np.sum(chi_squared_map)
print("Chi-squared = ", chi_squared)
print("Chi-squared via fit = ", fit.chi_squared)

"""
The reduced chi-squared is the `chi_squared` value divided by the number of data points (e.g., the number of pixels
in the mask). 

This quantity offers an intuitive measure of the goodness-of-fit, as it normalizes the `chi_squared` value by the
number of data points. That is, a reduced chi-squared of 1.0 indicates that the model provides a good fit to the data,
because every data point is fitted with a chi-squared value of 1.0.

A reduced chi-squared value significantly greater than 1.0 indicates that the model is not a good fit to the data,
whereas a value significantly less than 1.0 suggests that the model is overfitting the data.
"""
reduced_chi_squared = chi_squared / dataset.mask.pixels_in_mask
print("Reduced Chi-squared = ", reduced_chi_squared)

"""
Another quantity that contributes to our final assessment of the goodness-of-fit is the `noise_normalization`.

The `noise_normalization` is computed as the logarithm of the sum of squared noise values in our data: 

`noise_normalization` = np.sum(np.log(2 * np.pi * `noise_map`**2))

This is algebraically written as:

 $\sum_{\rm  j=1}^{J} { \mathrm{ln}} \left [2 \pi (\text{noise\_map})^2 \right]  \, .$

This quantity is fixed because the noise-map remains constant throughout the fitting process. Despite this, 
including the `noise_normalization` is considered good practice due to its statistical significance.

Understanding the exact meaning of `noise_normalization` isn't critical for our primary goal of successfully 
fitting a model to a dataset. Essentially, it provides a measure of how well the noise properties of our data align 
with a Gaussian distribution.
"""
noise_normalization = np.sum(np.log(2 * np.pi * dataset.noise_map**2))
print("Noise Normalization = ", noise_normalization)
print("Noise Normalization via fit = ", fit.noise_normalization)

"""
From the `chi_squared` and `noise_normalization`, we can define a final goodness-of-fit measure known as 
the `log_likelihood`. 

This measure is calculated by taking the sum of the `chi_squared` and `noise_normalization`, and then multiplying the 
result by -0.5:

`log_likelihood` = -0.5 * (`chi_squared` + `noise_normalization`)

Don't worry about why we multiply by -0.5; it's a standard practice in statistics to ensure the log likelihood is
defined correctly.
"""
log_likelihood = -0.5 * (chi_squared + noise_normalization)
print("Log Likelihood = ", log_likelihood)
print("Log Likelihood via fit = ", fit.log_likelihood)

"""
In the previous discussion, we noted that a lower \(\chi^2\) value indicates a better fit of the model to the 
observed data. 

When we calculate the log likelihood, we take the \(\chi^2\) value and multiply it by -0.5. This means that a 
higher log likelihood corresponds to a better model fit. Our goal when fitting models to data is to maximize the 
log likelihood.

The **reduced \(\chi^2\)** value provides an intuitive measure of goodness-of-fit. Values close to 1.0 suggest a 
good fit, while values below or above 1.0 indicate potential underfitting or overfitting of the data, respectively. 
In contrast, the log likelihood values can be less intuitive. For instance, a log likelihood value printed above 
might be around 5300.

However, log likelihoods become more meaningful when we compare them. For example, if we have two models, one with 
a log likelihood of 5300 and the other with 5310 we can conclude that the first model fits the data better 
because it has a higher log likelihood by 10.0. 

In fact, the difference in log likelihood between models can often be associated with a probability indicating how 
much better one model fits the data compared to another. This can be expressed in terms of standard deviations (sigma). 

As a rule of thumb:

- A difference in log likelihood of **2.5** suggests that one model is preferred at the **2.0 sigma** level.
- A difference in log likelihood of **5.0** indicates a preference at the **3.0 sigma** level.
- A difference in log likelihood of **10.0** suggests a preference at the **5.0 sigma** level.

All these metrics can be visualized together using the `FitImagingPlotter` object, which offers a comprehensive 
overview of the fit quality.
"""
fit = ag.FitImaging(dataset=dataset, galaxies=galaxies)

fit_bad_imaging_plotter = aplt.FitImagingPlotter(fit=fit)
fit_bad_imaging_plotter.subplot_fit()

"""
If you're familiar with model-fitting, you've likely encountered terms like 'residuals', 'chi-squared', 
and 'log_likelihood' before. 

These metrics are standard ways to quantify the quality of a model fit. They are applicable not only to 1D data but 
also to more complex data structures like 2D images, 3D data cubes, or any other multidimensional datasets.

__Incorrect Fit__

In the previous section, we successfully created and fitted a galaxy model to the image data, resulting in an 
excellent fit. The residual map and chi-squared map showed no significant discrepancies, indicating that the 
galaxy's light was accurately captured by our model. This optimal solution translates to one of the highest log 
likelihood values possible, reflecting a good match between the model and the observed data.

Now, let's modify our galaxy model to create a fit that is close to the correct solution but slightly off. 
Specifically, we will slightly offset the center of the galaxy by half a pixel (0.05") in both the x and y directions. 
This change will allow us to observe how even small deviations from the true parameters can impact the quality of the fit.
"""
galaxy = ag.Galaxy(
    redshift=0.5,
    bulge=ag.lp.Sersic(
        centre=(0.05, 0.05),  # This is different from the previous center.
        ell_comps=(0.0, 0.111111),
        intensity=1.0,
        effective_radius=1.0,
        sersic_index=2.5,
    ),
)

galaxies = ag.Galaxies(galaxies=[galaxy])

"""
After implementing this slight adjustment, we can now plot the fit. In doing so, we observe that residuals have 
emerged at the center of the galaxy, which indicates a mismatch between our model and the data. Consequently, 
this discrepancy results in increased chi-squared values, which in turn affects our log likelihood.
"""
fit_bad = ag.FitImaging(dataset=dataset, galaxies=galaxies)

fit_bad_imaging_plotter = aplt.FitImagingPlotter(fit=fit_bad)
fit_bad_imaging_plotter.subplot_fit()

"""
Next, we can compare the log likelihood of our current model to the log likelihood value we computed previously.
"""
print("Previous Likelihood:")
print(fit.log_likelihood)
print("New Likelihood:")
print(fit_bad.log_likelihood)

"""
As expected, we observe that the log likelihood has decreased! This decline confirms that our new model is indeed a 
worse fit to the data compared to the original model.

Now, let’s change our galaxy model once more, this time setting it to a position that is far from the true parameters. 
We will offset the galaxy's center significantly to see how this extreme deviation affects the fit quality.
"""
galaxy = ag.Galaxy(
    redshift=0.5,
    bulge=ag.lp.Sersic(
        centre=(
            0.65,
            0.65,
        ),  # This position is significantly different from the previous one.
        ell_comps=(0.0, 0.111111),
        intensity=1.0,
        effective_radius=1.0,
        sersic_index=2.5,
    ),
)

galaxies = ag.Galaxies(galaxies=[galaxy])

fit_very_bad = ag.FitImaging(dataset=dataset, galaxies=galaxies)

fit_very_bad_imaging_plotter = aplt.FitImagingPlotter(
    fit=fit_very_bad,
)
fit_very_bad_imaging_plotter.subplot_fit()

"""
It is now evident that this model provides a terrible fit to the data. The galaxies do not resemble a plausible 
representation of our simulated galaxy dataset, which we already anticipated given that we generated the data ourselves!

As expected, the log likelihood has dropped dramatically with this poorly fitting model.
"""
print("Previous Likelihoods:")
print(fit.log_likelihood)
print(fit_bad.log_likelihood)
print("New Likelihood:")
print(fit_very_bad.log_likelihood)

"""
__Model Fitting__

In the previous sections, we used the true model to fit the data, which resulted in a high log likelihood and minimal 
residuals. We also demonstrated how even small deviations from the true parameters can significantly degrade the fit 
quality, reducing the log likelihood.

In practice, however, we don't know the "true" model. For example, we might have an image of a galaxy observed with 
the Hubble Space Telescope, but the values for parameters like its `effective_radius`, `sersic_index`, and others are 
unknown. The process of determining the best-fit model is called model fitting, and it is the main topic of 
the next tutorial.

Let's perform a basic, hands-on model fit to develop some intuition about how we can find the best-fit model. We'll 
start by loading a simple dataset that was simulated using a `Sersic` profile, where the true parameters of this 
profile are unknown, and masking it to again exclude regions with low signal.
"""
dataset_name = "simple__sersic"
dataset_path = path.join("dataset", "imaging", dataset_name)

dataset = ag.Imaging.from_fits(
    data_path=path.join(dataset_path, "data.fits"),
    psf_path=path.join(dataset_path, "psf.fits"),
    noise_map_path=path.join(dataset_path, "noise_map.fits"),
    pixel_scales=0.1,
)

mask = ag.Mask2D.circular(
    shape_native=dataset.shape_native,
    pixel_scales=dataset.pixel_scales,
    radius=3.0,
)

dataset = dataset.apply_mask(mask=mask)

dataset_plotter = aplt.ImagingPlotter(dataset=dataset)
dataset_plotter.subplot_dataset()


"""
Now, you'll try to determine the best-fit model for this image, corresponding to the parameters used to simulate the 
dataset.

We'll use the simplest possible approach: try different combinations of light profile parameters and adjust them 
based on how well each model fits the data. You’ll quickly find that certain parameters produce a much better fit 
than others. For example, determining the correct values of the `centre` should not take too long.

Pay attention to the `log_likelihood` and the `residual_map` as you adjust the parameters. These will guide you in 
determining if your model is providing a good fit to the data. Aim to increase the log likelihood and reduce the 
residuals.

Keep experimenting with different values for a while, seeing how small you can make the residuals and how high you 
can push the log likelihood. Eventually, you’ll likely reach a point where further improvements become difficult, 
even after trying many different parameter values. This is a good point to stop and reflect on your first experience 
with model fitting, and then to scroll to the next cell to see a discussion of the exercise.
"""
galaxy = ag.Galaxy(
    redshift=0.5,
    bulge=ag.lp.Sersic(
        centre=(1.0, 10),  # These are the parameters
        ell_comps=(0.5, 0.9),  # you need to adjust
        intensity=1.0,  # to try and improve
        effective_radius=1.0,  #  the model's fit
        sersic_index=1.0,  # to the data!
    ),
)

galaxies = ag.Galaxies(galaxies=[galaxy])

fit = ag.FitImaging(dataset=dataset, galaxies=galaxies)

fit_plotter = aplt.FitImagingPlotter(fit=fit)
fit_plotter.subplot_fit()

print("Log Likelihood:")
print(fit.log_likelihood)

"""
Manually guessing model parameters repeatedly is a very inefficient and slow way to find the best fit. If the model 
were more complex—say, if the `galaxy` had additional light profile components beyond just its `bulge` (like a 
second `Sersic` profile representing a `disk`)—the model would become so intricate that this manual approach 
would be practically impossible. This is definitely not how model fitting is done in practice.

However, this exercise has given you a basic intuition for how model fitting works. The statistical inference tools 
that are actually used for model fitting will be introduced in the next section. Interestingly, these tools are not 
entirely different from the approach you just tried. Essentially, they also involve iteratively testing models until 
those with high log likelihoods are found. The key difference is that a computer can perform this process thousands of 
times, and it does so in a much more efficient and strategic way.

__Linear Light Profile__

In the example above, we iteratively adjusted the parameters of a `Sersic` light profile to fit the data. There were
7 parameters in total, which is a lot to adjust manually. Any trick which can reduce the number of parameters we need
to adjust would therefore be advantageous.

This is possible using linear light profiles, which solve for the `intensity` parameter of the light profile via 
efficient linear  algebra, using a process called an inversion. The details of how an inversion works are not important,
the thing to note is they always compute `intensity` values for each light profile that give the best 
fit to the data (e.g. they minimize the chi-squared and therefore maximize the likelihood). 

Below we show an example using a linear light profile, but replacing the call `ag.lp` with `ag_lp_linear`,
which if you compare to solutions above you will find have higher likelihood values because the `intensity` is
always set to maximize the likelihood.
"""
galaxy = ag.Galaxy(
    redshift=0.5,
    bulge=ag.lp_linear.Sersic(
        centre=(1.0, 10),
        ell_comps=(0.5, 0.9),
        effective_radius=1.0,
        sersic_index=1.0,
    ),
)

galaxies = ag.Galaxies(galaxies=[galaxy])

fit = ag.FitImaging(dataset=dataset, galaxies=galaxies)

fit_plotter = aplt.FitImagingPlotter(fit=fit)
fit_plotter.subplot_fit()

print("Log Likelihood:")
print(fit.log_likelihood)

"""
__Intensities__

The fit contains the solved for intensity values.

These are computed using a fit's `linear_light_profile_intensity_dict`, which maps each linear light profile 
in the model parameterization above to its `intensity`.

The code below shows how to use this.
"""
print(fit.linear_light_profile_intensity_dict)

print(
    f"\n Intensity of galaxy's bulge = {fit.linear_light_profile_intensity_dict[galaxy.bulge]}"
)

"""
__Wrap Up__

In this tutorial, you have learned how to fit a galaxy model to imaging data, a fundamental process in astronomy
and statistical inference. 

Let's summarize what we have covered:

- **Dataset**: We loaded the imaging dataset that we previously simulated, consisting of the galaxy image, noise map,
  and PSF.
  
- **Mask**: We applied a circular mask to the data, excluding regions with low signal-to-noise ratios from the analysis.

- **Masked Grid**: We created a masked grid, which contains only the coordinates of unmasked pixels, to evaluate the
  galaxy's light profile.
  
- **Fitting**: We fitted the data with a galaxy model, computing key quantities like the model image, residuals,
  chi-squared, and log likelihood to assess the quality of the fit.
  
- **Bad Fits**: We demonstrated how even small deviations from the true parameters can significantly impact the fit
  quality, leading to decreased log likelihood values.
  
- **Model Fitting**: We performed a basic model fit on a simple dataset, adjusting the model parameters to improve the
  fit quality.


Tutorial 4: Non-linear Search
=============================

The starting point for most scientific analysis conducted by an Astronomer is that they have observations of a galaxy
using a telescope like the Hubble Space Telescope, and seek to learn about the galaxy and the Universe from these
observations. With **PyAutoGalaxy**, we seek to learn about the galaxy's structure and morphology, asking questions like
how big is the galaxy, is it disky or bulgy, and how is its light distributed?

To answer these questions, we must therefore fit the dataset with a model of the galaxy, where the model defines the
light profile that make up the galaxy we fit. Our goal is the find the combination of light profile parameters that
best-fit the data, such that the model represents the galaxy, and therefore the Universe, as well as possible.

This process is called model-fitting, or "modeling" for short, and we actually did our first example of this in the
previous chapter. If you recall, in the fitting tutorial we set up a fit to a simulated dataset where the parameter
used to simulate the data were unknown, and you guessed the values of the parameters that best fit the data. You
iteratively improved the model-fit by guessing new parameters, over and over, finding solutions which produced
higher `log_likelihood` values.

However, this approach was not optimal: it was manual and slow, we had no certainty that we had found the best
(e.g. maximum likelihood) solution and for more complex models, with more parameters and light profiles, it would
have been completely unfeasible.

In this chapter, we perform modeling as a scientist would actually do it, and introduce the statistical inference
technique that will ultimately allow us to fit complex models made of many light profiles to real galaxy data,
and begin learning about real galaxies in the Universe.

This section introduces a number of key statistical concepts that are fundamental to understanding how
model-fitting works, both for **PyAutoGalaxy** and in general.

__Overview__

In this tutorial, we will use a non-linear search to fit a single Sersic light profile to simulated imaging of a
galaxy. We will:

- Introduce concept like a "parameter space", "likelihood surface" and "priors", and relate them to how a non-linear
  search works.

- Introduce the `Analysis` class, which defines the `log_likelihood_function` that quantifies the goodness of fit of a
  model instance to the data.

- Fit datasets using a "non-linear search" technique called nested sampling.

__Contents__

This tutorial is split into the following sections:

- **Parameter Space**: Introduce the concept of a "parameter space" and how it relates to model-fitting.
- **Non-Linear Search**: Introduce the concept of a "non-linear search" and how it fits models to data.
- **Nested Sampling**: Introduce the nested sampling search algorithm used in this tutorial.
- **Deeper Background**: Provide links to resources that more thoroughly describe the statistical principles that underpin non-linear searches.
- **Data**: Load and plot the galaxy dataset we'll fit.
- **Model**: Introduce the galaxy model we'll fit to the data.
- **Priors**: Introduce priors and how they are used to define the parameter space and guide the non-linear search.
- **Analysis**: Introduce the `Analysis` class, which contains the `log_likelihood_function` used to fit the model to the data.
- **Nested Sampling**: Perform a model-fit using the nested sampling search.
- **Result**: The result of the model-fit, including the maximum likelihood model.
- **Samples**: The samples of the non-linear search, used to compute parameter estimates and uncertainties.
- **Customizing Searches**: How to customize the settings of the non-linear search.
- **Wrap Up**: A summary of the concepts introduced in this tutorial.

__Parameter Space__

In mathematics, a function is defined by its parameters, which map inputs to outputs. For example, consider the simple function:

f(x) = x^2

Here, \(x\) is the input parameter, and f(x) returns the output x^2. This relationship defines
the "parameter space" of the function, which in this case forms a parabola.

Functions can also have multiple parameters, such as:

f(x, y, z) = x + y^2 - z^3

This defines a parameter space in three dimensions, representing the relationships between \(x\), \(y\), \(z\),
and the output f(x, y, z).

This concept of parameter space is closely related to how we approach model-fitting. For instance, in chapter 1, we created instances of a `Galaxy` object with
parameters like \(`centre_0`, `centre_1`, `ell_comps_0`, `ell_comps_1`, `intensity`, `effective_radius`, `sersic_index`\).
These parameters were used to fit data and compute a log likelihood.

We can think of this process as analogous to the function: 

f(`centre_0`, `centre_1`, `ell_comps_0`, `ell_comps_1`, `intensity`, `effective_radius`, `sersic_index`),

where the output is the log likelihood. This function, which maps parameter values to a log likelihood, is known
as the "likelihood function" in statistical inference. To be explicit, we’ll refer to it as the `log_likelihood_function`
since it deals with the log of the likelihood function.

By framing the likelihood this way, we can think of our model as having its own parameter space—a multidimensional
surface defined by all possible values of the
parameters (`centre_0`, `centre_1`, `ell_comps_0`, `ell_comps_1`, `intensity`, `effective_radius`, `sersic_index`).
This surface, known as the "likelihood surface," represents how the log likelihood changes across different parameter
values. During model-fitting, our goal is to find the peak of this surface, where the fit to the data is optimal.

This parameter space is "non-linear," meaning the relationship between the model parameters and the log likelihood is
not a simple linear one. Because of this non-linearity, we cannot predict the log likelihood from a given set of model
parameters without actually performing a fit to the data, as we did in tutorial 1.

__Non-Linear Search__

Now that we understand our problem in terms of a non-linear parameter space with a likelihood surface, we can
introduce the method used to fit the model to the data —- the "non-linear search".

Previously, our approach involved manually guessing models until finding one with a good fit and high log likelihood.
Surprisingly, this random guessing forms the basis of how model-fitting using a non-linear search actually works!

A non-linear search involves systematically guessing many models while tracking their log likelihoods. As the
algorithm progresses, it tends to favor models with parameter combinations that have previously yielded higher
log likelihoods. This iterative refinement helps to efficiently explore the vast parameter space.

There are two key differences between guessing random models and using a non-linear search:

- **Computational Efficiency**: The non-linear search can evaluate the log likelihood of a model parameter
  combinations in milliseconds and therefore many thousands of models in minutes. This computational speed enables
  it to thoroughly sample potential solutions, which would be impractical for a human.

- **Effective Sampling**: The search algorithm maintains a robust memory of previously guessed models and their log
  likelihoods. This allows it to sample potential solutions more thoroughly and converge on the highest
  likelihood solutions more efficiently, which is again impractical for a human.

Think of the non-linear search as systematically exploring parameter space to pinpoint regions with the highest log
likelihood values. Its primary goal is to identify and converge on the parameter values that best describe the data.
"""
from os import path
import autogalaxy as ag
import autogalaxy.plot as aplt

"""
__PyAutoFit__

Modeling uses the probabilistic programming language
[PyAutoFit](https://github.com/rhayes777/PyAutoFit), an open-source project that allows complex model
fitting techniques to be straightforwardly integrated into scientific modeling software. 

We import this library separately from **PyAutoGalaxy**.
"""
import autofit as af

"""
__Initial Setup__

Let's first load the `Imaging` dataset, which we will use to fit a model with a non-linear search.

The galaxy in this image was generated using a `Sersic` light profile, which we'll also use in our model fitting 
in this tutorial. This means the model we are going to fit is identical to the one used to simulate the data, 
allowing us to assess the fitting process under controlled conditions.

The dataset, as well as all subsequent datasets used in future tutorials, is stored in 
the `autogalaxy_workspace/dataset/imaging` folder. 
"""
dataset_name = "simple__sersic"
dataset_path = path.join("dataset", "imaging", dataset_name)

dataset = ag.Imaging.from_fits(
    data_path=path.join(dataset_path, "data.fits"),
    noise_map_path=path.join(dataset_path, "noise_map.fits"),
    psf_path=path.join(dataset_path, "psf.fits"),
    pixel_scales=0.1,
)

dataset_plotter = aplt.ImagingPlotter(dataset=dataset)
dataset_plotter.subplot_dataset()

"""
__Mask__

The fit requires a mask, which we define as a 3.0" circle.
"""
mask = ag.Mask2D.circular(
    shape_native=dataset.shape_native, pixel_scales=dataset.pixel_scales, radius=3.0
)

dataset = dataset.apply_mask(mask=mask)

dataset_plotter = aplt.ImagingPlotter(dataset=dataset)
dataset_plotter.subplot_dataset()

"""
__Model__

To compose a model, we set up a `Galaxy` using a `af.Model`. Instead of manually specifying every parameter 
for the galaxy's light profiles (as we did before), we will now define the galaxy using only the class of each 
profile. Using a `Model` object tells **PyAutoGalaxy** that the parameters of the profiles should be fitted for 
during the non-linear search.

In this case, we'll model the galaxy with an elliptical Sersic light profile, which represents 
its bulge component (the same profile used to simulate the galaxy). W

We again use the linear light profile variant via `ag.lp_linear`, which makes the modeling process more accurate
and efficient by not having to fit for the `intensity` parameter of the light profile.
"""
galaxy_model = af.Model(ag.Galaxy, redshift=0.5, bulge=ag.lp_linear.Sersic)

"""
We now input the model component into a `Collection` object, which groups all the model components used to fit the data.

As with profiles, we give galaxies descriptive names like `bulge`, or `disk`. Since this model has only one 
galaxy, we'll simply refer to it as `galaxy` throughout the tutorials.

It may seem odd that we define two `Collections`, with the `Collection` in the outer loop only having a `galaxies`
attribute. For certain tasks, we may have multiple galaxies in a model, and the code below would allow us to therefore
add multiple galaxies to the model. For now, however, we only have one galaxy.
"""
model = af.Collection(galaxies=af.Collection(galaxy=galaxy_model))

"""
The `info` attribute shows the model in a readable format.
"""
print(model.info)

"""
__Priors__

When we examine the `.info` of our model, we notice that each parameter (like `centre`, `effective_radius`, 
and `sersic_index` in our `Sersic` model) is associated with priors, such as `UniformPrior`. Priors define the 
range of permissible values that each parameter can assume during the model fitting process, for example a uniform
prior means that a parameter is equally likely to be any value within the given range, but cannot be outside of it.

The priors displayed above use default values which are broad, and contain the breadth of plausible solutions one 
should expect when fitting light profiles to a real galaxy.

For instance, consider the `centre` parameter of our `Sersic` light profile. In theory, it could take on any value from 
negative to positive infinity. However, imaging datasets are reduced such that the galaxy centre is close 
to (0.0", 0.0"). Therefore, a `GaussianPrior` with `mean=0.0` and `sigma=0.1` is a good description of where the
galaxy `centre` is. 

For certain tasks, the galaxy have have a different centre in the dataset, therefore the mean of the prior would be 
updated to reflect this.

Priors serve two primary purposes:

**Defining Valid Parameter Space:** Priors specify the range of parameter values that constitute valid solutions. 
This ensures that our model explores only those solutions that are consistent with our observed data and physical 
constraints.

**Incorporating Prior Knowledge:** Priors also encapsulate our prior beliefs or expectations about the model 
parameters. For instance, if we have previously fitted a similar model to another dataset and obtained certain 
parameter values, we can incorporate this knowledge into our priors for a new dataset. This approach guides the 
model fitting process towards parameter values that are more probable based on our prior understanding.

Below, we manually specify the priors on all parameter in our `Sersic` model. The custom priors below are
close to the default priors, with the main purpose of the code below to show you how to customize priors yourself.
"""
model.galaxies.galaxy.bulge.centre.centre_0 = af.GaussianPrior(mean=0.0, sigma=0.1)
model.galaxies.galaxy.bulge.centre.centre_1 = af.GaussianPrior(mean=0.0, sigma=0.1)
model.galaxies.galaxy.bulge.ell_comps.ell_comps_0 = af.UniformPrior(
    lower_limit=-1.0, upper_limit=1.0
)
model.galaxies.galaxy.bulge.ell_comps.ell_comps_1 = af.UniformPrior(
    lower_limit=-1.0, upper_limit=1.0
)
model.galaxies.galaxy.bulge.effective_radius = af.UniformPrior(
    lower_limit=0.0, upper_limit=10.0
)
model.galaxies.galaxy.bulge.sersic_index = af.UniformPrior(
    lower_limit=0.8, upper_limit=8.0
)

"""
By reprinting the `model.info`, we can see that the priors have been updated to the values we specified.
"""
print(model.info)

"""
__Analysis__

The `AnalysisImaging` object defines how an instance of a model, consisting of a set of parameters values for the 
light profiles, is fitted to the `Imaging` dataset.

The fit is performed using the analysis class's `log_likelihood_function`, which in model-fitting is a commonly used 
term to describe a function that given a model and data, fits the model to the data to return a value of log 
likelihood. 

In sections 1, 2 and 3 you essentially performed this likelihood function yourself by hand, when you 
entered different models to a `FitImaging` object and used its `log_likelihood` property to quantify how well it 
fitted the data.
"""
analysis = ag.AnalysisImaging(dataset=dataset)

"""
__Searches__

we now perform a non-linear search to fit the model of the galaxy to the data.

**Nested Sampling** is an advanced method for model-fitting that excels in fitting complex models with intricate 
parameter spaces. 

Here’s a simplified overview of its process:

1. Start with a set of "live points" in parameter space, each initialized with random parameter values drawn from their respective priors.

2. Compute the log likelihood for each live point.

3. Draw a new point based on the likelihood of the current live points, favoring regions of higher likelihood.

4. If the new point has a higher likelihood than any existing live point, it becomes a live point, and the lowest likelihood live point is discarded.

This iterative process continues, gradually focusing the live points around higher likelihood regions of parameter 
space until they converge on the highest likelihood solution.

Nested Sampling effectively maps out parameter space, providing accurate estimates of parameters and their uncertainties.
"""
search = af.Nautilus(
    name="example_0",
    n_live=50,
    iterations_per_update=1000,
    force_x1_cpu=True # This ensures the Google Colab code runs correctly
)

"""
To begin the model-fit via the non-linear search, we pass it our model and analysis and begin the fit.

It features a built-in stopping criterion, meaning the fit will stop running automatically when it has sampled all
of parameter space and identified the model with the highest likelihood. 

Model fitting typically takes between 5 and 10 minutes to run, which means the Jupyter notebook cell will be running
for this duration of time. Run the cell below to begin the non-linear search, and then read the cell afterwards
whilst it is running in order to understand how you can inspect the results of the fit during and after it has
completed.
"""
print(
    """
    The non-linear search has begun running.
    This Jupyter notebook cell with progress once the search has completed - this could take a few minutes!
    """
)

result = search.fit(model=model, analysis=analysis)

"""
__Output__

Owing to the relatively long run times of model fitting, the results are output and stored in a folder which you can 
manually inspect whilst the Jupyter notebook cell is running. 

In Google Colab, you can access this folder by clicking the folder icon on the left of the screen and navigating to 
the `BSc_Galaxies_Project/output` folder. This will contain a folder named `example`, corresponding to the input
`name=example'` we specified when we created the non-linear search above. 

The screenshot below shows how your Google Colab should appear when you click the folder icon, with red squares
highlighting the output folder and other folders which are important and described in the next paragraph:

![ColabFolderOutput](https://github.com/Jammy2211/BSc_Galaxies_Project/blob/master/Colab_Example_Folder_Output.png?raw=true)

Inside this folder is a folder which is a collection of characters, which is a unique identifier which ensures if you 
rerun the Jupyter notebook cell it loads the results from the previous run, thus saving time by not rerunning the
non-linear search.

Inside the unique identifier folder are a number of files you should inspect:

 - `model.info`: Summarizes the model, its parameters and their priors.
 
 - `model.results`: Summarizes the highest likelihood model inferred so far including errors.
 
 - `images`: Visualization of the highest likelihood model-fit to the dataset as a file called `subplot_fit.png`.

The files `model.results` and those contained in `images` are only generated after the non-linear search has completed
`iteration_per_update` number of iterations, which for the input value above of 1000 will take approximately 2-3 minutes.

The Jupyter notebook cell will display when it outputs these results, so you should monitor the cell and look
for these files once it has performed an update.

__Result__

Upon completion the non-linear search returns a `Result` object, which contains information about the model-fit.

The `info` attribute shows the result in a readable format.
"""
print("The search has finished run - you may now continue the notebook.")

print(result.info)

"""
One thing the result contains we'll use now is the `FitImaging` object that corresponds to the set of model
parameters that gave the maximum log likelihood solution. 

We plot this object to inspect how good our fit was.
"""
fit_plotter = aplt.FitImagingPlotter(fit=result.max_log_likelihood_fit)
fit_plotter.subplot_fit()

"""
__Wrap Up__

This tutorial has laid the foundation with several fundamental concepts in model fitting and statistical inference:

1. **Parameter Space**: This refers to the range of possible values that each parameter in a model can take. It 
defines the dimensions over which the likelihood of different parameter values is evaluated.

2. **Likelihood Function**: This function receives as input a model with specific parameter values and returns a
log likelihood value that quantifies how well the model describes the data.

3. **Likelihood Surface**: This surface represents how the likelihood of the model varies across the parameter space. 
It helps in identifying the best-fit parameters that maximize the likelihood of the model given the data.

4. **Non-linear Search**: This is an optimization technique used to explore the parameter space and find the 
combination of parameter values that best describe the data. It iteratively adjusts the parameters to maximize the 
likelihood. Many different search algorithms exist, each with their own strengths and weaknesses, and this tutorial
used nested sampling search called Nautilus.

5. **Priors**: Priors are probabilities assigned to different values of parameters before considering the data. 
They encapsulate our prior knowledge or assumptions about the parameter values. Priors can constrain the parameter 
space, making the search more efficient and realistic.

6. **Model Fitting**: The process of adjusting model parameters to minimize the difference between model predictions 
and observed data, quantified by the likelihood function.

Understanding these concepts is crucial as they form the backbone of model fitting and parameter estimation in 
scientific research and data analysis. In the project tasks, model fitting will be used to perform your
research project.
"""


