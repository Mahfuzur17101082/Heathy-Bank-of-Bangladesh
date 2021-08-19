import pandas as pd
from matplotlib import pyplot as plt

file = pd.ExcelFile('data.xlsx')

year=[ 2014, 2015, 2016, 2017, 2018]

prime = file.parse('Prime Bank')
dhaka = file.parse('Dhaka Bank')
bank = [prime, dhaka]
for c in range(0,2):
    for j in range(0, 14):
        x1=[0, 0, 0, 0, 0]
        for i in range(0, 5):
            x1[i]=bank[c][2014+i][j]
        x2=[0, 0, 0, 0, 0]
        for i in range(0, 5):
            x2[i]=bank[c][2014+i][14]
            
        if(c==0):
            print("Prime Bank")
        if(c==1):
            print("Dhaka Bank")    
        plt.plot(year, x1)
        plt.plot(year, x2)
        plt.xlabel("Year")
        plt.ylabel(prime['Name'][j])
        plt.legend([prime['Name'][j], 'NPL'])
        plt.show()
