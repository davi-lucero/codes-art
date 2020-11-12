# -*- coding: utf-8 -*-
N=32 #Número de partículas
IT=2392000 #586575 ts 0,5 #Quantidade total de iterações feitas no lammps através do comando run
R_1_O=104000#23463 #ts 0,5   #Iterações num timestep de  0.1 para uma recorrência
ts=0.1 #timestep

#8.25200111026924e-05 fequencia 1ordem para ts 0,5 pegando 22 ciclos
#3.7509095955769274e-06 freq 2 ordem para ts 0,5

#9.552379823463337e-05 freq 1ordem ts 0,1 pegando 22 ciclos
    #9.812290875550714e-05 para 1 ciclo
#4.341990828846971e-06 freq 2 ordem ts 0,1

import numpy as np
import math
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches


#Frequências de oscilação dos N modos normais
omegak2=[]
for x in range(1, N+1):
    omegak2.append(4*(math.sin(math.pi*x/(2*(N+1))))**2)
#

#Matrizes de posição e velocidade para as partículas    
POS=np.empty([IT,2*N+2])
VEL=np.empty([IT,2*N+2])
#

#Contadores
it=0
k=0
#
with open('dump_quad.comp') as f: 
    #Loop para obter a posição e a velocidade das partículas a partir da primeira iteração do LAMMPS
    for line in f:                
        k=k+1
        #Condições para eliminar as linhas inúteis
        if ((k-1)%(N+11)!=0 and (k-2)%(N+11)!=0 and (k-3)%(N+11)!=0 and (k-4)%(N+11)!=0 and (k-5)%(N+11)!=0 and (k-6)%(N+11)!=0 and (k-7)%(N+11)!=0 and (k-8)%(N+11)!=0 and (k-9)%(N+11)!=0  #O arquivo .comp tem linhas que se repetem, para situar qual iteração que é etc
        #Condições para eliminar as informações das partículas extremas que são na verdade as paredes do sistema
        and (k-10)%(N+11)!=0 and (k-(N+11))%(N+11)!=0
        #Condição para ignorar a iteração zero
        and k>(N+11)):                                                              
            line=line.split() 
            c=(k%(N+11)-10)
            POS[it,c]=float(line[0])-5*(c)
            VEL[it,c]=float(line[1])
            if (c==N):
                it=it+1
            #vale notar que no arquivo dump são escrito apenas o x e o vx para não ocupar muito espaço em disco
           
#Ajuste das matrizes para a transformada de Fourier           
POS[:,N+2:2*N+2]=-POS[:,N:0:-1]
VEL[:,N+2:2*N+2]=-VEL[:,N:0:-1]               
#

#A posição e a velocidade têm que estar organizadas em uma "matriz", ou lista de listas
# Para a transformada de Fourier temos que ter um zero, a função, outro zero, e o negativo da função ao contrário.  
 
#Transformada de Fourier       
sXF=((np.fft.fft(POS)).imag)/math.sqrt(2*(N+1))  
sVF=((np.fft.fft(VEL)).imag)/math.sqrt(2*(N+1))

#Conseguindo a energi dos primeiros cinco modos normais
Energ=np.empty([IT,5])
Energ[:,0:5]=(omegak2[0:5]*sXF[:,1:6]**2+sVF[:,1:6]**2)/2

#Conseguir as cores padrão de dessenho e fazer as legendas
cmap=plt.get_cmap('tab10') 
modo1=mpatches.Patch(color=cmap(0), label='modo 1')
modo2=mpatches.Patch(color=cmap(1), label='modo 2')
modo3=mpatches.Patch(color=cmap(2), label='modo 3')
modo4=mpatches.Patch(color=cmap(3), label='modo 4')
modo5=mpatches.Patch(color=cmap(4), label='modo 5')
#

tempo=np.array(list(range(1,R_1_O+1)))*ts/1000
plt.figure(0)
fig, ax=plt.subplots()
plt.xlabel('Tempo x $10^3$')
plt.ylabel('Energia')
plt.plot(tempo,Energ[0:R_1_O,:])
plt.yticks(np.arange(0, 0.08, 0.025))
plt.xticks(np.arange(0,max(tempo),2.5))
plt.legend(handles=[modo1,modo2,modo3,modo4,modo5],loc='best',ncol=3, fontsize='small')


tempo=np.array(list(range(1,IT+1)))*ts/10000
plt.figure(1)
fig, ax=plt.subplots()
plt.xlabel('Tempo x $10^4$')
plt.ylabel('Energia')
plt.plot(tempo,Energ[0:IT,0:2])
plt.yticks(np.arange(0, 0.08, 0.025))
plt.legend(handles=[modo1,modo2],loc='best',ncol=2,fontsize='medium')


