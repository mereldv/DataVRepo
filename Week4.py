# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:27:03 2020

@author: merel
"""
import numpy as np
import matplotlib.pyplot as plt

#%%

#Opdracht 5.1 A
def f(l,b):
    oppervlakte = l*b
    return oppervlakte

def dfdl(l,b):
    oppervlakte = b
    return oppervlakte

def dfdb(l,b):
    oppervlakte = l
    return oppervlakte

par_list = np.array([4.32,1.84])
sig_list = np.array([0.12,0.14])

z = f(*par_list)

sig_zl = sig_list[0]*np.absolute(dfdl(*par_list))
sig_zb = sig_list[1]*np.absolute(dfdb(*par_list))

sig_z = np.sqrt(sig_zl**2 + sig_zb**2)

print(z)
print(sig_z)

print((z*10000) / 32)
print((sig_z*10000) / 18)

#Opdracht 5.1 B

# Definieer de functie die behandeld wordt
def f(dh,h):
      temp = 100*dh/h
      return temp

# Voorbeeldwaarden voor beste schatters en onzekerheden van resp. x, a, b
par_list = np.array([0.03,1.87])
sig_list = np.array([0.01,0.05])

# Bereken de beste schatter voor z.
z      = f(*par_list)
# Merk op: *par_list maakt het mogelijk om alle argumenten 
#          tegelijk naar de functie te sturen.

# Bepaal de partiele onzekerheden
## Merk op! Om te zorgen dat het netjes binnen het kader past wordt
## gebruik gemaakt van line-breaks \, deze zorgen er expliciet voor
## dat Python dit als 1 lijn ziet, voor de wiskune doet het niets.
sig_zdh =  np.absolute( \
            f(par_list[0]-sig_list[0]/2,par_list[1]) \
            - f(par_list[0]+sig_list[0]/2,par_list[1]))
sig_zh =  np.absolute( \
            f(par_list[0],par_list[1]-sig_list[1]/2) \
          - f(par_list[0],par_list[1]+sig_list[1]/2))


# Bepaal de totale onzekerheid
sig_z  = np.sqrt(sig_zdh**2 + sig_zh**2)

# Print het antwoord (nog niet correct afgerond)
print(z)
print(sig_z)
#%%
#Opdracht 5.2 A
def f(a,b,c):
    joe = a*b*c
    return joe

def dfda(a,b,c):
    joe = b*c
    return joe

def dfdb(a,b,c):
    joe = a*c
    return joe

def dfdc(a,b,c):
    joe = a*b
    return joe

par_list = np.array([1.00,5.0,10.0])
sig_list = np.array([0.02,0.2,1.5])

z = f(*par_list)

sig_za = sig_list[0]*np.absolute(dfda(*par_list))
sig_zb = sig_list[1]*np.absolute(dfdb(*par_list))
sig_zc = sig_list[2]*np.absolute(dfdc(*par_list))

sig_z = np.sqrt(sig_zl**2 + sig_zb**2 + sig_zc**2)

print(z)
print(sig_z)

#Opdracht 5.2 B
# Definieer de functie die behandeld wordt
def f(a,b,c):
      temp = 5*a*3*b*c
      return temp

par_list = np.array([1.00,5.0,10.0])
sig_list = np.array([0.02,0.2,1.5])

# Bereken de beste schatter voor z.
z      = f(*par_list)
# Merk op: *par_list maakt het mogelijk om alle argumenten 
#          tegelijk naar de functie te sturen.

# Bepaal de partiele onzekerheden
## Merk op! Om te zorgen dat het netjes binnen het kader past wordt
## gebruik gemaakt van line-breaks \, deze zorgen er expliciet voor
## dat Python dit als 1 lijn ziet, voor de wiskune doet het niets.
sig_za =  np.absolute( \
            f(par_list[0]-sig_list[0]/2,par_list[1],par_list[2]) \
            - f(par_list[0]+sig_list[0]/2,par_list[1],par_list[2]))
sig_zb =  np.absolute( \
            f(par_list[0],par_list[1]-sig_list[1]/2,par_list[2]) \
          - f(par_list[0],par_list[1]+sig_list[1]/2,par_list[2]))
sig_zc =  np.absolute( \
            f(par_list[0],par_list[1],par_list[2]-sig_list[2]/2) \
          - f(par_list[0],par_list[1],par_list[2]+sig_list[2]/2))


# Bepaal de totale onzekerheid
sig_z  = np.sqrt(sig_za**2 + sig_zb**2 + sig_zc**2)

# Print het antwoord (nog niet correct afgerond)
print(z)
print(sig_z)
#%%
#Opdracht 5.3 
def f(Im,r,lamda,n,Io,Nsc,theta):
      d = (64*(Im*(2*(r**2))*lamda**4/(Io*Nsc*((1+np.cos(theta)**2)*(2*(np.pi)**4)*(((n**2)-1)/((n**2)+2)**2)))))**(1/6)
      return d
print(f(3.9E-12,0.4,405E-9,2.04,100,1E5,np.pi/2))  

## Volgorde van parameters:
# 0 , 1 , 2  , 3    , 4     , 5, 6
# Im, I0, Nsc, theta, lamda, n, r
par_list = np.array([3.9E-12,0.4,405E-9,2.04,100,1E5,np.pi/2])
sig_list = np.array([0.3E-12,3E-2,5E-9,5E-2,20,5E3,3*np.pi/180]) 

z      = f(*par_list) 

sig_zIm =  np.absolute( \
            f(par_list[0]-sig_list[0]/2,par_list[1],par_list[2],par_list[3],par_list[4],par_list[5],par_list[6]) \
            - f(par_list[0]+sig_list[0]/2,par_list[1],par_list[2],par_list[3],par_list[4],par_list[5],par_list[6]))
sig_zr =  np.absolute( \
            f(par_list[0],par_list[1]-sig_list[1]/2,par_list[2],par_list[3],par_list[4],par_list[5],par_list[6]) \
          - f(par_list[0],par_list[1]+sig_list[1]/2,par_list[2],par_list[3],par_list[4],par_list[5],par_list[6]))
sig_zlamda =  np.absolute( \
            f(par_list[0],par_list[1],par_list[2]-sig_list[2]/2,par_list[3],par_list[4],par_list[5],par_list[6]) \
          - f(par_list[0],par_list[1],par_list[2]+sig_list[2]/2,par_list[3],par_list[4],par_list[5],par_list[6]))
sig_zn = np.absolute( \
            f(par_list[0],par_list[1],par_list[2],par_list[3]-sig_list[3]/2,par_list[4],par_list[5],par_list[6]) \
          - f(par_list[0],par_list[1],par_list[2],par_list[3]+sig_list[3]/2,par_list[4],par_list[5],par_list[6])) 
sig_zIo = np.absolute( \
            f(par_list[0],par_list[1],par_list[2],par_list[3],par_list[4]-sig_list[4]/2,par_list[5],par_list[6]) \
          - f(par_list[0],par_list[1],par_list[2],par_list[3],par_list[4]+sig_list[4]/2,par_list[5],par_list[6]))
sig_zNsc = np.absolute( \
            f(par_list[0],par_list[1],par_list[2],par_list[3],par_list[4],par_list[5]-sig_list[5]/2,par_list[6]) \
          - f(par_list[0],par_list[1],par_list[2],par_list[3],par_list[4],par_list[5]+sig_list[5]/2,par_list[6]))
sig_ztheta = np.absolute( \
            f(par_list[0],par_list[1],par_list[2],par_list[3],par_list[4],par_list[5],par_list[6]-sig_list[6]/2) \
          - f(par_list[0],par_list[1],par_list[2],par_list[3],par_list[4],par_list[5],par_list[6]+sig_list[6]/2))

sig_z  = np.sqrt(sig_zIm**2 + sig_zr**2 + sig_zlamda**2 + sig_zn**2 + sig_zIo**2 + sig_zNsc**2 + sig_ztheta**2)

print(z)
print(sig_z) 





