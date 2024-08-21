import numpy as np
import matplotlib.pyplot as plt
import math

plt.style.use('ggplot')
plt.figure(figsize=(20,10))

N=50000 
T=10

c1 = 1
c2 = 1
r = 1

t = np.empty(N)
V1 = np.empty(N)
V2 = np.empty(N)
Vi = np.empty(N)

dt=T/N


V1[0]=0
V2[0]=0
t[0]=0
Is=10**(-12)
Vi[0]=0
for k in range(0, N - 1):
    t[k + 1] = t[k] + dt

 # Vi[k+1]=0.8  #remove the comment for 0.8V
    Vi[k + 1] = 5 * np.sin(t[k])  

    V1[k + 1] = V1[k] + ((Vi[k] - V1[k]) / (r * c1)) * dt - ((Is * dt) / c1) * (np.exp(40 * (V1[k] - V2[k])) - 1)
    V2[k + 1] = V2[k] + ((Is * dt) / c2) * (np.exp(40 * (V1[k] - V2[k])) - 1)

plt.plot(t, V1, label='Capacitor 1 Voltage')
plt.plot(t, V2, label='Capacitor 2 Voltage')
plt.plot(t, Vi, label='Input Voltage')

plt.xlabel('Time (s)')
plt.title('Second Project')
plt.legend()
plt.show() 
