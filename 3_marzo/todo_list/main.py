# Functions

# Variables
tasksList = []
checked = ""
increment = 0

# Classes
class Task:
  def __init__(self, title, id, status):
    self.title = title
    self.id = id
    self.status = status

# Main
while True:
  print("1. Add task")
  print("2. Get tasks")
  print("3. Check task")
  print("4. Delete task")
  print("5. Exit")

  choice = input("Choose an option: ")

  if choice == "1":
    increment += 1
    title = input("Enter task title: ")
    id = increment
    status = False
    task = Task(title, id, status)
    tasksList.append(task)
    print("Task added successfully!")

  elif choice == "2":
    for task in tasksList:
      if task.status == True:
        checked = "X"
        print(f"[{checked}] {task.title}")
        checked = ""
      else:
        print(f"[{checked}] {task.title}")

  elif choice == "3":
    taskId = int(input("Join task ID: "))
    for task in tasksList:
      if task.id == taskId : task.status = True

  elif choice == "5":
    break

  else:
    print("Type a valid option, please!")