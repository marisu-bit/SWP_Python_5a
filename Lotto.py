import random
zahlenpool = []
lotto = []
start =0
end = 45
anzziehen= 6
def befüllen(start, end):

    for x in range(start,end+1): # bei Range ist immer -1 
        zahlenpool.insert(x,x)
    
    

def ziehen():
 
    for y in range(start,anzziehen+1):
        z =random.randrange(start,len(zahlenpool))
        
        zahl = zahlenpool.pop(z)
        
        lotto.insert(y,zahl)
        

    
        
#return zahlen[:-6] alle ausßer die letzen 6
#return zahlen[-ziehen:-1] alle außer die letzen ziehen und die aller letzte
    
befüllen(start,end)
ziehen()
print(lotto)


#zahlen tauschen in einemr array das gezogene an der Stelle an die letzte stellen

#zahlen[stelle],zahlen[len(zahlen)-1-x]=zahlen[len(zahlen)-1-x],zahlen[stelle]
#Lösung von Marcel






def statisik():
    dict={}
    for i in range(1,46): # die einzelnen Werte
        dict[i]=0
    for i in range(0,1000):
        dict[int(random.random()*45+1)]+=1 # ziehung der einzellnen Werte und aufaddieren

    print(dict) #ausgabbe des dic
statisik()

#unterschied array liste -> array hat eine anfangs addresse -> die zahlen hängen im Speicher alle zusammen -> ein lbock nicht erweiterbar -> schneller
#in einer liste werden die einzelnen elmente auf die anderen verweisen, es können allso immer erweiter werden-> besteht aus einzelnen objekte welche über zeiger zusammenhängen

#python dot env-> konfig dateien