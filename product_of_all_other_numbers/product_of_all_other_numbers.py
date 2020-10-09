'''
Input: a List of integers
Returns: a List of integers
https://stackoverflow.com/questions/36288124/multiply-list-by-all-elements-of-the-list-except-at-its-own-index
reduce https://www.geeksforgeeks.org/reduce-in-python/
enumerate https://www.bitdegree.org/learn/python-enumerate
'''

from functools import reduce
import numpy as np

def product_of_all_other_numbers(arr):
    # Your code here
    res = []
    for i, el in enumerate(arr):
        res.append(reduce(lambda x, y: x*y, arr[:i] + arr[i+1:]))
    return res

    # Base case
    if(n == 1):
        print(0)
        return

    # O(n) solution using memoization
    # https://www.geeksforgeeks.org/a-product-array-puzzle/
    # # Allocate memory for temporary arrays left[] and right[]
    # left = [0]*n
    # right = [0]*n

    # # Allocate memory for the product array
    # prod = [0]*n

    # # Left most element of left array is always 1
    # left[0] = 1

    # # Rightmost most element of right array is always 1
    # right[n - 1] = 1

    # # Construct the left array
    # for i in range(1, n):
    #     left[i] = arr[i - 1] * left[i - 1]

    # # Construct the right array
    # for j in range(n-2, -1, -1):
    #     right[j] = arr[j + 1] * right[j + 1]

    # # Construct the product array using
    # # left[] and right[]
    # for i in range(n):
    #     prod[i] = left[i] * right[i]

    # # print the constructed prod array)
    # for i in range(n):
    #     print(prod[i], end =' ')

def product_with_division(input):
    arr = np.array(input)
    return arr.prod() / arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    print(f"Output of product_with_division: {product_with_division(arr)}")
