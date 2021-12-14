import numpy as np

__all__= [
    "gravitational_wave_function_of_time",
    "improved_gravitational_wave_function_of_time"
]

AMPLITUDE = 1/4
LAMBDA = 1/2
LAMBDA1 = .91


def gravitational_wave_function_of_time( X: np.ndarray, Y: np.ndarray, T: float ):
    """
    The four dimensional function that represents a gravitational wave in the plane.

    `f(t, x, y) = θ cos(λπ√(x^2 + y^2) - (tπ)/2)`
    """

    return AMPLITUDE * np.cos(LAMBDA * np.pi * np.sqrt(X**2 + Y**2) - (np.pi*T)/2)


def improved_gravitational_wave_function_of_time( X: np.ndarray, Y: np.ndarray, T: float, OMEGA: int = 2):

    if not X:
        return AMPLITUDE * np.cos( (LAMBDA1*np.pi*np.sqrt(X**2 + Y**2)) - np.pi - T)

    return AMPLITUDE * np.cos( (LAMBDA1*np.pi*np.sqrt(X**2 + Y**2)) - OMEGA*np.arctan(Y/X) - T)

improved_gravitational_wave_function_of_time = np.vectorize(improved_gravitational_wave_function_of_time)

