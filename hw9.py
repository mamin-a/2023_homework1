print()
print ("ЗАДАНИЕ 9")
print()

factorial = 5

a = []

while factorial != 0:
    a.append(factorial)
    factorial -= 1 
    
print(a)

import math

b = math.prod(a)

print("Факториал =",b)