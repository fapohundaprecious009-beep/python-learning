def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)


while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action == 'add':
        todo = input("Enter a todo: ") + "\n"

        todos = get_todos()
        todos.append(todo)

        write_todos(todos)

    elif user_action == 'show':
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action == 'edit':
        number = int(input("Number of the todo to edit: "))

        todos = get_todos()

        new_todo = input("Enter new todo: ") + "\n"
        todos[number - 1] = new_todo

        write_todos(todos)

    elif user_action == 'exit':
        break

    else:
        print("Invalid command.")

print("Goodbye!")