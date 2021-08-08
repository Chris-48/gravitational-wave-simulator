from mpl_toolkits.mplot3d.axes3d import Axes3D
from dataclasses import dataclass, field
from .plane_type_functions import map_wave_fucntion_types


@dataclass
class gravitationalWave():
    """
    Class responsible for ploting the gratitational wave.
    """

    function_type: str
    ax: Axes3D
    input_space: tuple
    view_point: list = field(default_factory=[0, 0])


    def __post_init__(self) -> None:

        self.function_type_map = map_wave_fucntion_types(self.ax, self.input_space, self.view_point)

        self.ax.view_init(*self.view_point)


    def execute(self) -> None:
        """
        Plot a gravitational wave of the specified `function_type`.
        """
        func, args = self.function_type_map[self.function_type]

        while True:
            func(*args)
