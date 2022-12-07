x = 1  # int
x = "Curso em video"  # str
x = 15.6  # float
x = False  # bool

x = ["casa", "moto", "carro"]  # list/array
x[0] = "Bicicleta"

print("Valor da variável: " + str(x))
print("Tipo da variável: " + str(type(x)))


# quando colocamos a lista entre parenteses, trata-se de tupla; ela não aceita alteração exterior como o colchetes
y = ("casa", "moto", "carro")
print("Valor da variável: " + str(y))
print("Tipo da variável: " + str(type(y)))


y = range(0, 100, 1)  # cria uma lista de 0 a 100 contando de 1 em 1

# abaixo, ele cria um dict(dicionario, basicamente)
y = {
    "canal": "outros",
    "curso": "python",
    "aluno": "Alexandr"
}

print(y)
print(y["aluno"])


# nesse caso ele criou um 'set', que é definido pela chaves. ele nao repete numeros
y = {5, 6, 7, 8, 9, 8, 7, 4, 5, 6}

print(str(y))
print("Tipo da variável: " + str(type(y)))
