# Dictionary Carrent book with attributes

currentBook = {
    "title": "Possibility of an Island",
    "author": "Michel Houellebecq",
    "price": 40
}

print(currentBook)
print(currentBook["author"])

currentBook["ISBN"] = "374795"

print("The Current book has these values:")
for value in currentBook.values():
    print("  => {}".format(value))