import pandas as pd
from matplotlib import pyplot as plt

file = pd.ExcelFile('NPL Data.xlsx')

year=[ 2014, 2015, 2016, 2017, 2018]
city = file.parse('City Bank')
prime = file.parse('Prime Bank')
dhaka = file.parse('Dhaka Bank')
dbbl = file.parse('DBBL')
asia = file.parse('Bank Asia')
brac = file.parse('BRAC')
bcbl = file.parse('BCBL')
nrb = file.parse('NRB')
ab = file.parse('AB Bank')
ific = file.parse('IFIC')
ebl = file.parse('EBL')
jonota = file.parse('Jonota Bank')
jomuna = file.parse('Jomuna Bank')

sameBank=" "
reverseBank=" "
neutral=" "
bank = [city, prime, dhaka, dbbl, asia, jonota, jomuna, ebl, bcbl, brac, ific, ab, nrb]
name = ["City Bank", "Prime Bank", "Dhaka Bank", "DBBL", "Bank Asia", "Jonota Bank", "Jomuna Bank", "EBL", "BCBL", "BRAC Bank", "IFIC", "AB Bank", "NRB"]
reverse=0;
same=0;
case=0;
for c in range(0,13):
    
        x1=[0, 0, 0, 0, 0]
        for i in range(0, 5):
            x1[i]=bank[c][2014+i][0]
            
            
       #x2=[0, 0, 0, 0, 0]
       # for i in range(0, 5):
       #     x2[i]=bank[c][2014+i][1]
        x3=[0, 0, 0, 0, 0]
        for i in range(0, 5):
            x3[i]=((bank[c][2014+i][2] )*1000 )
        bankSame=0;
        bankReverse=0;
        for i in range(0,4):
            diffPro= x1[i+1]-x1[i];
            diffNPL= x3[i+1]-x3[i];
            if((diffPro<0 and diffNPL<0) or (diffPro>0 and diffNPL>0)):
                same=same+1;
                bankSame=bankSame+1;
            else:
                reverse=reverse+1;
                bankReverse=bankReverse+1;
                
            case=case+1
        
            
        
        print(name[c])
        if(bankSame>=3):
            sameBank=sameBank+"#"+name[c]+" "
        elif(bankReverse>=3):
            reverseBank=reverseBank+"#"+name[c]+" "
        else:
            neutral=neutral+"#"+name[c]+" "
        plt.plot(year, x1)
       # plt.plot(year, x2)
        plt.plot(year, x3)
        plt.xlabel("Year")
        plt.ylabel("BDT")
       # plt.legend(['Profit', 'NPL', 'NPL%'])
        plt.legend(['Profit', 'NPL%'])
        plt.show()
        
print("Case= ")
print(case)
print("Reverse= ")
print(reverse)
print(reverseBank)
print("Same= ")
print(same)
print(sameBank)
print("Neutral= ")
print(neutral)

