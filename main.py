from AppEngine.Persona import Persona
from AppEngine.Animale import Animale


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
