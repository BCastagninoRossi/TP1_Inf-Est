
import numpy as np
from scipy.stats import kstest, shapiro


c1_length = []
c1_width = []
c2_length = []
c2_width = []
file = "hojas_inferencia.csv"
with open(file, "r") as hojas: # appends the leafs' lengths and widths to their corresponding lists
    for line in hojas.readlines():
        values = line.split(',')
        if values[0] == "1":
            c1_length.append(int(values[1]))
            c1_width.append(int(values[2]))
        elif values[0] == "2":
            c2_length.append(int(values[1]))
            c2_width.append(int(values[2]))

class1_len = np.array(c1_length)
class2_len = np.array(c2_length)
class1_wid = np.array(c1_width)
class2_wid = np.array(c2_width)


# def cuantizacion( data, steps = 20):
#     """
#     Cuantización del vector <data> en <steps> niveles.
#     """
#     if steps < 2:
#         steps = 2
#     bins = np.arange(0.0,1.0+(1/steps), 1/steps)
#     bins = (np.max(data)-np.min(data))*bins + np.min(data) #determina los límites de cada bin-
#     bins = bins[1:-1]
#     return np.digitize(data,bins)

# print(class1_len)
# print(cuantizacion(class1_len))