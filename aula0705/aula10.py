dic = {'Joao':'a', 'maria':'b', 'pedro':'c'}
print(dic)
excluido = dic.pop('Joao')
print('excluido foi: ' + excluido)
print(str(dic))

dic.popitem() #apagara um nome aleatorio pq nao colocamos um nome dentro dos parenteses
print(str(dic))
