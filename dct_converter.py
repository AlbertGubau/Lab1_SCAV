# This script can convert and decode an input using the DCT -- Albert Gubau -- NIA: 229416

import math

pi = 3.142857


# Function to find discrete cosine transform of an input matrix g_x_y
def dct_transform(g_x_y):

    # g_u_v will store the discrete cosine transform of g_x_y
    g_u_v = []

    m = len(g_x_y)  # Number of rows in g_x_y
    n = len(g_x_y[0])  # Number of columns g_x_y

    # Initialize g_u_v as a matrix of None values
    for i in range(m):
        g_u_v.append([None for _ in range(n)])

    for u in range(m):
        for v in range(n):

            # alpha_u and alpha_v depends on frequency as well as
            # number of row and columns of specified matrix
            if u == 0:
                alpha_u = 1 / (m ** 0.5)
            else:
                alpha_u = (2 / m) ** 0.5

            if v == 0:
                alpha_v = 1 / (n ** 0.5)
            else:
                alpha_v = (2 / n) ** 0.5

            # sums will temporarily store the sum of cosines present in the formula

            sums = 0
            for x in range(m):
                for y in range(n):
                    dct = g_x_y[x][y] * math.cos((2 * x + 1) * u * pi / (
                          2 * m)) * math.cos((2 * y + 1) * v * pi / (2 * n))
                    sums = sums + dct

            g_u_v[u][v] = alpha_u * alpha_v * sums   # Store the final result

    return g_u_v


# Test part (simulation of a white 8x8 picture)

gxy = [[255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255, 255, 255, 255, 255]]

guv = dct_transform(gxy)


# Print the result of the DCT

for i in range(len(guv)):
    for j in range(len(guv[0])):
        print(guv[i][j], end="\t")
    print()
