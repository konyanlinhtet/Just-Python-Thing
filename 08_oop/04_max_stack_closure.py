def stack() : 
    lst = []
    def push(ele): 
        lst.append(ele)

    def pop():
        return lst.pop()
    
    def is_empty():
        return len(lst) == 0
    
    return push, pop, is_empty, lst
    
push, pop, is_empty, lst = stack()
push(100)
push(200)
push(300)
push(400)
pop()

print(lst)

# have to create with new name 