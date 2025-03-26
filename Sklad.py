class Sklad:
 
    def __init__(self, number, name, group, kolvo, price):
        self.number = number      # номер детали
        self.name = name          # название детали
        self.group = group        # группа детали
        self.kolvo = kolvo        # количество на складе
        self.price = price        # стоимость
     
    def display_info(self):
        print(f"Name: {self.name}  Number: {self.number} Group: {self.group} Kolvo: {self.kolvo} Price: {self.price}")
 
 
Obivka = Sklad(21093.6102100, 'Obivka', "Dver", 23, 2100)
Ruchka = Sklad(21083.6816082, 'Ruchka', "Sidenie", 12, 145)
Prokladka = Sklad(21083.1003020, 'Prokladka', "Dvigatel", 42, 649)
Vtulka= Sklad(21080.1003277, 'Vtulka', "Dvigatel", 69, 159)
Svecha = Sklad(21080.3707010, 'Svecha', "Electrik", 121, 115)
Kommutator = Sklad(21083.3734910, 'Kommutator', "Electrik", 13, 1299)
Obivka.display_info()
Ruchka.display_info()
Prokladka.display_info()
Vtulka.display_info()
Svecha.display_info()
Kommutator.display_info()
 