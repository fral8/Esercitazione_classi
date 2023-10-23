from AppEngine.Persona import Persona
from AppEngine.Animale import Animale
from AppEngine.Impiegato import Impiegato
from AppEngine.Automobile import Automobile


if __name__=="__main__":
    print("ESERCIZIO 0:")
    persona1=Persona("","","")
    persona1.setNome("Marco")
    persona1.setSesso("m")
    persona1.setAge(32)
    persona1.presentati()
    
if __name__=="__main__":
    print("ESERCIZIO 1:")
    animale1=Animale("","","")
    animale1.setNome("Fuffy")
    animale1.setSpecie("cane")
    animale1.emetti_suono()
    
    print("ESERCIZIO 1.1:")
    animale2=Animale("","","")
    animale2.setNome("Pallino")
    animale2.setSpecie("gatto")
    animale2.emetti_suono()
    
if __name__=="__main__":
    print("ESERCIZIO 2:")
    impiegato1=Impiegato("","","","")
    impiegato1.setNome("Mario")
    impiegato1.setCognome("Rossi")
    impiegato1.setMatricola("A001")
    impiegato1.setStipendio(2000)
    #impiegato1.aumenta_stipendio()
    impiegato1.stampa_dettagli()
    print("ESERCIZIO 3:\n")
    automobile1=Automobile("","","")
    automobile2=Automobile("","","")
    automobile3=Automobile("","","")
    automobile4=Automobile("","","")
    automobile5=Automobile("","","")
    automobile1.set_marca("Toyota")
    automobile2.set_marca("Ford")
    automobile3.set_marca("Honda")
    automobile4.set_marca("BMW")
    automobile5.set_marca("Volkswagen")
    automobile1.set_modello("Corolla")
    automobile2.set_modello("Mustang")
    automobile3.set_modello("Civic")
    automobile4.set_modello("X5")
    automobile5.set_modello("Golf")
    automobile1.set_anno(2019)
    automobile2.set_anno(2022)
    automobile3.set_anno(2020)
    automobile4.set_anno(2021)
    automobile5.set_anno(2018)
    automobile1.descrizione()
    automobile2.descrizione()
    automobile3.descrizione()
    automobile4.descrizione()
    automobile5.descrizione()
    
