f = open("city.txt", "r")
lines = f.readlines()
f.close()

cities = []
for line in lines:
    name, pop, area = line.split()
    cities.append((name, float(pop), float(area)))

for c in cities:
    print(c[0], c[1], c[2])

for c in cities:
    if c[1] > 10:
        print(c[0])

total_area = sum(c[2] for c in cities)
print(total_area)