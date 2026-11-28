# function with yield : yield is used to return a value from a function 
# when the function is called, it returns a generator object 
# when the generator object is iterated, it returns a value


# even numbers generator 


# def even_generator(n):
#     for i in range(2,n+1,2):
#         yield i 

# result = even_generator(10) 
# print(result)



# Why this happens

# When a function uses the yield keyword instead of return,
#  Python automatically turns it into a generator function.

# When you call even_generator(10):

# It does not run the code immediately.
# Instead, it returns a generator object 
# (e.g. <generator object even_generator at 0x100904580>),
#  which is like a paused machine waiting to produce numbers on
#  demand (lazy evaluation).



def even_generator(n):
    for i in range(2,n+1,2):
        yield i 

result = even_generator(10) 
for i in result:
    print(i)


# Other methods :     


# 2. Convert it to a list (if you want all values at once)
# python
# result = list(even_generator(10))
# print(result)

# Output:

# [2, 4, 6, 8, 10]
# 3. Use next() to get values one by one
# python
# result = even_generator(10)
# print(next(result))  # 2
# print(next(result))  # 4
# print(next(result))  # 6