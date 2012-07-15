from matplotlib import use as matplotlibuse, rc as matplotlibrc
matplotlibrc('figure.subplot', left = 0.05, right=0.95, bottom=0.05, top=0.95)
import matplotlib as mpl
mpl.rcParams['font.size'] = 10
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class Qt4MplCanvas(FigureCanvas):
    """
    Class to represent the FigureCanvas widget.
    """
    def __init__(self, parent = None):
        # Standard Matplotlib code to generate the plot
        self.fig = Figure()
        # initialize the canvas where the Figure renders into
        super(Qt4MplCanvas, self).__init__(self.fig)
        self.setParent(parent)
