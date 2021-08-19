import pandas as pd

file = pd.ExcelFile('data.xlsx')


prime = file.parse('Prime Bank')
for i in range(0, 13):
    for j in range(i+1, 14):
         same=0
         reverse=0
         for c in range(0, 3):
             x1=prime[2014+c][i]-prime[2015+c][i]
             x2=prime[2014+c][j]-prime[2015+c][j]
             #print(x1)
             if((x1>0 and x2>0)or(x1<0 and x2<0)):
                 same=same+1
        
             if((x1<0 and x2>0)or(x1>0 and x2<0)):
                 reverse=reverse+1
         
        
         if(same>=3):
             print("Same: ")
             print(prime['Name'][i]+"<-->"+prime['Name'][j])
         if(reverse>=3):
             print("Reverse: ")
             print(prime['Name'][i]+"<-->"+prime['Name'][j])
             
    print("")