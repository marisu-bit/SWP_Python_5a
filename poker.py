import numpy as np
import random

global cards
cards = []

for i in range(52): # 52 Ziffern weil 13Karten * 4Farben
    cards.append(i) # cards bestücken


def zahlkarten(random_cards):
    symbols = []
    for i in range(5):
        symbols.append(random_cards[i] % 13) # moodulo division gibt die Zahl
    return symbols


def farbe(zuflligekarte):
    farbe = []
    for i in range(5):
        farbe.append(zuflligekarte[i] // 13) # floor division gibt die Farbe
    
       #
       #  print(zuflligekarte[i] // 13)
    return cards

  # die verschiedenen Farben jeweils von 0-3


def randomf(): # fünf random karten ausgeben
    cnt=0
    rnfive=[]
    randomcards =cards
    random.shuffle(randomcards)
    while cnt < 5 :
        rnfive.append(randomcards[cnt])
        cnt = cnt+1
    return rnfive



def checkmulti(randomcards):
    #print(randomcards)
    thisdic={}
    for x in range (0,len(randomcards)):
        thisdic.update({randomcards[x]: randomcards.count(randomcards[x])})
    
    return thisdic

def paar(random_cards):
    if 2 in checkmulti(zahlkarten(random_cards)).values():
        return (True)

def drilling(random_cards):
    if 3 in checkmulti(zahlkarten(random_cards)).values():
        return (True)

def full_house(random_cards):
    if 3 in checkmulti(zahlkarten(random_cards)).values() and 2 in checkmulti(zahlkarten(random_cards)).values():
        return (True)

def vierling(random_cards):
    if 4 in checkmulti(zahlkarten(random_cards)).values():
        return (True)

def flush(random_cards):
    if 5 in checkmulti(farbe(random_cards)).values():
        return (True)        


def straight(random_cards):
    sorted_cards = sorted(zahlkarten(random_cards))
    counter = 0
    for index in range(4):
        if sorted_cards[index] + 1 == sorted_cards[index + 1]:
            counter = counter + 1

    if counter == 4:
        return (True)


def straight_flush(random_cards):
    sorted_cards = sorted(zahlkarten(random_cards))
    counter = 0
    for index in range(4):
        if sorted_cards[index] + 1 == sorted_cards[index + 1]:
            counter = counter + 1

    if counter == 4 and 5 in checkmulti(farbe(random_cards)).values():
        return (True)

dic = {
    "paar" : 0,
    "drillinge" : 0,
    "staight" : 0,
    "flush" : 0,
    "full house" : 0,
    "four of a kind" : 0,
    "straight flush" : 0,
    
    }

for i in range(0,100000):
    randomCard = randomf()

    if(straight_flush(randomCard)):
        dic["straight flush"] = dic["straight flush"]+1
    elif(vierling(randomCard)):
        dic["four of a kind"] = dic["four of a kind"]+1
    elif(full_house(randomCard)):
        dic["full house"] = dic["full house"]+1
    elif(flush(randomCard)):
        dic["flush"] = dic["flush"]+1
    elif(straight(randomCard)):
        dic["staight"] = dic["staight"]+1
    elif(drilling(randomCard)):
        dic["drillinge"] = dic["drillinge"]+1
    elif(paar(randomCard)):
        dic["paar"] = dic["paar"]+1
    
for i in dic:
    dic[i]=dic[i]/10000*100
print(dic)


