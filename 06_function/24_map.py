my_lst = [1,2,3,4,5,6]
incTen = lambda x : x + 10

def is_even(x) : 
     return x % 2 ==0

print(list(map(incTen, filter(is_even, my_lst))))
