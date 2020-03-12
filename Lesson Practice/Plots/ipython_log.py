# IPython log file

import pandas as pd
get_ipython().run_line_magic('logstart', '')
pd.read.cvs("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")
pd.read.csv("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")
pd.read_csv("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")
df = pd.read_csv("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")
df["erruptions"]
df
df["erruptions"]
df["eruptions"]
df["waiting"]
import matplotlip.pyplot as plt
import matplotlib.pyplot as plt
plt.plot(df["eruptions"],df["waiting"], "b.")
plt.hist(df["eruptions"])
plt.savefig("hist.png")
plt.hist(df["eruptions"])
plt.savefig("hist.png")
quit()
