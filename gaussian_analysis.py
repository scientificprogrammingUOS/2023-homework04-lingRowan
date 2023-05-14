import numpy as np
from numpy.random import normal

# implement the function gaussian_analysis

def gaussian_analysis(data):
    
    mean = np.mean(data)
    stdev = np.std(data)

    return mean, stdev
    


if __name__ == "__main__":
    print(gaussian_analysis([1,2,3,4]))
    

    pass
