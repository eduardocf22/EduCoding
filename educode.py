# Open a file

#file = open ("/home/ecastillo/Downloads/seaslug.txt", mode = "r")

# print import
#print (file.read())

# check whether file is closed
#print (file.closed)

# Close file
#file.close()

# check whether file is closed
#print (file.closed)


#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib as pyplot
#import sys
#print (sys.path)



#file = "/home/ecastillo/Downloads/seaslug.txt"

#data = np.loadtxt ("/home/ecastillo/Downloads/seaslug.txt", delimiter='\t', dtype=str)

#print(data[0])

#data_float = np.loadtxt("/home/ecastillo/Downloads/seaslug.txt", delimiter="\t", dtype=float, skiprows=1)

#print (data[10])

#plt.scatter(data_float[:, 0], data_float[:, 1])
#plt.xlabel('time (min.)')
#plt.ylabel('percentage of larvae')
#plt.show()


#data = np.genfromtxt('/home/ecastillo/Downloads/titanic.csv', delimiter=',', names=True, dtype=None)
#print (data["Fare"])
#print (data["Survived"])

file = "/home/ecastillo/Downloads/titanic.csv"
d= np.recfromcsv(file)
print(d[:3])


import pandas as pd
filename= "winequality-red.csv"
data= pd.read_csv(filename)
data.head(n)


