# python3
# Dmitrijs Firsovs 211RDB310

import sys
import threading
import numpy as np

def compute_height(n, parents):
    heights = np.zeros(int(n))
    max_height = 0
    for i in range(int(n)):
        if heights[i] > 0:
            continue
        height = 0
        j = i
        while j != -1:
            if heights[j] > 0:
                height += heights[j]
                break
            else:
                height += 1
                j = int(parents[j])
        heights[i] = height
        if height > max_height:
            max_height = height
    return max_height

def main():
    input_method = input().strip()
    n, parents = None, None

    if input_method == "F":
        file_dir = input().strip()
        if str(file_dir[-1]) != "a":
            try:
                with open(f"./test/{file_dir}") as f:
                    contents = f.readlines()
                    n = contents[0].strip()
                    if n:
                        parents = contents[1].strip().split(" ")
            except:
                print("ERROR")
    elif input_method == "I":
        n = input().strip()
        if n:
            parents = input().strip().split(" ")

    if n and parents:
        height = compute_height(n, parents)
        print(int(height))

sys.setrecursionlimit(10 ** 7) 
threading.stack_size(2 ** 27)  
threading.Thread(target=main).start()
