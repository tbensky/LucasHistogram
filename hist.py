#https://docs.google.com/spreadsheets/d/1NtlYL6UEo1wg6VWzHioeN1AqAFn1ZlmwQaBPRMG932U/edit?gid=0#gid=0

#abstract https://docs.google.com/document/d/1uyscJ0LITkTgOfa_U9ZtFTJ9ORAZ5BMYVJGi7-pSm8k/edit?usp=drivesdk

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import math

def gauss(x,A,x0,b,c):
    return A*np.exp(-(x-x0)**2/b**2)+c

d = []

with open("centers_table.csv","r") as f:
    for line in f.readlines():
        d.append(float(line.strip())/1000)

fig,ax = plt.subplots()
n,bins,patches = plt.hist(d,bins=10,edgecolor='black')
print(f"n={n}, {len(n)}\nbins={bins}, {len(bins)}\npatches={patches}")

plt.xticks(rotation=45) # or rotation=90
plt.tight_layout()
ax.ticklabel_format(axis='x', style='plain', useOffset=False)


xx = np.array(bins[:-1])
yy = np.array(n)

plt.xlabel("Frequency (kHz)")
plt.ylabel("Count")
plt.margins()
#plt.plot(bins[:-1],n)
#plt.show()


x = np.arange(bins[0],1.000002*bins[-1],0.0001)
y = gauss(x,10,573.336,0.0001,0)

popt, pconv = curve_fit(gauss,xx,yy,p0=[20,573.336,0.001,0])
print(popt)
popt[1] += 0.0004
plt.plot(x,gauss(x,*popt))

sigma = math.sqrt(popt[2]/2)
fwhm = 2.35 * sigma
center = popt[1]*1000
Q = round(center/fwhm,0)

plt.title(f"${{\\bar f}}$={round(center,3)} Hz, FWHM={round(fwhm,6)} Hz, Q={Q}")
plt.tight_layout()
print(popt)
plt.savefig("hist.png",dpi=300)
plt.close()