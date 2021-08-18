from gravitational_wave_ploting.gravitational_wave import gravitationalWave
import matplotlib.pyplot as plt
from sys import argv
import numpy as np
import matplotlib as mpl

mpl.rcParams['toolbar'] = 'None'


def main() -> None:

	plt.style.use( "dark_background" )
	fig = plt.figure()

	ax = fig.add_subplot( projection='3d' )
	ax.set_zlim( -1, 1 )

	xs = np.linspace( -12, 12, 50 )
	ys = np.linspace( -12, 12, 50 )

	X, Y = np.meshgrid( xs, ys )

	plt.axis( "off" )

	gw = gravitationalWave(argv[1], ax, (X, Y), [77, 14] )

	gw.execute()


if __name__ == "__main__":
	main()