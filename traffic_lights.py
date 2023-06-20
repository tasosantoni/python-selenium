""" This is a traffic lights simulation."""

import time
from itertools import cycle

lights = [('Green', 2), ('Yellow', 1), ('Red', 2)]
colors = cycle(lights)

timeout = 21
time_start = time.time()

while time.time() < time_start + timeout:
    c,s = next(colors)
    print(c)
    time.sleep(s)

