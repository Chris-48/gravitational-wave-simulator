from types import FunctionType
import matplotlib.pyplot as plt
import numpy as np


def gravitational_wave_function_of_time(X, Y, T):
    """
    The four dimensional function that represents a gravitational wave in the plane.

    `f(t, x, y) = cos(π√(x^2 + y^2) - (tπ)/2)`
    """

    return 1/4 * np.cos(1/2 * np.pi * np.sqrt(X**2 + Y**2) - (np.pi*T)/2)


def static_plane(ax, X, Y):

    """
    View of the R^3 plane without camera motion.
    """
    for T in np.linspace(0, 20, 100):

        Z = gravitational_wave_function_of_time(X, Y, T)
        wframe = ax.plot_wireframe(X, Y, Z,  rstride=2, cstride=2)

        plt.pause(.07)
        ax.collections.remove(wframe)


def rotation_plane() -> FunctionType:
    """
    View of the R^3 with camera motion.
    """
    azimuth = 0

    def _rotation_plane(ax, X, Y, elevation, start_azimuth) -> None:

        nonlocal azimuth

        azimuth = start_azimuth if azimuth == 0 else azimuth

        for T in np.linspace(0, 24, 100):

            azimuth += .2
            ax.view_init(elev=elevation, azim=azimuth)

            Z = gravitational_wave_function_of_time(X, Y, T)
            wframe = ax.plot_wireframe(X, Y, Z,  rstride=2, cstride=2)

            plt.pause(.084)
            ax.collections.remove(wframe)

    return _rotation_plane


def map_wave_fucntion_types(ax, input_space, view_point):
    """
    Map all the wave functions and their respective inputs to char keys.
    """
    return {
            "r" : (rotation_plane(), (ax, *input_space, *view_point)),
            "s" : (static_plane, (ax, *input_space))
    }