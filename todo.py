
#Create an empty list
todos = []

#While loop
while True:
    #Gets the user input
    user_action = input("Type add,show or exit: ")
    user_action = user_action.strip() #in case we accidentally write add,show or exit with a space after this method will remove the extra space
#Varies between the user selections and do something depending on the selection
    match user_action:
#if the user select add it will add an item to the list
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo) #Append the input in the list
#If the user select show it will print the list
        case 'show':
            for item in todos: #will print the items in the list one by one with no bracts
                print(item)
        case 'exit':
            break  #if the user selects exit it will break the loop and exit the program

print("Bye!")
