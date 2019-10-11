from matplotlib.pylab import *
from scipy.integrate import odeint
import random

#Unidades base SI
_m = 1.
_kg = 1.
_s = 1.
_cm = 1e-2*_m
_mm = 1e-3 *_m
_gr = 1e-3 * _kg
_in = 2.54*_cm

g = 9.81*_m/_s**2
d = 0.15*_mm
x = linspace(0, 20*d,4000)
x_mod_d = (x % d) - d/2
y = sqrt((d/2)**2 - x_mod_d**2)


rho_agua = 1000.*_kg/(_m**3)
rho_particula = 2650.*_kg/(_m**3)

dt = 0.0001*_s    	# paso de tiempo 
tmax = 2*_s  # tiempo maximo de simulacion
ti = 0.*_s # tiempo actual


data = load("initial_condition.npz")
x0 = data["x0"]
y0 = data["y0"]
vx0 = data["vx0"]
vy0 = data["vy0"]
Nparticulas = data["Nparticulas"]
print "Numero de particulas: ",Nparticulas
data = close



A = pi*(d/2)**2
V = (4./3.)*pi*(d/2)**3
m = rho_particula*V


W = array([0, -m*g])

t= arange(0,tmax,dt)
Nt = len(t)

norm = lambda v: sqrt(dot(v,v))

Cd = 0.47 # Para particula esferica
Cm = 0.5
CL = 0.2
Rp = 73.
R = (rho_particula/rho_agua - 1)
alpha = 1/(1 + R + Cm)

tau_star = 0.067   # Tau star (Shear stress)
tau_cr = 0.22*Rp**(-0.6)+0.06*10**(-7*Rp**(-0.6))   # tau critico
ustar = sqrt(tau_star * g * Rp * d)		# uestrella de verdad ahora si final final ok para siempre

ihat = array([1,0])
jhat = array([0,1])

#ustar = 0.14 # paper entre 0.14 y 0.23 (m/s)
def velocity_field(x):
	z = x[1] /d
	if z > 1./30:
		uf = ustar*log(30.*z)/0.41
	else:
		uf = 0
	return array([uf,0])
	

vfx = velocity_field([0, 10*d])[0]
k_penal = 0.5*Cd*rho_agua*A*norm(vfx)**2/(d/20)

def fuerzas_hidrodinamicas(x,v,d,area,masa):

	xtop = x + (d/2)*jhat
	xbot = x - (d/2)*jhat
	vf = velocity_field(x + 0*jhat)

	vrelf_top = abs(velocity_field(xtop)[0])
	vrelf_bot = abs(velocity_field(xbot)[0])

	vrel = vf - v

	Cd = 0.47
	fD = (0.5*Cd*alpha*rho_agua*norm(vrel)*area)*vrel

	fL = (0.5*CL*alpha*rho_agua*(vrelf_top - vrelf_bot)*area)*vrel[0]*jhat
	fW = (-masa*g)*jhat

	Fh = fW + fD + fL

	return Fh



def particula(z,t):
	zp = zeros(4*Nparticulas)

	for i in range(Nparticulas):

		di = d 
		xi = z[4*i:(4*i+2)]
		vi = z[4*i+2:(4*i+4)]
		Fi = fuerzas_hidrodinamicas(xi,vi,di,A,m)
		#Rebote en cama de esferas
		x_mod_d = (xi[0] % d) - d/2
		y = sqrt((d/2)**2 - x_mod_d**2)

		if xi[1] < y :
			
			coordenadaX = round(xi[0]/d)*d+d/2
			rij = xi - [coordenadaX,0]
			if norm(rij) < d:
				delta = d - norm(rij)
				nij = rij/norm(rij)
				Fi += k_penal*delta*nij
				
		zp[4*i:(4*i+2)] = vi
		zp[4*i+2:(4*i+4)] = Fi/m

		for i in range(Nparticulas):
			xi = z[4*i:(4*i+2)]
			for j in range(Nparticulas):
				if i > j:
					xj = z[4*j:(4*j+2)]
					rij = xj - xi
					if norm(rij) < d:
						delta = d - norm(rij)
						nij = rij/norm(rij)
						Fj = k_penal*delta*nij
						Fi = -k_penal*delta*nij
						zp[4*i+2:(4*i+4)] += Fi/m
						zp[4*j+2:(4*j+4)] += Fj/m

	return zp

z0 = zeros(4*Nparticulas)
z0[0::4] = x0
z0[1::4] = y0
z0[2::4] = vx0
z0[3::4] = vy0

print "Integrando"
z = odeint(particula,z0,t)
print "Finalizado"


fig = figure()

ax=gca() #para linea suelo

for i in range(Nparticulas):
	xi = z[:,4*i]
	yi = z[:,4*i+1]
	col=rand(4)
	plot(xi,yi,"--.",color=col)

ax.axhline(d/2,color="k",linestyle="--")


savefig("Grafico_{0:02.0f}.png".format(Nparticulas))
#show()
axis("equal")

