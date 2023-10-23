class Impiegato():
    def __init__(self,nome,cognome,matricola,stipendio):
        self.nome_classImpiegato=nome
        self.cognome_classImpiegato=cognome
        self.matricola_classImpiegato=matricola
        self.stipendio_classImpiegato=stipendio

    def getNome(self):
        return self.nome_classImpiegato
    def getCognome(self):
        return self.cognome_classImpiegato
    def getMatricola(self):
        return self.matricola_classImpiegato
    def getStipendio(self):
        return self.stipendio_classImpiegato
    
    def setNome(self,new_nome):
        self.nome_classeImpiegato=new_nome
    
    def setCognome(self,new_cognome):
        self.cognome_classeImpiegato=new_cognome

    def setMatricola(self,new_matricola):
        self.matricola_classeImpiegato=new_matricola
        
    def setStipendio(self,new_stipendio):
        try:
            new_stipendio=float(new_stipendio)
            self.stipendio_classeImpiegato=new_stipendio
        except:
            print('Inserisci un importo valido')
        
    def aumenta_stipendio(self):
        print(self.getStipendio())
        a= float(self.getStipendio())
        b= 10
        c= (a * b)/100
        print(c)
        self.setStipendio(c)

    def stampa_dettagli(self):
        print(f"Impiegato: {self.getNome()} {self.getCognome()}, matricola: {self.getMatricola()}, stipendio: {self.getStipendio()}")
   