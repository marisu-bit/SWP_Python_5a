import random
zahlenpool = []
lotto = []
def befüllen():

    for x in range(1,46):
        zahlenpool.insert(x,x)
    

def ziehen():
 
    for y in range(1,7):
        z =random.randrange(0,len(zahlenpool))
        
        zahl = zahlenpool.pop(z)
        lotto.insert(y,zahl)
    
        

    
befüllen()
ziehen()
print(lotto)


def statisik():
    dict={}
    for i in range(1,46): # die einzelnen Werte
        dict[i]=0
    for i in range(0,1000):
        dict[int(random.random()*45+1)]+=1 # ziehung der einzellnen Werte
    print(dict)
statisik()

