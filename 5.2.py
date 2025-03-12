slovar = {'Консоль' : 12, 'Кронштейн' :35, 'Облицовка':89, 'Втулка' :74, 'Накладка' :3, 'Заглушка' :34, 'Уплотнитель':3, 'Пружина' :9}
zakaz={}
zapas={}
izbytok={}
print("Состояние склада ", slovar)
def zapas_mm():
    minimum= int(input('Введите минимальное количество '))
    maksimum = int(input('Введите максимальное количество '))
    return minimum, maksimum
minimum,maksimum=zapas_mm ()
def prov (minimum, maksimum):
    if minimum>0 and minimum<maksimum:
        print ('Проверка склада')    
    else: 
        print ("Ошибка, неверные значения")
        minimum,maksimum=zapas_mm ()
        prov (minimum, maksimum)
prov (minimum, maksimum)
for i in slovar:
    if slovar[i] < minimum:
        print('На складе малое количество деталей - ',i)
        print("Добавляем в заказ")
        zakaz[i] = minimum - slovar[i]
    elif (slovar[i] >= minimum) and (slovar[i] <= maksimum):
        zapas[i]=slovar[i]
    elif slovar[i] > maksimum:
        izbytok[i]=slovar[i]
print("Список заказа", zakaz)
print("Запас остальных запчастей", zapas)
print("На складе избыток запчастей", izbytok)