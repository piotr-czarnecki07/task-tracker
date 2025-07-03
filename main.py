from datetime import datetime
import json
import argparse
import os

def add(task):
    task = str(task)
    now = datetime.now()
    now_string = now.strftime("%d.%m.%Y %H:%M:%S")

    try:
        with open(f"{path}\\tasks.json") as file:
            python_object = json.load(file)

        last_id = python_object[-1]["task_id"]
        current_id = last_id + 1

        new_task = {
            "task_id" : current_id,
            "task" : task,
            "status" : "todo",
            "created_at" : now_string,
            "updated_at" : now_string
        }

        python_object.append(new_task)

    except FileNotFoundError or json.decoder.JSONDecodeError: # file wasn't created yet or file is empty
        python_object = []
        current_id = 1

        new_task = {
            "task_id" : current_id,
            "task" : task,
            "status" : "todo",
            "created_at" : now_string,
            "updated_at" : now_string
        }

        python_object.append(new_task)

    with open(f"{path}\\tasks.json", "w") as file:
        file.write(json.dumps(python_object))
    print(f"Task added successfully, with ID: {current_id}")

def delete(task_id):
    try:
        task_id = int(task_id)
    except ValueError:
        print("ID must be a number")
        return

    if task_id < 1:
        print("ID must be greater than or equal to 1")
        return

    try:
        with open(f"{path}\\tasks.json") as file:
            python_object = json.load(file)
        
        for i in range(len(python_object)):
            if python_object[i]["task_id"] == task_id:
                python_object.pop(i)
                with open(f"{path}tasks.json", "w") as file:
                    file.write(json.dumps(python_object))
                print(f"Task with ID {i + 1} was deleted successfully")
                return

        print("Task with given ID could not be found")

    except FileNotFoundError or json.decoder.JSONDecodeError: # file wasn't created yet or file is empty
        print("No tasks were added yet")

def update(task_id, task):
    try:
        task_id = int(task_id)
    except ValueError:
        print("ID must be a number")
        return

    if task_id < 1:
        print("ID must be greater than or equal to 1")
        return

    try:
        with open(f"{path}\\tasks.json") as file:
            python_object = json.load(file)
        
        for i in python_object:
            if i["task_id"] == task_id:
                now = datetime.now()
                now_string = now.strftime("%d.%m.%Y %H:%M:%S")

                i["task"] = task
                i["updated_at"] = now_string

                with open(f"{path}\\tasks.json", "w") as file:
                    file.write(json.dumps(python_object))
                print(f"Task updated successfully")
                return

        print("Task with given ID could not be found")

    except FileNotFoundError or json.decoder.JSONDecodeError: # file wasn't created yet or file is empty
        print("No tasks were added yet")

def mark_in_progress(task_id):
    try:
        task_id = int(task_id)
    except:
        print("Incorrect data")
        return

    try:
        with open(f"{path}\\tasks.json") as file:
            python_object = json.load(file)
        
        for i in python_object:
            if i["task_id"] == task_id:
                i["status"] = "in_progress"

                with open(f"{path}\\tasks.json", "w") as file:
                    file.write(json.dumps(python_object))
                print("Status chaned")
                return

        print("Task with given ID could not be found")

    except FileNotFoundError or json.decoder.JSONDecodeError: # file wasn't created yet or file is empty
        print("No tasks were added yet")

def mark_done(task_id):
    try:
        task_id = int(task_id)
    except ValueError:
        print("ID must be a number")
        return

    if task_id < 1:
        print("ID must be greater than or equal to 1")
        return

    try:
        with open(f"{path}\\tasks.json") as file:
            python_object = json.load(file)
        
        for i in python_object:
            if i["task_id"] == task_id:
                i["status"] = "done"

                with open(f"{path}\\tasks.json", "w") as file:
                    file.write(json.dumps(python_object))
                print("Status changed")
                return

        print("Task with given ID could not be found")

    except FileNotFoundError or json.decoder.JSONDecodeError: # file wasn't created yet or file is empty
        print("No tasks were added yet")

def list_all_tasks():
    try:
        with open(f"{path}\\tasks.json") as file:
            python_object = json.load(file)
        
        for i in python_object:
            print(i["task"])

    except FileNotFoundError or json.decoder.JSONDecodeError: # file wasn't created yet or file is empty
        print("No tasks were added yet")

def list_to_do():
    try:
        with open(f"{path}\\tasks.json") as file:
            python_object = json.load(file)

        print('Tasks marked as "to do": ')
        for i in python_object:
            if i["status"] == "todo":
                print(i["task"], end=' ')

    except FileNotFoundError or json.decoder.JSONDecodeError: # file wasn't created yet or file is empty
        print("No tasks were added yet")

def list_done():
    try:
        with open(f"{path}\\tasks.json") as file:
            python_object = json.load(file)

        print('Tasks marked as "done": ')
        for i in python_object:
            if i["status"] == "done":
                print(i["task"], end=' ')

    except FileNotFoundError or json.decoder.JSONDecodeError: # file wasn't created yet or file is empty
        print("No tasks were added yet")

def list_in_progress():
    try:
        with open(f"{path}\\tasks.json") as file:
            python_object = json.load(file)
        
        print('Tasks marked as "in progress": ')
        for i in python_object:
            if i["status"] == "in_progress":
                print(i["task"], end=' ')

    except FileNotFoundError or json.decoder.JSONDecodeError: # file wasn't created yet or file is empty
        print("No tasks were added yet")

functions = {
    "add" : add,
    "delete" : delete,
    "update" : update,
    "mark_in_progress" : mark_in_progress,
    "mark_done" : mark_done,
    "list_all_tasks" : list_all_tasks,
    "list_to_do" : list_to_do,
    "list_done" : list_done,
    "list_in_progress" : list_in_progress
}

parser = argparse.ArgumentParser()
parser.add_argument("function_name")
parser.add_argument("parameters", nargs="*")
args = parser.parse_args()

path = os.getcwd()

if args.function_name in functions:
    try:
        functions[args.function_name](*args.parameters)
    except TypeError:
        print("Given argument caused an exception")
else:
    print("Entered command could not be found")