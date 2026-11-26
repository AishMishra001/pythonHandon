# check for leap year ( divided by 4 but not 100 or divied by 400)


Year = int(input("Enter the year : ")) 


if ( Year %4 == 0 and Year % 100 != 0 ) or ( Year % 400 == 0 ):
    print ( Year , "is leap year")

else:
    print( Year , "is not a leap year")