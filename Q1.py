# Import libraries
import matplotlib.pyplot as plt
import numpy as np
group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15,40,45,50,62]
group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]
#Box plot of GroupA data
plt.boxplot(group_A)
plt.title("Group A")
plt.ylabel("Data")
plt.show()
#Box plot of GroupB data
plt.boxplot(group_B)
plt.title("Group B")
plt.ylabel("Data")
plt.show()
