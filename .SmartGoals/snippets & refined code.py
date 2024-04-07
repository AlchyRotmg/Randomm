import time



# print("ERROR: File not found", end='', flush=True )
# for _ in range(3):
#     time.sleep(0.75)
#     print(".", end='', flush=True)

# def execute_query(self, query, values=None, fetch=False):
#     try:
#         cursor = self.conn.cursor()
#         cursor.execute(query, values)
#         if fetch:
#             goals = cursor.fetchall()
#             print()
#             for goal in goals:
#                 print("Goal ID:", goal[0])
#                 print("User ID:", goal[1])
#                 print("Title:", goal[2])
#                 print("Description:", goal[3])
#                 print("Start Date:", goal[4])
#                 print("End Date:", goal[5])
#                 print("Priority:", goal[6])
#                 print("Achieved:", goal[7])
#                 print()
#         else:
#             self.conn.commit()  # Commit changes for non-select queries
#             print("Operation completed successfully.")
#     except Error as e:
#         print(e)

# view_goals = lambda self: self.execute_query('''
#     SELECT * FROM goals
# ''', fetch=True)
