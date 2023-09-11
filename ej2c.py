
import numpy as np
import scipy.stats as stats
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


def cuantizacion( data, steps = 20):
    """
    Cuantización del vector <data> en <steps> niveles.
    """
    if steps < 2:
        steps = 2
    bins = np.arange(0.0,1.0+(1/steps), 1/steps)
    bins = (np.max(data)-np.min(data))*bins + np.min(data) #determina los límites de cada bin-
    bins = bins[1:-1]
    return np.digitize(data,bins)

print(class1_len)
print(cuantizacion(class1_len))

cuant_1_len = cuantizacion(class1_len, steps=10)
cuant_1_wid = cuantizacion(class1_wid, steps=10)
cuant_2_len = cuantizacion(class2_len, steps=10)
cuant_2_wid = cuantizacion(class2_wid, steps=10)

# print(f'x: \n {cuan}')
# print(f'norm_x: \n {cuant_1_len}')
# print(f'y: \n {y}')
# print(f'norm_y: \n {cuant_1_wid}')

table = stats.contingency.crosstab(cuant_1_len, cuant_1_wid)
st = stats.chi2_contingency(table[1])
print(f'p:{st[1]}')
print(f'rango_x: {table[0][0]}')
print(f'rango_y: {table[0][1]}')
print(f'frecuencias:\n {table[1]}')
if st[1] > 0.05:
    print(f'Se acepta H0(independencia). st: {st[0]}, p: {st[1]}')
else:
    print(f'Se rechaza H0, st: {st[0]}, p: {st[1]}')
print('\n')

table = stats.contingency.crosstab(cuant_2_len, cuant_2_wid)
st = stats.chi2_contingency(table[1])
print(f'p:{st[1]}')
print(f'rango_x: {table[0][0]}')
print(f'rango_y: {table[0][1]}')
print(f'frecuencias:\n {table[1]}')
if st[1] > 0.05:
    print(f'Se acepta H0(independencia). st: {st[0]}, p: {st[1]}')
else:
    print(f'Se rechaza H0, st: {st[0]}, p: {st[1]}')
print('\n')