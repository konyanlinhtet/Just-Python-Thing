from functools import * 
my_lst = [1,2,3,4,5]

def add (a,b) :
     return a + b

total = reduce(add, my_lst)
print(total)