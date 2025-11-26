import streamlit as st
import functions

# Load existing todos
todos = functions.get_todos()

def add_todo():
    """
    Adds a new todo item from the text input,
    writes it to the list, and updates the storage.
    """
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# App Title and Description
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

# Display todo items
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# Input field for new todos
st.text_input(
    label="",
    placeholder="Add new todo...",
    on_change=add_todo,
    key='new_todo'
)
