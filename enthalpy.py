import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
import constants as con


def enthalpyWater(T2):
    T1 = 313
    integrand = lambda T: (5.05536*T - (T**2)*5.6552*10**(-3) - (T**3)*1.9*10**(-5))
    integralCp = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    enthalpi = con.hf[1] + integralCp[0]
    
    return enthalpi

print(enthalpyWater(379))

def AbsEnthalpyWater(T2, m):
    return enthalpyWater(T2)*m

print(AbsEnthalpyWater(379,45))



def enthalpy_MEA_H20(T2):
    T1 = 313
    integrand = lambda T: (-4.9324*T - (T**2)*0.01469 - (T**(-0.5859))*169.6243)
    
    integralCp = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    
    enthalpi_2 = -26722.3 + integralCp[0]
    
    return enthalpi_2
print(enthalpy_MEA_H20(379)) ##usikker på om det er denne teorien den endres til, se strøm 4


def enthalpy_MEA_H20_CO2(T2):
    T1 = 298
    integrand = lambda T: (0.585*T - (T**2)*0.0009)
    
    integralCp = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    
    enthalpi_3 = -35655.3 + integralCp[0]
    
    return enthalpi_3


print(enthalpy_MEA_H20_CO2(393))

