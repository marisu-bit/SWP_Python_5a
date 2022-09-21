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
