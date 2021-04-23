import matplotlib.pyplot as plt
city = ["Maha", "Guj", "TN", "Del", "UP", "MP", "Bh"]
cases = [33053, 11379, 11224, 10054, 5202, 4977, 1262]
plt.bar(city,cases,color=["r","orange","b","k","y","g","g"])
plt.xlabel("City infected by COVID-19")
plt.ylabel("Cases of COVID-19")
plt.show()
