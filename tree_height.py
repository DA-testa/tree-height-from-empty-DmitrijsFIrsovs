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

def read_input():
   
    n = input().strip()
    if not n:
        return None, None
    parents = input().strip().split()
    if len(parents) != int(n):
        return None, None
    return n, parents

def read_input_file(filename):
    try:
        with open(filename) as f:
            contents = f.readlines()
    except FileNotFoundError:
        print(f"Error: could not open file '{filename}'")
        return None, None

    n = contents[0].strip()
    if not n:
        return None, None
    parents = contents[1].strip().split()
    if len(parents) != int(n):
        print("Error: invalid input format")
        return None, None

    return n, parents

def main():
   
    input_method = input().strip().lower()
    if input_method not in ("i", "f"):
        print("Error: invalid input method")
        return

    
    if input_method == "f":
        filename = input().strip()
        if not filename.endswith(".txt"):
            print("Error: invalid input file format")
            return
        n, parents = read_input_file(filename)
    else:
        n, parents = read_input()

    if n is None or parents is None:
        print("Error: invalid input format")
        return

    # 
    height = compute_height(n, parents)
    print(int(height))

if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    threading.Thread(target=main).start()
