import numpy as np
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n= len(arr)
    for i in range(n):
        min_indx= i
        for j in range(i+1, n):
            if arr[j] < arr[min_indx]:
                min_indx= j
            
        arr[i], arr[min_indx] = arr[min_indx], arr[i]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot= arr[len(arr)//2]
    left= [x for x in arr if x < pivot]
    middle= [x for x in arr if x == pivot]
    right= [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

sizes= [1000,2000,4000,8000,16000]
bubble_times= []
selection_times= []
quick_times= []


for i in sizes:
    arr = np.random.randint(0, 1000, i).tolist()

    arr_copy = arr.copy()
    start_time = time.time()
    bubble_sort(arr_copy)
    bubble_times.append(time.time() - start_time)
    
    arr_copy = arr.copy()
    start_time = time.time()
    selection_sort(arr_copy)
    selection_times.append(time.time() - start_time)
    
    arr_copy = arr.copy()
    start_time = time.time()
    quick_sort(arr_copy)
    quick_times.append(time.time() - start_time)

plt.figure(figsize=(10, 6))
plt.loglog(sizes, bubble_times, label="Bubble Sort", marker='o')
plt.loglog(sizes, selection_times, label="Selection Sort", marker='o')
plt.loglog(sizes, quick_times, label="Quick Sort", marker='o')
plt.xlabel("Tamanho do vetor (N)")
plt.ylabel("Tempo de execução (s)")
plt.title("Comparação de algoritmos de ordenação")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()
