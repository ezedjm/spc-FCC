import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # convierto lista en matriz de 3x3
    matrix = np.array(list).reshape(3, 3)
    
    # calculo estadistica
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()]
    max_values = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()]
    min_values = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()]
    sum_values = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    
    # creoo diccionario
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_values,
        'min': min_values,
        'sum': sum_values
    }
    
    return calculations