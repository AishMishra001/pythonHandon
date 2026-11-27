# find the first none repeated character 

string = "aabccdeeff" 

for char in string : 

    print(char)

    if string.count(char) ==1:
        print("None Repeated Character is :",char)
        

     