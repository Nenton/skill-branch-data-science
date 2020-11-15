import numpy as np
import copy

def func_1(x: float):
    return np.cos(x) + 0.05*x**3 + np.log2(x**2)

def func_2(x):
    return x[0]**2*np.cos(x[1]) + 0.05*x[1]**3 + 3*x[0]**3*np.log2(x[1]**2)

def derivation(x: float, function = func_1):
    delta = 1e-5
    
    start = function(x)
    end = function(x + delta)
    return round((end - start) / delta, 2)

print(derivation(10))

def gradient(queue, function = func_2):
    
    delta = 1e-5
    
    values = []
    
    for index, value in enumerate(queue):
        new_queue = copy.deepcopy(queue)
        new_queue[index] += delta
        
        val = round(function(new_queue), 2)

        values.append(val)
    
    return values

print(gradient([10,1]))


def gradient_optimization_one_dim(function = func_1, start_pos = 10, epsilon = 0.001, count = 50):
    position = start_pos
    
    i = 0
    while i < count:
        position -= derivation(position, function) * epsilon
        i += 1
    return round(position, 2)

print(gradient_optimization_one_dim(func_1, 10))


def gradient_optimization_multi_dim(function = func_2, start_poses = [4, 10], epsilon = 0.001, count = 50):
    values = copy.deepcopy(start_poses)
    
    i = 0
    
    while i < count:
        gradient_local = gradient(values, function)
        
        for index, _ in enumerate(gradient_local):
            values[index] -= gradient_local[index] * epsilon
            values[index] = round(values[index], 2)
        
        i += 1
    
    return values

print(gradient_optimization_multi_dim())
