import json 

message = '''
---TO-DO LIST---
Type
1. to add task
2. to view task
3. to delete task 
4. to mark task as done
5. to exit
'''


# Load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            normalized = []

            if isinstance(tasks, list):
                for item in tasks:
                    if isinstance(item, dict):
                        normalized.append({
                            "Title": item.get("Title", item.get("title", "")),
                            "Done": bool(item.get("Done", item.get("done", False)))
                        })
                    elif isinstance(item, str):
                        normalized.append({"Title": item, "Done": False})
                return normalized

            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to the todo file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    
# Show menu
def show_menu():
    print(message)

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"Title": task, "Done": False})
    save_tasks(tasks)
    print("Your task has been added")
    
# View tasks
def view_tasks(tasks):
    if tasks:
        print("\nYour tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task["Done"] else "Not Done"
            print(f"{i + 1}. {task['Title']} - {status}")
    else:
        print("You do not have any saved tasks yet.")
            
# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task you want to delete it: "))
        if 0 <= (index - 1) < len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Task number {index} has been deleted: {removed}")
        else:
            print("invalid index number!")
    except ValueError:
        print("Enter a valid number")
        
# Mark task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Number of the task you want to mark as done: "))
        if 0 <= (index - 1) < len(tasks):
            tasks[index - 1]["Done"] = True
            save_tasks(tasks)
            print(f"Task number {index} has been marked as done: {tasks[index - 1]}")
        else:
            print("invalid index number!")
    except ValueError:
        print("Enter a valid number")

# Main program
def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = (input("Choose an option: "))
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Enter a valid option")
        
# Run the app
if __name__ == "__main__":
    main()