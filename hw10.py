print()
print ("ЗАДАНИЕ 10")
print()


lst = [5,6,3,4,5,1]

x = 0
a = 0
b = []

while x < len(lst):
    a = x*lst[x]
    b.append(a)
    x +=1

print("Исходный список =",lst)
print("Результат =",b)
    