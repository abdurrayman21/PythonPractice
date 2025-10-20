import json

file_name = "todo_list.json"

def load_task():
    try:
     with open(file_name, "r") as file:
         return json.load(file)
    except:
        return {"tasks": []}

def save_task(task):
    try:
        with open(file_name, "w") as file:
            return json.dump(task, file, indent=4)
    except:
       print("failed to save task")

def view_task(tasks):
    task_list = tasks["tasks"]
    if len(tasks["tasks"]) == 0:
     print("no tasks to display")
    for idx, task in enumerate(task_list):
        status = "[completed]" if task["completed"] else "[pending]"
        print(f"{idx + 1}. {task['description']} | {status}")
def create_task(tasks):
    description = input("enter description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "completed": False})
        save_task(tasks)
        print("text added")
def mark_task_complete(tasks):
    view_task(tasks)
    try:
        task_number = int(input("Enter task number: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["completed"] = True
            save_task(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_task()
    print(tasks)

    while True:
        print("welcome")
        print("1. view task")
        print("2. add task")
        print("3. complete task")
        print("4. quit task/exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()