'''
write a program to accept week day number from user and display name of day.
input : 1 output : monday
input : 2 output : tuesday
'''
day = int(input("enter day of week"))
match day :
         case 1:
                     print("monday")
         case 2:
                     print("tuesday")
         case 3:
                     print("wednesday")
         case 4:
                     print("thursady")
         case 5: 
                     print("friday")
         case 6:
                     print("saturday")
         case 7:
                     print("sunday")
         case _:
                     print("it is not valid day")



        