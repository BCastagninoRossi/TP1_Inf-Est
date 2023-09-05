import matplotlib.pyplot as plt
import numpy as np

def generate_hist(file):

    c1_length = []
    c1_width = []
    c2_length = []
    c2_width = []

    with open(file, "r") as hojas: # appends the leafs' lengths and widths to their corresponding lists
        for line in hojas.readlines():
            values = line.split(',')
            if values[0] == "1":
                c1_length.append(int(values[1]))
                c1_width.append(int(values[2]))
            elif values[0] == "2":
                c2_length.append(int(values[1]))
                c2_width.append(int(values[2]))

    hist_c1_length = plt.hist(np.array(c1_length), bins=10)
    hist_c1_width = plt.hist(np.array(c1_width), bins=10)
    hist_c2_length = plt.hist(np.array(c2_length), bins=10)
    hist_c2_length = plt.hist(np.array(c2_length), bins=10)

    plt.title("Histograma")
    plt.xlabel("Largo")
    plt.ylabel("Frecuencia")
    plt.show()

print(generate_hist("hojas_inferencia.csv"))
