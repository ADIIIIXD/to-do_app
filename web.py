import streamlit as st
import functions

todos = functions.get_todo()


def add_todo():
    todo_ = st.session_state["add"] + "\n"
    todos.append(todo_)
    functions.write_todo(todos)


st.title("My TO-DO List")
st.subheader("This is my to-do app")
st.write("this app is to make your life easy")

for index, tod in enumerate(todos):
    checkbox = st.checkbox(tod, key=tod)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[tod]
        st.experimental_rerun()

st.text_input(label="Enter a to-do item", placeholder="Add a To-Do Item...",
              on_change=add_todo, key="add")