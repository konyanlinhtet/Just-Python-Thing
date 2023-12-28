with open("02_write_file.py","r") as file:
    ten_char = file.read(10)
    print("Ten character ",ten_char)
    print("tell ",file.tell())


    line = file.readline()
    print("Line ",line)

    lines = file.readlines()
    print("lines ",lines)

