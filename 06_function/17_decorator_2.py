def check_none (fn) : 
    def inner(msg) : 
        if msg == None : 
            return ""
        else : 
            return fn(msg)
    return inner
        
def add_hi (fn) : 
    def inner(msg) : 
        return fn(msg) + "Hi"
    return inner

@check_none
@add_hi
def to_upper (msg) : 
    return msg.upper()

print(to_upper(None))