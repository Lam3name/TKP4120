import scipy.optimize
import numpy as np
import WtFrac
import constants as con
import MassBalance

Ta = con.T[8]+273.15
pa = con.p[8]
pb = 4
Tc = 303+273.15
pc = 4
pd = 8
Te = 303+273.15
pe = 8
pf = 20
Tg = 303+273.15
pg = 20

def partialPressureCO2(alpha, T = 273, K2 = 3.93*(10**5)): #calculating for T = 273K by standard
    KH = ((con.Hc[0] + con.Hc[1]*alpha*(1/T))**((con.Hc[2]*(alpha**2) + con.Hc[3]*(1/T) + con.Hc[4]*alpha*(1/(T**2)))))
    print("KH = ", KH)
    return ((KH*(alpha**2))/(K2*(1-2*alpha)**2))

def tempAfterComp(T1, p1, p2, Cp):
    return ((p2/p1)**((con.gasConst*0.001)/Cp))*T1

def realCompWorkKnownTemp(T1, T2, Cp, m):
    return (m*Cp*(T1-T2))/con.eta

def realCompWorkUnknownTemp(T1, p1, p2, Cp):
    return ((Cp*T1)/con.eta)*((p1/p2)**(con.gasConst*0.001/Cp)-1)+T1

def heatExchanger(T1, T2, m, Cp):
    return m*Cp*(T2-T1)

def threeStageComp(Tinn, Tout, pinn, pout, m, Cp):
    Tb = tempAfterComp(Tinn, pinn, pb, Cp)
    Td = tempAfterComp(Tc, pc, pd, Cp)
    Tf = tempAfterComp(Te, pe, pf, Cp)
    temps = [Tb, Td, Tf]
    return temps

temps = threeStageComp(Ta, Tg, pa, pg, MassBalance.ans_m9, con.cpg[0])
print("Tb =",temps[0])
print("Td =",temps[1])
print("Tf =",temps[2])