import pandas as pd
from matplotlib import pyplot as plt

file = pd.ExcelFile('dt.xlsx')

ab = file.parse('Prime Bank')
zero=[ 0, 0, 0, 0, 0]

parameter = ["Deposits", "Loans and advances","Investments", "NPA",  "NPL %", "Profit"]


row= [0, 1, 2, 3, 4]
inp= [ 0, 0, 0, 0, 0]
proOfInput=[ 0, 0, 0, 0, 0]
for i in range (0,5):
    if((ab[2016][row[i]]-ab[2015][row[i]])>0):
        inp[i]=inp[i]+1
    else:
        inp[i]=inp[i]-1

proInc=0
proDec=0

sameSeen4Inc = [ 0, 0, 0, 0, 0]
sameSeen4Dec = [ 0, 0, 0, 0, 0]

for i in range (0,9):
    if((ab[2007+i][5]-ab[2006+i][5])>0):
        proInc=proInc+1
        for j in range (0,5):
            if(inp[j]>0):
                if((ab[2007+i][row[j]]-ab[2006+i][row[j]])>0):
                   sameSeen4Inc[j]= sameSeen4Inc[j]+1
            else:
                if((ab[2007+i][row[j]]-ab[2006+i][row[j]])<0):
                    sameSeen4Inc[j]= sameSeen4Inc[j]+1
    else:
        proDec=proDec+1
        for j in range (0,5):
            if(inp[j]>0):
                if((ab[2007+i][row[j]]-ab[2006+i][row[j]])>0):
                   sameSeen4Inc[j]= sameSeen4Inc[j]+1
            else:
                if((ab[2007+i][row[j]]-ab[2006+i][row[j]])<0):
                    sameSeen4Dec[j]= sameSeen4Dec[j]+1

probaProInc=proInc/9
probaProDec=proDec/9


for i in range (0, 5):
    sameSeen4Inc[i]=sameSeen4Inc[i]/proInc
    sameSeen4Dec[i]=sameSeen4Dec[i]/proDec

#print(sameSeen4Inc)
#print(sameSeen4Dec)  

inc=1
dec=1


for i in range (0,5):
    if(sameSeen4Inc[i]!=0 and sameSeen4Dec[i]!=0):
        inc=inc*sameSeen4Inc[i]
        dec=dec*sameSeen4Dec[i]
    else:
        zero[i]=1

inc=inc*probaProInc
dec=dec*probaProDec
#print(inc)
#print(dec)


for i in range (0,5):
        for j in range (0,9):
            #if(j!=1):
                if(inp[i]>0):
                    if((ab[2007+j][row[i]]-ab[2006+j][row[i]])>0):
                       proOfInput[i]=proOfInput[i]+1
                else:
                    if((ab[2007+j][row[i]]-ab[2006+j][row[i]])<0):
                        proOfInput[i]= proOfInput[i]+1
                    

for i in range (0,5):
    proOfInput[i]= proOfInput[i]/9

#print(proOfInput)

pOI=1
for i in range (0,5):
    if(zero[i]==0):
        pOI= proOfInput[i]*pOI


#print(pOI)       
print("Probability of Profit increase:", inc/pOI)
print("Probability of Profit decrease:",dec/pOI)

if(ab[2016][5]-ab[2015][5]>0):
    print("True Value: Profit Increase")
else:
    print("True Value: Profit Decrease")
