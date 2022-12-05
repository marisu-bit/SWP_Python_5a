
#1 = Schere
#2 =Stein
#3= Papier
#4 = echse
#5= spock
    

class player():
    def __init__(self,turn,counter):
        self.turn= turn
        self.counter=counter

def getInputPlayer():
    symbollist = []
    
    for x in range (1,6): 
     symbollist.append(x)

def game():
    a = getInputPlayer()
    

#main
def main():
    game()
    getInputPlayer()
    
if __name__ == '__main__':
    main()
