# Queremos ver si las varianzas de los anchos de las clases c1 y c2 son estables. Podemos verlo mediante el test de homocedasticidad
# Si son estables, podemos comparar las medias de los anchos de las hojas con el test de t-student
#IMPORTANTE: EL ZTEST SOLO SE PUEDE HACER PORQUE LA SUMA DE LA CANTIDAD DE MUESTRAS ES MAYOR A 30


import numpy as np
import scipy.stats as stats

def get_widths(file):

    c1_width = []
    c2_width = []

    with open(file, "r") as hojas: # appends the leafs' lengths and widths to their corresponding lists
        for line in hojas.readlines():
            values = line.split(',')
            if values[0] == "1":
                c1_width.append(int(values[2]))
            elif values[0] == "2":
                c2_width.append(int(values[2]))
    return c1_width, c2_width

def variance_test(samples): #H0 is the hypothesis that the variances of rv1 and rv2 are the same

    group1 = samples[:int(len(samples)/2)]
    group2 = samples[int(len(samples)/2):]

    statistic = np.var(group1, ddof=1)/np.var(group2, ddof=1)
    print(statistic)
    p = 1 - stats.f.cdf(statistic, len(group1) - 1, len(group2) - 1)

    if p > 0.05:
        print(f"\nH0 can't be refuted, as the value of p is {p} \n")
    elif p < 0.05:
        print(f"\nH0 is refuted, as the value of p is {p} \n")

    return p

# def variance_test(c1, c2): #H0 is the hypothesis that the variances of rv1 and rv2 are the same

#     group1 = c1[:222]
#     group2 = c2

#     statistic = np.var(group1, ddof=1)/np.var(group2, ddof=1)
#     statistic = (np.std(group1)/np.std(group2))**2
#     p = 1 - stats.f.cdf(statistic, len(group1) - 1, len(group2) - 1)

#     if p > 0.05:
#         print(f"\nH0 can't be refuted, as the value of p is {p} \n")
#     elif p < 0.05:
#         print(f"\nH0 is refuted, as the value of p is {p} \n")

#     return p

c1_width, c2_width = get_widths("hojas_inferencia.csv")

def two_sample_t_test(group1, group2):
    
    # stdp = np.sqrt(((len(group1) - 1) * np.var(group1) + (len(group2) - 1) * np.var(group2)) / (len(group1) + len(group2) - 2))
    
    # statistic = (np.mean(group1)-np.mean(group2)) / (stdp*(np.sqrt((1/len(group1)) + (1/len(group2)))))

    # if statistic < 0:
    #     p = 2 * stats.norm.cdf(statistic)
    # else:
    #     p = 2 * (1 - stats.norm.cdf(statistic))

    group1 = np.random.choice(group1, 50)
    group2 = np.random.choice(group2, 50)
    n1 = len(group1)
    n2 = len(group2)

    sp = np.sqrt(((n1-1)*np.var(group1) + (n2-1)*np.var(group2)) / (n1+n2-2))
    nn = np.sqrt(1/len(group1)+1/len(group2))
    # z-test (normal) de una muestra
    z = (np.mean(group1)-np.mean(group2))/(sp*nn)
    print(z)
    if z<0:
        p = 2*stats.norm.cdf(z)
    else:
        p = 2*(1-stats.norm.cdf(z))

    if p < 0.05:
        print(f"\nH0 is rejected, as the value of p is {p}\n")
    elif p > 0.05:
        print(f"\nH0 can't be rejected, as the value of p is {p}")

    return p


# variance_test(c1_width, c2_width)
variance_test(c1_width)
variance_test(c2_width)
two_sample_t_test(c1_width, c2_width)