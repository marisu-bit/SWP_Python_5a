import random
import json
from flask import Flask, jsonify

def aufrufen(Countplayerwins,Countcompwins,symbols_player,symbols_comp):
    print("Wilkommen bei Schere Stein Papier Echse Spock")

    print("Schere = 0, Stein = 1, Papier = 2, Echse = 3, Spock = 4")
    print("")
  
    comp =symbols_player.index(max(symbols_player))
    
    #print(comp)        #computer wahl 
   # comp = str(random.randint(0,4)) #ohne logik
    player = str(input())

    symbols_player[int(player)] += 1
    symbols_comp[int(comp)] += 1

    print("Computer: " + str(comp))

    if player == comp: print("Unentschieden")
    elif player == "0":
        if comp == "1" or comp == "4": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt") ; Countplayerwins += 1
    elif player == "1":
        if comp == "2" or comp == "4": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt") ; Countplayerwins += 1
    elif player == "2":
        if comp == "0" or comp == "3": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt")   ; Countplayerwins += 1
    elif player == "3":
        if comp == "1" or comp == "0": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt") ; Countplayerwins += 1
    elif player == "4":
        if comp == "2" or comp == "3": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt") ; Countplayerwins += 1
    else: print("Falsche Eingabe")

    again = str(input("Nochmal? (y/n)"))

    if again == "y": aufrufen(Countplayerwins,Countcompwins,symbols_player,symbols_comp)
    elif again == "n":
        
        playerstats = {"Schere": symbols_player[0], "Stein": symbols_player[1], "Papier": symbols_player[2], "Echse": symbols_player[3], "Spock": symbols_player[4], "Gewonnen": Countplayerwins}
        compstats = {"Schere": symbols_comp[0], "Stein": symbols_comp[1], "Papier": symbols_comp[2], "Echse": symbols_comp[3], "Spock": symbols_comp[4], "Gewonnen": Countcompwins}

        with open('playerdb.json', 'w') as f: #ueberschreben des Json- genutzt als DB
            json.dump(playerstats, f)
        with open('computerdb.json', 'w') as f: #ueberschreben des Json- genutzt als DB
            json.dump(compstats, f)

        print("Auf Wiedersehen")
    else: print("Falsche Eingabe")

def statistics( Countplayerwins, Countcompwins, symbols_player, symbols_comp):
    timesplayed = Countplayerwins + Countcompwins
    print("Gespielt: " + str(timesplayed))
    print("Spieler: " + str(Countplayerwins) + " Percent: " + str((Countplayerwins/timesplayed)*100)+ "%")
    print("Symbole: " + str(symbols_player))
    print("Computer: " + str(Countcompwins) + " Percent: " + str((Countcompwins/timesplayed)*100) + "%")
    print("Symbole: " + str(symbols_comp))

if __name__ == '__main__':

    with open('playerdb.json', 'r') as f:
        playerstats = json.load(f)

    with open('computerdb.json', 'r') as f:
        compstats = json.load(f)

    Countplayerwins = playerstats["Gewonnen"]
    Countcompwins = compstats["Gewonnen"]
    symbols_player = [playerstats["Schere"],playerstats["Stein"],playerstats["Papier"],playerstats["Echse"],playerstats["Spock"]]
    symbols_comp = [compstats["Schere"],compstats["Stein"],compstats["Papier"],compstats["Echse"],compstats["Spock"]]

    app = Flask(__name__)
    @app.route('/')
    def statistic():
        
        return jsonify({"Playerdata": playerstats, "Computerdata": compstats})
    
    print("Willkommen bei Schere Stein Papier Echse Spock")
    print("1. Spiel starten")
    print("2. Statistik")
    print("3. Beenden")
    choice = str(input())
    if choice == "1":
        print(symbols_player)
        aufrufen(Countplayerwins,Countcompwins,symbols_player,symbols_comp)
    elif choice == "2":
        statistics( Countplayerwins, Countcompwins, symbols_player, symbols_comp)
        app.run()
    elif choice == "3":
        print("Auf Wiedersehen")
        exit()
    else: print("Falsche Eingabe")