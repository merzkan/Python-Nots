#figür

import matplotlib.pyplot as plt
import numpy as np
'''
x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2
figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])#soldan 0.1,alttan 0.1,genişlik 0.8,yükseklik0.8  #figur alanına eklenecek axis alanının konumunu düzlemin tamamı 1:([sağdan yüzde getircek 0.1,alttan 0.1 gelsin,genişlik 0.8(yüzde80lik alan),yükseklik0.8(yüzde80lik alan)]) 1in
axes_cube.plot(x,y,'b')
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")

axes_square = figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x,z,'r')
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.set_title("Square")
plt.show()
'''

print("******************************************")

'''
x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")

axes.legend(loc=4) #normal yeri sol üst #1sağ üst- 2solüst - 3solaşağı - 4sağaşağı
plt.show()
'''

print("******************************************")

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8))
 
axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
#fig.savefig("figure.png") #fig.savefig("figure.pdf")
plt.show()