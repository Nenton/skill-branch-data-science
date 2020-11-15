import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import copy

def func_1(x: float):
    return math.cos(x) + 0.05*x**3 + math.log(x**2, 2)

def func_2(x):
    return x[0]**2*np.cos(x[1]) + 0.05*x[1]**3 + 3*x[0]**3*np.log2(x[1]**2)

def func_3(x: float):
    return math.cos(x) + 0.05*x**3 + math.log(x**2, 2)

def func_4(x: float):
    return math.cos(x) + 0.05*x**3 + math.log(x**2, 2)

def derivation(x: float, function = func_1):
    delta = 1e-5
    
    start = function(x)
    end = function(x + delta)
    return (end - start) / delta

derivation(10)

def derivation_many(queue, function):
    delta = 1e-5
    
    start = function(queue)
    end = function(x + delta)
    return (end - start) / delta

def gradient(queue, function = func_2):
    
    delta = 1e-5
    
    values = []
    
    for index, value in enumerate(queue):
        new_queue = copy.deepcopy(queue)
        new_queue[index] += delta
        
        val = round((function(new_queue) - function(queue)) / delta, 2)

        values.append(val)
    
    return values

gradient([10,1])