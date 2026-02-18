"""Store details of n movies in a dictionary by taking input from the user. Each
movie must store details like name, year, director name, production cost,
collection made (earning) & perform the following :-
a) print all movie details
b) display name of movies released before 2015
c) print movies that made a profit.
d) print movies directed by a particular director."""

n = int(input("Enter number of movies: "))

movies = {}


for i in range(n):
    mname = input("Enter movie name: ")
    year = int(input("Enter year of release: "))
    director = input("Enter director name: ")
    cost = float(input("Enter production cost: "))
    earning = float(input("Enter collection made: "))
    
    movies[mname] = {
        "year": year,
        "director": director,
        "cost": cost,
        "earning": earning
    }


print("\nAll Movie Details:")
for name in movies:
    print("Movie Name:", name)
    print("Year:", movies[name]["year"])
    print("Director:", movies[name]["director"])
    print("Cost:", movies[name]["cost"])
    print("Earning:", movies[name]["earning"])
    print()


print("Movies released before 2015:")
for name in movies:
    if movies[name]["year"] < 2015:
        print(name)


print("Movies that made profit:")
for name in movies:
    if movies[name]["earning"] > movies[name]["cost"]:
        print(name)


dname = input("Enter director name to search: ")

print("Movies directed by", dname, ":")
for name in movies:
    if movies[name]["director"] == dname:
        print(name)
