import csv
import sys
import pandas as pd
import tkinter as tk

def main():
    #root = tk.Tk()
    #root.title("To Do List")
    #label = tk.Label(root, text="Hello")
    #label.pack()
    #root.mainloop()
    #menucheck()
    while True:
        try:
            choice = int(input("Enter a number for your task of choice: "))
            if choice == 1:
                addTask()
            elif choice == 2:
                viewTask()
            elif choice == 3:
                removeTask()
            elif choice == 4:
                taskComplete()
            elif choice == 5:
                sys.exit("Exiting Program")
            else:
                print("Please enter a number 1-5")
        except ValueError:
            print("Please enter a valid choice")
    
    
def menucheck():
    print("To Do List Menu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Mark Task as Complete")
    print("5. Exit")
    
    
def addTask():
    counter = 1
    with open("todolist.csv") as file:
        next(file)
        for line in file:
            counter = counter + 1
            
    while True:
        newtask = input("Enter a task to be added to your to do list or type 'exit' to finish: ")
        if newtask.lower() == 'exit':
            sys.exit()
        else:
            with open("todolist.csv", "a", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["counter", "tasks"], delimiter=":")
                writer.writerow({"counter": counter, "tasks": newtask})
        counter = counter + 1


def viewTask():
    with open("todolist.csv") as file:
        print("=== To Do List ===")
        next(file)
        for line in file:
            print(line.strip())
    sys.exit()

    
def removeTask():
    with open("todolist.csv") as file:
        print("=== To Do List ===")
        next(file)
        for line in file:
            print(line.strip())
    while True:
        option = input("Enter the number of the task you wish to remove or type 'exit' to finish: ")
        if option.lower() == "exit":
            sys.exit()
        else:
            newrows = []
            with open("todolist.csv", "r", newline='') as file:
                reader = csv.DictReader(file, delimiter=":")
                for row in reader:
                    if row["counter"] != option:
                        newrows.append(row)
                    else:
                        pass
                
            for index, row in enumerate(newrows, start=1):
                row["counter"] = index
                
            with open("todolist.csv", "w", newline='') as file:
                file.write("counter:tasks\n")
                writer = csv.DictWriter(file, fieldnames=["counter", "tasks"], delimiter=":")
                for row in newrows:
                    writer.writerow(row)
    
    
def taskComplete():
    with open("todolist.csv") as file:
        print("=== To Do List ===")
        next(file)
        for line in file:
            print(line.strip())
            
    while True:
        found = False
        option = input("Enter the number of the task you wish to mark as complete or type 'exit' to finish: ")
        message = " - (Task Completed)"
        if option.lower() == "exit":
            sys.exit()
        else:
            newrows = []
            with open("todolist.csv", "r", newline='') as file:
                reader = csv.DictReader(file, delimiter=":")
                for row in reader:
                    if row["counter"] == option:
                        found = True
                        if message not in row["tasks"]:
                            row["tasks"] += message
                            print("Task marked as complete.")
                    newrows.append(row)
            if not found:
                print("Task not found")
                continue
                      
            with open("todolist.csv", "w", newline='') as file:
                file.write("counter:tasks\n")
                writer = csv.DictWriter(file, fieldnames=["counter", "tasks"], delimiter=":")
                for row in newrows:
                    writer.writerow(row)
    

if __name__ == "__main__":
    main()
    