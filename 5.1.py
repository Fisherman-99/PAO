slovar = {'Консоль' : 12, 'Кронштейн' :35, 'Облицовка':89, 'Втулка' :74, 'Накладка' :3, 'Заглушка' :34, 'Уплотнитель':3, 'Пружина' :9}
zakaz={}
zapas={}
print("Состояние склада ", slovar)
#c=len(slovar)
#print(c)
minimum= int(input('Введите минимальное количество '))
#minimum = 10
for i in slovar:
    if slovar[i] < minimum:
        print('На складе малое количество деталей - ',i)
        print("Добавляем в заказ")
        zakaz[i] = minimum - slovar[i]
    else:
        zapas[i]=slovar[i]
print("Список заказа", zakaz)
print("Запас остальных запчастей", zapas)