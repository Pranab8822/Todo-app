import os
import json


class Task_Manager:
    def __init__(self):
        self.tasks = "tasks.json"
        self.users_db=self.load_tasks()
        
    def load_tasks(self):     #checking file in the system
        if os.path.exists(self.tasks):  
            try:
                with open(self.tasks, "r") as f:
                    return json.load(f) 
            except (json.JSONDecodeError, IOError): 
                return {}
        return {}
    
    # function for creating new accounnt
    def Acc_creation(self):
        user_name=input("Create username: ")
        if len(user_name) < 5:
            print("Username length should be more than 8 characters.")
            return{}
        if user_name in self.users_db:
            print("Username already exists.")
            return
        else:
            Password=input("Enter password: ")
            if len(Password) < 8: 
                print("Username length should be more than 8 characters with special characters.") 
        # Create user with password + empty tasks list
        self.users_db[user_name] = {
            "password": Password,
            "tasks":[]
        }
        self.save_tasks()
        print("Account created successfully. Please login to continue. ")
        self.task_oper(user_name)

    # function for login
    def login(self):                     
        print("--- SYSTEM LOGIN ---")
        username = input("Enter your username: ")
        if username not in self.users_db:
            print("Username not found in database.")
            return None
        attempt=3
        while attempt > 0:
            password = input("Enter your password: ") # Check if password matches the one stored for that specific user
            if password == self.users_db[username]["password"]:
                print("Logged in successfully!")
                self.task_oper(username)
                return # Proceed to next step
            else:
                attempt -=1
                # Give feedback on failure
                print("Incorrect password. Please try again.")
                  
        print("Too many failed attempt")    

    #function for adding new task to the database
    def add_task(self,username):
        task=input("Enter the task you want to add: ")
        self.users_db[username]["tasks"].append(task)
        self.save_tasks()
        print("Task added successfully.")

    #function for Saving users_db to JSON file.
    def save_tasks(self):               
        with open(self.tasks, "w") as f:
            json.dump(self.users_db, f, indent=4)

    #function for removing task
    def remove_task(self,username):
        user_task=self.users_db[username]["tasks"]
        try:
            if not user_task:
                print("No task to delete.")
                return
            print("-----CURRENT TASK IN YOUR DASHBOARD-----")
            for task in user_task:
                print(task)
            task_to_delete= input("\nEnter the task you want to delete: ")

            if task_to_delete in user_task:
                user_task.remove(task_to_delete)
                self.save_tasks()
                print(f"{task_to_delete} removed successfully")
            else:
                print("Task not found ")   
        except ValueError:
            print("Invalid input")  

    #function for viewing task 
    def View_task(self,username):
        user_tasks = self.users_db[username]["tasks"]
        # 1. Check if list is empty first
        if not user_tasks:
            print("\n📭 Your task list is empty.")
            return
        print(f"\n--- TASKS FOR {username.upper()} ---")
        for index, task in enumerate(user_tasks, 1):
            print(f"{index}. {task}")
            
        print("---------------------------------")        



    # Main login screen
    def Acc_operations(self):
        try:
            choice=int(input("Enter you choice:\n 1. Create account\n 2.Login\n "))
            if choice==1:
                self.Acc_creation()
            if choice==2:
                self.login()
        except ValueError:
            print("Invalid choice")

    #Task appeareance after login
    def task_oper(self,username):
        while True:
            print(" 1. Add task\n 2.Remove task\n 3.View Tasks\n 4.Exit")
            try:
                choice1=int(input("Enter you choice:"))
                if choice1==1:
                    self.add_task(username)
                if choice1==2:
                    self.remove_task(username)
                if choice1==3:
                    self.View_task(username)    
                if choice1==4:
                    print("Logging Out")
                    break        
            except ValueError:
                print("Invalid choice. Please enter number only.")    



tsk=Task_Manager()
try:
    choose=int(input("1.LOGIN\n 2.CREATE ACCOUNT\t"))
    if choose==1:
        tsk.login()
    if choose==2:
        tsk.Acc_creation()    
except ValueError:
    print("Invalid choice")