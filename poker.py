import numpy as np
import random

global cards
cards = []

for i in range(52): # 52 weil 13*4
    cards.append(i)


def farbe(zuflligekarte):
    cards = []
    for i in range(5):
        cards.append(zuflligekarte[i] // 13)
        print(zuflligekarte[i])
        print(zuflligekarte[i] // 13)
    return cards

  # die verschiedenen Farben jeweils von 0-3


def zahlkarten(random_cards):
    symbols = []
    for i in range(5):
        symbols.append(random_cards[i] % 13)
    return symbols

def paar(random_cards):
    if 2 in repetition(zahlkarten(random_cards)).values():
        return (True)

def fuenfzufaelligezahlen():
    index = 0
    rn = []
    while index < 5:
        randomn = random.randint(0, 51 - index)
        cards[randomn], cards[51 - index] = cards[51 - index], cards[randomn]
        rn.append(cards[51 - index])
        index = index + 1
    return rn


def repetition(random_cards):
    return {item: random_cards.count(item) for item in random_cards}



def drilling(random_cards):
    if 3 in repetition(zahlkarten(random_cards)).values():
        return (True)



def full_house(random_cards):
    if 3 in repetition(zahlkarten(random_cards)).values() and 2 in repetition(symbols_of_5(random_cards)).values():
        return (True)


def straße(random_cards):
    sorted_cards = sorted(zahlkarten(random_cards))
    counter = 0
    for index in range(4):
        if sorted_cards[index] + 1 == sorted_cards[index + 1]:
            counter = counter + 1

    if counter == 4:
        return (True)


def flush(random_cards):
    if 5 in repetition(farbe(random_cards)).values():
        return (True)



def straight_flush(random_cards):
    sorted_cards = sorted(zahlkarten(random_cards))
    counter = 0
    for index in range(4):
        if sorted_cards[index] + 1 == sorted_cards[index + 1]:
            counter = counter + 1

    if counter == 4 and 5 in repetition(farbe(random_cards)).values():
        return (True)



def vierling(random_cards):
    if 4 in repetition(zahlkarten(random_cards)).values():
        return (True)

