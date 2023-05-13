import numpy as np
from numpy.random import normal

# implement the function gaussian_analysis

def gaussian_analysis(n):
        norm = normal(size = n)
        return norm
    


if __name__ == "__main__":
    print(gaussian_analysis(50))
    

    pass
