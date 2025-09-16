#list is an ordered and mutable collection. allows duplicate members
lists = ["car", "bike", "skate"]
lists.append("Ship")
lists.insert(2,"Plane")
del lists[3]
print(len(lists))
print("-"*30)

#tuples is an ordered and immutable collection. allows duplicate members
tuples = ("nome", True, 2, 6.5)
print(tuples)
print(tuples[2])
print("-"*30)

#set is an unordered, unindexed collection. does not allow duplicate members
conjunto = {"car",True,3,2.5}
print(conjunto)

print("-"*30)

hat = [1,2,3,4,5]
hat[2] = 6
del hat[4]
hat.append(input("type: "))
hat += ["eu", "você", "e tua avó"]
hat.extend(["meu dog",2,"vem que tem"])
print(len(hat))
print(hat)