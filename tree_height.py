# python3
# Dmitrijs Firsovs 211RDB310

import sys


def compute_height(n, parents):
    
    heights = [0] * n
    
    for i in range(n):
        
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
                j = parents[j]
       
        heights[i] = height
   
    return max(heights)


def main():
    n = int(input("Enter the number of nodes in the tree: "))
    parents = list(map(int, input("Enter the parent nodes of each node in the tree, separated by spaces: ").split()))
    print("The maximum height of the tree is:", compute_height(n, parents))


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
