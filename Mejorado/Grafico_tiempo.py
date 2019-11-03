'''
Todos los intentos fueron con los parametro:
d = 0.15*_mm

rho_agua = 1000.*_kg/(_m**3)
rho_particula = 2650.*_kg/(_m**3)

dt = 0.00001 segundos   
tmax = 0.05 segundos
'''
from matplotlib.pylab import *

n = [1,3,10,15,20,30,45,70,100,120,150]
t = [3.01,7.34,20.09,30.29,39.3,60.53,91.71,161.23,257,334.62,433.89]

plot(t,n)
title("Grafico N vs T",size=30)
ylabel("Tiempo en segundos")
xlabel("Numero de particulas")

savefig("grafico.png")
