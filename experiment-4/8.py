"""Take two sets and apply various set operations on them :
S1 = {Red ,yellow, orange , blue }
S2 = {violet, blue , purple}"""

s1 = {"Red" ,"yellow", "orange" , "blue" }
s2 = {"violet", "blue" , "purple"}

print("set1: ",s1)
print("set2 : ",s2)

print("union",s1|s2)
print("Intersection",s1&s2)
print("difference ",s1-s2)
print("difference ",s2-s1)
print("symmetric difference",s1^s2)
