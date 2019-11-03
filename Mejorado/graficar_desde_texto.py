from matplotlib.pylab import *
import h5py


with h5py.File("Resultados.hdf5", 'r') as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[1]

    # Get the data
    data = list(f["z"])

d = 0.15e-3 #pegado

Nparticulas = (len(data[0]) -1) /4

figure()

color = "006B93"
ax = gca()
colorlist = []
xi =[]
yi =[]

for i in range(Nparticulas):
	for j in range(len(data)-1):

		xi.append(data[j][1 + 4*i] / d)
		yi.append(data[j][1 + 4*i + 1] / d)
	
	col=rand(3)
	colorlist.append(col)
	ax.plot(xi[0::100],yi[0::100],"o",color=col)
	ax.plot(xi,yi,"--",color=col,alpha=0.5)
	xi = []
	yi = []

#ax.set_ylim([0,5])
ax.axhline(0.,color="k",linestyle="--")
#ax.axhline(1/30.,color="gray",linestyle="--")
texto ="Grafico de {} particulas".format(Nparticulas)
ax.set_title(texto)
ax.set_xlabel("$\\dfrac{x}{d}$")
ax.set_ylabel("$\\dfrac{z}{d}$")

tight_layout()
savefig("grafico/{}.png".format(Nparticulas)) #guardo frame


#show()