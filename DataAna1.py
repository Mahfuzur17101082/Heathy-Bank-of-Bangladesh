#import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file = pd.ExcelFile('data.xlsx')

year=[ 2014, 2015, 2016, 2017, 2018]

prime = file.parse('Prime Bank')
dhaka = file.parse('Dhaka Bank')
mtb = file.parse('MTB')

for j in range(0, 14):
    x1=[0, 0, 0, 0, 0]
    for i in range(0, 5):
        x1[i]=prime[2014+i][j]


    x2=[0, 0, 0, 0, 0]
    for i in range(0, 5):
        x2[i]=dhaka[2014+i][j]
    
    x3=[0, 0, 0, 0, 0]
    for i in range(0, 5):
        x3[i]=mtb[2014+i][j]
    
    
    plt.plot(year, x1)
    plt.plot(year, x2)
    plt.plot(year, x3)
    plt.xlabel("Year")
    plt.ylabel(prime['Name'][j])
    plt.legend(["Prime Bank", "Dhaka Bank", "MTB"])
    plt.show()
    
    
    
