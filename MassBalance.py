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

print(molPercentToWtPercent(con.alpha3,con.Mw[1],con.MwMEA)*(100/(100+molPercentToWtPercent(con.alpha3,con.Mw[1],con.MwMEA))))

def massStream(educatedGuess):
    m1 = con.m1
    mc1 = m1 * con.wc1
    mh1 = m1 * con.wh1
    mn1 = m1 * con.wn1
    mo1 = m1 * con.wn1
    mn3 = 0
    mo3 = 0
    mh4 = 0
    mn4 = 0
    mo4 = 0
    #EducatedGuesses
    m3 = educatedGuess[0]
    m4 = educatedGuess[1]
    m9 = educatedGuess[2]

    k = 1/(con.waMEA+(1-con.waMEA)+(con.wcapture*con.waMEA))

    wmc3 = (con.wcapture*con.waMEA)*k
    wmh3 = (1-con.waMEA)*k
    wmMEA3 = con.waMEA*k

    #volum 1
    
    
    mMEA3 = m3 * wmMEA3 #con.waMEA*(100/(100+molPercentToWtPercent(con.alpha3,con.Mw[1],con.MwMEA)))
    mc3 = m3 * wmc3 #molPercentToWtPercent(con.alpha3,con.Mw[1],con.MwMEA)*(100/(100+molPercentToWtPercent(con.alpha3,con.Mw[1],con.MwMEA)))
    mc2 = mc1 - mc3 #(mc1 - mc1 * (1-con.wcapture) + molPercentToWtPercent(con.alpha3,con.Mw[0],con.Mw[1]) * mMEA3)
    mh3 = m3 * wmh3 #(1-con.waMEA)*(100/(100+molPercentToWtPercent(con.alpha3,con.Mw[1],con.MwMEA)))
    mh4 = mh3
    mc4 = mc1 + mc3 - mc2
    mMEA4 = mMEA3
    m2 = mh1 + mn1 + mc1 + mo1 - mc3

    #volum 2
    mc5 = mc4
    mh7 = mh3
    mh6 = mh7
    mh5 = mh4
    mMEA5 = mMEA4
    mMEA3 = mMEA5

    m5 = mc5 + mMEA5 + mh5

    #volum 3
    mc6 = mc3
    mc6 = mc5 - m9*con.wc9
    mc9 = mc5 - mc3 
    mc5 = mc9 + mc6
    mh5 = mh6

    #EQUATIONS
    equation0 = m5 - m9 - m2 + m1 - m3  #mMEA3 + mc3 + mh3 - m3            #m3
    equation1 = m1 + m3 - m2 - m4     #mc4 + mh4 + mn4 + mo4 - m4  #m4
    equation2 = mc9 - m9              #m9

    balance = [equation0, equation1, equation2]
    return balance

def massStream1(educatedGuess):
    m1 = con.m1
    wc1 = con.wc1
    wh1 = con.wh1
    wn1 = con.wn1
    wo1 = con.wo1
    wMEA1 = 0
    k = 1/(con.waMEA+(1-con.waMEA)+(con.wcapture*con.waMEA))
    wc3 = (con.wcapture*con.waMEA)*k
    wh3 = (1-con.waMEA)*k
    wMEA3 = con.waMEA*k
    wc2 = 1

    #EducatedGuesses
    m4 = educatedGuess[0]
    m9 = educatedGuess[1]

    #volum 1
    wc4 = (m1 * wc1 + m3 * wc3 - m2 * wc2)/m4
    wMEA4 = (m1 * wMEA1 + m3 * wMEA3 - m2 * wMEA2)/m4
    wh4 = (m1 * wh1 + m3 * wh3 - m2 * wh2)/m4
    wo4 = (m1 * wo1 + m3 * wo3 - m2 * wo2)/m4
    wn4 = (m1 * wn1 + m3 * wn3 - m2 * wn2)/m4

    wc9 = (m5 * wc5 - m6 * wc6)/m9
    wMEA9 = (m5 * wMEA5 - m6 * wMEA6)/m9

    wMEA4 = wMEA5
    wMEA6 = wMEA3
    m4 = m5
    m6 = m3
    m2 = ((1-con.wcapture)*m1*wc1)/wc2
    wo4 = -(wc4 + wn4 + wh4 + wMEA4 - 1)
    wh3 = -(wc3 + wn3 + wo3 + wMEA3 - 1)

    #volum 2
    #volum 3
    #EQUATIONS
    equation1 = m1 + m3 - m2 - m4
    equation1 = m1 - m2 - m9
    


    balance = [equation0, equation1]
    return balance

guess0 = 150
guess1 = 200
guess2 = 50

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