with open("Students.csv") as f:
    content = f.readlines()

for row in content[1:]:
    row = row.strip()
    values = row.split(",")
    num = int(values[1])
    if num >= 18:
        print(values[0], values[2])

