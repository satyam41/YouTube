import matplotlib.pyplot as plt
cases = [33053, 11379, 11224, 10054, 5202, 4977, 1262]
death = [1198, 659, 78, 160, 131, 248, 8]
plt.plot(cases, "r", death, "k")  #k and r is code of colours.
plt.legend(["Corona Cases", "Death rate"])
plt.xlabel("Corona cases in the city")
plt.ylabel("Death Rating in the city")
plt.show()
