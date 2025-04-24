from SQL_functions import (
    createTable, validTable, validDate, checkExist, selectAll, createTask, updateTaskName, updateDescription, updateStatus, updateDueDate, removeTask
)
import argparse
import sqlite3
import os



# ADD ARGUMENTS
def main():
    parser = argparse.ArgumentParser(description="Task Management Script")
    subparsers = parser.add_subparsers(dest="command", title="Available Commands", metavar="<command>", required=True)

    #Select all
    select_parser = subparsers.add_parser("selectAll", help="Select all tasks from the given database")
    select_parser.add_argument("--database", required=True, help="The database to which tasks can be created, removed, and/or modified")
    select_parser.add_argument("--table", required=True, help="The table to which tasks can be created, removed, and/or modified")

    #Create task
    create_parser = subparsers.add_parser("createTask", help="Create a new task")
    create_parser.add_argument("--database", required=True, help="The database to which tasks can be created, removed, and/or modified")
    create_parser.add_argument("--table", required=True, help="The table to which tasks can be created, removed, and/or modified")
    create_parser.add_argument("--taskName", required=True, type=str, help="The name of the task; ensure this is in quotes")
    create_parser.add_argument("--description", required=True, type=str, help="The description of the task; ensure this is in quotes")
    create_parser.add_argument("--status", choices=["Complete", "In Progress", "On Hold", "Not Started"], required=True, type=str, help="The status of the task; ensure this is in quotes")
    create_parser.add_argument("--dueDate", type=validDate, help="The due date of the task; ensure this is in quotes and DD/MM/YYYY format")

    #Update name
    updateName_parser = subparsers.add_parser("updateTaskName", help="Update the name of a task")
    updateName_parser.add_argument("--database", required=True, help="The database to which tasks can be created, removed, and/or modified")
    updateName_parser.add_argument("--table", required=True, help="The table to which tasks can be created, removed, and/or modified")
    updateName_parser.add_argument("--taskName", required=True, type=str, help="The NEW name of the task; ensure this is in quotes")
    updateName_parser.add_argument("--taskID", type=int, required=True, help="The number ID of the task (automatically assigned to task at creation); this is REQUIRED to locate the task to rename. To view relevant ID, use selectAll command")

    #Update description
    updateDesc_parser = subparsers.add_parser("updateDescription", help="Update the description of a task")
    updateDesc_parser.add_argument("--database", required=True, help="The database to which tasks can be created, removed, and/or modified")
    updateDesc_parser.add_argument("--table", required=True, help="The table to which tasks can be created, removed, and/or modified")
    updateDesc_parser.add_argument("--description", required=True, type=str, help="The description of the task; ensure this is in quotes")
    updateDesc_parser.add_argument("--taskID", type=int, help="The number ID of the task (automatically assigned to task at creation)")
    updateDesc_parser.add_argument("--taskName", type=str, help="The name of the task; ensure this is in quotes")

    #Update status
    updateStatus_parser = subparsers.add_parser("updateStatus", help="Update the status of a task")
    updateStatus_parser.add_argument("--database", required=True, help="The database to which tasks can be created, removed, and/or modified")
    updateStatus_parser.add_argument("--table", required=True, help="The table to which tasks can be created, removed, and/or modified")
    updateStatus_parser.add_argument("--status", choices=["Complete", "In Progress", "On Hold", "Not Started"], required=True, type=str, help="The status of the task; ensure this is in quotes")
    updateStatus_parser.add_argument("--taskID", type=int, help="The number ID of the task (automatically assigned to task at creation)")
    updateStatus_parser.add_argument("--taskName", type=str, help="The name of the task; ensure this is in quotes")

    #Update due date
    updateDate_parser = subparsers.add_parser("updateDueDate", help="Update the due date of a task")
    updateDate_parser.add_argument("--database", required=True, help="The database to which tasks can be created, removed, and/or modified")
    updateDate_parser.add_argument("--table", required=True, help="The table to which tasks can be created, removed, and/or modified")
    updateDate_parser.add_argument("--dueDate", required=True, type=validDate, help="The due date of the task; ensure this is in quotes and DD/MM/YYYY format")
    updateDate_parser.add_argument("--taskID", type=int, help="The number ID of the task (automatically assigned to task at creation)")
    updateDate_parser.add_argument("--taskName", type=str, help="The name of the task; ensure this is in quotes")

    #Delete task
    remove_parser = subparsers.add_parser("removeTask", help="Delete a task and its information")
    remove_parser.add_argument("--database", required=True, help="The database to which tasks can be created, removed, and/or modified")
    remove_parser.add_argument("--table", required=True, help="The table to which tasks can be created, removed, and/or modified")
    remove_parser.add_argument("--taskName", type=str, help="The name of the task; ensure this is in quotes")
    remove_parser.add_argument("--taskID", type=int, help="The number ID of the task (automatically assigned to task at creation)")


    # PARSE ARGUMENTS
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        exit(1)

    
    if args.command == "removeTask" or args.command == "updateDescription" or args.command == "updateStatus" or args.command == "updateDueDate":
        if not args.taskName and not args.taskID:
            print("Missing argument. Please provide --taskName or --taskID to remove task.")
            print("Exiting...")
            exit(1)
    

    update_commands = {"updateTaskName", "updateDescription", "updateStatus", "updateDueDate"}

    # CHECK IF DATABASE EXISTS AND CREATE TABLE (if needed)

    if not os.path.exists(args.database):
        print(f"The database '{args.database}' does not exist.")
        if args.command in update_commands:
            print(f"Able to create '{args.database},' but the task will not be created/updated.")
            create_database = input("Continue? [Enter yes or no]: ")
            if create_database == "yes":
                print("Creating database and table...")
                createTable(args.database, args.table)
                print(f"Database '{args.database}' and table '{args.table}' created. Exiting without task update/creation...")
                exit(1)
            elif create_database == "no":
                print("Exiting...")
                exit(1)
            else:
                print("Invalid input. Please enter 'yes' or 'no.' Exiting...")
                exit(1)
        elif args.command == "selectAll":
            print(f"Able to create '{args.database}, but there will be no tasks for selection.")
            create_database = input("Continue? [Enter yes or no]: ")
            if create_database == "yes":
                print("Creating database and table...")
                createTable(args.database, args.table)
                print(f"Database '{args.database}' and table '{args.table}' created.")
            elif create_database == "no":
                print("Exiting...")
                exit(1)
            else:
                print("Invalid input. Please enter 'yes' or 'no.' Exiting...")
                exit(1)
        elif args.command == "removeTask":
            print(f"Able to create '{args.database}, but there will be no task created for deletion.")
            create_database = input("Continue? [Enter yes or no]: ")
            if create_database == "yes":
                print("Creating database and table...")
                createTable(args.database, args.table)
                print(f"Database '{args.database}' and table '{args.table}' created. Exiting without task creation and deletion...")
                exit(1)
            elif create_database == "no":
                print("Exiting...")
                exit(1)
            else:
                print("Invalid input. Please enter 'yes' or 'no.' Exiting...")
                exit(1)
        elif args.command == "createTask":
            create_database = input(f"Would you like to create '{args.database}'? [Enter 'yes' or 'no']: ")
            if create_database == "yes":
                print("Creating database and table...")
                createTable(args.database, args.table)
                print(f"Database '{args.database}' and table '{args.table}' created. Running commands...")
            elif create_database == "no":
                print("Exiting...")
                exit(1)
            else:
                print("Invalid input. Please enter 'yes' or 'no.' Exiting...")
                exit(1)
    
            taskExists = checkExist(args.database, args.table, args.taskName)
            if taskExists:
                print(f"The task '{args.taskName}' already exists. Please create a unique task.")
                print("Exiting...")
                exit(1)


    # CHECK IF TABLE EXISTS AND CREATE TABLE (if needed)

    if not validTable(args.database, args.table):
        print(f"The table '{args.table}' does not exist within '{args.database}.'")
        if args.command in update_commands:
            print(f"Able to create '{args.table},' but the task will not be created/updated.")
            create_database = input("Continue? [Enter yes or no]: ")
            if create_database == "yes":
                print("Creating database and table...")
                createTable(args.database, args.table)
                print(f"Table '{args.table}' created within database '{args.database}'. Exiting without task update/creation...")
                exit(1)
            elif create_database == "no":
                print("Exiting...")
                exit(1)
            else:
                print("Invalid input. Please enter 'yes' or 'no.' Exiting...")
                exit(1)
        elif args.command == "selectAll":
            print(f"Able to create '{args.table}, but there will be no tasks for selection.")
            create_database = input("Continue? [Enter yes or no]: ")
            if create_database == "yes":
                print("Creating database and table...")
                createTable(args.database, args.table)
                print(f"Database '{args.database}' and table '{args.table}' created.")
            elif create_database == "no":
                print("Exiting...")
                exit(1)
            else:
                print("Invalid input. Please enter 'yes' or 'no.' Exiting...")
                exit(1)
        elif args.command == "createTask":
            create_table = input(f"Would you like to create '{args.table}' within '{args.database}? [Enter 'yes' or 'no']: ")
            if create_table == "yes":
                print("Creating table...")
                createTable(args.database, args.table)
                print(f"Table '{args.table}' created within '{args.database}.' Running commands...")
            elif create_table == "no":
                print("Exiting...")
                exit(1)
            else:
                print("Invalid input. Please enter 'yes' or 'no.' Exiting...")
                exit(1)

            taskExists = checkExist(args.database, args.table, args.taskName)
            if taskExists:
                print(f"The task '{args.taskName}' already exists. Please create a unique task.")
                print("Exiting...")
                exit(1)

        elif args.command == "removeTask":
            print(f"Able to create '{args.database}, but there will be no task created for deletion.")
            create_table = input(f"Would you like to create '{args.table}' within '{args.database}? [Enter 'yes' or 'no']: ")
            if create_table == "yes":
                print("Creating table...")
                createTable(args.database, args.table)
                print(f"Table '{args.table}' created within database '{args.database}.' Exiting without task creation and deletion...")
                exit(1)
            elif create_table == "no":
                print("Exiting...")
                exit(1)
            else:
                print("Invalid input. Please enter 'yes' or 'no.' Exiting...")
                exit(1)
    else:
        if args.command == "createTask" or args.command == "updateTaskName":
            taskExists = checkExist(args.database, args.table, args.taskName)
            if taskExists:
                print(f"The task '{args.taskName}' already exists. Please create a unique task.")
                print("Exiting...")
                exit(1)
        print(f"Database '{args.database}' and table '{args.table}' found. Running commands...")


    # ACTIONS
    if args.command == "selectAll":
        print(f"All tasks from {args.database}: ")
        selectAll(args.database, args.table)
    elif args.command == "createTask":
        createTask(args.database, args.table, args.taskName, args.description, args.dueDate, args.status)
        print("Task created.")
    elif args.command == "updateTaskName":
        updateTaskName(args.database, args.table, args.taskName, args.taskID)
        print("Task name updated.")
    elif args.command == "updateDescription":
        updateDescription(args.database, args.table, args.description, args.taskID, args.taskName)
        print("Description updated.")
    elif args.command == "updateStatus":
        updateStatus(args.database, args.table, args.status, args.taskID, args.taskName)
        print("Status updated.")
    elif args.command == "updateDueDate":
        updateDueDate(args.database, args.table, args.dueDate, args.taskID, args.taskName)
        print("Due date updated.")
    elif args.command == "removeTask":
        removeTask(args.database, args.table, args.taskID, args.taskName)
        print("Task deleted.")
    else:
        print("No action specified. Use --help for usage instructions")
        exit(1)

if __name__ == "__main__":
    main()