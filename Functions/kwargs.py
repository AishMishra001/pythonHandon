# function with **kwargs : it allows to pass multiple keyword arguments to a function  when the number of arguments are unknown 

def student(**kwargs):
    # print(kwargs)
    for key,value in kwargs.items():
        print(key," : ", value) 

student(name = "John", age = 20, city = "New York")
student(name = "Aisha", age = 21, course = "Computer Science")
student(name = "Akash", age = 22, course = "Maths", roll_no = 123)