# This script changes from RGB color space to YUV and vice-versa

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
except:
    print("Incorrect value, exiting program...")
    option = 0

if option == 1:
    r = float(input("Choose the RED component: "))
    g = float(input("Choose the GREEN component: "))
    b = float(input("Choose the BLUE component: "))
    y, u, v = rgb_to_yuv(r, g, b)
    print("The YUV result is: ", round(y, 3), ", ", round(u, 3), ", ", round(v, 3))

if option == 2:
    y = float(input("Choose the Y component: "))
    u = float(input("Choose the U component: "))
    v = float(input("Choose the V component: "))
    r, g, b = rgb_to_yuv(y, u, v)
    print("The RGB result is: ", round(r, 3), ", ", round(g, 3), ", ", round(b, 3))


