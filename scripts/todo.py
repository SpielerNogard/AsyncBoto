from beaupy import select_multiple
import os
import json
import argparse
this_dir = os.path.dirname(os.path.abspath(__file__))
TODO_DIR = os.path.join(this_dir, "todos")
os.makedirs(TODO_DIR, exist_ok=True)


def create_new_todo_list(todo_list_name: str):
    """
    Create a new TODO list file with the given name.
    """
    todo_list_path = os.path.join(TODO_DIR, f"{todo_list_name}.json")
    if os.path.exists(todo_list_path):
        print(f"TODO list '{todo_list_name}' already exists.")
        return

    with open(todo_list_path, "w") as f:
        json.dump([], f)
    print(f"TODO list '{todo_list_name}' created.")


def add_todo_item(todo_list_name: str, item: str):
    """
    Add a TODO item to the specified list.
    """
    todo_list_path = os.path.join(TODO_DIR, f"{todo_list_name}.json")
    if not os.path.exists(todo_list_path):
        create_new_todo_list(todo_list_name)
        add_todo_item(todo_list_name, item)

    with open(todo_list_path, "r+") as f:
        todo_list = json.load(f)
        todo_list.append({"item": item, "status": "❌"})
        f.seek(0)
        json.dump(todo_list, f)
    print(f"Added '{item}' to TODO list '{todo_list_name}'.")


def view_todo_list(todo_list_name: str):
    """
    View the items in the specified TODO list.
    """
    todo_list_path = os.path.join(TODO_DIR, f"{todo_list_name}.json")
    if not os.path.exists(todo_list_path):
        print(f"TODO list '{todo_list_name}' does not exist.")
        return

    with open(todo_list_path, "r") as f:
        todo_list = json.load(f)

    print(f"TODO list '{todo_list_name}':")
    ticked = []
    options = []
    for counter, item in enumerate(todo_list):
        options.append(item["item"])
        if item["status"] == "✅":
            ticked.append(counter)
    selected_items = select_multiple(options=options, ticked_indices=ticked)
    for item in selected_items:
        for _todo in todo_list:
            if item == _todo["item"]:
                _todo["status"] = "✅"
                break

    with open(todo_list_path, "w") as f:
        json.dump(todo_list, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage TODO lists.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Command: new
    new_parser = subparsers.add_parser("new", help="Create a new TODO list.")
    new_parser.add_argument("todo_list_name", type=str, help="Name of the TODO list to create.")

    # Command: add
    add_parser = subparsers.add_parser("add", help="Add a TODO item to a list.")
    add_parser.add_argument("todo_list_name", type=str, help="Name of the TODO list.")
    add_parser.add_argument("todo", type=str, nargs="+", help="TODO item to add.")

    # Command: view
    view_parser = subparsers.add_parser("view", help="View a TODO list.")
    view_parser.add_argument("todo_list_name", type=str, help="Name of the TODO list to view.")

    args = parser.parse_args()

    if args.command == "new":
        create_new_todo_list(args.todo_list_name)
    elif args.command == "add":
        add_todo_item(args.todo_list_name, " ".join(args.todo))
    elif args.command == "view":
        view_todo_list(args.todo_list_name)
