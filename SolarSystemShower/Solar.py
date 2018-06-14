from Parameter import Parameters as P
from ODESolver import *


class SolarSystem:

    def __init__(self):

        self.G = P.currentSolarIrradiance
        self.mc = 20.
        self.Ac = 20.
        self.kAc = 20.
        self.eta0 = 0.6

        self.mt = P.fluidLevelHot
        self.mtf = P.fluidLevelCold

        self.c = 4200.
        self.Ta = P.collectorTemp

        self.x0 = np.array([P.collectorTemp, P.hotTankTemp, P.coldTankTemp])



    def F(self,x,t):

        Tc = x[0]
        Tt = x[1]
        Tf = x[2]
        dTc_dt = (self.G*self.Ac*self.eta0 + P.collectorFlowRate * self.c*(Tt - Tc) - self.kAc*(Tc - self.Ta))/(self.mc*self.c)
        dTt_dt = P.collectorFlowRate/self.mt*(Tc - Tt)- (self.kAc*(Tt - self.Ta))/(self.mt*self.c)
        dTf_dt = -self.kAc*(Tf - self.Ta)/(self.mtf*self.c)

        return np.array([dTc_dt, dTt_dt, dTf_dt])
