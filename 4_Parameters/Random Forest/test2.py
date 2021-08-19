import pandas as pd
import random
from matplotlib import pyplot as plt

file = pd.ExcelFile('data.xlsx')
p = file.parse('Prime Bank')
countInc=0;
countDec=0;
inp= [ 0, 0, 0, 0]
row= [0, 1, 2, 4]
pr=2017
dS=2007
dE=2015
ye=0
#for ye in range(0,2):
for i in range (0,4):
    if((p[2018][row[i]]-p[2017][row[i]])>0):
        inp[i]=inp[i]+1
    else:
        inp[i]=inp[i]-1
#print(inp)

profitInc=0
profitDec=0
year=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#print(random.choice(row))
for x in range (0,5):
    for y in range (0,10):
        year[y]=random.randint(2006,2016)
        
    for i in range (0,5):
        pre1=random.choice(row)
        pre1index=row.index(pre1)
        pre2=random.choice(row)
        pre2index=row.index(pre2)
        if(inp[pre1index]>0 and inp[pre2index]>0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])>0 and (p[year[j]+1][pre2]-p[year[j]][pre2])>0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1


        elif(inp[pre1index]>0 and inp[pre2index]<0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])>0 and (p[year[j]+1][pre2]-p[year[j]][pre2])<0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1
                        
                        
        elif(inp[pre1index]<0 and inp[pre2index]<0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])<0 and (p[year[j]+1][pre2]-p[year[j]][pre2])<0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1
                        
                        
        elif(inp[pre1index]<0 and inp[pre2index]>0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])<0 and (p[year[j]+1][pre2]-p[year[j]][pre2])>0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1
                        
  
                      
for x in range (0,5):
    for y in range (0,10):
        year[y]=random.randint(2006,2015)
        
    for i in range (0,5):
        pre1=random.choice(row)
        pre1index=row.index(pre1)
        pre2=random.choice(row)
        pre2index=row.index(pre2)
        pre3=random.choice(row)
        pre3index=row.index(pre3)
        if(inp[pre1index]>0 and inp[pre2index]>0 and inp[pre3index]>0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])>0 and (p[year[j]+1][pre2]-p[year[j]][pre2])>0 and (p[year[j]+1][pre3]-p[year[j]][pre3])>0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1


        elif(inp[pre1index]>0 and inp[pre2index]>0 and inp[pre3index]<0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])>0 and (p[year[j]+1][pre2]-p[year[j]][pre2])>0 and (p[year[j]+1][pre3]-p[year[j]][pre3])<0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1
                        
                        
        elif(inp[pre1index]>0 and inp[pre2index]<0 and inp[pre3index]>0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])>0 and (p[year[j]+1][pre2]-p[year[j]][pre2])<0 and (p[year[j]+1][pre3]-p[year[j]][pre3])>0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1
                        
                        
        elif(inp[pre1index]>0 and inp[pre2index]<0 and inp[pre3index]<0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])>0 and (p[year[j]+1][pre2]-p[year[j]][pre2])<0 and (p[year[j]+1][pre3]-p[year[j]][pre3])<0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1
                        
        elif(inp[pre1index]<0 and inp[pre2index]>0 and inp[pre3index]>0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])<0 and (p[year[j]+1][pre2]-p[year[j]][pre2])>0 and (p[year[j]+1][pre3]-p[year[j]][pre3])>0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1
                        
                        
        elif(inp[pre1index]<0 and inp[pre2index]>0 and inp[pre3index]<0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])<0 and (p[year[j]+1][pre2]-p[year[j]][pre2])>0 and (p[year[j]+1][pre3]-p[year[j]][pre3])<0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1
                        
        elif(inp[pre1index]<0 and inp[pre2index]<0 and inp[pre3index]>0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])<0 and (p[year[j]+1][pre2]-p[year[j]][pre2])<0 and (p[year[j]+1][pre3]-p[year[j]][pre3])>0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1
                        
                        
        elif(inp[pre1index]<0 and inp[pre2index]<0 and inp[pre3index]<0):
            for j in range(0,10):
                if((p[year[j]+1][pre1]-p[year[j]][pre1])<0 and (p[year[j]+1][pre2]-p[year[j]][pre2])<0 and (p[year[j]+1][pre3]-p[year[j]][pre3])<0):
                    if((p[year[j]+1][5]-p[year[j]][5])>0):
                       profitInc= profitInc+1
                    else:
                        profitDec= profitDec+1

if(profitInc>profitDec):
  print("Prediction: Profit Increase")
   
else:
  print("Prediction: Profit Decrease")


if(p[2018][5]-p[2017][5]>0):
    print("True Value: Profit Increase")
else:
    print("True Value: Profit Decrease")
        





