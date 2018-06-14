import numpy as np
from Parameter import Parameters as P

class ODESolver:
    def __init__(self, model):

        self.F = model.F
        self.x0 = model.x0

        self.tEnd = 1000000.
        self.dt = 1.

        self.reInit()

    def reInit(self):

        self.n = int(self.tEnd / self.dt)

        self.t = np.linspace(0., self.tEnd, self.n)
        self.x = np.zeros((self.n, len(self.x0)), dtype=float)

        self.t[0] = 0
        self.x[0] = self.x0

    def integrate(self, i):
        #raise RuntimeError('You need to implement the method integrate in every subclass for ODESolver!')
        raise NotImplementedError('You need to implement the method integrate in every subclass for ODESolver!')

class Euler(ODESolver):

    def __init__(self, model):
        super().__init__(model)

    def integrate(self, i):
        print("TankTem = " + str(P.hotTankTemp) + "   CollTemp = " + str(P.collectorTemp))
        self.x[i][1] = P.hotTankTemp
        self.x[i][0] = P.collectorTemp
        self.x[i][2] = P.coldTankTemp
        self.x[i+1] = self.x[i] + 1 * self.F(self.x[i], self.t[i])
        P.collectorTemp = self.x[i+1][0]
        P.hotTankTemp = self.x[i+1][1]
        P.coldTankTemp = self.x[i+1][2]

    def getCalcTime(self):
        self.x[0][1] = P.hotTankTemp
        self.x[0][0] = P.collectorTemp
        for i in range(0, self.n - 1):
            self.x[i + 1] = self.x[i] + 1 * self.F(self.x[i], self.t[i])
            if(self.x[i][1] >= 340):
                P.calcTimeForHeatUp = self.t[i]
                break


class RungeKutta(ODESolver):

    def __init__(self, model):
        super().__init__(model)

    def integrate(self):
        for i in range(0, self.n-1):
            k1 = self.F(self.x[i], self.t[i])
            k2 = self.F(self.x[i]+self.dt/2.0*k1, self.t[i]+0.5*self.dt)
            k3 = self.F(self.x[i]-self.dt*k1+2.0*self.dt*k2, self.t[i]+self.dt)
            self.x[i+1] = self.x[i] + self.dt*(k1 + 4.0*k2 + k3)/6.0
