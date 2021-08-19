import pandas as pd
from matplotlib import pyplot as plt

file = pd.ExcelFile('data.xlsx')

ab = file.parse('Prime Bank')
parameter = [ "Deposits","Loabs and Advences", "Investments",  "NPL %", "Profit"]
row= [3, 4, 5, 15]
inp= [ 0, 0, 0, 0]
zero=[0, 0, 0, 0]
proOfInput=[ 0, 0, 0, 0]
for i in range (0,4):
    if((ab[2018][row[i]]-ab[2017][row[i]])>0):
        inp[i]=inp[i]+1
    else:
        inp[i]=inp[i]-1
        
#print(inp)

proInc=0
proDec=0

sameSeen4Inc = [ 0, 0, 0, 0]
sameSeen4Dec = [ 0, 0, 0, 0]

for i in range (0,3):
    if((ab[2015+i][16]-ab[2014+i][16])>0):
        proInc=proInc+1
        for j in range (0,4):
            if(inp[j]>0):
                if((ab[2015+i][row[j]]-ab[2014+i][row[j]])>0):
                   sameSeen4Inc[j]= sameSeen4Inc[j]+1
            else:
                if((ab[2015+i][row[j]]-ab[2014+i][row[j]])<0):
                    sameSeen4Inc[j]= sameSeen4Inc[j]+1
    else:
        proDec=proDec+1
        for j in range (0,4):
            if(inp[j]>0):
                if((ab[2015+i][row[j]]-ab[2014+i][row[j]])>0):
                   sameSeen4Dec[j]= sameSeen4Dec[j]+1
            else:
                if((ab[2015+i][row[j]]-ab[2014+i][row[j]])<0):
                    sameSeen4Dec[j]= sameSeen4Dec[j]+1

#print(proInc)
#print(proDec)
#print(sameSeen4Inc)
#print(sameSeen4Dec)


probaProInc=proInc/3
probaProDec=proDec/3

for i in range (0, 4):
    sameSeen4Inc[i]=sameSeen4Inc[i]/proInc
    sameSeen4Dec[i]=sameSeen4Dec[i]/proDec
#print(probaProInc)
#print(probaProDec)
#print(sameSeen4Inc)
#print(sameSeen4Dec)
inc=1
dec=1    
for i in range (0,4):
    if(sameSeen4Inc[i]!=0 and sameSeen4Dec[i]!=0):
        inc=inc*sameSeen4Inc[i]
        dec=dec*sameSeen4Dec[i]
    else:
        zero[i]=1
    

inc=inc*probaProInc
dec=dec*probaProDec

#print(inc)
#print(dec)

for i in range (0,4):
        for j in range (0,3):
                if(inp[i]>0):
                    if((ab[2015+j][row[i]]-ab[2014+j][row[i]])>0):
                       proOfInput[i]=proOfInput[i]+1
                else:
                    if((ab[2015+j][row[i]]-ab[2014+j][row[i]])<0):
                        proOfInput[i]= proOfInput[i]+1
                        
                        
#print(proOfInput)
for i in range (0,4):
    proOfInput[i]= proOfInput[i]/3
#print(proOfInput)

pOI=1
for i in range (0,4):
    if(zero[i]==0):
        pOI= proOfInput[i]*pOI
#print(pOI)
        
print(inc/pOI)
print(dec/pOI)