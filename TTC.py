# importing the necessary modules
from datetime import datetime
import os
import json

# setup for the rest of code
if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as file:
        data = {
            "empty": 0,
            "tasks": [],
            "todo": {},
            "in-progress": {},
            "done": {}
        }
        json.dump(data, file, indent=4)

# functions to be used in the code
def add_task(description, current_time):
    id = 0
    task = {}
    data = {} 

    with open("tasks.json", "r") as file:
        data = json.load(file)
        task = { 
            "id": len(data["tasks"]),
            "description": description,
            "status": "todo",
            "created": current_time,
            "updated": current_time
        }

        if data["empty"] >= len(data["tasks"]):
            data["tasks"].append(task)
            data["empty"] = len(data["tasks"])
        else:
            data["tasks"]
            id = data["empty"]
            for n in data["tasks"][data["emppty"]:len(data["tasks"])]:
                if n == 0:
                    task = {
                        "id": id,
                        "description": description,
                        "status": "todo",
                        "created": current_time,
                        "updated": current_time
                    }
                    data["tasks"][id] = task
                    break
                id += 1
                
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
    
    return id

def update_task(id, description, current_time):
    data = {}
    with open("tasks.json", "r") as file:
        data = json.load(file)
        data["tasks"][id]["description"] = description
        data["tasks"][id]["updated"] = current_time

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)

def can_be_int(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def delete_task(id):
    # This function deletes a task from the json file
    pass

while True:
    # This is the commands sectino
    # We handle all commands here
    cmd = input("task-cli ").split()

    if cmd[0] == "exit":
        break
    
    elif cmd[0] == "add":
        description = " ".join(cmd[1:]).strip(" \"")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        id = add_task(description, current_time)
        print(f"Task added successfully (ID: {id})")
    
    elif cmd[0] == "update":
        if len(cmd) < 3 and can_be_int(cmd[1]):
            print("Invalid command")
        else:
            id = int(cmd[1])
            description = " ".join(cmd[2:]).strip(" \"")
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            update_task(id, description, current_time)
            print(f"Successfully updated task (ID: {id})")
    
    elif cmd[0] == "delete":
        pass # to be implemented
    
    elif cmd[0] == "mark-in-progress":
        pass # to be implemented
    
    elif cmd[0] == "mark-done":
        pass # to be implemented
    
    elif cmd[0] == "list":
        if len(cmd) == 1:
            pass # to be imp
    
    else:
        print("Invalid command")