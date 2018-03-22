#https://stackoverflow.com/questions/22366299/extending-regressions-beyond-data-in-matplotlib
#https://stackoverflow.com/questions/6148207/linear-regression-with-matplotlib-numpy

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [3,5,7,10] # 10, not 9, so the fit isn't perfect

#linear regression prediction
extended_range = list(range(0,20)) #extend line to 20
model = np.polyfit(x, y, 1)
predicted = np.polyval(model, extended_range)

#linear regression
fit = np.polyfit(x,y,1)
fit_fn = np.poly1d(fit)

plt.plot(x,y,'blue') #plot main data

plt.plot(extended_range, predicted) #plot linear regression prediction
plt.plot(x, fit_fn(x), color='red', linestyle='--') #plot linear regression


plt.show()
