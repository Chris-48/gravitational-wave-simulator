from .gravitational_wave_function_of_time import improved_gravitational_wave_function_of_time as gwf
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
from types import FunctionType
import numpy as np

STOP_LINSPACE = 360
NUM_LINSPACE = 1000
FRAME_DISPLAY_INTERVAL = .084


def static_plane( ax: Axes3D, X: np.ndarray, Y: np.ndarray ) -> None:
    """
    View of the R^3 plane without camera motion.
    """
    for T in np.linspace(0, STOP_LINSPACE, NUM_LINSPACE):

        Z = gwf(X, Y, T)
        wframe = ax.plot_surface(X, Y, Z,  cmap=plt.cm.viridis)

        plt.pause(FRAME_DISPLAY_INTERVAL)
        ax.collections.remove(wframe)


def rotation_plane() -> FunctionType:
    """
    View of the R^3 with camera motion.
    """
    azimuth = 0

    def _rotation_plane( ax: Axes3D, X: np.ndarray, Y: np.ndarray, elevation: float, start_azimuth: float ) -> None:

        nonlocal azimuth

        azimuth = start_azimuth if not azimuth else azimuth

        for T in np.linspace(0, STOP_LINSPACE, NUM_LINSPACE):

            azimuth += .2
            ax.view_init(elev=elevation, azim=azimuth )

            Z = gwf(X, Y, T)
            wframe = ax.plot_surface(X, Y, Z,  cmap=plt.cm.viridis)

            plt.pause(FRAME_DISPLAY_INTERVAL)
            ax.collections.remove(wframe)

    return _rotation_plane


def map_wave_fucntion_types( ax: Axes3D, input_space: tuple, view_point: list ) -> dict:
    """
    Map all the wave functions and their respective inputs to char keys.
    """
    return {
            "r" : (rotation_plane(), (ax, *input_space, *view_point)),
            "s" : (static_plane, (ax, *input_space))
    }