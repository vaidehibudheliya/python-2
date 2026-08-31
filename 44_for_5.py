# for loop with string 
# findout how many letters string has 
# input : apple output : 5 letters 
# input : banana output : 6 letters 


line = input("enter our name to count the letters")
count = 0
for letter in line:
 count = count + 1
print(f"{count} letters")