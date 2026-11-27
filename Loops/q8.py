# List uniqueness checker : check if the list is unique , if duplication found exit the loop and print 


List = ["apple","banana","kiwi","orange","apple","banana","kiwi","orange"]


for i in List:
    if List.count(i)>1 :
        
        print("Duplication element found: ", i)
        break