import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
import WtFrac
import constants as con
import compression as comp

def taskPatrialPressureCO2():
    alphalist = []
    pressurelist = []
    for i in range(0,50):
        alphalist.append(i*0.01)
        pressurelist.append(comp.partialPressureCO2(alphalist[i]))
    print(alphalist)
    print(pressurelist)
    plt.semilogy(alphalist, pressurelist)
    plt.grid()
    plt.xlabel("Alpha %")
    plt.ylabel("Pressure kPa")
    plt.show()
    return 0
taskPatrialPressureCO2()

def taskWtFracCO2():
    print(WtFrac.WtFracCO2(con.alpha3))
    return 0

