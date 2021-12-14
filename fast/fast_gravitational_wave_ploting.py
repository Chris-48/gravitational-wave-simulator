import matplotlib.pyplot as plt
import matplotlib as mpl
from sys import argv
import numpy as np

mpl.rcParams['toolbar'] = 'None'

ELEVATION = 77
AZIMUTH = 0

AMPLITUDE = 1/4
LAMBDA = .91
OMEGA = int( argv[1] )

del argv
del mpl


def gravitational_wave_function_of_time(x, y, t):
    """
    The four dimensional function that represents a gravitational wave in the plane.
    """

    if not x:
        return AMPLITUDE * np.cos( (LAMBDA*np.pi*np.sqrt(x**2 + y**2)) - np.pi - t)

    return AMPLITUDE * np.cos( (LAMBDA*np.pi*np.sqrt(x**2 + y**2)) - OMEGA*np.arctan(y/x) - t)

gravitational_wave_function_of_time = np.vectorize(gravitational_wave_function_of_time)


plt.style.use( "dark_background" )
fig = plt.figure()

ax = fig.add_subplot( projection='3d' )
ax.set_zlim(-1, 1)

xs = np.linspace( -6, 6, 35 )
ys = np.linspace( -6, 6, 35 )

X, Y = np.meshgrid(xs, ys)

plt.axis("off")
ax.view_init(elev=ELEVATION, azim=AZIMUTH)

while True:

	for T in np.linspace(0, 360, 1000):

		Z = gravitational_wave_function_of_time(X, Y, T)
		wframe = ax.plot_surface(X, Y, Z,  cmap=plt.cm.viridis)

		plt.pause(.084)
		ax.collections.remove(wframe)

