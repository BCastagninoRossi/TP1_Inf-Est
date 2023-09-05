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



def testKSnormal(data, data_name):
    print("KOLPOGOROV-SMIRNOV: ")
    print(data_name)

    data_test = (data - np.mean(data))/np.std(data)

    ks = kstest(data_test, 'norm')
    print (f'KS_est: {ks.statistic} \np_value: {ks.pvalue}')
    if ks.pvalue < 0.05:
        print('Rechazada H_0: no es distrib normal (p < 0.05)')
    else:
        print('Aceptada H_0: se considera distrib normal (p > 0.05)')
    return ks

def testShapironormal(data, data_name):
    print("SHAPIRO ")
    print(data_name)
    # Shapiro - Wilks
    # Baja cantidad de muestras
    # se extrae media y varianza para adaptar al test.
    data_test = (data - np.mean(data))/np.std(data)
    
    sh = shapiro(data_test)
    print (f'Shapiro_est: {sh.statistic} \np_value: {sh.pvalue}')
    if sh.pvalue < 0.05:
        print('Rechazada H0: no es distrib normal (p < 0.05)')
    else:
        print('Aceptada H0: se considera distrib normal (p > 0.05)')
    return sh

testKSnormal(class1_len, "Class 1 Length")
testShapironormal(class1_len, "Class 1 Length")
testKSnormal(class2_len,"Class 2 Length" )
testShapironormal(class2_len,"Class 2 Length" )
testKSnormal(class1_wid, "Class 1 Width")
testShapironormal(class1_wid, "Class 1 Width")
testKSnormal(class2_wid, "Class 2 Width")
testShapironormal(class2_wid, "Class 2 Width")

