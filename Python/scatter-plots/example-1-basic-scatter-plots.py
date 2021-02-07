## Step 0: import required libraries 

import numpy as np
import matplotlib.pyplot as plt


## Step 1: Create X and Y coordinates to plot

# Creates an array x of length 100 with linearly spaced numbers between 0 and 10
x = np.linspace(0, 10, 20)
# Creates an array y that is square of x plus some error
func1 = x ** 2 + 20
obs1 = func1 + np.random.uniform(-10,10, x.shape[0])


## Step 2: Plot
plt.plot(x, func1, '-', color='black')
plt.plot(x, obs1, 'o', color='blue')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Plot of $y = x^2 + \epsilon$')
plt.legend(['$y = x^2 + 20$', 'Observation'])

## Step 3: Show the plot
plt.show()