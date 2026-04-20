# create empty list
tasks = []

def add_task():
    enterTask = input("Enter Task: ")
    tasks.append(enterTask)
    print(f"'{enterTask.upper()}' added successfully.")

def list_tasks():
    # loop through tasks and enumerate
    for index, task in enumerate(tasks):
        print(f"{index+1}. {task}")

def del_task():
    for index, task in enumerate(tasks):
        print(f"{index+1}. {task}")
    delete = input("Enter task you want to delete: ")
    # remove by value
    tasks.remove(delete)
    print(f"'{delete.upper()}' deleted successfully.")


def main():
    while True:
        # prompt user
        print('''
            1. Add Task
            2. List Tasks
            3. Delete Task
            4. Quit
        ''')

        choice = input("Choose: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            del_task()
        elif choice == '4':
            break
        else:
            print("Invalid Input!")

main()