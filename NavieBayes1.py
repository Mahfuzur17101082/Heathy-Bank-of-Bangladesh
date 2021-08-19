import pandas as pd
from matplotlib import pyplot as plt

file = pd.ExcelFile('data.xlsx')

#city = file.parse('City Bank')
#prime = file.parse('Prime Bank')
#dhaka = file.parse('Dhaka Bank')
#mtb = file.parse('MTB')
ab = file.parse('AB Bank')
zero=[ 0, 0, 0, 0, 0, 0, 0, 0]
#bank = [city, prime, dhaka, mtb, ab]
#name = ["City Bank", "Prime Bank", "Dhaka Bank", "MTB", "AB Bank"]
parameter = ["Paid-up capital", "Deposits", "Loans and advances","Investments", "Total assets", "Import", "Export", "NPL %", "Profit"]


row= [1, 3, 4, 5, 8, 10, 11, 15]
inp= [ 0, 0, 0, 0, 0, 0, 0, 0]
proOfInput=[ 0, 0, 0, 0, 0, 0, 0, 0]
for i in range (0,8):
    if((ab[2018][row[i]]-ab[2017][row[i]])>0):
        inp[i]=inp[i]+1
    else:
        inp[i]=inp[i]-1

#print(inp)
proInc=0
proDec=0

sameSeen4Inc = [ 0, 0, 0, 0, 0, 0, 0, 0]
sameSeen4Dec = [ 0, 0, 0, 0, 0, 0, 0, 0]

for i in range (0,8):
    if((ab[2010+i][16]-ab[2009+i][16])>0):
        proInc=proInc+1
        for j in range (0,8):
            if(inp[j]>0):
                if((ab[2010+i][row[j]]-ab[2009+i][row[j]])>0):
                   sameSeen4Inc[j]= sameSeen4Inc[j]+1
            else:
                if((ab[2010+i][row[j]]-ab[2009+i][row[j]])<0):
                    sameSeen4Inc[j]= sameSeen4Inc[j]+1
    else:
        proDec=proDec+1
        for j in range (0,8):
            if(inp[j]>0):
                if((ab[2010+i][row[j]]-ab[2009+i][row[j]])>0):
                   sameSeen4Inc[j]= sameSeen4Inc[j]+1
            else:
                if((ab[2010+i][row[j]]-ab[2009+i][row[j]])<0):
                    sameSeen4Dec[j]= sameSeen4Dec[j]+1

probaProInc=proInc/8
probaProDec=proDec/8
#print(probaProInc)
#print(probaProDec)
#print(sameSeen4Inc)
#print(sameSeen4Dec)


for i in range (0, 8):
    sameSeen4Inc[i]=sameSeen4Inc[i]/proInc
    sameSeen4Dec[i]=sameSeen4Dec[i]/proDec
    
#print(sameSeen4Inc)
#print(sameSeen4Dec)
inc=1
dec=1
    
for i in range (0,8):
    if(sameSeen4Inc[i]!=0 and sameSeen4Dec[i]!=0):
        inc=inc*sameSeen4Inc[i]
        dec=dec*sameSeen4Dec[i]
    else:
        zero[i]=1
inc=inc*probaProInc
dec=dec*probaProDec
#print(inc)
#print(dec)
for i in range (0,8):
        for j in range (0,8):
            #if(j!=1):
                if(inp[i]>0):
                    if((ab[2010+j][row[i]]-ab[2009+j][row[i]])>0):
                       proOfInput[i]=proOfInput[i]+1
                else:
                    if((ab[2010+j][row[i]]-ab[2009+j][row[i]])<0):
                        proOfInput[i]= proOfInput[i]+1
                    

for i in range (0,8):
    proOfInput[i]= proOfInput[i]/8
#print(proOfInput)
    
pOI=1
for i in range (0,8):
    if(zero[i]==0):
        pOI= proOfInput[i]*pOI
    
#print(pOI)  
#print("Probability of Profit Increase: ")
print(inc/pOI)

#print("Probability of Profit Decrease: ")
print(dec/pOI)
