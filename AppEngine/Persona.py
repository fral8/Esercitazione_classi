'''Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. 
.'''



class Persona():
    #self --> serve per leggere all'interno della classe, variabili e metodi in essa definit
    def __init__(self,nome,age,sesso):
        self.nome_classePersona=nome
        self.age_classePersona=age
        self.sesso_classePersona=sesso

    #getter--> metodo che permette di effettuare return di una variabile
    def getNome(self):
        return self.nome_classePersona
    def getAge(self):
        return self.age_classePersona
    def getSesso(self):
        return self.sesso_classePersona
    
    #setter --> metodo che permette di assegnare il valore a una variabile
    def setNome(self,new_nome):
        self.nome_classePersona=new_nome
    
    def setAge(self,new_age):
        try:
            new_age=int(new_age)
            self.age_classePersona=new_age
        except Exception as e:
            print("Eta inserita non valida")
    def setSesso(self,new_sesso):
        if new_sesso.lower()=="m" or new_sesso.lower()=="f" or new_sesso.lower()=="nb":
            self.sesso_classePersona=new_sesso
        else:
            print("Errore: sesso non valido")
    
    '''Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, 
ad esempio “Ciao, mi chiamo Marco e ho 32 anni”'''
    def presentati(self):
        print(f"Ciao, mi chiamo {self.getNome()} e ho {self.getAge()} anni")
