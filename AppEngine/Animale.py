class Animale():
    #self --> serve per leggere all'interno della classe, variabili e metodi in essa definit
    def __init__(self,nome,specie, suono):
        self.nome_classeAnimale=nome
        self.specie_classeAnimale=specie
        self.suono_classeAnimale=suono
         
#getter--> metodo che permette di effettuare return di una variabile
    def getNome(self):
        return self.nome_classeAnimale
    def getSpecie(self):
        return self.specie_classeAnimale
            
    #setter --> metodo che permette di assegnare il valore a una variabile
    def setNome(self,new_nome):
        self.nome_classeAnimale=new_nome
    
    def setSpecie(self,new_specie):
        self.specie_classeAnimale=new_specie
    
    
# metodo emetti_suono
    def emetti_suono(self):
        if self.getSpecie()=="gatto":
            a="Miao"
        elif self.getSpecie()=="cane":
            a='Bau'
        else:
           "Animale sconosciuto"
        print(f"Ciao, mi chiamo {self.getNome()} e sono un {self.getSpecie()}, emetto questo suono: {a}")