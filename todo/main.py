# List to store tasks
todo_list = []

# Function to add a task
def add_task():
    try:
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f" Added: '{task}'")
    except Exception as e:
        print(f" Error while adding task: {e}")

# Function to show all tasks
def show_tasks():
    try:
        if not todo_list:
            print(" Your TODO list is empty.")
        else:
            print("\n Here are your tasks:")
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")
            print("End of list.")
    except Exception as e:
        print(f" Error while showing tasks: {e}")

# Function to delete a task by number
def delete_task():
    try:
        show_tasks()
        if todo_list:
            num = int(input("Enter the task number to delete: "))
        # Check first if the number is at least 1 and Then check if it’s not bigger than the number of tasks.
        if num >= 1 and num <= len(todo_list):
                removed_task = todo_list.pop(num - 1)
                print(f"Great! '{removed_task}' removed.")
                print(f"Now you have {len(todo_list)} tasks left.")
        else:
                print("Oops! That task number doesn't exist. Please pick a correct one.")

    except Exception as e:
        print(f" Error while deleting task: {e}")

# Main menu loop
def main():
    while True:
        print("\n======== TODO MENU ========")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Exit")
        print("===========================")

        try:
            choice = input("Choose an option (1-4): ")
            if choice == '1':
                add_task()
            elif choice == '2':
                show_tasks()
            elif choice == '3':
                delete_task()
            elif choice == '4':
                print(" Exiting!")
                break
            else:
                print(" Invalid option. Try again.")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the app
main()
