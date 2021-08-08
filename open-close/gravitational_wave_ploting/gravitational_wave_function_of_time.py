import numpy as np

FUNCTION_OUTPUT_SCALE = 1/4
LAMBDA_INVERSE_SCALE = 1/2


def gravitational_wave_function_of_time( X: np.ndarray, Y: np.ndarray, T: float ):
    """
    The four dimensional function that represents a gravitational wave in the plane.

    `f(t, x, y) = θ cos(λπ√(x^2 + y^2) - (tπ)/2)`
    """

    return FUNCTION_OUTPUT_SCALE * np.cos(LAMBDA_INVERSE_SCALE * np.pi * np.sqrt(X**2 + Y**2) - (np.pi*T)/2)