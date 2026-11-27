# Factorial : Compute the factorial of the number using While loop 

number = int(input("Enter the number : ")) 

fact = 1 
while number > 0 : 
    fact = fact * number    
    number = number -1 

print(fact)    