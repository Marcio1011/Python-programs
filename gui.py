import functions                          # Custom module for handling reading/writing todos
import FreeSimpleGUI as sg                # GUI library, imported as 'sg' for convenience
import time                                # For displaying the current time in the app
import os                                  # For interacting with the operating system (file checks, etc.)

# --- ENSURE TODO FILE EXISTS ---
if not os.path.exists("todo.txt"):        # Check if the todo file exists
    with open("todo.txt", "w") as file:   # If not, create an empty file
        pass

# Set the visual theme for the GUI
sg.theme("Black")

# --- GUI ELEMENT DEFINITIONS ---
clock = sg.Text('', key='clock')          # Text element to display a live clock
label = sg.Text("Type in a To-Do")        # Label prompting the user what to do
input_box = sg.InputText(
    tooltip="Enter todo", key="todo"      # Input field where user types a new todo
)

add_button = sg.Button("Add")             # Button to add a new todo

list_box = sg.Listbox(
    values=functions.get_todos(),         # Display current todos from the file
    key='todos',                           # Key used to reference this listbox in events
    enable_events=True,                    # Allow clicking/selecting items to trigger events
    size=[45, 10]                          # Width and height of the listbox
)

edit_button = sg.Button("Edit")           # Button to edit the selected todo
complete_button = sg.Button("Complete")   # Button to mark a todo as complete (removes it)
exit_button = sg.Button("Exit")           # Button to exit the app

# --- WINDOW SETUP ---
window = sg.Window(
    'My To-Do App',                        # Window title
    layout=[                                # Defines the layout of elements (each inner list is a row)
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button]
    ],
    font=('Helvetica', 20)                  # Sets a consistent font for readability
)

# --- MAIN EVENT LOOP ---
while True:
    event, values = window.read(timeout=200)       # Read GUI events, update every 200ms
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))  # Update clock display

    match event:                                  # Handle different actions based on what the user does

        case "Add":                               # When the Add button is clicked
            todos = functions.get_todos()        # Load existing todos
            new_todo = values['todo'] + "\n"     # Get new todo text and add newline
            todos.append(new_todo)               # Add it to the list
            functions.write_todos(todos)         # Save updated todos to file
            window['todos'].update(values=todos) # Refresh the listbox display

        case "Edit":                              # When the Edit button is clicked
            try:
                todo_to_edit = values['todos'][0]    # Get the selected todo
                new_todo = values['todo']           # Get new text from input

                todos = functions.get_todos()       # Load current todos
                index = todos.index(todo_to_edit)   # Find index of selected todo
                todos[index] = new_todo             # Replace old todo with new text
                functions.write_todos(todos)       # Save updated list
                window['todos'].update(values=todos) # Refresh display
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))  # Warn if no selection

        case "Complete":                          # When Complete button is clicked
            try:
                todo_to_complete = values['todos'][0] # Get selected todo
                todos = functions.get_todos()        # Load current todos
                todos.remove(todo_to_complete)       # Remove the selected todo
                functions.write_todos(todos)        # Save updated list
                window['todos'].update(values=todos) # Refresh display
                window['todo'].update(value='')      # Clear input field
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))  # Warn if nothing selected

        case "Exit":                               # When Exit button is clicked
            break                                  # Exit the event loop

        case 'todos':                              # When a todo item is selected from the listbox
            window['todo'].update(value=values['todos'][0]) # Fill input box for easy editing

        case sg.WIN_CLOSED:                        # When window is manually closed
            break                                  # Exit the loop

# --- CLEANUP ---
window.close()                                   # Close the GUI window gracefully
