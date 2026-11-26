#Grade Calculator 
# A (90-100) , B (80-89) , C (70-79) , D (60-69) , F (<60) 


Marks = int(input("Enter your marks : ")) 

Grade = "A" if Marks >= 90 else "B" if Marks >=80 else "C" if Marks >= 70 else "D" if Marks >=60 else "F" 

print("Grade = ", Grade) 