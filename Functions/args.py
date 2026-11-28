# Function with args : write a function that takes multiple number of inputs and return there sum 


def sums(*args):

   

    for i in args:
        print(i*2)

    return sum(args)    

result = sums(1,2,3,4,5)
result1 = sums(10,20,30)
result2 = sums(1,2,5,7,3,7,34,467,44,734)

print(result , result1 , result2)