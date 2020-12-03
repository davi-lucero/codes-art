# -*- coding: utf-8 -*-
N=34 #Número de partículas simuladas com duas partículas a mais para servirem de parede
b=[]
a=1.0 #amplitude de deslocamento
import math
for x in range(1, N-1):
    b.append(a*math.sin(math.pi*x/(N-1))) #Atribuindo os deslocamentos relativos da x-ésima particula em relação ao seu centro de equilíbrio
    
with open('data_quad.inicial','w+') as f:
    f.write('atoms position and bonds\n')
    f.write(str(N)+' atoms\n')
    f.write(str(N-1)+' bonds\n')
    f.write('1 atom types\n')
    f.write('1 bond types\n')
    f.write('0 '+str(N*5)+' xlo xhi\n')
    f.write('-0.5 0.5 ylo yhi\n')
    f.write('-0.5 0.5 zlo zhi\n\n')
    f.write('Atoms\n\n')
    f.write(str(0+1)+' 1 1 ' +str(0*5)+'.0'+' 0.0 0.0\n')
    for i in range(1,N-1):
        f.write(str(i+1)+' 1 1 ' +str(i*5+b[i-1])+'.0'+' 0.0 0.0\n')
    f.write(str(N)+' 1 1 ' +str((N-1)*5)+'.0'+' 0.0 0.0\n')
    f.write('\nBonds\n\n')
    for i in range(1,N):
        f.write(str(i) +' 1 '+str(i)+' '+str(i+1)+'\n')
    
