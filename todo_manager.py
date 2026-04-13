import os
DEFAULT_FILE = "todo.txt"

# Create / Reset Todo File

def create_file(filename=DEFAULT_FILE):
    with open(filename, "w") as f:
        f.write("Hello! Your Daily To-Do List:\n")
    print(f"File '{filename}' created/reset successfully.")


# Add Tasks

def add_tasks(filename=DEFAULT_FILE):
    print("\nEnter your tasks one by one. Type 'done' to finish.\n")

    with open(filename, "a") as file:
        while True:
            task = input("Enter task: ")
            if task.lower() == "done":
                break
            file.write(task + "\n")
            print("Task added successfully!")

# Rename File

def rename_file(old_name):
    choice = input("Do you want to rename the file? (yes/no): ")

    if choice.lower() in ["yes", "y"]:
        new_name = input("Enter new file name: ")

        if not os.path.exists(old_name):
            print("Error: File does not exist.")
            return old_name

        try:
            os.rename(old_name, new_name)
            print(f"File renamed from '{old_name}' to '{new_name}'.")
            return new_name
        except PermissionError:
            print("Error: Permission denied while renaming.")
            return old_name

    return old_name


# Delete File

def delete_file(filename):
    choice = input("Do you want to delete the file? (yes/no): ")

    if choice.lower() in ["yes", "y"]:
        if not os.path.exists(filename):
            print("Error: File does not exist.")
            return

        try:
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        except PermissionError:
            print("Error: Permission denied while deleting.")
    else:
        print("File was not deleted.")

# Main Program

def main():
    file_name = DEFAULT_FILE

    create_file(file_name)
    add_tasks(file_name)
    file_name = rename_file(file_name)
    delete_file(file_name)


if __name__ == "__main__":
    main()
