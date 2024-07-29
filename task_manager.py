#=====importing libraries===========
user_credentials = {}
#I have first created an empty dictionary as a placeholder for user credentials
with open("user.txt", "r") as file:
# This line is to read the credentials from the user.txt file
    for line in file:
        username, password = line.strip().split(", ")
        user_credentials[username] = password

#====Login Section====
input_username = input("Please enter your username:")
while input_username != username:
      username_retry = input("The username you have entered is incorrect, please try again: ")
      if username_retry == username:
            break
input_password = input("Please enter your password:")
while input_password != password:
      password_retry = input("The password you have entered is incorrect, please try again:")
      if password_retry == password:
            break
print("You have successfully logged in!")
# I have use 2 while loops above to validate the user credentials

while True:
# I included a while loop here so the user can be taken back to the menu display and select another option
# until they specifically choose to exit the programme
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
    if menu == 'r':
        with open("user.txt", "a") as file:
              new_username = input("To register a user, please enter the username of the new user: ").lower()
              new_password = input("Please enter the password for the new user: ").lower()
              confirmed_password = input("Please confirm the password for the new user: ").lower()
              while new_password != confirmed_password:
                    confirmed_password_retry = input("This does not match the previous password, please try again: ").lower()
                    if confirmed_password_retry == new_password:
                          file.write(f"\n{new_username}, {new_password}")
                          print("New user successfully registered!")
                          break
    elif menu == 'a':
        assigned_username = input("You can now assign tasks, please enter the username of the person you would like to assign tasks to: ")
        task_title = input("Please enter the title of the task: ")
        task_description = input("Please enter the task description: ")
        task_due_date = input("Please enter the due date of the task in the format dd/mm/yyyy:")
        assigned_date = input("Please enter the date today in the format dd/mm/yyyy:")
        # Here I am collecting the necessary input from the user
        with open('tasks.txt', 'a') as file:
        # I have opened the 'tasks.txt' file with the 'a' mode to add information to the file
              file.write(f"\n{assigned_username}, {task_title}, {task_description}, {task_due_date}, {assigned_date}, No")
              print("The task has been assigned successfully!")

    elif menu == 'va':
         with open('tasks.txt', 'r') as file:
              for line in file:
                task_information = line.strip().split(", ")
                #This line is to split the line where there is a comma to make the task information more readable
                print(f"Assigned to: {task_information[0]}")
                print(f"Title: {task_information[1]}")
                print(f"Description: {task_information[2]}")
                print(f"Due Date: {task_information[3]}")
                print(f"Assigned Date: {task_information[4]}")
                print(f"Status: {task_information[5]}")
                print()
                #Here I used indexed to access the specific information in the dictionary
    elif menu == 'vm':
         with open("tasks.txt", "r") as file:
                for line in file:
                     task_information = line.strip().split(", ")
                     # Here again, I am splitting the line where there is a comma and space
                     if task_information[0] == username:
                          print(f"Title: {task_information[1]}")
                          print(f"Description: {task_information[2]}")
                          print(f"Due Date: {task_information[3]}")
                          print(f"Assigned Date: {task_information[4]}")
                          print(f"Status: {task_information[5]}")
                          print()

    elif menu == 'e':
        print('Goodbye!')
        exit()

    else:
         print("You have entered an invalid input. Please try again")