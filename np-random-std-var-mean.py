import numpy
import random

#random vs  numpy.random https://stackoverflow.com/questions/7029993/differences-between-numpy-random-and-random-random-in-python
#random and numpy.random are not the same and the .seed does not affect the other
rand = random.random()
print(rand)
random.seed(rand)


nrand = numpy.random.randint(1, high=100)
print(nrand)
numpy.random.seed(nrand)  #is not thread-safe
#numpy.random.seed(10)

# Do this for random (new version)
from numpy.random import default_rng
rng = default_rng()
vals = rng.standard_normal(10)
more_vals = rng.standard_normal(10)



ran = numpy.random.randint(995, high=1005, size=14, dtype=int)
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86, 1000]

xbar = numpy.mean(speed)
x = numpy.median(speed)
s = numpy.std(speed)
v = numpy.var(speed)

rxbar = numpy.mean(ran)
rx = numpy.median(ran)
rs = numpy.std(ran)
rv = numpy.var(ran)

print(f'mean: {xbar} std: {s} var: {v}')
print(f'mean: {rxbar} std: {rs} var: {rv} list: {ran}')
#print(x, xbar, s)


#speed = [99,86,87,88,111,86,103,87,94,78,77,85,86, 86, 86, 86, 86]
#mean: 88.88235294117646 std: 8.252503028074193

#speed = [99,86,87,88,111,86,103,87,94,78,77,85,86, 1000]
#mean: 154.78571428571428 std: 234.58997012155626