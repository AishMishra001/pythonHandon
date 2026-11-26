# Movie ticket price based on age  
# $ 12 of adult ( above 18 ) and 8 for children and on wednesday $2 discount 

Age = int(input("Please enter your age : "))
Day = input("Enter the day : ")

price = 12 if Age > 18 else 8 

if Day == 'wednesday':
    price -= 2



print("Your ticket price is : ", price) 