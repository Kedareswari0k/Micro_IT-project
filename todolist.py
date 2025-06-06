import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks to show.")
    else:
        print("\n📝 To-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✅" if task['completed'] else "❌"
            print(f"{idx}. {status} {task['title']} - {task['description']}")

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description, "completed": False})
    print("✅ Task added successfully!")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            print("🎉 Task marked as complete!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def edit_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            tasks[index]['title'] = new_title
            tasks[index]['description'] = new_description
            print("✏️ Task updated!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Task '{removed['title']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n📋 MENU:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
