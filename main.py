# Import library of functions
import file_control

def main():
  # Get tasks from file
  tasks = file_control.load_tasks()

  # Create loop for menu
  while True:
    print("---Task Tracker Menu---")
    print("1. Display tasks",
         "\n2. Add tasks",
         "\n3. Mark task as complete",
         "\n4. Save and exit")

    # Get user choice
    choice = input()

    # Navigate user based on choice
    if choice == "1":
      display_tasks(tasks)
    elif choice == "2":
      tasks = add_tasks(tasks)  
    elif choice == "3":
      tasks = complete(tasks)
    elif choice == "4":
      file_control.save_tasks(tasks)
      print("Thank you for using Task Tracker.")
      break
    else:
      print("That is not a valid option.")



# Create a function called display_tasks that takes a list of tasks and
# displays every task in the list.
def display_tasks(tasks):

  # inform user if there are no tasks to be displayed
  if tasks == []:
    print("The task list has not been created. Please add a task.")
  
  
  else: 
    # display tasks
    for index in tasks:
      print('\n' + index[0] + '\n' + index[1] + '\n' + index[2] + '\n' + index[3])




# Create a function called add_task that takes a list of tasks, prompts
# the user for another task, and then appends the new tasks to the 
# end of the list.
def add_tasks(tasks):

  # get the task title from the user
  task_title = input("What is the title of the task? ")

  # get the task description from the user
  task_desc = input("Enter a description of the task. ")

  # get the due date from the user
  due_date = input("What date does the task need to be completed by? ")

  # get whether the task has been completed from the user
  complete = input("Is the task complete? complete for yes, incomplete for no. ")

    #validate input
  while complete != "complete" and complete != "incomplete":

    # tell user the input is invalid
    print("Invalid input")

    # reprompt
    complete = input("Is the task complete? enter complete for yes, incomplete for no. ")

  # assign inputs to a variable as a list
  added_task = [task_title, task_desc, due_date, complete]

  # reassign tasks if tasks is empty
  if tasks == []:
    tasks = [added_task]

  # append the added task to tasks
  else:
    tasks.append(added_task)
  
  # return with the full list of tasks
  return tasks




# Create a function called complete that takes a lists of tasks,
# displays them to the user, and then lets the user choose one
# to mark as complete. It will then update the status of the 
# task in the list and return the updated list.
def complete(tasks):

  # inform user if there are no tasks to be completed
  if tasks == []:
    print("The task list has not been created. Please add a task.")
    return tasks

  # print list of tasks and their completion status
  for task in tasks:
    print(task[0] + '\n' + task[3] + '\n')

  # get input from user about which task to complete
  completed = input("Which task would you like to complete? ")

  # variable showing the input has not been found 
  found = False

  # loop to validate input
  while found == False:

    # look for the input in each task
    for task in tasks:

      # if input is found, turn variable to true and change the index in that task to completed
      if completed in task:
        found = True
        task[3] = "completed"


    if found == False:
      # if input is invalid, inform user the task they entered does not exist
      print("Task does not exist.")

      # print tasks again
      for task in tasks:
        print(task[0] + '\n' + task[3] + '\n')

      # reprompt for a valid task or return to menu
      completed = input("Enter a task to complete or type back to return to menu. ")

      # break the loop if user wants to return to the menu
      if completed == "back":
        break

    
    
  # return with updated list
  return tasks
  

if __name__ == "__main__":
  main()
