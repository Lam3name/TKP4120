import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
import constants as con


def enthalpyWater(T2):
    T1 = 298
    integrand = lambda T: (5.05536*T - (T**2)*5.6552*10**(-3) - (T**3)*1.9*10**(-5))
    integralCp = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    enthalpi = con.hf[1] + integralCp[0]
    
    return enthalpi

print(enthalpyWater(398))

def AbsEnthalpyWater(T2, m):
    return enthalpyWater(T2)*m

print(AbsEnthalpyWater(398,45))