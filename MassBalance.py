import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import constants as con
import WtFrac
import compression

def WtFracToAbsMols(tot, percent, molarMass):
    return((tot*percent)/molarMass*1000)     # mol/s


def massStream(educatedGuess):
    m1 = con.m1
    mc1 = m1 * con.wc1
    mh1 = m1 * con.wh1
    mn1 = m1 * con.wn1
    mo1 = m1 * con.wn1

    #EducatedGuesses
    m4  = educatedGuess[0]

    mc2 = mc1 - mc1*con.wcapture
    mc3 = WtFrac.WtFracCO2(con.alpha3)

    #volum 1
    mc4 = mc1 + mc3 - mc2
    mh4 = mh1 + mh3 - mh2
    mn4 = mn1 + mn3 - mn2
    mo4 = mo1 + mo3 - mo2
    mMEA4 = mMEA3
    m4 = mc4 + mh4 + mn4 + mo4
    #volum 2
    mc5 = mc4
    mMEA5 = mMEA4
    mc3 = mc6
    mMEA3 = mMEA6
    #volum 3
    mc9 = mc5 - mc6
    mMEA6 = mMEA5

    




# Stream 1
molsStream1 = [None]*5

molsStream1[0] = WtFracToAbsMols(con.m1, con.wc1, con.Mw[0]) # CO2 mol/s
molsStream1[1] = WtFracToAbsMols(con.m1, con.wh1, con.Mw[1]) # H2O mol/s
molsStream1[2] = WtFracToAbsMols(con.m1, con.wn1, con.Mw[2]) # N2 mol/s
molsStream1[3] = WtFracToAbsMols(con.m1, con.wo1, con.Mw[3]) # O2 mol/s
molsStream1[4] = 0                                           # MEA mol/s

print(molsStream1)


# Stream 2
molsStream2 = [None]*5

molsStream1[0] = molsStream1[0] * con.alpha3 # CO2 mol/s
molsStream1[1] = 0 # H2O mol/s
molsStream1[2] = 0 # N2 mol/s
molsStream1[3] = 0 # O2 mol/s
molsStream1[4] = 0                                           # MEA mol/s