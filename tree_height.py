# python3

import argparse
import numpy as np

def calculate_tree_height(n, parents):
    heights = np.zeros(n)
    max_height = 0
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
        if height > max_height:
            max_height = height
    return max_height

def read_input(input_file):
    with open(input_file) as f:
        n = int(f.readline().strip())
        parents = np.fromstring(f.readline().strip(), sep=' ', dtype=int)
        if n != parents.size:
            raise ValueError("Invalid input: number of nodes and parent nodes don't match.")
        return n, parents

def main(input_file=None):
    if input_file:
        try:
            n, parents = read_input(input_file)
        except Exception as e:
            print(f"Error: {str(e)}")
            return
    else:
        parser = argparse.ArgumentParser(description="Calculate height of a tree.")
        parser.add_argument("-n", type=int, required=True, help="Number of nodes in the tree")
        parser.add_argument("-p", type=int, nargs='+', required=True, help="Parent nodes of each node in the tree")
        args = parser.parse_args()
        n = args.n
        parents = np.array(args.p)
        if n != parents.size:
            print("Error: number of nodes and parent nodes don't match.")
            return

    try:
        height = calculate_tree_height(n, parents)
        print(height)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
