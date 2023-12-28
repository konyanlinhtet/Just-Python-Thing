import csv

with open("data.csv","a",newline='') as file:
    writer = csv.writer(file)
    id = 100
    name = "Nyan"
    school = "TTU"
    writer.writerow([id,name,school])
    
print("Writing done")