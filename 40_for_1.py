#example of for loop 
# write a program to make sum of all values in list and display it also calculate & display average 
list =[100,75,200,150,500,400,1000,2000,5000]
sum = 0
count = 0
for number in list:
    sum = sum + number
    count = count + 1
    print("total",sum)
    mean = sum / count
    print("average",mean)