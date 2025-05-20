dic1 = {'Joao':'a', 'maria':'b', 'pedro':'c'}
print(dic1)

dic2 = {'Joao0':1,'pedro':3}
print(dic2)

dic1.update(dic2) #com esse update, os valores serao substituidos por outrp valor pois nao pode haver 2 valores
print(dic1)