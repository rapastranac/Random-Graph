# load libraries
import numpy as np
from numpy.random import seed
from numpy.random import rand
#from rdoclient_py3 import RandomOrgClient

#seed = RandomOrgClient(key1)
#r = seed.generate_decimal_fractions(2, 4)


def getrndgraph(n, p):
    g = np.zeros([n, n], dtype=int)
    seed(1)

    for i in range(0, n):
        for j in range(i + 1, n):
            r = rand()
            if r <= p:
                g[i][j] = 1
                g[j][i] = 1
    print(g)
    return g


def printfile(g, n):
    file = open("graph.txt", "w")
    for i in range(0, n):
        file.write("%s\t" % i)
        for j in range(0, n):
            if g[i][j] == 1:
                file.write("%s\t" % j)
        file.write(str('\n'))


def main():
    n = 70
    #p = 4 / n
    p = 0.04
    g = getrndgraph(n, p)
    printfile(g, n)


main()
