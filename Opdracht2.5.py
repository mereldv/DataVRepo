# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:08:13 2020

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt

# Spanning (V)
v=np.array([0.5,0.9,1.6,2.3,2.6,3.0])
# Stroom en onzekerheid in stroom (A)
i=np.array([5.8e-5,1.12e-4,1.66e-4,2.13e-4,2.08e-4,3.07e-4])
sigmai=np.array([3e-5,3e-5,3e-5,3e-5,3e-5,3e-5])
# een lijst om de stroom als functie van de spanning te plotten
vl=np.arange(0.,np.amax(v),np.amax(v)/100)

## Hieronder een verzameling van kleuren
# b: blauw                           # m: magenta
# g: groen                           # y: geel
# r: rood                            # k: zwart
# c: cyaan                           # w: wit

## Het is ook mogelijk om de stijl te varieren. Enkele voorbeelden zijn:
# .:  punten                         # -.: stip-punt lijn
# o:  grote punten                   # : : stippellijn
# -:  lijn                           # --: gestreepte lijn

# Met deze regel kun je globaal het type font instellen en de grootte 
# Met ** laat je deze definities los op bijvoorbeeld een asbijschrift
axis_font = {'fontname':'Arial', 'size':'24'}

# definieer een figuuromgeving
plt.figure()
# hier maken we eerst de plot van de datapunten
# errorbar laat plotten met onzekerheden in x- en y-richting toe
# tekst kan opgemaakt worden op de (mogelijk bekende) LaTeX-manier
plt.errorbar(v,i,xerr=0.0,yerr=sigmai,fmt='y.', label='$I$($V$)')
plt.axis([0,10,0,2e-3])
plt.xlabel("x-label",**axis_font)
# Je kunt zoiets als de fontgrootte ook lokaal instellen
plt.ylabel("y-label",size='6')
# Hiermee pas je de grootte van de tick labels aan
# Deze optie laat ook specificatie van positie van ticks toe (anders automatisch)
plt.xticks(fontsize=24)
plt.yticks(fontsize=6)
plt.legend(loc='upper left')
# vervolgens plotten we ook de verwachting, met een weerstand R = 1 kOhm 
plt.plot(vl, vl/10000,'g--',label='Expected',linewidth=5)
# Hiermee passen we ook de fontgrootte van de legenda aan
plt.legend(loc='upper right',fontsize=12)
# Je kunt een grid aanzetten
#plt.grid()
plt.show()
#Om als bestand weg te schrijven (komt in week 4 bij DATA-Py aan de orde)
#plt.savefig('vidata.png',dpi=300,bbox_inches='tight')