#Rule 1 , can be stored in variable
#Rule 2, can be passed as parameter.
#Rule 3, can be returned from function

#Rule 1
def fun1 () :
    return "Hello"

var = fun1
print(var())

#Rule 2
def para(fn) :
    return fn()

print(para(fun1))

#Rule 3
def ret() : 
    return fun1()

print(ret())