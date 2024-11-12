import numpy as np

def fibonacci(n):
    seq= [0,1]
    for i in range(n-2):
        novo= seq[-1]+seq[-2]
        seq.append(novo)
    
    return seq

print(fibonacci(11))


def fibonacciRec(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2: 
        return [0,1]
    else:
        seq= fibonacciRec(n-1)
        novo= fibonacciRec(n-1)[-2] + fibonacciRec(n-1)[-1]
        seq.append(novo)
    
    return seq

print(fibonacciRec(11))
    