import numpy as np
import matplotlib.pyplot as plt

def voltage(t, T) :
    if t%T <= T/2 :
        return 5
    else :
        return 0



R = 10 #Resistance
C = 0.001 #Capacitance
T = 1 #Time period
tau = R*C
h = 0.0005
x = [0.0]
y = [0.0]

def deriv(y, t) :
    return voltage(t,T)/tau - 1/tau * y

#for i in range(10000) :
 #   x.append(x[i]+h)
  #  y.append(y[i]*(1 - (h/tau)) + h*voltage(x[i], T)/R)

for i in range(10000) :
    x.append(x[i]+h)
    k1 = h*deriv(y[i], x[i])
    k2 = h*deriv(y[i] + h/2, x[i])
    k3 = h*(deriv(y[i] + h, x[i]))
    k4 = h*(deriv(y[i]+h, x[i]))
    y.append(y[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4))
        

plt.plot(x, y)
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.savefig('fig1.png')
plt.show()


