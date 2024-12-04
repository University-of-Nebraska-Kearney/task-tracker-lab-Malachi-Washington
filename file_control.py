# Create a function called load_tasks that reads tasks from a file
# into a list and then returns the list.
def load_tasks():
    
    # attempt to open the task list file for reading
    try:
        with open("task list.txt", "r") as task_list:
        
            #read first line as the title of the task
            task_title = task_list.readline()

            #create an empty list of tasks
            tasks = []

            # read the rest of the task as long as there is something to read. 
            while task_title != "":

                # second line is the task description
                task_desc = task_list.readline()

                # third line is the due date
                due_date = task_list.readline()

                # fourth line is the completion status
                completion = task_list.readline()

                # strip new line from all lines in the record
                task_title = task_title.rstrip("\n")
                task_desc = task_desc.rstrip("\n")
                due_date = due_date.rstrip("\n")
                completion = completion.rstrip("\n")

                # assign the record to a variable
                task = [task_title, task_desc, due_date, completion]

                # append the record to the task list
                tasks.append(task)

                # read the next task title
                task_title = task_list.readline()
        return tasks

    # if the file doesn't exist return nothing
    except FileNotFoundError:
        return []




# Create a function called save_tasks that takes a list of tasks and 
# writes them to a file for long non-volatile storage.
def save_tasks(tasks):

    # open the task list file with writing capability
    with open("task list.txt", "w") as task_file:
        
        # cast each index of each task to a string and write it to the task list file 
        for task in tasks:
            task_file.write(str(task[0]) + "\n" + str(task[1]) + "\n" + str(task[2]) 
            + "\n" + str(task[3]) + "\n")
