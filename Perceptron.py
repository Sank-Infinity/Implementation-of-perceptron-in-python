# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:31:52 2020

@author: Sanket Kale
"""

# Implementation of First Neuron From scratch

#Importing required libraries
import numpy as np

# Sigmoid activation function
def sigmoid(h):
  y = 1/(1+ np.exp(-h))
  return y

# calculation of perceptron
def activate(x,w):
  h = 0
  for x , w in zip(x,w):  
    h += x*w                             # Z(n) = Wn*A(n-1) + B(n);
  return sigmoid(h)                      # f(Z) ;


if __name__ == '__main__':

# compile time initialization of inputs and weight
x = [10,5,3]
w = [0.2 , 0.4, 0.5]

"""
Random initialization of input and weight vector

x = np.random.rand(3)
w = np.random.rand(3)

"""

 # pass input and weight vector
output = activate(x , w)

print(output)

"""
u  = 1 /  (1 + np.exp(-5.5))
print(u)

"""