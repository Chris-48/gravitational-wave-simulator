import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['toolbar'] = 'None'

elevation = 77
azimuth = 0


def gravitational_wave_function_of_time(X, Y, T):
    """
    The four dimensional function that represents a gravitational wave in the plane.

    `f(t, x, y) = cos(π√(x^2 + y^2) - (tπ)/2)`
    """

    return 1/4 * np.cos(1/2 * np.pi * np.sqrt(X**2 + Y**2) - (np.pi*T)/2)


plt.style.use( "dark_background" )
fig = plt.figure()

ax = fig.add_subplot( projection='3d' )
ax.set_zlim(-1, 1)

xs = np.linspace( -12, 12, 50 )
ys = np.linspace( -12, 12, 50 )

X, Y = np.meshgrid(xs, ys)

plt.axis("off")

while True:

	for T in np.linspace(0, 24, 100):

		azimuth += .2
		ax.view_init(elev=elevation, azim=azimuth)

		Z = gravitational_wave_function_of_time(X, Y, T)
		wframe = ax.plot_wireframe(X, Y, Z,  rstride=2, cstride=2)

		plt.pause(.084)
		ax.collections.remove(wframe)
