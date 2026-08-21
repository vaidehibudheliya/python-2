book = {} 
print(book)

book['name'] = "Learning Python"
book['price'] = 500
book['author'] = "Ankit Patel"
print(book)
book['price'] = 599
print(book['price'])

book['topics'] = ['Index','introduction','variables','control statements','functions']
print(book)

book['chapters'] = (1,2,3,4,5)
print(book)

print(book['topics'][1])

print(book['chapters'][2])

book['topics'][1] = "introduction to python"
print(book['topics'][1])

