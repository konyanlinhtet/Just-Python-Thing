def security(fn):
    print("Security check")
    return fn

@security
def order():
    print("Order Processing")
    
order()