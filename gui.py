import functions                          # Imports custom functions used for reading and writing todo items
import FreeSimpleGUI as sg                # Imports the GUI library under a shorter alias for convenience

# --- GUI ELEMENT DEFINITIONS ---

label = sg.Text("Type in a To-Do")        # Creates a text label to instruct the user what to enter
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# Creates an input field where the user types a todo item. The 'key' identifies this field in events.

add_button = sg.Button("Add")             # Button that adds a new todo item to the list

list_box = sg.Listbox(
    values=functions.get_todos(),         # Loads current todos from the file and shows them in the listbox
    key='todos',                          # Key used to reference the listbox in events
    enable_events=True,                   # Enables event triggering when the user selects an item
    size=[45, 10]                         # Sets the width and height of the listbox
)

edit_button = sg.Button("Edit")           # Button that replaces the selected todo with updated text
complete_button = sg.Button("Complete")   # Button that marks the selected todo as completed (removes it)
exit_button = sg.Button("Exit")           # Button that closes the application

# --- WINDOW SETUP ---

window = sg.Window(
    'My To-Do App',                       # Title of the application window
    layout=[                              # GUI layout: each inner list represents a row
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button]
    ],
    font=('Helvetica', 20)                # Sets a uniform large font for readability
)

# --- EVENT LOOP ---

while True:
    event, values = window.read()         # Waits for any user interaction and returns the event and input values
    print(1, event)                       # Debug output: prints which event occurred
    print(2, values)                      # Debug output: prints all current GUI input values
    print(3, values['todos'])             # Debug: prints currently selected todo item(s)

    match event:                          # Pattern matching to handle different user actions

        case "Add":                       # Triggered when the Add button is clicked
            todos = functions.get_todos() # Loads the existing list of todos from the file
            new_todo = values['todo'] + "\n"  # Gets the user-entered text and ensures proper newline format
            todos.append(new_todo)        # Adds the new todo to the list
            functions.write_todos(todos)  # Saves the updated list back to the file
            window['todos'].update(values=todos)  # Refreshes the listbox display

        case "Edit":                      # Triggered when the Edit button is clicked
            todo_to_edit = values['todos'][0]   # Gets the currently selected todo item
            new_todo = values['todo']          # Gets the new replacement text from the input field

            todos = functions.get_todos()      # Loads the current list of todos
            index = todos.index(todo_to_edit)  # Finds the position of the selected item in the list
            todos[index] = new_todo            # Replaces the old todo with the new text
            functions.write_todos(todos)       # Saves the updated list
            window['todos'].update(values=todos)  # Updates the listbox display

        case "Complete":                  # Triggered when the Complete button is clicked
            todo_to_complete = values['todos'][0]  # Gets the selected todo item
            todos = functions.get_todos()         # Loads current todos
            todos.remove(todo_to_complete)        # Removes the selected item from the list
            functions.write_todos(todos)          # Saves the updated list
            window['todos'].update(values=todos)  # Updates the listbox
            window['todo'].update(value='')       # Clears the input field after completing the item

        case "Exit":                      # Triggered when the Exit button is clicked
            break                         # Breaks the loop and exits the program

        case 'todos':                     # Triggered when a todo item is selected in the listbox
            window['todo'].update(value=values['todos'][0])
            # Fills the input box with the selected todo for easy editing

        case sg.WIN_CLOSED:               # Triggered when the user manually closes the window
            break                         # Exits the program loop

# --- CLEANUP ---

window.close()                            # Closes the application window gracefully


