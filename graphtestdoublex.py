import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

N = 5
men_means = (20, 35, 30, 35, 27)
women_means = (25, 32, 34, 20, 25)
value_list = ['uoft', 'university of waterloo', 'university of british columbia', 'university of ottawa', 'mcmaster']

ind = np.arange(N)
width = 0.35
plt.bar(ind, men_means, width, label='Men')
plt.bar(ind + width, women_means, width,
    label='Women')

plt.ylabel('Scores')
plt.title('Scores by group and gender')

plt.xticks(ind + width / 2, value_list)
plt.legend(loc='best')
plt.show()

plt.bar(val_pos, chart_vals, color='green')
plt.xlabel("University Name")
plt.ylabel("Search Amount")
plt.title("What Canadian University has the most searches?")

plt.xticks(val_pos, value_list)

plt.show()
