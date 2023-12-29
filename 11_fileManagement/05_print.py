file = open("02_write_file.py","r")

lines = file.readlines()
print("lines",lines)
for line in lines:
    print(line,end='')

file.close()
