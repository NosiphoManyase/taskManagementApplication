from datetime import datetime

def reg_user():
    #while True
    print("\n Create login details for new user below.")
    # New string variables declared for writing over to a text file.
    while 1:
        new_username = input("\n username: ")
        if new_username in dic:
            print("Sorry. The Username Already Exists. Please Select Another Username\n")
        else:
            break
    while 1:
        new_user_password = input("password: ")
        confirm_password = input("confirm password: ")
        if new_user_password == confirm_password: # Only passwords that users can confirm are going to be written to the text file.
            break
        else:
            print("The Passwords Do Not Match. Please Re Enter The Password.")

    add_new_user = open('user.txt', 'a+') #Text file user opened.
    new_user = new_username + ", " + new_user_password # Two string variables compacted to one in order for 1 step process of writing over to text file.
    add_new_user.write("\n"+new_user) #* #Variable above written over to text file. 
    add_new_user.close()
    print("\n user successfuly registered!")
    
                       

def add_task():
    print("\n Enter details about new task below. \n")
    # Text file opened; new variables declared in order to get relevant information to write over to text file.
    add_new_task = open('tasks.txt','a')
    task_username = input("Enter username of person task is assigned to: ")
    task_title = input("Title of task: ")
    task_descr = input("Discription of assigned task: ")
    task_due_date = input("Due date (format eg. 01 Jan 2020): ")
    completeness = "No"
    
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    date_time = datetime.fromtimestamp(timestamp)
    current_date = date_time.strftime("%d %B %Y")
    # New variables above compacted into 1 variable in order for 1 step process to saving data under selection = "a"
    task_details = task_username +", "+ task_title +", "+ task_descr +", "+ current_date +", "+ task_due_date+", " + completeness 
    task_file = open("tasks.txt", "a") #Text file tasks opened.
    task_file.write("\n"+ task_details) # varible task_details written over to text file "tasks".
    task_file.close()
    print("\n New Task successfully added!")

def view_all():
    task_count = 0
    task_file = open('tasks.txt', 'r+') # text file "tasks" opened in reading and writing mode.
    task_count_list = [] # declare list for storing each number of task for user.
    for line in task_file: # looping through each line in text file.
        task_count += 1     # task_count increases by 1 at each iteration.
        task_count_list.append(task_count) #
        task_details = line.split(",")
        print("\n\t\t\tTask Number: "+str(task_count))
        print("Username      : "+task_details[0])
        print("Task Title    :"+task_details[1])
        print("Discription   :"+task_details[2])
        print("Date Assigned :"+task_details[3])
        print("Due Date      :"+task_details[4])
        print("Complete      :"+task_details[5])
    print("    -END OF TASKS-\n")                    # lines in text file all displayed on screen.
    task_file.close()

def view_mine():
    task_count = 0
    task_file = open('tasks.txt', 'r+') # text file "tasks" opened in reading and writing mode.
    task_count_list = [] # declare list for storing each number of task for user.
    for line in task_file: # looping through each line in text file.
        task_count += 1     # task_count increases by 1 at each iteration.
        task_count_list.append(task_count) #
        if username in line: # should string username optained at login step be in one of lines in text file.
            task_details = line.split(",")
            print("\n\t\t\tTask "+str(task_count))
            print("Username      : "+task_details[0])
            print("Task Title    :"+task_details[1])
            print("Discription   :"+task_details[2])
            print("Date Assigned :"+task_details[3])
            print("Due Date      :"+task_details[4])
            print("Complete      :"+task_details[5])
    print("    -END OF TASKS-\n")
    task_count = False
    edit = input("Do You Want To Edit A Task Y/N? ").strip()
    temp_File = ""
    if(edit == "y" or edit == "Y"):
        task_no = input("Please Enter The Task Number: ").strip()
        task_file = open('tasks.txt', 'r+')
        temp_counter = 1
        for line in task_file: # looping through each line in text file.
            temp_Line = line
            #print("In Here")
            if int(task_no) == temp_counter:
                if line.find("No") != -1:
                    task_count = True
                    temp_userName = task_details[0]
                    date_update = task_details[4]
                    temp_username = input("Do You Want To Edit The Username Y/N?").strip()
                    if(temp_username == "y" or edit == "Y"):
                        temp_userName = input("Please Enter The Username: ").strip()
                    temp_date = input("Do You Want To Edit The Date Y/N? ").strip()
                    if(temp_date == "y" or edit == "Y"):
                        date_update = input("Enter new due date (format eg. 01 Jan 2020): ")
                    #task_details = line.split(",")
                    #date_update = task_details[4]
                    temp_Line = temp_userName+","+task_details[1]+","+task_details[2]+","+task_details[3]+", "+date_update+","+task_details[5]
                else:
                    print("Sorry, This Task Is Marked As Complete")
                temp_task = input("Do You Want To Mark The Task As Complete Y/N? ").strip()
                if(temp_task == "y" or edit == "Y"):
                   temp_Line = temp_userName+","+task_details[1]+","+task_details[2]+","+task_details[3]+","+date_update+", Yes"
            
            temp_counter+=1
            temp_File += temp_Line
            
        if task_count == False:
            print("Sorry, The Task Number Does Not Exist")
            
    task_file.close()
    if temp_File != "":
        f = open("tasks.txt","w")
        f.write(temp_File)
        f.close()




