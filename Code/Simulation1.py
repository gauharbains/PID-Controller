"""
@author: Gauhar Bains
         Aalap Rana
         
Affiliation :   
University of Maryland, College Park
Maryland,USA      
"""


from math import sin
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np


def model(x,t,u,c,a):    
    dy=x[1]
    xdot=[[],[]]
    xdot[0]=dy
    xdot[1]=a*sin(x[0])+0.5*x[1] +u
    return xdot
    
c=1    
dt=0.01  # Timestep
setpoint=1 # Desired Variable
x2=[2,2]
int1=[]
x1=[3]
error1=[setpoint-x1[0]] 
int1=[error1[0]*dt]
Kp,Ki,Kd=[10,1,2]
L1=3
L2=1
error=np.zeros((10,2000))

#alist=random.sample(range(-1*L1,L1),10)
a_list=np.random.uniform(low=-1*L1,high=L1,size=(10,))
b_list=np.random.uniform(low=-1*L2,high=L2,size=(10,))
initial_condition=[3,2]
for j in range(10):    
    a=a_list[j]
    b=b_list[j]
    for i in range(1,int(20/dt)):
        error1.append(setpoint-x1[i-1])
        proportional_force=Kp*error1[i]
        derivative=(error1[i]-error1[i-1])/dt
        derivative_force=Kd*derivative
        int1.append(error1[i]*dt/2)      
        integral=sum(int1)
        integral_force=Ki*integral
        U= proportional_force+derivative_force+integral_force
        t=np.linspace(i*dt,(i+1)*dt,2)
        z2 = odeint(model,initial_condition,t,args=(U,c,a))
        x1.append(z2[-1,0])
        initial_condition=z2[-1,:]
    error[j,:]=error1
    error1=[setpoint-x1[0]]
    x1=[3]
    int1=[error1[0]*dt]
    initial_condition=[3,2]
    
error_sum=np.mean(error,axis=0)
    
  
setp=[0 for i in range(2000)]  
time=np.linspace(0,20,2000)    
plt.plot(time,error_sum,'b',label='Error for L1=15') 
plt.plot(time,setp,'r--',label='Error=0')
plt.xlabel('Time')
plt.ylabel('Error')
plt.xlim(0,20)
plt.legend(loc="bottom right")
plt.show()
plt.savefig('L1-15.png')

    
