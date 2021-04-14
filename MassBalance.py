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


def massStream(educatedGuess):
    m1 = con.m1
    mc1 = m1 * con.wc1
    mh1 = m1 * con.wh1
    mn1 = m1 * con.wn1
    mo1 = m1 * con.wn1
    mh3 = 0
    mn3 = 0
    mo3 = 0
    mh4 = 0
    mn4 = 0
    mo4 = 0
    #EducatedGuesses
    m3 = educatedGuess[0]
    m4 = educatedGuess[1]
    m9 = educatedGuess[2]

    mc2 = mc1 - mc1*con.wcapture
    mc3 = WtFrac.WtFracCO2(con.alpha3)
    mMEA3 = con.waMEA*m3

    #volum 1
    mc4 = mc1 + mc3 - mc2
    mMEA4 = mMEA3
    
    #volum 2
    mc5 = mc4
    mMEA5 = mMEA4
    mc6 = mc3
    mMEA3 = mMEA5

    #volum 3
    mMEA6 = mMEA5

    #EQUATIONS
    equation0 = mMEA3 + mc3 - m3            #m3
    equation1 = mc4 + mh4 + mn4 + mo4 - m4  #m4
    equation2 = mc5 - mc6 - m9              #m9

    balance = [equation0, equation1, equation2]
    return balance

guess0 = 1
guess1 = 1
guess2 = 1

guess =  [guess0, guess1, guess2]
ans = scipy.optimize.root(massStream, guess)

ans_m3, ans_m4, ans_m9 = ans['x']
print(f'm3 = {ans_m3}')
print(f'm4 = {ans_m4}')
print(f'm9 = {ans_m9}')
    




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