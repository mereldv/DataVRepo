# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:21:33 2020

@author: dadav
"""

import numpy as np
import matplotlib.pyplot as plt
#%%
#opgaven 2.5 a,b

# Spanning (V)
v=np.array([0.5,0.9,1.6,2.3,2.6,3.0])
# Stroom en onzekerheid in stroom (A)
i=np.array([5.8e-5,1.12e-4,1.66e-4,2.13e-4,2.08e-4,3.07e-4])
sigmai=np.array([3e-5,3e-5,3e-5,3e-5,3e-5,3e-5])
# een lijst om de stroom als functie van de spanning te plotten
vl=np.arange(0.,np.amax(v),np.amax(v)/100)


axis_font = {'fontname':'Arial', 'size':'20'}

# definieer een figuuromgeving
plt.figure()
# hier maken we eerst de plot van de datapunten
# errorbar laat plotten met onzekerheden in x- en y-richting toe
# tekst kan opgemaakt worden op de (mogelijk bekende) LaTeX-manier
plt.errorbar(v,i,yerr=sigmai,fmt='r.', label='$I$($V$)')
plt.axis([0,3.2,0,0.5e-3])
plt.xlabel("V(volt)",**axis_font)
# Je kunt zoiets als de fontgrootte ook lokaal instellen
plt.ylabel("I(ampere)",**axis_font)
# Hiermee pas je de grootte van de tick labels aan
# Deze optie laat ook specificatie van positie van ticks toe (anders automatisch)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.legend(loc='upper right')
plt.suptitle('leuk')
# vervolgens plotten we ook de verwachting, met een weerstand R = 1 kOhm 
plt.plot(vl, vl/10000,'b-',label='Expected',linewidth=3)
# Hiermee passen we ook de fontgrootte van de legenda aan
plt.legend(loc='upper right',fontsize=12)
# Je kunt een grid aanzetten
#plt.grid()
plt.show()
#Om als bestand weg te schrijven (komt in week 4 bij DATA-Py aan de orde)
#plt.savefig('vidata.png',dpi=300,bbox_inches='tight')
#%%

#opgaven 2.6 

# Volgorde: Mercurius, Venus, Aarde, Mars, Jupiter, Saturnus, Uranus, Neptunus
# Omlooptijden T in jaren
T = np.array([0.24,0.62,1.00,1.88,11.86,29.46,84.01,164.8])
# Gemiddelde afstand tot de zon a in AU
a = np.array([0.39,0.72,1.00,1.52,5.20,9.54,19.22,30.06])

c=1

plt.loglog(T**2,a**3,'or')
plt.loglog(c*a**3,a**3)

#%%


a = np.array ([4.36 ,3.75 ,4.10 ,4.86 ,4.45 ,4.45 ,4.28 ,3.97 ,4.30 ,4.09 ,\
3.74 ,3.79 ,3.91 ,3.60 ,4.51 ,4.59 ,4.27 ,3.74 ,4.30 ,4.12 ,\
3.81 ,4.44 ,4.36 ,4.44 ,3.90 ,4.29 ,4.35 ,4.16 ,4.63 ,3.92 ,\
3.90 ,4.28 ,4.42 ,4.54 ,3.68 ,4.43 ,3.84 ,4.06 ,4.20 ,4.01,4.23])

gem= np.mean(a)
SD = np.std(a,ddof=1)
SDOM = (1/40)**0.5*SD

print (gem)
print (SDOM)









#%%

# Massadichtheid \rho in g/cm^3
np.array([18.5,21.0,16.8,15.3,19.6,19.8])

#%%
































