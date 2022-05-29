
import pandas
import matplotlib.pyplot as plt
import scipy
from scipy import stats

d1 = pandas.read_excel("Температура.xlsx")
s = pandas.Series.dropna(d1["T"])
print(s)

print(stats.kstest(list(s), 'norm',(s.mean(), s.std())))
plt.show()
