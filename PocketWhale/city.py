import geocoder
import numpy as np
g = geocoder.ip('me')
print("chose option:")
print("1. city")
print("2. ip adress")
opt = input("")
if opt == "1":
    print("Write city you want to get weather forecast about")
    iu = input("")
    with open('City.txt', 'w') as f:
            f.write(iu)
if opt == "2":
    with open('City.txt', 'w') as f:
            f.write(g.city)
