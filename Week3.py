# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 09:15:04 2020

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt

#%%
#Opdracht3.3
getallen = np.array([2,7,2,1,5,7,3,4,2,1,4,3,1,4,3,3,4,1,1,2,1,1,3,1,6,2,3,1,4,2])
uitkomst = np.arange(8)
frequentie = np.bincount(getallen)
#print(frequentie)

plt.figure()
plt.plot(uitkomst,frequentie,'og')
plt.bar(uitkomst,frequentie,.05, color='k')
#%%
#Opdracht 3.4
getallen = np.array([7.7,4.8,7.2,9.6,6.0,7.4,9.0,8.4,8.2,8.1,8.2,4.2,5.6,\
9.0,8.2,6.3,7.0,7.0,9.1,3.8,8.5,8.0,3.4,1.9,1.3,2.3,\
4.4,7.9,4.9,8.2,7.1,9.8,3.7,7.3,5.5,8.7,8.9,7.6,6.7,\
7.3,7.0,6.5,6.2,7.2,4.8,7.8,3.1,8.6,2.3,7.1,7.0,7.7,\
8.8,7.3,7.4,6.4,6.1,6.7,7.5,7.8,7.7,7.7,7.0,7.1,6.1,\
8.8,8.2,7.6,9.3,7.8,8.6,4.7,7.2,8.9,8.6,6.7,7.2,9.2,\
9.0,7.7,1.5,6.5,7.5,9.4,4.0,8.1,6.3])

plt.figure()
plt.hist(getallen,20)
plt.show()

#normaliseren
plt.figure()
plt.hist(getallen,10,density=True,range=(0,10))

plt.xlabel("leuk")
plt.ylabel("Kansdichtheid") 
plt.show()

#%%
#Opdracht 4.2

# Deze regel laadt commando's omtrent de normale verdeling
from scipy.stats import norm

# Maak een lijst met x-waarden voor plotdoeleinden
x = np.arange(-5,5,.1) 
# Normale verdeling met verwachtingswaarde 0, standaarddeviatie 1:
# norm.pdf(x,loc=0,scale=1)
# Cumulatieve verdeling voor dezelfde gegevens:
# norm.cdf(x,loc=0,scale=1)

# Een plot van de verdeling en de cumulatieve verdeling
plt.plot(x,norm.pdf(x),label='PDF')
plt.plot(x,norm.cdf(x),label='CDF')
plt.legend()
plt.show()

# 1000 random getallen trekken
randnum=norm.rvs(loc=2,scale=1,size=1000)
# Een bin-histogrammetje van de data
plt.hist(randnum,density=True)
plt.show()

# Berekening op de kans op een waarde tussen 2 en 3, 
# ongeveer 2.1%
print(norm.cdf(1,loc=0,scale=1)-norm.cdf(3,loc=0,scale=1))




