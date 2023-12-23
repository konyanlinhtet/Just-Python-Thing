def push(lst, ele) : 
    lst.append(ele)

def pop(lst) : 
    return lst.pop()

def is_empty(lst) : 
    return len(lst) == 0 

my_lst = []
push(my_lst, 100)
push(my_lst, 200)
push(my_lst, 300)
push(my_lst, 400)

print(my_lst)

while not is_empty(my_lst) : 
    pop(my_lst)

print(my_lst)