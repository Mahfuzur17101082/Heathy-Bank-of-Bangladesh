import pandas as pd

file = pd.ExcelFile('data.xlsx')


prime = file.parse('Prime Bank')
dhaka = file.parse('Dhaka Bank')
bank = [prime, dhaka]
for i in range(0, 2):
    for j in range(0, 14):
        same=0
        reverse=0
        for c in range(0, 3):
            x1=bank[i][2014+c][14]-bank[i][2015+c][14]
            x2=bank[i][2014+c][j]-bank[i][2015+c][j]
            if((x1>0 and x2>0)or(x1<0 and x2<0)):
                 same=same+1
                
            if((x1<0 and x2>0)or(x1>0 and x2<0)):
                 reverse=reverse+1
                 
                
            if(same>=3):
                 print("Same: ")
                 print(bank[i]['Name'][14]+"<-->"+bank[i]['Name'][j])
            if(reverse>=3):
                 print("Reverse: ")
                 print(bank[i]['Name'][14]+"<-->"+bank[i]['Name'][j])
                 