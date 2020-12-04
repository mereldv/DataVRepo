# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:29:57 2020

@author: merel
"""

import numpy as np
import matplotlib.pyplot as plt

T = np.array([0.24,0.62,1.00,1.88,11.86,29.46,84.01,164.8])
a = np.array([0.39,0.72,1.00,1.52,5.20,9.54,19.22,30.06])


plt.figure()
plt.loglog(a**3, T**2, 'or')
plt.xlabel("$a^3$ in $AU^3$")
plt.ylabel("$T^2$ in $yr^2$")
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.grid()

c = 0.95
plt.loglog(a**3, c*a**3,'g-')
plt.show() 


jaar = 365*24*60*60 #Dit is in seconde 
AU = 149597870700 #Dit is in meter 
constante = c*(jaar**2)/(AU**3) 
print(constante) 

pi = 3.14
G = 6.67e-11
M = (4*pi**2)/(G*constante)
print(M) 
