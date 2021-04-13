import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import constants as con
import compression

def WtFracToAbsMols(tot, percent, molarMass):
    return((tot*percent)/molarMass*1000)     # mol/s

# Stream 1
molsStream1 = [None]*4 

molsStream1[0] = WtFracToAbsMols(con.m1, con.wc1, con.Mw[0]) # mol/s
molsStream1[1] = WtFracToAbsMols(con.m1, con.wh1, con.Mw[1]) # mol/s
molsStream1[2] = WtFracToAbsMols(con.m1, con.wn1, con.Mw[2]) # mol/s
molsStream1[3] = WtFracToAbsMols(con.m1, con.wo1, con.Mw[3]) # mol/s

print(molsStream1)