import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use("classic")

filename = "temperature.xvg"

lines = open(filename, "r").readlines()
xlabel = lines[14][19:-2]
yunit = lines[15][19:-2]

newfilename = "new" + filename
file = open(newfilename, "w")
for line in lines:
    if line[0] != '#':
        file.write(line)
file.close()

df = np.loadtxt(newfilename, comments="@", unpack=True)
print(df)

plt.figure(facecolor='white')
plt.plot(df[0], df[1])
plt.grid()
plt.xlabel(xlabel)
plt.ylabel(filename[:-4].capitalize() + r" " + yunit + "")
plt.show()
