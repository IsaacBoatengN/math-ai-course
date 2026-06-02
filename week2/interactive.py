# Fourier Series Interactive Visualization
# This work demonstrates the Fourier series approximation of a square wave using an interactive slider to adjust the number of terms in the series.
#%
import numpy as np
import matplotlib.pyplot as plt

 #%    
# Define the sawtooth function  
def sawtooth(x):
    return x - np.floor(x + 0.5)
#%
#Compute the nth partial sum of the Fourier series
def fourier_series(n, x):
    sum_val = np.zeros_like(x)
    for k in range(1, n + 1):
        sum_val += ((-1)**(k+1)) * (1 / k) * np.sin(2 * np.pi * k * x)
    return (1 / np.pi) * sum_val
#%
# plot partial sums for n = 1, 3, 5, 10 against the sawtooth function
x = np.linspace(0, 1, 1000)
plt.figure(figsize=(12, 8))
plt.plot(x, sawtooth(x), label='Sawtooth Function', color='black', linewidth=2)
for n in [1, 3, 5, 10]:
    plt.plot(x, fourier_series(n, x), label=f'Fourier Series n={n}')
plt.title('Fourier Series Approximation of a Sawtooth Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
#%
#Plot the L2 error between the partial sum and the sawtooth function as a function of n
def l2_error(n):
    return np.sqrt(np.mean((fourier_series(n, x) - sawtooth(x)) ** 2))
n_values = np.arange(1, 51)
errors = [l2_error(n) for n in n_values]
plt.figure(figsize=(12, 6))
plt.plot(n_values, errors, marker='o')
plt.title('L2 Error of Fourier Series Approximation')
plt.xlabel('Number of Terms (n)')
plt.ylabel('L2 Error')
plt.grid()
plt.show()  