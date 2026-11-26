model_types = { 'openai' : 'gpt' , 'google' : 'gemini' , 'anthropic' : 'claude' }

print(model_types)

for types in model_types : 
    print(types , " : " , model_types[types])


# using items() method
for key , value in model_types.items():
    print(key , ' : ' , value)    

# output of above code is 
# openai  :  gpt
# google  :  gemini
# anthropic  :  claude

squares = {number : number**2 for number in range(11)}

print(squares)

keys = ["apple","banana","cherry","dates","elderberry"]  

daufault_value = "fruit" 

new_dict = dict.fromkeys(keys,daufault_value)

print(new_dict)

# output : {'apple': 'fruit', 'banana': 'fruit', 'cherry': 'fruit', 'dates': 'fruit', 'elderberry': 'fruit'}