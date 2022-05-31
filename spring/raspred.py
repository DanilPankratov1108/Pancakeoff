
import pandas
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
from scipy import stats

d1 = pandas.read_excel("temperature.xlsx")
s = pandas.Series.dropna(d1["T"])
print(s)
print(stats.kstest(list(s), 'norm',(s.mean(), s.std())))
sns.histplot(s)
plt.show()
