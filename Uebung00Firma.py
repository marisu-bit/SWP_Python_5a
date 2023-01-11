#in Python ist alles ein Objetk

class Person:
    name = ""
    gender =""
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

class Mitarbeiter(Person):
    abteilung =""
    salary = 0.0
    def __init__(self,name,gender,abteilung,salary):
        Person.__init__(self,name,gender)
        self.abteilung=abteilung
        self.salary=salary
    
class Gruppenleiter(Mitarbeiter):
    privaterparkplatz=0
    leitervon=""
    def __init__(self,name,gender,abteilung,salary,privaterparkplatz,leitervon):
        Mitarbeiter.__init__(self,name,gender,abteilung,salary)
        self.privaterparkplatz=privaterparkplatz
        self.leitervon=leitervon    

class Firma():
    nameFirma=""
    FN=0
    Anschrift=""
    def __init__(self,mitarbeiter,gruppenleiter,nameFirma,FN,Anschrift):
        self.mitarbeiter=mitarbeiter
        self.gruppenleiter=gruppenleiter
        self.nameFirma=nameFirma
        self.FN=FN
        self.Anschrift=Anschrift
    
    def countMitarbeiter(self):
        return (len(self.mitarbeiter))

    def countGruppenleiter(self):       
        return (len(self.gruppenleiter))

#main
def main():
    p1=Person("Max","man")
    p2=Person("Max1","man")
    p3=Person("Max2","man")
    p4=Person("Max3","man")

    personen=[p1,p2,p3,p4]
    

    m1=Mitarbeiter(p1.name, p1.gender,"IT",10000.0)
    m2=Mitarbeiter(p2.name,p2.gender,"IT",10000.0)
    m3=Mitarbeiter(p3.name,p3.gender,"costumer",10000.0)
    m4=Mitarbeiter(p4.name,p4.gender,"costumer",10000.0)

    mitarbeiterliste=[m1,m2,m3,m4]

    g1=Gruppenleiter(m1.name,m1.gender,m1.abteilung,m1.salary,12,"IT")
    g2=Gruppenleiter(m2.name,m2.gender,m2.abteilung,m2.salary,10,"costumer")

    gruppenleiterliste = [g1,g2]
    
    f1=Firma(mitarbeiterliste,gruppenleiterliste,"ITserviceHallo",122332,"6020 Innsbruck")
    
    zahl=f1.countMitarbeiter()
    print(zahl)
    

    
if __name__ == '__main__':
    main()