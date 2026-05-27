with open("products.csv") as p:
    lines = p.readlines()

for items in lines[1:]:
    row = items.strip()
    row = row.split(",")
    if row[2] == "electronics":
        print(row[0], row[1])