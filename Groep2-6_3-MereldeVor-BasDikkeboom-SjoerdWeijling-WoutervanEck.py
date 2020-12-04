# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:02:00 2020

@author: merel
"""

import numpy as np
import matplotlib.pyplot as plt

#INLEVEROPDRACHT DEEL 1

#Opdracht A
# Hoogte, onzekerheid daarin, in m.
h = np.array([0.,0.50,0.80,1.60,2.10,2.60,3.40,4.20]) 
sig_h = np.array([0,0.05,0.05,0.05,0.05,0.05,0.05,0.05])
# Gekwadrateerde snelheid, onzekerheid daarin, in (m/s)^2.
v2 = np.array([0,10,18,24,37,45,66,80])
sig_v2 = np.array([0,3,4,5,6,7,8,9])

#Opdracht B
y = 18.5*h #Dus de helling van de centralelijn is ongeveer 18.5 

#Opdracht C
y2 = 20*h  #bovenste onzekerheidslijn
y3 = 17*h  #onderste onzekerheidslijn

#Opmaak plus plots van bovenstaande opdrachten
plt.figure()

plt.xlabel("$h$ (m)", fontsize=15)
plt.ylabel("$v^2$ (m/s)$^2$", fontsize=15)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.errorbar(h,v2, xerr = sig_h, yerr = sig_v2, fmt = "none")
plt.plot(h,y, label = "Centrale lijn")
plt.plot(h,y2,'m:', label = "Bovenste onzekerheidslijn")
plt.plot(h,y3,':', label = "Onderste onzekerheidslijn")
plt.legend(loc='upper left', fontsize=11)
plt.title("Verticale worp", fontsize=15)
plt.ylim(0)
plt.xlim(0)
plt.grid()
plt.show()

#Opdracht D
g_y = 18.5/2
g_y2 = 20/2
g_y3 = 17/2
print("g_y =",g_y,"m/s^2")
print("g_y2 =",g_y2,"m/s^2")
print("g_y3 =",g_y3,"m/s^2")

sig_hellingplus = g_y2 - g_y
sig_hellingmin = g_y3 - g_y
print("sig_hellingplus =",sig_hellingplus,"en sig_hellingmin =",sig_hellingmin) #Deze zijn gelijk
#De onzekerheid in de helling is 0.8 m/s^2 
print("SDOM =",0.8/(7**0.5),"m/s^2") 



#INLEVEROPDRACHT DEEL 2

#Opdracht E
v2_2 = np.array([50.5,46.8,48.2,48.6,47.8,48.4,49.1,48.9,49.4,46.7]) #in (m/s)^2
print("\nHet gemiddelde van v2_2 =",v2_2.mean(),"(m/s)^2")
print("SDOM =",np.std(v2_2,ddof=1)/np.sqrt(len(v2_2)),"(m/s)^2")

g1 = (48.4 + 0.4)/(2*(2.50-0.05)) #Maximale g
g2 = (48.4 - 0.4)/(2*(2.50+0.05)) #Minimale g
print("g1 =",g1,"m/s^2 en g2 =",g2,"m/s^2") 
sig_g = (g1-g2)/4 
print("sig_g =",sig_g,"m/s^2")
g = 48.4/(2*2.5) 
print("g =",g,"m/s^2") 

#Opdracht F
#geaccepteerde_waarde_g = 9.8125 +/- 0.0001 m/s^2
sig_delta = ((0.14)**2 + (0.0001)**2)**0.5 
twee_sigma_delta = sig_delta*2
verschil_g = 9.8125 - 9.68

if twee_sigma_delta > verschil_g: 
    print("De waarde is significant afwijkend van de geaccepteere waarde.")
else:
    print("De waarde is niet significant awfwijkend van de geaccepteerde waarde.")


