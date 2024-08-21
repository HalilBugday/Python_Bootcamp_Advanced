#%%
import numpy as np
from matplotlib import pyplot as plt
import random
#----------------->Please run all cells
exp_1 = []
for i in range(200000):
   a=np.random.uniform(0,1)
   b=np.random.uniform(0,1)
   c= a+b
   exp_1.append(c)

plt.hist(exp_1, bins=100, label='histogram',density=True)
mu = 1 #(a+b)/2
sigma = 0.408 #sqrt (b-a)/12---> 2/12
x=np.linspace(0,2,100)
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (x - mu)**2 / (2 * sigma**2) ) ,label='normal distribution')
plt.title("Experiment1")
plt.legend()
plt.show()


# %%
exp_2=[]
for i in range(200000):
   sum = 0
   for j in range(4):
      a=np.random.uniform(0,1)
      sum=sum+a
      
   exp_2.append(sum)
plt.hist(exp_2, bins=100,label='histogram',density=True)
mu = 2 #(a+b)/2
sigma = 0.577 #sqrt (b-a)/12 ---> 4/12
x=np.linspace(0,4,100)
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (x - mu)**2 / (2 * sigma**2) ) ,label='normal distribution')
plt.title("Experiment2")
plt.legend()
plt.show()


# %%
exp_3=[]
for i in range(200000):
   sum = 0
   for j in range(50):
      a=np.random.uniform(0,1)
      sum=sum+a   
   exp_3.append(sum)
plt.hist(exp_3, bins=100,label='histogram',density=True)
mu = 25 #(a+b)/2
sigma = 2.04  #sqrt (b-a)/12 ---> (50/12)
x=np.linspace(0,50,100)
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (x - mu)**2 / (2 * sigma**2) ) ,label='normal distribution')
plt.title("Experiment3")
plt.legend() 
plt.show()

# %%

exp_4=[]
for i in range(200000):
   sum = 0
   x1=0
   x2=0
   for j in range(50): 
      a = np.random.uniform(0,200)
      if (a<99):
         b = np.random.uniform(0,200)
         x1=x1+1
         sum=sum+b
      else:
         b = np.random.uniform(98,102)
         x2=x2+1
         sum=sum+b
   exp_4.append(sum)
plt.hist(exp_4, bins=100,label='histogram',density=True)

variance=((x1*200*200)/12) + ((x2*4*4)/12)
mu = 5000 #50*100
sigma = np.sqrt(variance)  #sqrt (50/12)
x=np.linspace(0,6000,100)
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (x - mu)**2 / (2 * sigma**2) ) ,label='normal distribution')
plt.title("Experiment4")
plt.legend() 
plt.show()

# %%

exp_5=[]
for i in range(200000):
   sum = 0
   for j in range(50):
      a=np.random.uniform(0,1)
      b=np.random.uniform(0,1)
      c=np.random.uniform(a,(b-a))
      sum=sum+c
   exp_5.append(sum)
plt.hist(exp_5, bins=100,label='histogram',density=True)
mu = np.mean(exp_5) 
sigma = np.std(exp_5) 
x=np.linspace(0,20,100)
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (x - mu)**2 / (2 * sigma**2) ) ,label='normal distribution')
plt.title("Experiment5")
plt.legend()
plt.show()


# %%