
#import math
#import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
#import random

def cdf_exp(x, h):
    return 1.0 - np.exp(-h * x)


print(cdf_exp(0.5,5))
'''xs = np.linspace(0, 2.5, 24)
ys = [cdf_exp(x, 2) for x in xs]
plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("CDF(x)")
plt.title("Exponential CDF")'''

