import os
import glob
import random

files = glob.glob("*.png")
i = 0
length = len(files) 
x = random.sample(range(0,length),length)
print x
print "length of x  {}".format(len(x))
for file in files:
    os.rename(file, "{}.png".format(x[i]))
    i = i + 1
