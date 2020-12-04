# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:27:36 2020

@author: merel
"""
import numpy as np

a = np.array([4.36,3.75,4.10,4.86,4.45,4.45,4.28,3.97,4.30,4.09,\
              3.74,3.79,3.91,3.60,4.51,4.59,4.27,3.74,4.30,4.12,\
              3.81,4.44,4.36,4.44,3.90,4.29,4.35,4.16,4.63,3.92,\
              3.90,4.28,4.42,4.54,3.68,4.43,3.84,4.06,4.20,4.01,4.23])
gemiddelde = a.mean()

standaarddeviatie = np.std(a,ddof=1)
print(gemiddelde, standaarddeviatie) 
