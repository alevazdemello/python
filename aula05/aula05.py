import random

num_i = 10
num_f = 5.2
num_c = 1j


num_r = random.randrange(0, 5)
num_e = [random.randrange(0, 50),
         random.randrange(0, 50),
         random.randrange(0, 50),
         random.randrange(0, 50),
         random.randrange(0, 50),
         random.randrange(0, 50),
         random.randrange(0, 50),
         random.randrange(0, 50),
         random.randrange(0, 50),
         random.randrange(0, 50)]  # a funcao random tb pode ser usada em arrays
x = int(num_f)  # mesmo o numero nao sendo inteiro, quando usamos int() ele faz a conversao e imprime apenas o valor inteiro, sem a casa decimal
# mesmo caso de conversão usado acima, mas agora de int>float (apresentado agra como 10.0)
x = float(num_i)
print("Valor: " + str(x) + " - Tipo : " + str(type(x)))


print(num_r)
print(num_e)
