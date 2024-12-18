"""
Simulator: Disk 0
=================
"""
# %matplotlib inline
# from pyprojroot import here
# workspace_path = str(here())
# %cd $workspace_path
# print(f"Working Directory has been set to `{workspace_path}`")

from os import path
import autogalaxy as ag
import autogalaxy.plot as aplt

"""
__Dataset Paths__
"""
dataset_type = "task_2_colours"

dataset_wavelength_list = ["F115W", "F150W", "F277W", "F444W"]

wavelength_effective_radius_dict = {
    "F115W": 1.0,
    "F150W": 1.5,
    "F277W": 2.0,
    "F444W": 2.5
}

wavelength_sersic_index_dict = {
    "F115W": 1.0,
    "F150W": 1.2,
    "F277W": 1.4,
    "F444W": 1.6
}

for dataset_wavelength in dataset_wavelength_list:

    dataset_name = dataset_wavelength
    dataset_path = path.join("dataset", dataset_type, dataset_name)

    """
    __Grid__
    """
    grid = ag.Grid2D.uniform(
        shape_native=(100, 100),
        pixel_scales=0.1,
        over_sample_size=8
    )

    psf = ag.Kernel2D.from_gaussian(
        shape_native=(11, 11), sigma=0.1, pixel_scales=grid.pixel_scales
    )

    simulator = ag.SimulatorImaging(
        exposure_time=300.0,
        psf=psf,
        background_sky_level=0.1,
        add_poisson_noise_to_data=True,
    )

    """
    __Galaxies__
    """
    galaxy = ag.Galaxy(
        redshift=0.5,
        bulge=ag.lp.Sersic(
            centre=(0.0, 0.0),
            ell_comps=ag.convert.ell_comps_from(axis_ratio=0.8, angle=45.0),
            intensity=1.0,
            effective_radius=wavelength_effective_radius_dict[dataset_wavelength],
            sersic_index=wavelength_sersic_index_dict[dataset_wavelength]
        ),
    )

    galaxies = ag.Galaxies(galaxies=[galaxy])
    galaxies_plotter = aplt.GalaxiesPlotter(galaxies=galaxies, grid=grid)
    galaxies_plotter.figures_2d(image=True)

    dataset = simulator.via_galaxies_from(galaxies=galaxies, grid=grid)

    dataset_plotter = aplt.ImagingPlotter(dataset=dataset)
    dataset_plotter.subplot_dataset()

    """
    __Output__
    
    Output the simulated dataset to the dataset path as .fits files.
    """
    dataset.output_to_fits(
        data_path=path.join(dataset_path, "data.fits"),
        psf_path=path.join(dataset_path, "psf.fits"),
        noise_map_path=path.join(dataset_path, "noise_map.fits"),
        overwrite=True,
    )

    """
    __Visualize__
    
    """
    mat_plot = aplt.MatPlot2D(output=aplt.Output(path=dataset_path, format="png"))

    dataset_plotter = aplt.ImagingPlotter(dataset=dataset, mat_plot_2d=mat_plot)
    dataset_plotter.subplot_dataset()
    dataset_plotter.figures_2d(data=True)

    """
    The dataset can be viewed in the folder `dataset/task_2_colours`.
    """
