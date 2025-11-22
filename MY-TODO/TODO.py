import os
import json


class Task_Manager:
    def __init__(self):
        self.tasks = "tasks.json"
        self.users_db=self.load_tasks()
        

    def load_tasks(self):                       #checking file in the system
        if os.path.exists(self.tasks):  
            try:
                with open(self.tasks, "r") as f:
                    return json.load(f) 
            except (json.JSONDecodeError, IOError):            # load JSON into Python dict
                return {}
        return {}
    
#Saving users_db to JSON file.
    def save_tasks(self):               
        with open(self.tasks, "w") as f:
            json.dump(self.users_db, f, indent=4)



    # function for creating new accounnt
    def Acc_creation(self):
        user_name=input("Create username: ")
        if len(user_name) < 8:
            print("Username length should be more than 8 characters.")
            return{}
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


    def Acc_operations(self):
        choice=int(input("Enter you choice:\n 1. Create account\n 2.Login\n "))
        if choice==1:
            self.Acc_creation()
        if choice==2:
            self.login()

    def task_oper(self,username):
        choice1=int(input("Enter you choice:\n 1. Add task\n 2.Remove task\n "))
        if choice1==1:
            self.add_task(username)
        if choice1==2:
            pass    
                



tsk=Task_Manager()
choose=int(input("1.LOGIN\n 2.CREATE ACCOUNT\t"))
if choose==1:
    tsk.login()
if choose==2:
    tsk.Acc_creation()    
