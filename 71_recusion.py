#write a program to print following series 
#2 4 6 8 10 12.......100
#define function 
def printseries(num):
    if num <= 100:
        print(num,end=' ')
        num = num + 2 #4
        printseries(num)
num = 2
printseries(num)