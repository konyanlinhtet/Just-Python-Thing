def custom_range (start, end) : 
     while start < end : 
          yield start
          start += 1
    
for x in custom_range(1,5) :
     print(x)