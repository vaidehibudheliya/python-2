fruits = {'apple','banana','mango','orange','pineapple'}
print(fruits)
#let us add values into set
fruits.add('kiwi') #it will be added 
fruits.add('banana') #it will not be added because there is already banana
print("now fruits contains",fruits)

#remove value from set
fruits.remove('kiwi')
print("now fruit contains = ",fruits)

other_fruits = ['coconut','water melon','cherry','avacado','graps','graps','coconut']

fruits_2 = set(other_fruits)
print(fruits_2)

#convert set into list 
fruits_3 = list(fruits)
print(fruits_3)