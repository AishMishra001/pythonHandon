# age group categorization based on input 
# child (0-12) , teenager (13-17) , adult(18-64), senior (65+)

age = int(input("Enter your age : "))

if( age <= 12):
    print("child")
elif( age < 18):
    print("teenager")
elif(age < 65):
    print("adult")
else:
    print("senior")