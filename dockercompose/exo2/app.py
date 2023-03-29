import math

import time

n = 10000

values = []

for i in range(n):

     a = min(i, 2000)

     b = math.exp(10/(n *0.001 + 10)) + math.cos(n)

     values.append(b)

     values.append("coucou")

     time.sleep(0.001)
