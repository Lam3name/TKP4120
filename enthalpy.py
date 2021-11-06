import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
import constants as con
import MassBalance as mb


coeff_CO2 = [con.Ac, con.Bc]
coeff_MEA = [con.Aa, con.Ba, con.Ca]
coeff_water = [con.Aw, con.Bw, con.Cw]
coeff_CHM = [con.As, con.Bs, con.Cs]



    
    

def enthalpyWater(T1,T2,m):
    a = coeff_water[0]
    b = coeff_water[1]
    c = coeff_water[2]
    integrand = lambda T: a + b*T + c*T**2
    integralCp = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    enthalpy = (con.hf[1] + integralCp[0])*m
    return enthalpy


def enthalpy_MEA(T1, T2, m):
    a = coeff_MEA[0]
    b = coeff_MEA[1]
    c = coeff_MEA[2]
    integrand = lambda T: a + b*T + c*T**2
    integralCp = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    ##enthalpi = (con.hfsol + integralCp[0])*m
    return integralCp
    
   
def Enthalpy_CO2(T1,T2, w_co2):
    a = coeff_CO2[0]
    b = coeff_CO2[1]
   
    integrand = lambda T: a + b*T 
    integralCp = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    print("Cp CO2 =", integralCp[0])
    enthalpy = (con.hf[0] + integralCp[0])*w_co2
    return enthalpy/1000
    


def enthalpy_MEAsol(wMEA,T1,T2):
    a = coeff_CHM[0]
    b = coeff_CHM[1]
    c = coeff_CHM[2]
    d = coeff_water[0]
    e = coeff_water[1]
    f = coeff_water[2]
    g = coeff_MEA[0]
    h = coeff_MEA[1]
    i = coeff_MEA[2]
    
    integrand = lambda T: (1-wMEA)*(d + e*T + f*T**2) + wMEA*(g + h*T + i*T**2) + wMEA*(1-wMEA)*(a + b*T + wMEA*c*(T-273.15)**(-1.5859))
    Cp_sol = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    print("Cp MEA-sol = ",Cp_sol[0])
    enthalpy = (con.hfsol + Cp_sol[0])*wMEA
    return enthalpy/1000
    
##def enthalpy_MEAsol(wMEA, T1,T2):
  ##  integrand = lambda T: Heatcapasity_MEAsol(wMEA)
    ##integralCp = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    ##enthalpy = (con.hfsol + integralCp[0])*wMEA
    ##return enthalpy/1000
    
    
    

##def enthalpy_MEA_H20(T2):
  ##  integrand = lambda T: (-4.9324*T - (T**2)*0.01469 - (T**(-0.5859))*169.6243)    
    ##integralCp = scipy.integrate.quad(integrand, T1, T2) #returns analytic result [0] and estimated error[1]
    ##enthalpi = -26722.3 + integralCp[0]
    ##return enthalpi



def enthalpy_MEA_H20_CO2(mass,w_MEAsol, w_co2, T1,T2,):
    
    enthalpy_MEA = enthalpy_MEAsol(w_MEAsol, T1,T2)
    enthalpy_co2 = Enthalpy_CO2(T1,T2, w_co2)
    #print(enthalpy_co2)
    enthalpy = (enthalpy_MEA + enthalpy_co2 + con.habs_m - con.habs_m)*mass
    return enthalpy






def stream8(mass,w_co2,w_h2o, T1,T2):
    ##entalpi_co2 = (-8933 + 0.868*(T2-T1))*mass*w_co2
    ##entalpi_h2o = (-13423.3 +  1.866*(T2-T1))*mass*w_h2o
    entalpi = (con.hf[0]*w_co2 + con.hf[1]*w_h2o + (con.cpg[0]*w_co2 + con.cpg[1]*w_h2o))*mass
    return entalpi/1000

def stream9(mass, w_co2):
    entalpi = con.hf[0]*mass*w_co2
    return entalpi/1000

def stream12(mass,w_h2o, w_co2):
    enthalpy_water = (enthalpyWater(0,0,mass))*w_h2o
    enthalpy_co2 = con.hf[0]*w_co2*mass
    enthalpy = enthalpy_water + enthalpy_co2
    return enthalpy/1000

def Co2_MEA(mass,w_h2o, w_co2,T1,T2):
    enthalpy_water = (enthalpyWater(T1,T2,mass))*w_h2o
    enthalpy_co2 = con.hf[0]*w_co2*mass
    enthalpy = enthalpy_water + enthalpy_co2
    return enthalpy/1000








def stream7enthalpy():
    H7 = stream6 - stream5 + stream4
    return H7


    
stream3 = enthalpy_MEA_H20_CO2(mb.ans_m3,mb.ans_wMEA3, mb.wc3, 379, 313)
stream4 = enthalpy_MEA_H20_CO2(mb.ans_m4,mb.ans_wMEA4, mb.wc4,313,328)
stream5 = enthalpy_MEA_H20_CO2(mb.ans_m5, mb.ans_wMEA5, mb.wc5,328,379)
stream6 = enthalpy_MEA_H20_CO2(mb.ans_m6, mb.ans_wMEA6, mb.wc6, 379, 393)
stream7 = stream7enthalpy()
stream8 =  stream8(mb.m8,1-mb.wc8,mb.wc8,379,298)
stream9 =  stream9(mb.ans_m9,1)
stream12 =  stream12(mb.m8, 1-mb.wc8,mb.wc8)
    






def heattransferareal(t_c_inn, t_c_ut, t_h_inn, t_h_ut):
    q= (stream5-stream4)*10**6
    f = 1
    U = 1150  # W/(m^2*K) 
    T_lm = ((t_h_inn-t_c_ut)- (t_h_ut-t_c_inn))/np.log((t_h_inn-t_c_ut)/(t_h_ut-t_c_inn))
    A = q/(f*U*T_lm)
    return A

Areal = heattransferareal(328,379,393, 366.8)




def CoolerV2(T2,T1): ##T2 = T11 og T1=T10
    q_v2 = stream7 - stream3
    a = coeff_water[0]
    b = coeff_water[1]
    c = coeff_water[2]
    integrand = lambda T: a + b*T + c*T**2
    integralCp = scipy.integrate.quad(integrand, T1, T2)
    m10= q_v2*10**3/integralCp[0]
    return m10

m10 = CoolerV2(298,278)
q_v_3 = stream12 - stream8
q_v_1 = stream5 - stream4
q_v_2 = stream7 - stream3
q_v_4 = stream6 + stream9 - stream5 - q_v_3
stream1 =  (500*0.09*(-8933) + 500*0.03*(-13423.3))/1000  ##m1*w_co2*h_co2_1 + m1*w_h20*h_h20
stream2 =(464*0.0194*(-8933) + 500*0.032*(-13423.3))/1000

print("stream 1 =", stream1)
print("stream 2 = ", stream2 )
print("stream 3 = ", stream3)
print("stream 4 =",stream4)
print("stream 5 = ",stream5)
print("stream 6 = ",stream6)
print("stream 7 = ", stream7)
print("stream 8 = ", stream8)
print("stream 9 =",stream9)
print("stream 12 =",stream12)
print("m10 =", m10)
print("m11 = ", m10)
print("q_v_1 =",q_v_1 )
print("q_v_2 =", q_v_2 )
print("q_v_3 = ", q_v_3 )
print("q_v_4 =", q_v_4  )
print("T7 = 366.8") ##93.8 Celcius
print("Heattransfer Areal = ",Areal)


