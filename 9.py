class Sklad:
 
    def __init__(self, number, name, kolvo, price):
        self.number = number      # номер детали
        self.name = name          # название детали
        self.group(number)        # группа детали
        self.kolvo = kolvo        # количество на складе
        self.price = price        # стоимость
     
    def group(self,number):
        if number[6] == '6':
            self.group='Salon' 
        elif number[6] == '3':
            self.group='Electrik'
        elif number[6] == '1':
            self.group='Dvigatel'
        else:
            self.group='Obshchij'
    def plus(self, p):
        print ("После заказа количество деталей составит", self.kolvo + p, "     Стоимость заказа:", self.price*p*0.7 )
        self.kolvo = self.kolvo + p
    def minus(self, m):
        if self.kolvo >=m:
            print("На складе достаточно деталей:", self.kolvo, "   Стоимость покупки составит:", self.price*m, "  *стоимость 1 ед:",  self.price)
            self.kolvo = self.kolvo - m

    def display_info(self):
        print(f"Name: {self.name}     Number: {self.number}     Group: {self.group}    Kolvo: {self.kolvo}     Price: {self.price}")
    
 
Obivka = Sklad('21093_6102100', 'Obivka', 23, 2100)
Ruchka = Sklad('21083_6816082', 'Ruchka', 12, 145)
Prokladka = Sklad('21083_1003020', 'Prokladka', 42, 649)
Vtulka= Sklad('21080_1003277', 'Vtulka', 69, 159)
Svecha = Sklad('21080_3707010', 'Svecha', 121, 115)
Kommutator = Sklad('21083_3734910', 'Kommutator', 13, 1299)
Obivka.display_info()
Ruchka.display_info()
Prokladka.display_info()
Vtulka.display_info()
Svecha.display_info()
Kommutator.display_info()
Kommutator.minus(2)
Kommutator.display_info()
Kommutator.plus(5)
Kommutator.display_info()