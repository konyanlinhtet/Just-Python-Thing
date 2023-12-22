def counter() : 
     yield 1
     yield 2

count = counter()
print(next(count))
print(next(count))

count2 = counter()
for x in count2: 
     print (x)