import matplotlib.pyplot as plt
import numpy as np

def generate_hists(file):

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

    h_type = []
    hists = []

    hist_c1_length = plt.hist(np.array(c1_length), bins=10)
    hist_c1_width = plt.hist(np.array(c1_width), bins=10)
    hist_c2_length = plt.hist(np.array(c2_length), bins=10)
    hist_c2_width = plt.hist(np.array(c2_width), bins=10)
    hist_c1 = plt.hist(np.array(np.array(c1_length), np.array(c1_width)))
    hist_c2 = plt.hist(np.array(np.array(c2_length), np.array(c2_width)))

    hists.append(hist_c1_length, hist_c1_width, hist_c2_length, hist_c2_width, hist_c1, hist_c2)
    h_type.append(("largo", "1"), ("ancho", "1"), ("largo", "2"), ("ancho", "2"), ("largo y ancho", "1"), ("largo y ancho", "2"))

    return hists, h_type

def plot_hists(hists, h_type):
    for i in range(len(hists)):
        plt.title(f"Histograma del {h_type[i][0]} de las hojas de clase {h_type[i][1]}")
        plt.xlablel(f"{h_type[0]}".capitalize())
        plt.ylabel("Frecuencias")
        plt.show()

hists, h_type = generate_hists("hojas_inferencia.csv")
plot_hists(hists, h_type)
