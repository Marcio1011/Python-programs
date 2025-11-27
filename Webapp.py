import streamlit as st
import functions  # Custom module handling reading/writing todos from storage

# Load existing todos when the app starts
# This typically reads todos from a text file or database
todos = functions.get_todos()


def add_todo():
    """
    Triggered automatically when the text input changes.
    - Retrieves the string the user typed into the input field.
    - Adds a newline (for text-file formatting).
    - Appends the new todo to the list.
    - Saves the updated list to persistent storage.
    """
    todo = st.session_state["new_todo"] + "\n"   # Retrieve todo text from session state
    todos.append(todo)                           # Add new todo to the list
    functions.write_todos(todos)                 # Save updated list externally


# ----------------------
#       UI SECTION
# ----------------------

# Main title displayed at the top of the page
st.title("My Todo App")

# Additional UI text for context
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

# Loop through all todo items and create a checkbox for each
# enumerate() provides both index and text of each todo
for index, todo in enumerate(todos):
    # Each checkbox uses the todo text as the unique session key
    checkbox = st.checkbox(todo, key=todo)

    # If a checkbox is checked, the todo is considered "completed"
    if checkbox:
        todos.pop(index)                 # Remove the completed todo
        functions.write_todos(todos)     # Save updated todo list
        del st.session_state[todo]       # Remove checkbox state from session
        st.rerun()                       # Reload app to refresh UI


# Text input for adding new todo items
# - `on_change=add_todo` triggers the function when user submits
# - Stored in session_state under key 'new_todo'
st.text_input(
    label="",                             # No label for cleaner UI
    placeholder="Add new todo...",        # Hint text for the user
    on_change=add_todo,                   # Function called when input changes
    key='new_todo'                        # Stores the input text
)
