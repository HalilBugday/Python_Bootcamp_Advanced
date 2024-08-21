#%%
import numpy as np
from matplotlib import pyplot as plt

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []
avg=0 #average
mean=0 #mean
var=0 #variance
# Populate the given arrays.
### YOUR CODE HERE ###
for i in range(50000):
    u=np.random.rand()
    U.append(u)
    x=(np.sqrt(U[i]))
    Xa.append(x)
    avg=(avg+x)
    av_Xa.append(avg/(i+1))
    mean=avg/(i+1)
    var=(1/(i+1))*((x-mean)**2)
    vr_Xa.append(var)
#print(av_Xa)
# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,density=True)
hXa = plt.hist(Xa,100,alpha=0.5,density=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))
# Plot the average and variance values.
### YOUR CODE HERE ###
#average 
plt.figure()
av = plt.hist(av_Xa,density=True,bins=np.linspace(0,1,30))
#variance
plt.show()
plt.plot(vr_Xa)
#%%
# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []
FX=[]
avg1=0
mean1=0
var1=0
# Populate the given arrays.
### YOUR CODE HERE ###
def f(x):
    if 0<=x<=1:
        fx=(x**2)
    else:
        fx=0
    return fx
for i in range(-200,200):
    FX.append(f(i/100))
a=0
b=1
c=0.6
j=0
while j <50000:
    u=np.random.rand()
    v=np.random.rand()
    x=(b-a)*u+a
    y=c*v
    if y<=f(x):
        Xb.append(x)
        j=j+1
        avg1=avg1+x
        av_Xb.append(avg1/(j+1))
        mean1=avg1/(j+1)
        var1=(1/(j+1))*((x-mean1)**2)
        vr_Xb.append(var1)
# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,density=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))
# Plot the average and variance values.
### YOUR CODE HERE ###
#average
plt.figure()
av1 = plt.hist(av_Xb,density=True,bins=np.linspace(0,1,30))
#variance
plt.show()
plt.plot(vr_Xa)
