import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import constants as con

def WtFracCO2(alpha):
    return ((con.Mw[0])*alpha)/((1+(0.7/0.3))*con.MwMEA)

