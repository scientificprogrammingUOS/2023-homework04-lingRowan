import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, method='product'):
    if method == 'product':
        return arr1 * arr2.reshape(1, 1, 2, 2)
    elif method == 'sum':
        return arr1 + arr2.reshape(1, 1, 2, 2)
    else:
        raise ValueError('Invalid combination method specified.')


if __name__ == "__main__":
    # use this for your own testing!
   #print(combination([1,6,9],[3,5,9]))
   pass
    
