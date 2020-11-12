# -*- coding: utf-8 -*-
N=32
m1=[0]
m2=[0]
m3=[0]
import math
for i in range(1,33):
    m1.append(math.sin(i*math.pi/33))
    m2.append(math.sin(2*i*math.pi/33))
    m3.append(math.sin(3*i*math.pi/33))
m1.append(0)
m2.append(0)
m3.append(0)

a=list(range(0,34))

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(a, m1, 'k--', label='Modo 1')
ax.plot(a, m2, 'k:', label='Modo 2')
ax.plot(a, m3, 'k.', label='Modo 3')

legend = ax.legend(loc='lower left', shadow=True, fontsize='large')
plt.xlabel('Número da Conta')
plt.ylabel('Deslocamento Relativo do Centro de Equilíbrio')

plt.show()