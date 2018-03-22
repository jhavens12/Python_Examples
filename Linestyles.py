#https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]
y2 = [6,7,8,9,10]
y3 = [11,12,13,14,15]
y4 = [16,17,18,19,20]


lw = 3
#plt.plot(x,y, 'yo', x, fit_fn(x), '--k') #from example
plt.plot(x,y,color='blue', label=':', linestyle=':', linewidth=lw) #me
plt.plot(x,y2,color='red', label='--', linestyle='--', linewidth=lw)
plt.plot(x,y3,color='green',label='-.', linestyle='-.', linewidth=lw)
plt.plot(x,y4,color='black', label='-',linestyle='-', linewidth=lw)
plt.legend()

plt.show()
