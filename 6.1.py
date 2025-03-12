#order=['Ruchka: 2', 'Steklo: 3']
order=['Kronshtein :35 \n', ' Oblitcovka:89 \n',' Vtulka :74 \n', ' Nakladka :3 \n', ' Zaglushka :34 \n', ' Uplotnitel:3 \n',' Prugina :9 \n']
o1=open('data.txt','w')
o2=o1.write(' Ruchka: 7 \n ')
o3=o1.writelines(order)
o1.close
o4=open('data.txt')
o4.close
#pp=o4.read()
print(o4.read())
