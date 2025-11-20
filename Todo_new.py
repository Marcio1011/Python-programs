import functions  # Imports a custom module that handles reading and writing the todo list from a file
import time  # Imports Python's time module for working with date and time

now = time.strftime("%b %d, %Y %H:%M:%S")  # Generates a formatted string representing the current date and time
print("It is", now)  # Displays the current date and time to the user

while True:  # Starts an infinite loop to repeatedly ask the user for actions
    user_action = input("Type add,show,edit, complete or exit: ")  # Requests a command from the user
    user_action = user_action.strip()  # Removes extra spaces at the beginning or end of the input

    if user_action.startswith('add'):  # Checks if the user wants to add a new todo item
        todo = user_action[4:]  # Extracts the text after the word 'add' to get the todo content

        todos = functions.get_todos()  # Reads the current list of todos from the file

        todos.append(todo + '\n')  # Adds the new todo item to the list, ensuring a newline for file formatting
        functions.write_todos(todos)  # Saves the updated list back to the file


    elif user_action.startswith('show'):  # Checks if the user selected the 'show' command
        todos = functions.get_todos()  # Reads the existing todos from the file

        for index, item in enumerate(todos):  # Loops through each todo with its index
            item = item.strip('\n')  # Removes the newline character from the item
            row = f"{index + 1}. {item}"  # Formats the item with a human-friendly numbering starting at 1
            print(row)  # Prints the formatted todo entry


    elif user_action.startswith('edit'):  # Checks if the user wants to edit an existing todo
        try:
            number = int(user_action[5:])  # Converts the number after 'edit' to an integer (the item to modify)
            number = number - 1  # Converts the user’s number into a zero-based list index

            todos = functions.get_todos()  # Reads the current list of todos

            new_todo = input("Enter new todo: ")  # Asks the user for the updated todo text
            todos[number] = new_todo + '\n'  # Replaces the selected item with the new text

            functions.write_todos(todos)  # Saves the updated list back to the file

        except ValueError:  # Triggered when the user enters invalid input (e.g., letters instead of numbers)
            print("Your command is not valid.")
            continue  # Restarts the loop without crashing the program


    elif user_action.startswith('complete'):  # Checks if the user wants to mark a todo as completed (remove it)
        try:
            number = int(user_action[9:])  # Extracts the number after 'complete' and converts it to an integer

            todos = functions.get_todos()  # Reads the current list of todos

            index = number - 1  # Converts the number to a zero-based index
            todo_to_remove = todos[index].strip('\n')  # Gets the text of the todo to remove (without newline)
            todos.pop(index)  # Removes the selected todo from the list

            functions.write_todos(todos)  # Writes the updated list back to the file

            message = f"Todo '{todo_to_remove}' was removed from the list"  # Builds a confirmation message
            print(message)  # Displays confirmation to the user

        except IndexError:  # Triggered when user enters a number outside the range of the list
            print("There is no item with that number.")
            continue  # Restarts the loop without stopping the program


    elif user_action.startswith('exit'):  # Checks if the user wants to exit the program
        break  # Exits the infinite loop and ends the program


    else:
        print("Command is not valid")  # Handles any unrecognized command from the user

print("Bye!")  # Prints a farewell message after exiting the loop
