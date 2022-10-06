# This script changes from RGB color space to YUV and vice-versa -- Albert Gubau -- NIA: 229416

def rgb_to_yuv(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = -0.169 * r - 0.331 * g + 0.499 * b + 128
    v = 0.499 * r - 0.418 * g - 0.0813 * b + 128

    return y, u, v


def yuv_to_rgb(y, u, v):
    r = 1.164 * (y - 16) + 2.018 * (u - 128)
    g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
    b = 1.164 * (y - 16) + 1.596 * (v - 128)

    return r, g, b


try:
    option = int(input("What do you want to convert? (1 --> RGB to YUV), (2 --> YUV to RGB):  "))

except ValueError as E:
    print("Incorrect value, exiting program...")
    option = 0

if option == 1:
    R = float(input("Choose the RED component: "))
    G = float(input("Choose the GREEN component: "))
    B = float(input("Choose the BLUE component: "))
    Y, U, V = rgb_to_yuv(R, G, B)
    print("The YUV result is: ", round(Y, 3), ", ", round(U, 3), ", ", round(V, 3))

if option == 2:
    Y = float(input("Choose the Y component: "))
    U = float(input("Choose the U component: "))
    V = float(input("Choose the V component: "))
    R, G, B = rgb_to_yuv(Y, U, V)
    print("The RGB result is: ", round(R, 3), ", ", round(G, 3), ", ", round(B, 3))
