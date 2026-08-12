fruits = ['mango','apple','kiwi','banana','graps']
vegetables = ['potato','tomato','lady finger']
print("fruits")
fruits.extend(vegetables)
print(fruits)
fruits.remove('potato')
fruits.remove("mango")

fruits.pop(1)
print(fruits)
vegetables.clear()
print(vegetables)

