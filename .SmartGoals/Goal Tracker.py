import mysql.connector
from mysql.connector import Error
import time
from datetime import datetime

class SmartGoal:
    def __init__(self, goal_id, user_id, title, description, start_date, end_date, priority, achieved=False):
        self.goal_id = goal_id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.priority = priority
        self.achieved = achieved

    def __repr__(self):
        return f"SmartGoal(goal_id={self.goal_id}, title='{self.title}', achieved={self.achieved}, start_date={self.start_date}, end_date={self.end_date})"

class SmartGoalManager:
    def __init__(self):
        self.conn = self.create_connection()
        self.create_goal_table()  # Create goal table if not exists

    def create_connection(self):
        conn = None
        try:
            conn = mysql.connector.connect(
                host='127.0.0.1',
                database='goals',
                user='root',
                password='1234'
            )
            if conn.is_connected():
                print('Connected to MySQL database')
                return conn
        except Error as e:
            print(e)
        return conn

    def create_goal_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS goals (
                    goal_id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    title VARCHAR(255),
                    description TEXT,
                    start_date DATE,
                    end_date DATE,
                    priority INT,
                    achieved BOOLEAN
                )
            ''')
            self.conn.commit()  # Commit changes
        except Error as e:
            print(e)

    def create_goal(self, user_id, title, description, start_date, end_date, priority):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO goals (user_id, title, description, start_date, end_date, priority, achieved)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (user_id, title, description, start_date, end_date, priority, False))  # False for not achieved
            self.conn.commit()
            print("Goal created successfully.")
        except Error as e:
            print(e)

# *Alternate use of view_goals with lambda, seemed kinda neat but lacks structure and security 
# view_goals = lambda self: self.execute_query('''
#                 SELECT * FROM goals
#             ''', fetch=True)      
    def view_goals(self): 
        self.execute_query('''
            SELECT * FROM goals
        ''', fetch=True)

    def execute_query(self, query, values=None, fetch=False):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, values)
            if fetch:
                goals = cursor.fetchall()
                print()
                for goal in goals:
                    priority = "Yes" if goal[6] == 1 else "No"
                    print("Goal ID:", goal[0])
                    print("User ID:", goal[1])
                    print("Title:", goal[2])
                    print("Description:", goal[3])
                    print("Start Date:", goal[4])
                    print("End Date:", goal[5])
                    print("Priority:", priority)
                    print("Achieved:", goal[7])
                    print()
            else:
                self.conn.commit()  # Commit changes for non-select queries
                print("Operation completed successfully.")
        except Error as e:
            print(e)

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
            print('Disconnected from MySQL database')

# Create an instance of SmartGoalManager
goal_manager = SmartGoalManager()

while (again := int(input(f"""Select a function by number:             
{1}. Create Goal
{2}. Edit Goal
{3}. View Goals
{4}. Delete Goal
{5}. Exit Program: """))) != 5:
    
    if again == 1 :
        user_id = int(input("Enter user ID: "))
        title = input("Enter goal title: ")
        description = input("Enter goal description: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        priority = int(input("Enter priority: "))

        goal_manager.create_goal(user_id, title, description, start_date, end_date, priority)
    elif again == 2:
         pass
    elif again == 3:
         goal_manager.view_goals()
    elif again == 4:
         pass
    else:
         print("Invalid choice.")

print("\nI hope you accomplish your wildest goals!")
