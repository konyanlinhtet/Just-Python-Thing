our_marks = {
    "eng":100,
    "math":20,
    "myanmar":30
}

def sum_marks(**marks) :#to skip pass by ref
     global our_marks
     print(id(our_marks), id(marks))
     print(type(marks))
     total = 0
     for k , v  in marks.items(): 
          total += v
     return total

print(sum_marks(**our_marks))