print("\n - WELCOME TO THE TASK MANAGER - \n ")

# Initiate login variable
login = False
dic = {}

# External text file opened in read mode
with open('user.txt','r') as f:
    for line in f:
        login_dets = line.split(",")
        dic[login_dets[0].strip()] = login_dets[1].strip() # dictionary store username as key and password as value.
            
# Inputs obtained 
while login == False:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username in dic:
        if password == dic[username]:
            # login will be set to true should if statement above be true.
            login = True
        else:
            print("\n ERROR! please ensure your login details are correct.")
    else:
        print("Sorry. The Username Does Not Exist\n")
            
            
                
# If statement for successful login into task manager.               
if login == True:
    if username == "admin": # Allow user with username admin excess to speacial options.
        flag = True
        while flag:
            print('''\n Please select one of the following:

                        r - register user
                        a - add task
                        va - view all tasks
                        vm - view my tasks
                        gr - generate reports
                        ds - display statistics
                        e - exit ''')
        # Option put in by user saved into variable selection.
            selection = input("\n Enter selection : ")
        
            if(selection == "r" or selection == "a" or selection == "va" or selection == "vm" or selection == "gr" or selection == "ds" or selection == "e"):
                flag = False
            else:
                print('''\n Incorrect Selection. Please select one of the following:

                        r - register user
                        a - add task
                        va - view all tasks
                        vm - view my tasks
                        gr - generate reports
                        ds - display statistics
                        e - exit ''')


    else: # else statement with general options for all users with standard access.
        flag = True
        while flag: # loop will run while flag is true
            print('''\n Please select one of the following:

                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    e - exit ''')
    # Option put in by user saved into variable selection.
            selection = input("\n Enter selection : ")
            if(selection == "a" or selection == "va" or selection == "vm" or selection == "e"):
                flag = False
            else:
                print('''\n Incorrect Selection. Please select one of the following:

                    a - add task
                    va - view all tasks
                    vm - view my tasks
                    e - exit ''')

      
# If statements for input in variable selection.   
if selection == "r" and username == "admin":
    reg_user() # Calling a function

elif selection == "a":
    add_task()

elif selection == "va":
    view_all()

elif selection == "vm":
    view_mine()

