import scipy.optimize
import numpy as np
import WtFrac
import constants as con

def partialPressureCO2(alpha, T = 273, K2 = 3.93*(10**5)): #calculating for T = 273K by standard
    KH = ((con.Hc[0] + con.Hc[1]*alpha*(1/T))**((con.Hc[2]*(alpha**2) + con.Hc[3]*(1/T) + con.Hc[4]*alpha*(1/(T**2)))))
    print("KH = ", KH)
    return ((KH*(alpha**2))/(K2*(1-2*alpha)**2))