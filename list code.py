# 1st Program
friends = ["Apple", "Oranges", 34, 309.81, False,"Anshika"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])

# 2nd Program
friends = ["Apple", "Oranges", 34, 309.81, False,"Anshika"]
print(friends)

friends.append("Chanchal")
print(friends)

l1 = [1, 5,2,0,9]
l1.remove(0)

print(l1)

# 3rd Program
a = (1, 2, 5, 6 , "Chanchal")
print(a)
print(type(a))

# 4th Program
a = (1, 2, 6, 677, False, "Chanchal")
print(a)

no = a.count(2)
print(no)

i = a.index(2)
print(i)
print(len(a))

# 5th Program
marks = {
    "Chanchal" : 59,
    "Dishank" : 56,
    "Anshika" : 55
}

# print(marks, type(marks))
print(marks["Chanchal"])

# 6th Program
marks = {
    "Chanchal" : 59,
    "Dishank" : 56,
    "Anshika" : 55
}

print(marks.get("Chanchal")) 

# 7th Program
e = set() 
print (type(e))

s = {1, 2, 87, 2, 2, 2}
print(s)

# 8th Program
s = {1, 2, 5, 7, "Chanchal"}

print(s, type(s))

s.pop()
print(s)

# 9th Program
name = "Chanchal"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1] # characters can be define by index numbers or called slicing
print(character1)

# 10th Program
name = "Chanchal is"

print(len(name))
print(name.endswith("hal"))
print(name.startswith("Ch"))
print(name.capitalize())
print(name.title())
print(name.count("h"))