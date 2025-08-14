# Use loop to calculate the sum of the numbers below
"""numbers = [10, 5, 20, 8, 14]
sum = 0
for number in numbers:
  sum = sum + number
  print(sum)"""

"""# Define a register user function
def register_user(name, email, password):
    # Check if usrf does not already exist 
    # Hash user password
    # Validate inputs 
    # Check if user is not a robot
    # Return response
    return "User register successfully!"
def add_task(task):
    # Save the task to data base
    # Return response
    return True"""

"""def show_tasks():
    # Get all tasks from database
    # Return response
    return []"""

"""def add_task(task):
    # Save task to database
    # Return response
    return True
    
def show_tasks():
    # Get all task from database
    # Return response
    Return []

def update_task(task, update):
    # Update task in database
    # Return response
    return True

def delete_task(task):
    # Delete task from database
    # Return response
    return True"""

import add
import show
import update
import delete 

add_task_response = add.add_task("Sleep")
print(add_task_response)

show_tasks_response = show.show_tasks()
print(show_tasks_response)

update_task_response = update.update_task("Sleep", "Wake Up")
print(update_task_response)

delete_task_response = delete.delete_task("Wake Up")
print(delete_task_response)

