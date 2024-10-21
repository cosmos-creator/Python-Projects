import json, os
path = r"tasks.json"
empty = 0
try:
    with open(path) as file:
        file.seek(0)
        tasks = json.load(file) # converts to a python list
        empty = 0 if not tasks else 1
        print("Current tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
except FileNotFoundError:
    print("File not found. Creating new...")
    with open(path,"w") as file:
        json.dump([],file)
        print("File Created.")
except Exception as e:
    print(f"Error occurred: {e}")
    exit()

def methods():
    print("\n1. Add\n2. Delete\n3. Quit")
    answer = int(input("Option: "))
    if answer == 1:
        add()
    elif answer == 2:
        deleteTask() if empty else print("No tasks to delete.")
    else:
        print("Quitting...")
        exit()
    return answer
def add():
    while True:
        task = input("Enter task: ")
        try:
            with open(path,"+r") as file:
                data = json.load(file)
                data.append(task)
                file.seek(0)
                json.dump(data,file,indent=4)
                print("Task Added.")
                file.truncate()
        except Exception as e:
            print(f"Error occurred: {e}")
        more = input("Add More? [Y/N]: ")
        if more.lower() == 'n':
            break
def deleteTask():
    while True:
        delTask = int(input("Task ID to delete: "))
        try:
            with open(path,"r+") as file:
                tasks = json.load(file) # change into python list/array
                if (len(tasks) < delTask-1 or delTask <= 0):
                    print(f"No task with id {tasks}.")
                    continue
                tasks.pop(delTask-1)
                file.seek(0)
                json.dump(tasks,file,indent=4)
                print("Tasks Deleted.")
                file.truncate()
        except Exception as e:
            print(f"Error occurred: {e}")
        if not tasks:
            print("No more tasks to delete.")
            break
        delMore = input("Delete more tasks? [Y/N]: ")
        if delMore.lower() == 'n':
            break
        else:
            os.system('cls')
            # tasks with updated ID's
            print("Current tasks: ")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

methods()
