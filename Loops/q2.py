# Sum of even numbers till n 

# 5 , 1 , 2 ,3 , 4 5,  : 

n = int(input("Enter a number : "))

sum = 0 

for n in range(1, n+1):  # 1 2 3 4 5 
    if (n % 2 == 0): 
        sum = sum + n 
    else : 
        continue 

print (sum) 


# Print multiplication table of a number, but skip the 5th iteration 


for num in range(1 , n + 1): 
    if ( num == 5 ) : 
        continue 
    else : 
        print( n , " x " , num , " = " , n*num)