slovar = {'Консоль' : 12, 'Кронштейн' :35, 'Облицовка':89, 'Втулка' :74, 'Накладка' :3, 'Заглушка' :34, 'Уплотнитель':3, 'Пружина' :9}
print(slovar)
minimum = 39
detal = str(input('Название детали '))
print('Проверка наличия на складе', detal)
while slovar[detal]<minimum:
#if  slovar[detal]<minimum:
    proc=str(input('Заказать деталь да или нет'))
    if proc=="да":
        print('Заказываем запчасти', detal)
        slovar[detal] += (minimum-slovar[detal])
        print(slovar)
    else :#proc =="нет":
        print("Отмена заказа деталей", detal)
#else:
   # print("Деталей достаточно", slovar[detal]
print('Выход из заказа')
