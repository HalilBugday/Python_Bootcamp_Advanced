#%%
#-------------------------->>Please run all cells.
import numpy 
from matplotlib import pyplot as plt
import random
from random import randrange

#for P1:
print("P1: The probability that at least one dice 3")
#in theory 1-(5/6)*(5/6)*(5/6)*(5/6)*(5/6)
# sample space = 1 
# possibities of undesirable situations = (5/6)**5

theory1=1-(5/6)**5
print("P1 in theory: ",theory1)
print("Observational experiment: ")

count=0
n=0
for N in [10,50,100,500,1000,5000,10000,50000,100000]:
    results=[]
    for i in range(N):
        n=n+1
        list1=numpy.random.randint(1,7, size=(1,5))
        match_count=numpy.sum(list1==3)
        #print(list1)
        if match_count!=0:
            count=count+1
            #print(count)
        results.append(count/n)
    
    print ('Experimental probability for length {}: {:.4f} %' .format(N, results[-1]*100))
    plt.plot(range(N), results)
    plt.xscale('log')
    plt.ylim(0,1)
    plt.xlabel('N - Axis.')
    plt.ylabel('P - Axis.')
    plt.title("P1 Theoretically = 0.598122427983539")


# %%
import numpy 
from matplotlib import pyplot as plt
import random
from random import randrange

#for P2:
print("P2: The probability that at least one dice 3 given one of the dice is even")
#in theory 1-(5/6)*(5/6)*(5/6)*(5/6)*1
# sample space = 1 
# possibities of undesirable situations = ((5/6)**4)*1
# note: if a given dice is even number, the probability of not having that dice is 1
theory2=1-(5/6)**4
print("P2 in theory: ",theory2)
print("Observational experiment: ")
count=0
n=0
for N in [10,50,100,500,1000,5000,10000,50000,100000,500000,1000000]:
    results=[]
    for i in range(N):
        n=n+1
        list1=numpy.random.randint(1,7, size=(1,4))
        match_count=numpy.sum(list1==3)
        #print(list1)
        if match_count!=0:
            count=count+1
            #print(count)
        results.append(count/n)
    
    print ('Experimental probability for length {}: {:.4f} %' .format(N, results[-1]*100))
    plt.plot(range(N), results)
    plt.xscale('log')
    plt.ylim(0,1)
    plt.xlabel('N - Axis.')
    plt.ylabel('P - Axis.')
    plt.title("P2 Theoretically = 0.5177469135802468")
    plt.plot(range(N), results, label=str())


#%%
import numpy 
from matplotlib import pyplot as plt
import random
from random import randrange

#for P3:
print("P3: The probability that at least one dice 3 given only one of the dice is even")
#in theory 1-(2/3)*(2/3)*(2/3)*(2/3)*1
# sample space = 1 
# possibities of undesirable situations = ((2/3)**4)*1
# note: if a given only one of the dice is even, the probability of not having that dice is 1
# note2: the probability that the other dice given given are odd is 1/3

theory3=1-(2/3)**4
print("P3 in theory: ",theory3)
print("Observational experiment: ")
count=0
n=0
for N in [10,50,100,500,1000,5000,10000,50000,100000,500000,1000000]:
    results=[]

    for j in range(N): 
        n=n+1      
        list1 = [random.randrange(1,6,2) for k in range(4)]
        #print(list1)
        countt=0
        for k in list1:
            if k==3:
                countt=countt+1               
        if countt>=1:
            count=count+1
        #print(countt)
        #print("count=",count)
        results.append(count/n)
    
    print ('Experimental probability for length {}: {:.4f} %' .format(N, results[-1]*100))
    plt.plot(range(N), results)
    plt.xscale('log')
    plt.ylim(0,1)
    plt.xlabel('N - Axis.')
    plt.ylabel('P - Axis.')
    plt.title("P3 Theoretically = 0.8024691358024691")
    plt.plot(range(N), results, label=str())

