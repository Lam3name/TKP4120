import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import constants as con
import WtFrac
import compression

def WtFracToAbsMol(tot, percent, molarMass):
    return((tot*percent)/molarMass*1000)     # mol/s

def fracMolToFracWt(tot, percent, molarmass):
    return(((tot*percent)*molarmass)/1000)      #kg/s

def molPercentToWtPercent(percent, mw1, mw2):       #percent Returns weight percent from mole percent.
    return((mw2/mw1)*percent)

#Calculation testing
#wc3 = WtFrac.WtFracCO2(con.alpha3)
#print(wc3+(1-wc3)*0.7+(1-wc3)*0.3)


def massStream(educatedGuess):
    #EducatedGuesses
    m2 = educatedGuess[0]
    m3 = educatedGuess[1]
    m4 = educatedGuess[2]

    #Stream 1
    m1 = con.m1
    mc1 = m1 * con.wc1
    mh1 = m1 * con.wh1
    mn1 = m1 * con.wn1
    mo1 = m1 * con.wn1

    #Stream 2
    #m2 = m1 + m3 - m4
    mc2 = (1 - con.wcapture) * mc1
    mh2 = mh1
    mn2 = mn1
    mo2 = mo1
    #m2 = mc2 + mh2 + mn2 + mo2 

    #Stream 3
    #m3 = m4 - m9
    mc3 = WtFrac.WtFracCO2(con.alpha3) * m3
    mh3 = (1 - WtFrac.WtFracCO2(con.alpha3)) * 0.7 * m3
    mMEA3 = (1 - WtFrac.WtFracCO2(con.alpha3)) * 0.3 * m3
    #m3 = mc3 + mh3 + mMEA3
    
    #Stream 4
    #m4 = m1 + m3 - m2
    mc4 = mc1 * con.wcapture + mc3
    mh4 = mh3
    mMEA4 = mMEA3
    #m4 = mc4 + mh4 + mMEA4


    m5 = m4
    m6 = m3

    #Stream 9
    m9 = m5 - m6
    mc9 = mc4
    m9 = mc9

    equation0 = m1 + m3 - m4 - m2
    equation1 = m4 - m9 - m3
    equation2 = m1 + m3 - m2 - m4

    balance = [equation0, equation1, equation2]
    return balance

guess0 = 450
guess1 = 100
guess2 = 150

guess =  [guess0, guess1, guess2]
ans = scipy.optimize.root(massStream, guess)

ans_m2, ans_m3, ans_m4 = ans['x']
print(f'm2 = {ans_m2}')
print(f'm3 = {ans_m3}')
print(f'm4 = {ans_m4}')


    




# Stream 1
molsStream1 = [None]*5

molsStream1[0] = WtFracToAbsMol(con.m1, con.wc1, con.Mw[0]) # CO2 mol/s
molsStream1[1] = WtFracToAbsMol(con.m1, con.wh1, con.Mw[1]) # H2O mol/s
molsStream1[2] = WtFracToAbsMol(con.m1, con.wn1, con.Mw[2]) # N2 mol/s
molsStream1[3] = WtFracToAbsMol(con.m1, con.wo1, con.Mw[3]) # O2 mol/s
molsStream1[4] = 0                                           # MEA mol/s


# Stream 2
molsStream2 = [None]*5

molsStream1[0] = molsStream1[0] * con.alpha3 # CO2 mol/s
molsStream1[1] = 0 # H2O mol/s
molsStream1[2] = 0 # N2 mol/s
molsStream1[3] = 0 # O2 mol/s
molsStream1[4] = 0                                           # MEA mol/s