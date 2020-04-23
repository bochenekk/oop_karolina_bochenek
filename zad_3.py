# B map

wielomian = lambda x: 5 * x ** 3 + 3 * x ** 2 - 2 * x + 5

print(list(map(wielomian, list(range(-100, 101)))))