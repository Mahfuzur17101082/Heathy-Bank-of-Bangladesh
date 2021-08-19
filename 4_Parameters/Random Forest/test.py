import pandas as pd
import random
from matplotlib import pyplot as plt

file = pd.ExcelFile('data.xlsx')
p = file.parse('AB Bank')

inp= [ 0, 0, 0, 0, 0]
row= [0, 1, 2, 3, 4]
pr=2016
dS=2009
dE=2015
for ye in range(0,3):
    countInc=0;
    countDec=0;
    for i in range (0,4):
        if((p[pr+ye][row[i]]-p[pr+ye-1][row[i]])>0):
            inp[i]=inp[i]+1
        else:
            inp[i]=inp[i]-1
    #print(inp)
    for xy in range(0,200):
        profitInc=0
        profitDec=0
        year=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        #print(random.choice(row))
        for x in range (0,5):
            for y in range (0,10):
                year[y]=random.randint(dS,dE+ye)
                
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
                year[y]=random.randint(dS,dE+ye)
                
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
           # print("Prediction: Profit Increase")
           countInc=countInc+1
        else:
            #print("Prediction: Profit Decrease")
            countDec=countDec+1
    print("///////  ",pr+ye,"  ///////")
    if(countInc>countDec):
       print("Prediction: Profit Increase")
       
    else:
        print("Prediction: Profit Decrease")
    print("Total Incerse: ", countInc)
    print("Total Decerse: ", countDec)
    
    
    
    if(p[pr+ye][5]-p[pr+ye-1][5]>0):
        print("True Value: Profit Increase")
    else:
        print("True Value: Profit Decrease")