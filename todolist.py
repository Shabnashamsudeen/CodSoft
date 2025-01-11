# TO DO LIST
todo_list = []

def Addlist():
    item = input("Enter a new task: ")
    todo_list.append(item)
    print(f"{item} added to do list")

def Displaylist():
    print("TO DO List:")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index} - {item}")

def Removelist():
    Displaylist()
    index = int(input("Enter your item number to remove: ")) - 1
    if 0 <= index < len(todo_list):
        removed_item = todo_list.pop(index)
        print(f"{removed_item} removed from list")
    else:
        print("Invalid input")

while True:
    print("TO DO List app")
    print("1- Add to list")
    print("2- Display to list")
    print("3- Remove from list")
    print("4- Exit")

    option = input("Select your option: ")

    if option == '1':
        Addlist()
    elif option == '2':
        Displaylist()
    elif option == '3':
        Removelist()
    elif option == '4':
        print("Exiting...")
        break
    else:
        print("Invalid option")