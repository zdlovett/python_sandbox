import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np
import random

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=12, height=8)
        m.move(0,0)

        button = QPushButton('button', self)
        button.setToolTip('This s an example button')
        button.move(500,0)

        self.show()


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        N = 5
        X = [i for i in range(N)]
        Y = [random.random() for i in range(N)]
        labels = [f'point{i}' for i in range(N)]

        ax = self.figure.add_subplot(111)
        ax.set_facecolor((75/255,75/255,85/255))
        ax.scatter(X, Y, marker='o', color=(244/255,50/255,74/255))
        ax.set_title('PyQt Matplotlib Example')

        for label, x, y in zip(labels, X, Y):
            ax.annotate(
            label,
            xy=(x, y), xytext=(-10, 10),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc=(252/255,199/255,85/255), alpha=0.9),
            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0')
            )

        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
