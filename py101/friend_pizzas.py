pizzas = ['hawaaian', 'tikka', 'meat deluxe', 'perriperri', 'chicken tikka']
pizzas.append("veggie")
print(pizzas)
friends_pizzas = pizzas[:]
friends_pizzas.append("pepper")
print(friends_pizzas)
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friends favorite pizzas are:")
for piza in friends_pizzas:
    print(piza)