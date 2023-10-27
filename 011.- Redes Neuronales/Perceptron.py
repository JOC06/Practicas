# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:09:33 2023

@author: JOCELYNE
"""

import numpy as np



def funcionSigno(value):
    if value > 0: 
        return 1 
    else: 
        return 0


def perceptron_AND(value):
    alfa = 0.5
    W = [1,1,1]
    X = [[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
    error = 1
    _y = 0
    y = [0,0,0,1]
    while error > 0.05 or error < -0.5:
        for i in range(4):
            _y = funcionSigno(W[0]*X[i][0] + W[1]*X[i][1] + W[2]*X[i][2])
            error = y[i] - _y
            if error < 0.05 and error > -0.5:
                break
            for j in range(len(W)):
                W[j] = W[j] + alfa * error * X[i][j]
    print("Valores de los pesos: ", W)

    
    # print("A ", "B ", "Y ")
    # value1 = funcionSigno(W[0]*X[0][0] + W[1]*X[0][1] + W[2]*X[0][2])
    # print("0 ", "0 ", value1)
    # value1 = funcionSigno(W[0]*X[1][0] + W[1]*X[1][1] + W[2]*X[1][2])
    # print("0 ", "1 ", value1)
    # value1 = funcionSigno(W[0]*X[2][0] + W[1]*X[2][1] + W[2]*X[2][2])
    # print("1 ", "0 ", value1)
    # value1 = funcionSigno(W[0]*X[3][0] + W[1]*X[3][1] + W[2]*X[3][2])
    # print("1 ", "1 ", value1)
    
    print("Tu entrada fue: ", value)
    print("A ", "B ", "Y ")
    value1 = funcionSigno(W[0]*1 + W[1]*value[0] + W[2]*value[1])
    print("0 ", "0 ", value1)


perceptron_AND([0,0])
perceptron_AND([0,1])
perceptron_AND([1,0])
perceptron_AND([1,1])