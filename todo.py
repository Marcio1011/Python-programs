#Initial user prompt
user_prompt = "Enter a todo:"

#Create an empty list
todos = []

#While loop
while True:
    #Gets the user input
    todo = input(user_prompt)
    #Append the input in the list
    todos.append(todo)
    #Prints the list
    print(todos)
