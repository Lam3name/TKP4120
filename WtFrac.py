import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import constants as con

def WtFracCO2(alpha):
    return ((con.Mw[0])*alpha)/((1+(0.7/0.3))*con.MwMEA)

def WtFracToAbsMol(tot, percent, molarMass):
    return((tot*percent)/molarMass*1000)     # mol/s

def fracMolToFracWt(tot, percent, molarmass):
    return(((tot*percent)*molarmass)/1000)      #kg/s
