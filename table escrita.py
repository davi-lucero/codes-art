# -*- coding: utf-8 -*-
alpha=0.25
beta=8
k=1 #Valor da rigidez da mola, numericamente igual a massa
l=5 #Distância básica dos átomos em que a mola está em repouso
dx=0.01 #Incremento para o tamanho da ligação
ux=2.5 #Máximo deslocamento da mola do seu centro de equilíbrio
N=int(2*ux/dx+1) #Quantidades de 'pontos' na tabela
                 #Transformando para valor inteiro, cuidado que pode ter a parte decimal truncada

with open('bonds.table','w+') as f:
    f.write('#Termo linear e termo quadrático\n\n')
    f.write('QUAD\n')
    f.write('N '+str(N) +'\n\n')
    k2=k*alpha
    for i in range(N):
        x=i*dx+ux
        f.write(str(i+1) +' '+ str(x) +' '+ str(k*x**2/2+k2*x**2*l-k2*x**3/3-k*l*x-k2*l**2*x) +' '+ str(k*(l-x)+k2*(l-x)**2) +'\n')  
    f.write('\nCUB\n')
    f.write('N '+str(N) +'\n\n')
    k2=k*beta
    for i in range(N):
        x=i*dx+ux
        f.write(str(i+1) +' '+ str(x) +' '+ str(-x*(k*l+k2*l**3)+x**2*(k/2+3*k2/2*l**2)+x**3*k2*l-x**4*k2/4) +' '+ str(k*(l-x)+k2*(l-x)**3) +'\n')  
