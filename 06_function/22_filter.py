my_list = [1,2,3,4]

def get_even(x) : 
     return x % 2 == 0

even_lst = list(filter(get_even, my_list))
print(even_lst)