status = True
tasks = {}


def add_task():
    new_task = input("Enter Task: ")
    tasks[new_task] = status
    print(f"'{new_task.capitalize()}' added successfully.")


def list_tasks():
    # print(tasks)
    for index, key in enumerate(tasks.keys()):
        print(f"{index+1}. {key}")


def mark_done():
    print("\n\t=== YOUR TASKS ===")
    for index, (key, value) in enumerate(tasks.items()):
        print(f"\t{index+1}. {key}: {'pending' if value == True else 'DONE'}")
    marked_task = input("Enter Task to mark as DONE: ")
    if marked_task in tasks:
        tasks[marked_task] = False
        if marked_task in tasks and tasks[marked_task] == False:
            # print(f"Specific task {marked_task} located")
            # del tasks[marked_task]
            # scope test: print(tasks)
            tasks[marked_task] = False
            print(f"{marked_task} ")
            for index, (key, value) in enumerate(tasks.items()):
                print(f"{index+1}. {key}: {'DONE' if value == False else 'pending'}")

        # debug: print(tasks)


def del_task():
    for index, (key, value) in enumerate(tasks.items()):
        print(f"{index+1}. {key}: {'pending' if value == True else 'DONE'}")

    deleted_task = input("Enter task to delete: ")
    if deleted_task in tasks:
        del tasks[deleted_task]
        print(f"'{deleted_task.capitalize()}' deleted successfully.")


def main():
    while True:
        print(
            """
        1. Add Task
        2. Lists Tasks
        3. Mark Task as DONE
        4. Delete Task
        5. Quit
        """
        )

        choice = input("Choose: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            del_task()
        elif choice == "5":
            break
        else:
            print("Invalid Input!")


main()
