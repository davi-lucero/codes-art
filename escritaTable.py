# -*- coding: utf-8 -*-
alpha=0.25
beta=8
# Valor da rigidez da mola, numericamente igual a massa
k=1 
# Distância básica dos átomos em que a mola está em repouso
l=5 
# Incremento para o tamanho da ligação
dx=0.01 
# Máximo deslocamento da mola do seu centro de equilíbrio
ux=2.5 
# Quantidades de 'pontos' na tabela
N=int(2*ux/dx+1) 

with open('bonds.in','w+') as f:
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
