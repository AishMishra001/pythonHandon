# Validate input : keep asking user for input until they give a number between 1-10 


n = int(input("Enter the number : "))  

while n < 1 or n > 10 : 
    
    n1= int(input("Enter the number : "))
    if 1 <= n1 <= 10 :
        print("You entered a valid number : ", n1)  
        break 



# A shorter version of this will be when we use while True in a loop    

while True :
    n1= int(input("Enter the number : "))
    if 1 <= n1 <= 10 :
        print("You entered a valid number : ", n1)  
        break 