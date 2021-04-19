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
    m5 = educatedGuess[3]
    m6 = educatedGuess[4]
    m9 = educatedGuess[5]
    wc2 = educatedGuess[6]
    wh2 = educatedGuess[7]
    wn2 = educatedGuess[8]
    wo2 = educatedGuess[9]
    wMEA3 = educatedGuess[10]
    wMEA4 = educatedGuess[11]
    wMEA5 = educatedGuess[12]
    wMEA6 = educatedGuess[13]

    wcapture = con.wcapture

    m1 = con.m1
    wc1 = con.wc1
    wh1 = con.wh1
    wn1 = con.wn1
    wo1 = con.wo1
    
    wc3 = WtFrac.WtFracCO2(con.alpha3)
    wc4 = WtFrac.WtFracCO2(con.alpha4)
    wc5 = wc4
    wc6 = wc3
    wc8 = molPercentToWtPercent(con.xc8,con.Mw[0],con.Mw[1])
    wc9 = con.wc9

    wh8 = molPercentToWtPercent((1-con.xc8),con.Mw[1],con.Mw[0])
    m8 = (m1 * wc1) * wcapture + ((m1 * wc1) * wcapture)*wh8

    wMEA1 = 0
    wMEA2 = 0
    wh3 = 0
    wh4 = 0
    wo3 = 0
    wo4 = 0
    wn3 = 0
    wn4 = 0
    wMEA9 = 0


    equation1 = m1 * wc1 + m3 * wc3 - m4 * wc4 - m2 * wc2
    equation2 = m1 * wMEA1 + m3 * wMEA3 - m4 * wMEA4 - m2 * wMEA2
    equation3 = m1 * wh1 + m3 * wh3 - m4 * wh4 - m2 * wh2
    equation4 = m1 * wo1 + m3 * wo3 - m4 * wo4 - m2 * wo2
    equation5 = m1 * wn1 + m3 * wn3 - m4 * wn4 - m2 * wn2
    equation6 = m5 * wc5 - m9 * wc9 - m6 * wc6 
    equation7 = m5 * wMEA5 - m9 * wMEA9 - m6 * wMEA6
    equation8 = m5 - m4
    equation9 = m6 - m3
    equation10 = wMEA4 - wMEA5
    equation11 = wMEA3 - wMEA6
    equation12 = wc4 + wh4 + wo4 + wn4 + wMEA4 - 1
    equation13 = wc3 + wh3 + wo3 + wn3 + wMEA3 - 1
    equation14 = ((1 - wcapture) * (m1 * wc1)) - (m2 * wc2) 
    
    balance = [equation1, equation2, equation3, equation4, equation5, equation6, equation7, equation8, equation9, equation10, equation11, equation12, equation13, equation14]
    return balance

guess1 = 450
guess2 = 900
guess3 = 950
guess4 = 950
guess5 = 900
guess6 = 36
guess7 = 0.02
guess8 = 0.03
guess9 = 0.8
guess10 = 0.15
guess11 = 0.9
guess12 = 0.9
guess13 = 0.9
guess14 = 0.9



guess =  [guess1, guess2, guess3, guess4, guess5, guess6, guess7, guess8, guess9, guess10, guess11, guess12, guess13, guess14]
ans = scipy.optimize.root(massStream, guess)

ans_m2, ans_m3, ans_m4, ans_m5, ans_m6, ans_m9, ans_wc2, ans_wh2, ans_wn2, ans_wo2, ans_wMEA3, ans_wMEA4, ans_wMEA5, ans_wMEA6 = ans['x']
print(f'm2 = {ans_m2}')
print(f'm3 = {ans_m3}')
print(f'm4 = {ans_m4}')
print(f'm5 = {ans_m5}')
print(f'm6 = {ans_m6}')
print(f'm9 = {ans_m9}')
print(f'wc2 = {ans_wc2}')
print(f'wh2 = {ans_wh2}')
print(f'wn2 = {ans_wn2}')
print(f'wo2 = {ans_wo2}')
print(f'wMEA3 = {ans_wMEA3}')
print(f'wMEA4 = {ans_wMEA4}')
print(f'wMEA5 = {ans_wMEA5}')
print(f'wMEA6 = {ans_wMEA6}')