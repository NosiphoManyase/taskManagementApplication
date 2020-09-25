# taskManagementApplication

Task management application that creates and tracks users and tasks for an organisation.

## Usefulness

The application can perform multiple functions that an organisation would require from a task managements application. Some useful functions of this apllication
would be the security of the program as it requires for a user to have login details to be able to use the application; being able to view tasks assigned to
the user that is currently logged in; as well as giving special access to user **admin** for the process of creating a new user .

## Contributors and maintenance

This project is not open to the public and currently not open for any changes. There sre no additional contributors to this task.

## Usage

Login Process
1. Enter username and password
 Code checks the external files tasks.txt and user.txt to verify if user credentials exist and whether to allow user to re-enter user details or allow user to 
 proceed to relevant main menu. User **admin** gets access to main menu with an extra features.


## Main  Menu options

### Menu only available if *admin* is logged on
1. create new user, 
2. add task
3. view all tasks
4. view my tasks
5. generate reports
6. display statistics
7. exit

### Menu available to *all* other users
1. add task
2. view all tasks
3. view my tasks
