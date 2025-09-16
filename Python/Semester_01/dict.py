#dict is an ordered and mutable collection. does not allow duplicate members
val = 0
dictionary = {"book1": 5,
              "book2": 10, 
              "book3": 30}
print(dictionary["book2"])

print("-"*30)

dictionary["book4"] = 36
dictionary.pop("book4")

for books in dictionary:
    print(books)

print("-"*30)

for books in dictionary:
    vale = dictionary[books]
    val += vale
    print(val)

print("-"*30)

for books, valu in dictionary.items():
    print(f"{books}: {valu}")