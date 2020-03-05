
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


def model(x,t,u,c):    
    dy=x[1]
    xdot=[[],[]]
    xdot[0]=dy
    xdot[1]=0.5*sin(x[0])+0.5*x[1] +u
    return xdot
    
c=1    
dt=0.01  # Timestep
setpoint=1 # Desired Variable
x2=[2,2]
int1=[]
x1=[3]
error1=[setpoint-x1[0]] 
int1=[error1[0]*dt]
Kp_Ki_Kd=[3,1,3]
L1=20
L2=1
initial_condition=[3,2]

alpha_list=[1,3,5,10,20]
error=np.zeros((5,2000))
for j in range(5):
    alpha=alpha_list[j]
    Kp=alpha*Kp_Ki_Kd[0]
    Ki=alpha*Kp_Ki_Kd[1]
    Kd=alpha*Kp_Ki_Kd[2]
    
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
        z2 = odeint(model,initial_condition,t,args=(U,c))
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
plt.plot(time,setp,'y--')  
plt.plot(time,error[0,:],'r',label=' Alpha = 1') 
#plt.plot(time,error[1,:],'g',label=' Alpha = 3') 
plt.plot(time,error[2,:],'b',label=' Alpha = 5') 
#plt.plot(time,error[3,:],'y',label=' Alpha = 10') 
plt.plot(time,error[4,:],'g',label=' Alpha = 20') 
plt.legend(loc="bottom right")
plt.xlabel('Time')
plt.ylabel('Error')
plt.xlim(0,20)
plt.savefig('simulation2.png')
plt.show()