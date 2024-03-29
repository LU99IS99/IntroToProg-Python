# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Junyan Lu,5.16.2023,Created started script
# <YOUR NAME HERE>,<DATE>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data from the ToDoList.txt file into a python list of dictionaries rows
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.strip().split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = input("Which option would you like to perform? [1 to 5] - ")
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for row in lstTable:
            print(row["Task"] + " | " + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("Enter a new task: ")
        strPriority = input("Enter the priority of the task: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strTask = input("Enter the task to remove: ")
        for row in lstTable:
            if row["Task"] == strTask:
                lstTable.remove(row)
                break
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting the program")
        break
