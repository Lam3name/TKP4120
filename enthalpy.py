

import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt


def entalpivann(T2):
    
    T1 = 298
    Cp = 5.05536*T - (T^2)*5.6552*10^(-3) - (T^3)*1.9*10^(-5)
    integral_cp = scipy.integrate.quad(Cp, T1, T2)
    
    entalpi = -13423.3 + integral_cp
    print(entalpi) 
    return

entalpivann(398)
