import matplotlib.pyplot as plt
import numpy as np
'''
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,"o--r")  # "marker,line,color "
#plt.plot(x,y,color="red",linewidth="5")# x ekseni 1,2,3,4 y ekseni 1,4,9,16
plt.axis([0,6,0,20]) #x ekseni 0dan 6 ya y ekseni 0dan 20ye kadar
plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
#plt.show()
'''
print("***************************************")

'''
x = np.linspace(0,2,100) #0la2arası 100 eşit parçaya ayır
plt.plot(x, x, label="linear")
plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**3, label="cubic")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("simple plot")
plt.legend()#sol üstte bilgiyi göster
plt.show()
'''
print("***************************************")

'''
x = np.linspace(0,2,100)
fig,axs = plt.subplots(3)#3 tane axis alanı oluşturur
axs[0].plot(x, x, color="red")
axs[0].set_title("linear")
axs[1].plot(x, x**2, color="green")
axs[1].set_title("quanratic")
axs[2].plot(x, x**3, color="yellow")
axs[2].set_title("cubic")

plt.tight_layout()#ibaşlıklar iç içe geçiyordu düzeltmek için
plt.show()
'''
print("***************************************")
'''
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("grafik başlığı")
axs[0,0].plot(x, x, color="red")
axs[0,1].plot(x, x**2, color="blue")
axs[1,0].plot(x, x**3, color="green")
axs[1,1].plot(x, x**4, color="yellow")

plt.show()

'''
print("***************************************")

import pandas as pd

df = pd.read_csv("C:\\Users\\omerozkan\\Desktop\\python\\matplotlip\\nba.csv")
df = df.drop(["Number"],axis=1).groupby("Team").mean("Number")

df.head().plot(subplots=True) #subplots=True her sütunu veya veri serisini ayrı bir grafik olarak çizmek için kullanılır.
plt.legend()
plt.show()