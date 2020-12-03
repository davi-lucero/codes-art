# -*- coding: utf-8 -*-
N=32 #Número de partículas têm que ser uma potência de dois
alpha=0.25 #Parâmetro não-linear
R_1_O=10500 # Tempo de recorrência de primeira ordem aproximadamente
R_2_O=R_1_O*23 #Tempo de recorrência de segunda ordem aproximadamente
DT=20
it=int(R_2_O/DT) 
t=list(range(DT,R_1_O+1,DT))
tspan= list(range (0,R_2_O+1, DT))

import math as m
import numpy as np

a=1
b=[]
omegak2=[]
#Loop para definir as condições iniciais e as frequênicas normais de oscilação do sistema
for x in range(1, N+1):
    b.insert(x-1,a*m.sin(m.pi*x/(N+1)))
    b.insert(x+N-1,0)
    omegak2.insert(x-1, 4*(m.sin(m.pi*x/2/(N+1)))**2)

#Integração temporal
from scipy.integrate import odeint
D=[0]*2*N
def dydt(y,t):
    D[N]=y[1]-2*y[0]+alpha*((y[1]-y[0])**2-y[0]**2)
    D[0]=y[N]
    D[2*N-1]=y[N-2]-2*y[N-1]+alpha*(y[N-1]**2-(y[N-1]-y[N-2])**2)
    D[N-1]=y[2*N-1]

    D[N+1:2*N-1] = y[2:N]+y[0:N-2]-2*y[1:N-1]+alpha*((y[2:N]-y[1:N-1])**2-(y[1:N-1]-y[0:N-2])**2)
    D[1:N-1] = y[N+1: 2*N-1]
    return D

sol=odeint(dydt, b, tspan)
tspan.pop(0)
#

TIME=[]
YX=[]
YV=[]
x=[]
v=[]
Energ=[]
E=[]
for i in range(0,it):
    YX.insert(i,[])
    YV.insert(i,[])
    x.insert(i,[])
    v.insert(i,[])
    Energ.insert(i,[])
for i in range(1,it+1):
    TIME.insert(i-1,i*DT*m.sqrt(omegak2[0])/2/m.pi)
    YX[i-1].insert(0,0)
    YV[i-1].insert(0,0)
    for j in range(0,N):
        YX[i-1].insert(j+1,sol[i-1][j])
        YV[i-1].insert(j+1,sol[i-1][j+N])
for i in range(0,it):
    for j in range (0,N+1):
        x[i].insert(j,YX[i][j])
        v[i].insert(j,YV[i][j])
    x[i].insert(N+1,0)
    v[i].insert(N+1,0)
    for j in range (N,0,-1):
        x[i].insert(66-j,-YX[i][j])
        v[i].insert(66-j,-YV[i][j])

sXF=((np.fft.fft(x)).imag)/m.sqrt(2*(N+1))
sVF=((np.fft.fft(v)).imag)/m.sqrt(2*(N+1))

#Código para obter figura de um ciclo de primeira ordem
for i in range (0,int(R_1_O/DT)):
    E.insert(i,[])
    for j in range (0,5):
        E[i].insert(j,(omegak2[j]*(sXF[i][j+1])**2+(sVF[i][j+1])**2)/2)
        
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

tempo=np.array(t)/1000
plt.figure(0)
fig, ax=plt.subplots()
plt.xlabel('Tempo x $10^3$')
plt.ylabel('Energia')
plt.plot(tempo,E)
plt.yticks(np.arange(0, 0.08, 0.025))
plt.xticks(np.arange(0,R_1_O/1000,2.5))

cmap=plt.get_cmap('tab10') #Conseguir as cores padrão de 

modo1=mpatches.Patch(color=cmap(0), label='modo 1')
modo2=mpatches.Patch(color=cmap(1), label='modo 2')
modo3=mpatches.Patch(color=cmap(2), label='modo 3')
modo4=mpatches.Patch(color=cmap(3), label='modo 4')
modo5=mpatches.Patch(color=cmap(4), label='modo 5')

plt.legend(handles=[modo1,modo2,modo3,modo4,modo5],loc='best',ncol=3, fontsize='small')

plt.show()

#Código para obter figura de um ciclo de segunda ordem
for i in range(0,len(Energ)):
    for j in range(0,2):
        Energ[i].insert(j,(omegak2[j]*(sXF[i][j+1])**2+(sVF[i][j+1])**2)/2)
tempo=np.array(tspan)/10000
plt.figure(1)
fig, ax=plt.subplots()
plt.xlabel('Tempo x $10^4$')
plt.ylabel('Energia')
plt.plot(tempo,Energ)
plt.yticks(np.arange(0, 0.08, 0.025))
plt.legend(handles=[modo1,modo2],loc='best',ncol=2,fontsize='medium')

plt.show()

ENE=[]
maxi=[0,0]
for i in range(0,len(Energ),510):
    maxi[0]=0
    inte=[]
    for j in range(510):
        if(i+j)<len(Energ):
            inte.append(Energ[i+j][0])
            if (Energ[i+j][0]>maxi[0]):
                maxi[0]=Energ[i+j][0]
                maxi[1]=i+j
    # print(maxi[0])
    ENE.append(max(inte))
tempo=np.linspace(0,maxi[1]*DT/10000,len(ENE))
plt.figure(2)
fig, ax=plt.subplots()
plt.xlabel('Tempo x $10^4$')
plt.ylabel('Energia')
plt.plot(tempo,ENE)
plt.yticks(np.arange(0, 0.08, 0.025))
plt.legend(handles=[modo1],loc='best',fontsize='medium')

plt.show()
