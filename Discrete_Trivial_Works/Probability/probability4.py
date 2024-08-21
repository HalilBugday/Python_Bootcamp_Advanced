#%%
import numpy as np
from matplotlib import pyplot as plt
def predict_theta_solving_by_MoM(X):
    Q= (np.mean(X))/2
    return Q
def predict_theta_solving_by_MLE(X):
    Q=min(X)
    return Q

X=[0.3,0.6,0.8,0.9]
print("MoM estimate for the sample is ",predict_theta_solving_by_MoM(X))
print("MLE estimate for the sample is ",predict_theta_solving_by_MLE(X))

def cal_avg_for_MoM(Avg_MoM_Values):
    avg= sum(Avg_MoM_Values)/(len(Avg_MoM_Values))
    return avg

def cal_standart_deviation_for_MoM(avg,Std_MoM_Values):
    i=0
    summation=0
    while i <len(Std_MoM_Values):
        summation= summation+((avg-Std_MoM_Values[i])*(avg-Std_MoM_Values[i]))
        i=i+1
    standart_deviation= np.sqrt(summation/(len(Std_MoM_Values)))
    return standart_deviation

def cal_avg_for_MLE(Mean_MLE_Values):
    avg=sum(Mean_MLE_Values)/len(Mean_MLE_Values)
    return avg

def cal_standart_deviation_for_MLE(avg,Std_MLE_Values):
    i=0
    summation=0
    while i <len(Std_MLE_Values):
        summation= summation+((avg-Std_MLE_Values[i])*(avg-Std_MLE_Values[i]))
        i=i+1
    standart_deviation= np.sqrt(summation/(len(Std_MLE_Values)))
    return standart_deviation


# Part b (Inverse Transform Method)
def inverse_transform_method():
    U = []
    val_of_x = []
    i=0
    while i<10000000:
        u = np.random.rand()
        U.append(u)
        x = ((5.76) / (1 - U[i])) ** (1 / 2)
        if x >= 2.4:
            val_of_x.append(x)
            i=i+1

    #plt.figure()
    #plt.hist(val_of_x, bins=np.linspace(0, 4.8, 20), alpha=0.9, density=True)
    #plt.show()
    return val_of_x


def cal_avg_and_standart_deviation_of_population(P, N):
    avg_and_stds=[]
    j=0
    while j<100000:
        val=[]
        i=0
        while i < N:
            number= np.random.randint(0, 10000000)
            a=P[number]
            val.append(a)
            i=i+1
        b=predict_theta_solving_by_MoM(val)
        Qp_MoM.append(b)
        c=predict_theta_solving_by_MLE(val)
        Qp_MLE.append(c)
        j=j+1
    avg_mom=cal_avg_for_MoM(Qp_MoM)
    avg_and_stds.append(avg_mom)
    standart_deviation_MoM= cal_standart_deviation_for_MoM(avg_mom,Qp_MoM)
    avg_and_stds.append(standart_deviation_MoM)
    avg_mle=cal_avg_for_MLE(Qp_MLE)
    avg_and_stds.append(avg_mle)
    standart_deviation_MLE=cal_standart_deviation_for_MLE(avg_mle,Qp_MLE)
    avg_and_stds.append(standart_deviation_MLE)
    return avg_and_stds

p=inverse_transform_method()

plt.hist(p, bins=np.linspace(0, 4.8, 100), alpha=0.9, density=True)
xa=np.linspace(2.4,4.8,100)
plt.plot(xa,11.52/(xa**3),label='PDF')
plt.legend()
plt.show()

N = [1,2,3,4,5,10,50,100,500,1000]

for k in range(0,10):
    Qp_MoM = []
    Qp_MLE = []
    my_array=[]
    for m in cal_avg_and_standart_deviation_of_population(p,N[k]) :
        my_array.append(m)

    print("For N= ",N[k])
    print("MoM estimate mean: ", my_array[0]," MoM estimate std: ", my_array[1])
    print("MLE estimate mean: ", my_array[2], " MLE estimate std: ",my_array[3])
    plt.figure()
    plt.hist(Qp_MoM,bins=np.linspace(0,4.8,100),alpha=0.5,density=True,label="MoM")
    plt.hist(Qp_MLE,bins=np.linspace(0,4.8,100),alpha=0.5,density=True,label="MLE")
plt.show()
