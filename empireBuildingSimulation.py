# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:33:49 2019

@author: dcamp
"""

import numpy as np
import matplotlib.pyplot as plt

# Initialize seed
np.random.seed(123)

# Initialize a variable that contains all final results of several simulations
all_ends = []

for i in range(500):
# Initialize random_walk
    random_walk = [0]

    for x in range(100) :
        step = random_walk[-1] 
        dice = np.random.randint(1,7)

        if dice <= 2:
            # Avoid going to negative floors
            step = max(step - 1, 0)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        
        #   Clumsy mistake
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
        
    # Plot current random_walk
    plt.plot(random_walk)
    # print(random_walk)
    all_ends.append(random_walk[-1])
# Show the plot
plt.show()

plt.hist(all_ends)
plt.show()
