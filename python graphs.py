import matplotlib.pyplot as plt
import numpy as np

categories = ["Marley", "Reagan", "Nadine", "Polly", "Judah", "Caden", "Cohen", "Lila", "Rachel", "Jack", "Claire"]
sets = [[7, 3, 3, 1, 2, 1, 3, 2, 1, 0, 1]]
dates = ["5/14/23"]

width = 0.8 / len(sets)  # Width of each bar group
x = np.arange(len(categories))  # Generate an array of the category indices

for i, set_values in enumerate(sets):
    offset = (i - len(sets) / 2 + 0.5) * width  # Calculate the offset for each set
    plt.bar(x + offset, set_values, width=width, label=dates[i])

plt.xlabel('Names')
plt.ylabel('Times Appeared')
plt.title('Friends in Marley\'s photos')
plt.legend()

plt.xticks(x, categories)  # Set the x-axis tick labels to the categories

plt.show()
