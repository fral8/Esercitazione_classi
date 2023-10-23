""" 🍰 Esercizio 3 ---> [ aggiungere come new Feature] Federico
Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”. Aggiungi un metodo 
“descrivi” che stampi una descrizione dell automobile, ad esempio “Questa è una Toyota Corolla del 2017”.
Merge con develop (in automatico) """

class Automobile():
    def __init__(self, marca, modello, anno):
        self.marca_automobile=marca
        self.modello_automobile=modello
        self.anno_automobile=anno
    #GETTER
    def get_marca(self):
        return self.marca_automobile
    def get_modello(self):
        return self.modello_automobile
    def get_anno(self):
        return self.anno_automobile
    #SETTER
    def set_marca(self, new_marca):
        self.marca_automobile = new_marca
    def set_modello(self, new_model):
        self.modello_automobile = new_model
    def set_anno(self, new_anno):
        try:
            new_anno = int(new_anno)
            self.anno_automobile = new_anno
        except Exception as e:
            print("Inserimento caratteri testuali non valido\n")
    #DESCRIZIONE AUTO
    def descrizione(self):
        print(f"Questa è una {self.get_marca()} {self.get_modello()} del {self.get_anno()}")