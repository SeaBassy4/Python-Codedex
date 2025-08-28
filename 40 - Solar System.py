from random import choice as ch
from math import pi

r = 0
planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn',
]

random_planet = ch(planets)

if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    print("oops :p , error")

area = 4 * pi * (r ** 2)

print(f"The planet {random_planet} has an approximate surface area of {area} km²")