elif selection == "gr":
    # Opening tasks.txt in read mode, variables for counting created below
    tasks_file = open('tasks.txt','r')
    task_count = 0
    complete_No = 0
    overdue_task = 0
    # using datetime module to obtain current date, current date aids in comparison of dates.
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    date_time = datetime.fromtimestamp(timestamp)
    current_date = date_time.strftime("%d %b %Y")
    users = [] # empty list
    for line in tasks_file:
        task_count += 1
        task_folder = line.rstrip().split(", ")
        users.append(task_folder[0]) # each username found at start of each task stored into list 'users'.
        if task_folder[5] == "No":
            complete_No += 1         # counting tasks that aren't completed
            # Should task not be complete, comparing due date of each task to current date to see if it's overdue.
            if(datetime.strptime(task_folder[4],'%d %b %Y') < datetime.strptime(current_date,'%d %b %Y')):
                overdue_task += 1    # counting tasks that are overdue
        elif task_folder[5] == "Yes":
            complete_Yes = (task_count - complete_No)
    task_count1 = task_count - 2
    total_tasks ="Total number of tasks generated through program: "+str(task_count1)+"\n" # -2 from task count to exclude 2 automated admin tasks
    total_task_incomplete ="Total number of incomplete tasks is: " +str(complete_No)+"\n"
    total_task_complete = "Total number of complete tasks is: " +str(complete_Yes)+"\n"
    overdue_Task =  "Total number of overdue tasks is: " +str(overdue_task)+"\n"   # no. of tasks that haven't been completed and are overdue
    percent_incomplete = "Percentage of incomplete tasks is: "+str(int((float(complete_No)/complete_No)*100))+"%\n"
    overdue_percentage = "Percentage of overdue tasks is: "+str(int((float(overdue_task)/complete_No)*100))+"%\n"
    # Variable below combines all variables related to tak overview, variable is then written over to text file 'task_overview.txt'.
    task_overview = total_tasks + total_task_incomplete + total_task_complete + overdue_Task + percent_incomplete + overdue_percentage
    task_overview_file = open('task_overview.txt','w')
    task_overview_file.write(task_overview)
    tasks_file.close()
    task_overview_file.close()

    # Creating information to write over to new text file task_overview.txt
    user_file = open('user.txt','r')
    user_count = 0    
    temp_file = []
    user_overview = open('user_overview.txt','w')
    for line in user_file:
        user_count += 1
        user_folder = line.strip().split(", ")
        temp_file.append(str(user_folder[0]))   # extracting usernames from user_file and saving them onto list 'temp_file'
    user_count = user_count - 1 # user admin only user not generated through program therefore -1.
    total_users = "Total number of users generated through program: " + str(user_count) + "\n"
    user_overview.write(total_users)   
    for i in temp_file:
        # Username at start of each line in tasks file stored in list 'users' in line 233 in code, therefore we can use i(username) and;
        # crosscheck amount of occurances of i in list 'users' ie. total tasks each username has.
        user_tasks = users.count(i)  #* 
        user_task_details ="\nUser " + str(i) +" has\t: " + str(user_num) +" total task(s).\n" #*
        user_overview.write(user_task_details)
        user_percent = (user_tasks / task_count)*100 # total number of tasks assigned to specified user divided by total tasks
        user_task_percent = "User " + str(i) + " has\t: " + str(user_percent) + "% of all task(s).\n"
        user_overview.write(user_task_percent)
        # Opening tasks file once again and declaring counters for use in loop.
        task_file = open('tasks.txt','r')
        count = 0
        counter = 0
        counting = 0
        each_user_task_count = 0
        for line in task_file:   # Looping through each line in task_file.
            task_folder = line.rstrip().split(", ")
            
            if i == task_folder[0]:     # Checking if each username matches username at start of a line in task_folder, if so if statements that follow will be processed.            
                each_user_task_count += 1 # counts number of tasks assigned to each i
                if task_folder[5] == "No":
                    count += 1                
                    if(datetime.strptime(task_folder[4],'%d %b %Y') < datetime.strptime(current_date,'%d %b %Y')): # checking if incomplete task is overdue.
                        counting += 1
                elif task_folder[5] == "Yes":
                    counter += 1
        # new usernames may not have tasks assigned to them yet therefore each_user_task_count may be 0, and dividing by zero is undefined
        # If and elif statement below provides for such instances.
        if each_user_task_count != 0:
            user_task_incomplete = "User " + str(i) + " has\t: " + str(count/each_user_task_count * 100) + "% of task(s) incomplete. \n"
        elif each_user_task_count == 0:
            user_task_incomplete = "User " + str(i) + " has\t: 0" + "% of task(s) incomplete. \n" 
        user_task_complete = "User " + str(i) + " has\t: " + str(counter/task_count * 100) + "% of task(s) completed. \n"
        user_task_overdue = "User " + str(i) + " has\t: " + str(counting/complete_No * 100) + "% of task(s) overdue. \n"
        user_File = user_task_incomplete + user_task_complete + user_task_overdue
        user_overview.write(user_File)
    #closing opened files
    tasks_file.close()
    task_file.close()
    user_file.close()
    user_overview.close()        
    
    
    
    
    
elif selection == "ds" and username == "admin":     # option displayed for username admin
    with open('task_overview.txt','r') as infile1:  # Opening text file in read format.
        print("\n\t GENERAL OVERVIEW OF ALL TASKS") # Header
        for line in infile1:
            line = line.rstrip()    # Stripping any new line(\n) for readability within program.
            print(line)
    with open('user_overview.txt','r') as infile2:
        print("\n\t BREAKDOWN OF USERS AND TASKS ASSIGNED TO EACH USER")
        for line in infile2:
            line = line.rstrip()
            print(line)
            
    
    
    

else: 
    print("\n Thank you for using the task managing application.") # 1 line message displayed before program ends, lets user know that program is ending.

