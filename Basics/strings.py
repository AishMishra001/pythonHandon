chai = "masala chai" 

print(chai.replace("masala","ginger"))

print(chai) 

types = "masala , ginger , lemon , new"

print(types.split(", ")) # output : ['masala', 'ginger', 'lemon', 'new']


order = 'I order {} cups of {} chai'

print(order.format(1, "lemon")) # output : I order 1 cups of lemon chai

Ai_model_types = ['gemini' , 'chatgpt' , 'claude' , 'perplexity'] 
print(" and ".join(Ai_model_types)) # output : gemini and chatgpt and claude and perplexity

print(len(types)) # output : 27 

for letters in types : 
    print(letters)  # it print each letter in types including spaces 