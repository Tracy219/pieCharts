#!/usr/bin/env python

import matplotlib
matplotlib.use("agg") # the code 'import matplotlib.pyplot as plt' must come out after 
# import matplotlib and matplotlib.use("agg")

import matplotlib.pyplot as plt


labels = 'Reading', 'Sleeping', 'Others', 'Chatting' # Labels of the parts of the pie chart
sizes = [15, 30.0, 45.0, 10] # Sizes of the parts of the carts
colors = ['yellowgreen', 'gold', 'lightskyblue', 'red'] # Colors of the parts of the carts
explode = (0, 0.1, 0, 0) # Explode means separate from the the graph, the numbers are the 
# distance of the part(s) from the main part

plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%0.1f%%', \
shadow = True) # sizes, explode(separate), labels, colors and autopct(can show the percent 
# of each part in the pie chart, '0.1' means the number will be the form xx.x(45.0))

plt.axis('equal') # x-axis and y-axis equals in this case, if x-axis is not equal to 
# y-axis, the form will be plt.axis(a, b, c, d)('a' for min of x-axis, 'b' for max of 
# x-axis, 'c' for min of y-axis, 'd' for max of x-axis)


plt.show()
plt.savefig("pieChartsExample.png")