with open("02_write_file.py","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line,end='')
