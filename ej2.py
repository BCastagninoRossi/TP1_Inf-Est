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
    hists.append((c1_length, c1_width, c2_length, c2_width))
    h_type.append((("largo", "1"), ("ancho", "1"), ("largo", "2"), ("ancho", "2"), ("largo y ancho", "1"), ("largo y ancho", "2")))

    return hists, h_type

def plot_hists(hists, h_type, bins):
    
    for i in range(len(hists)):

        plt.hist(np.array(hists[i]), bins=bins)
        plt.title(f"Histograma del {h_type[0][i][0]} de las hojas de clase {h_type[0][i][1]}")
        plt.xlabel(f"{h_type[0][0]}".capitalize())
        plt.ylabel("Frecuencia")
        plt.show()

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax2 = fig.add_subplot(111, projection='3d')
    
    hist_c1, c1_l_edges, c1_w_edges = np.histogram2d(hists[0][0], hists[0][1], bins=(bins, bins))
    hist_c2, c2_l_edges, c2_w_edges = np.histogram2d(hists[0][2], hists[0][3], bins=(bins, bins))
    frequency_c1 = hist_c1.ravel()
    frequency_c2 = hist_c2.ravel()
    hist_c1 = np.histogram2d(hists[0][0], hists[0][1], bins=bins, weights=frequency_c1)
    hist_c2 = np.histogram2d(hists[0][2], hists[0][3], bins=bins, weights=frequency_c2)

    c1_l_midpoints = (c1_l_edges[:-1] + c1_l_edges[1:]) / 2
    c1_w_midpoints = (c1_w_edges[:-1] + c1_w_edges[1:]) / 2
    c2_l_midpoints = (c2_l_edges[:-1] + c2_l_edges[1:]) / 2
    c2_w_midpoints = (c2_w_edges[:-1] + c2_w_edges[1:]) / 2

    c1_l_mesh, c1_w_mesh = np.meshgrid(c1_l_midpoints, c1_w_midpoints)
    c2_l_mesh, c2_w_mesh = np.meshgrid(c2_l_midpoints, c2_w_midpoints)

    ax1.bar3d(c1_l_mesh.ravel(), c1_w_mesh.ravel(), 0, 1, 1, frequency_c1, shade=True)
    ax2.bar3d(c2_l_mesh.ravel(), c2_w_mesh.ravel(), 0, 1, 1, frequency_c2, shade=True)

    ax1.set_xlabel('Largo')
    ax1.set_ylabel('Ancho')
    ax1.set_zlabel('Frecuencia')
    ax1.set_title('Histograma del largo y ancho de las hojas de clase C1')

    ax2.set_xlabel('Largo')
    ax2.set_ylabel('Ancho')
    ax2.set_zlabel('Frecuencia')
    ax2.set_title('Histograma del largo y ancho de las hojas de clase C2')

hists, h_type = generate_hists("hojas_inferencia.csv")
plot_hists(hists, h_type, 10)
