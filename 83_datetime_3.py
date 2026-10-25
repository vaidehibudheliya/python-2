#write a program to find out who is elder person in couple 
from datetime import datetime as dt
husband_birth_date = input("Enter husband birth date (%d-%m-%Y)")
wife_birth_date = input("Enter wife birth date (%d-%m-%Y)")
#convert it into date object for comparison
husband_birth_date = dt.strptime(husband_birth_date,"%d-%m-%Y")
wife_birth_date = dt.strptime(wife_birth_date,"%d-%m-%Y")

if husband_birth_date<wife_birth_date:
    print("Husband is elder person in couple")
else:
    print("Wife is elder person in couple")

#us format (%m-%d-%Y) it only format date into given format for display purpose 
print("husband birth date",dt.strftime(husband_birth_date,"%m-%d-%Y"))
print("wife birth date",dt.strftime(wife_birth_date,"%m-%d-%Y"))