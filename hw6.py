print()
print ("ЗАДАНИЕ 6")
print()

x = [-4,7,9,10,-15]
p = []

a=len(x)

print("Длина входного списка =",a)
print()

for elem in x:
    #print(x.index(elem))
    if x.index(elem)>a:
        break
    else:
        #print(elem)
        if elem>0:
          p.append(elem)

print()
print ("Кол-во положительных чисел в списке =",len(p))

