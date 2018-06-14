import matplotlib.pyplot as plt
import matplotlib.dates as da
import numpy as np

import Solar
import ODESolver
import XMLSaver as XS


def showTempStatistics():
    data = XS.getStatisticValuesTemp()
    x = data[0]
    yhot = data[1]
    ycold = data[2]
    ycollector = data[3]

    plt.plot_date(x, yhot, marker='', linestyle='-', color='r', label='Hot Tank', linewidth=2)
    plt.plot_date(x, ycold, marker='', linestyle='-', color='b', label='Cold Tank', linewidth=2)
    plt.plot_date(x, ycollector, marker='', linestyle='-', color='g', label='Collector', linewidth=2)

    formatter = da.DateFormatter('%H:%M:%S')
    plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
    plt.ylim(270, 360)


    plt.xlabel('Time')
    plt.ylabel('Temperature [K]')
    plt.title('Temperature of tanks during the day')
    plt.legend()
    plt.grid()
    plt.show()

def showLevelStatistics():
    data = XS.getStatisticsValuesLevel()
    x = data[0]
    yh = data[1]
    yc = data[2]
    plt.plot_date(x, yh, marker='', linestyle='-', color='r', label='Hot Tank', linewidth=2)
    plt.plot_date(x, yc, marker='', linestyle='-', color='b', label='Cold Tank', linewidth=2)

    formatter = da.DateFormatter('%H:%M:%S')
    plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
    plt.ylim(0, 310)

    plt.xlabel('Time')
    plt.ylabel('Fluid-Level [kg]')
    plt.title('Fluid-Level of tanks during the day')
    plt.legend()
    plt.grid()
    plt.show()

def showCalculationStatistics():
    solarSystem = Solar.SolarSystem()
    odeSolver = ODESolver.RungeKutta(solarSystem)

    odeSolver.tEnd = 1000
    odeSolver.dt = 10
    odeSolver.reInit()
    odeSolver.integrate()

    plt.plot(odeSolver.t, odeSolver.x[:, 0])
    plt.plot(odeSolver.t, odeSolver.x[:, 1])
    plt.plot(odeSolver.t, solarSystem.Ta * np.ones(odeSolver.n))
    plt.grid()
    plt.show()


