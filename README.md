# Python Project: To-Do List Database Manager

Hello! This is my repository for my python project for IT3038, Scripting Languages: The To-Do List Database Manager.

This project consists of:
  - `python_proj.py` — The main script to manage the database
  - `SQL_functions.py` — A helper module imported by the main script

The purpose for these scripts is to allow users to easily manage a database, which is a simple to-do list. The script allows users to manage a simple to-do list database with the following fields:
  - **Task ID** *(auto-assigned by SQL)*
  - **Task Name**
  - **Task Description**
  - **Task Status** *(e.g. Complete, In Progress, etc.)*
  - **Due Date** *(optional)*

The script can create, update, delete, and retrieve tasks. If a specified database or table does not yet exist, it will prompt the user to create it (note: update actions won't execute after creation).

<br/>

---

<br/>

## Available Commands

### `selectAll`
Used to select and view all tasks within the table.

**Command Usage:**
```python
python python_proj.py selectAll --database <database> --table <table>
```

**Options:**
```python
--database: The database to be modified. REQUIRED.
--table: The table to be modified. REQUIRED.
```

<br/>

### `createTask`
Used to create a task along with any appropriate characteristics (description, status, etc.). 

**Command Usage:**
```python
python python_proj.py createTask --database <database> --table <table> --taskName "<Name>" --description "<Description>" --status "<Status>" --dueDate "<dd/mm/yyyy>"
```

**Options:**
```python
--database: The database to be modified. REQUIRED.
--table: The table to be modified. REQUIRED.
--taskName: The name of the task to be created. REQUIRED.
--description: The description of the task to be created. REQUIRED.
--status: The status of the task. REQUIRED and LIMITED CHOICES: "Complete", "In Progress", "On Hold", "Not Started"
--dueDate: The date that the task should be completed by; must be in the format dd/mm/yyyy. OPTIONAL.
```

<br/>

### `updateTaskName`
Used to update the name of a task.

**Command Usage:**
```python
python python_proj.py updateTaskName --database <database> --table <table> --taskName "<updated_name>" --taskID <ID_number>
```

**Options:**
```python
--database: The database to be modified. REQUIRED.
--table: The table to be modified. REQUIRED.
--taskName: The NEW name of the task. REQUIRED.
--taskID: The ID number related to the task to be renamed. To view relevant ID, use selectAll command. REQUIRED.
```

<br/>

### `updateDescription`
Used to update the description of a task. NOTE: Either the --taskName option or --taskID option can be used, but ONE of the two is required.

**Command Usage:**
```python
python python_proj.py updateDescription --database <database> --table <table> --taskName "<task_name>" --taskID <taskID> --description "<new_description>"
```

**Options:**
```python
--database: The database to be modified. REQUIRED.
--table: The table to be modified. REQUIRED.
--taskName: The name of the task to be updated. REQUIRED if --taskID is not used.
--taskID: The ID number related to the task to be updated. REQUIRED if --taskName is not used.
--description: The new description of the task. REQUIRED.
```

<br/>

### `updateStatus`
Used to update the status of a task.

**Command Usage:**
```python
python python_proj.py updateStatus --database <database> --table <table> --taskName "<task_name>" --taskID <taskID> --status "<status>"
```

**Options:**
```python
--database: The database to be modified. REQUIRED.
--table: The table to be modified. REQUIRED.
--taskName: The name of the task to be updated. REQUIRED if --taskID is not used.
--taskID: The ID number related to the task to be updated. REQUIRED if --taskName is not used.
--status: The status of the task. REQUIRED and LIMITED CHOICES: "Complete", "In Progress", "On Hold", "Not Started"
```

<br/>

### `updateDueDate`
Used to update the due date of a task (i.e., when it should be completed by).

**Command Usage:**
```python
python python_proj.py updateDueDate --database <database> --table <table> --taskName "<task_name>" --taskID <taskID> --dueDate "<dd/mm/yyyy>"
```

**Options:**
```python
--database: The database to be modified. REQUIRED.
--table: The table to be modified. REQUIRED.
--taskName: The name of the task to be updated. REQUIRED if --taskID is not used.
--taskID: The ID number related to the task to be updated. REQUIRED if --taskName is not used.
--dueDate: The new due date of the task. Must be in dd/mm/yyyy format. REQUIRED.
```

<br/>

### `removeTask`
Used to delete a task from the list, including all of its characteristics.

**Command Usage:**
```python
python python_proj.py removeTask --database <database> --table <table> --taskName "<task_name>" --taskID <taskID>
```

**Options:**
```python
--database: The database to be modified. REQUIRED.
--table: The table to be modified. REQUIRED.
--taskName: The name of the task to be updated. REQUIRED if --taskID is not used.
--taskID: The ID number related to the task to be updated. REQUIRED if --taskName is not used.
```

<br/>

---

<br/>

## Testing

### General
**Errors:**
-[x] Call script with no command
  *Input*:
    ```python
    python python_proj.py
    ```
  *Result*:
    ```python
    python_proj.py: error: the following arguments are required: <command>
    ```

-[x] Call script with no command and invalid option
  *Input*:
    ```python
    python python_proj.py -f
    ```
  *Result*:
    ```python
    python_proj.py: error: the following arguments are required: <command>
    ```

<br/>

**Valid:**
-[x] Call script with --help or -h
  *Input*:
    ```python
    python python_proj.py -h
    ```
  *Result*:
    ```python
    Task Management Script

    options:
    -h, --help           show this help message and exit
    
    Available Commands:
    <command>
      selectAll          Select all tasks from the given database
      createTask         Create a new task
      updateTaskName     Update the name of a task
      updateDescription  Update the description of a task
      updateStatus       Update the status of a task
      updateDueDate      Update the due date of a task
      removeTask         Delete a task and its information
    ```

<br/>
<br/>

### Select All
**Errors:**
-[x] selectAll command with no options or arguments
  *Input:*
  ```python
  python python_proj.py selectAll
  ```
  Output:
  ```python
  usage: python_proj.py selectAll [-h] --database DATABASE --table TABLE
  python_proj.py selectAll: error: the following arguments are required: --database, --table
  ```

-[x] selectAll command with --database argument but no --table argument
  *Input:*
  ```python
  python python_proj.py selectAll --database database
  ```
  *Output:*
  ```python
  usage: python_proj.py selectAll [-h] --database DATABASE --table TABLE
  python_proj.py selectAll: error: the following arguments are required: --table
  ```

-[x] selectAll command with --table argument but no --database argument
  *Input:*
    ```python
    python python_proj.py selectAll --table tasks
    ```  
  *Output:*
    ```python
    usage: python_proj.py selectAll [-h] --database DATABASE --table TABLE
    python_proj.py selectAll: error: the following arguments are required: --database
    ```

<br/>

**Valid:**
-[x] selectAll command with -h or --help
  *Input:*
    ```python
    python python_proj.py selectAll -h
    ```
  *Ouput:*
    ```python
    usage: python_proj.py selectAll [-h] --database DATABASE --table TABLE

    options:
    -h, --help           show this help message and exit
    --database DATABASE  The database to which tasks can be created, removed, and/or modified
    --table TABLE        The table to which tasks can be created, removed, and/or modified
    ```

-[x] selectAll command with database that doesn't exist yet
  *Input:*
    ```python
    python python_proj.py selectAll --database database10 --table tasks
    ```
  *Output:*
    ```python
    The database 'database' does not exist.
    Would you like to create 'database'? [Enter 'yes' or 'no']: <yes>
    Creating database and table...
    Database 'database' and table 'tasks' created. Running commands...
    All tasks from database:
    []
    ```

-[x] selectAll command with table that doesn't exist yet but the database does
  *Input:*
    ```python
    python python_proj.py selectAll --database database --table tasks2
    ```
  *Output:*
    ```python
    The table 'tasks2' does not exist within 'database.'
    Would you like to create 'tasks2' within 'database? [Enter 'yes' or 'no']: <yes>
    Creating table...
    Table 'tasks2' created within 'database.' Running commands...
    All tasks from database:
    []
    ```

-[x] selectAll command
  *Input:*
    ```python
    python python_proj.py selectAll --database database --table tasks
    ```
    *Output:*
    ```python
    Database 'database' and table 'tasks' found. Running commands...
    All tasks from database: 
    [(1, 'Do dishes', 'Do dishes', 'Complete', '4/15/2025'), (2, 'Walk dog', 'Walk dog', 'Not Started', '4/15/2025')]
    ```

<br/>
<br/>

### Create Task
**Errors:**
-[x] createTask command with no options or arguments
  *Input:*
    ```python
    python python_proj.py createTask
    ```
  *Output:*
    ```python
    usage: python_proj.py createTask [-h] --database DATABASE --table TABLE --taskName TASKNAME --description DESCRIPTION --status {Complete,In Progress,On Hold,Not Started} [--dueDate DUEDATE]
    
    python_proj.py createTask: error: the following arguments are required: --database, --table, --taskName, --description, --status
    ```

-[x] createTask command with missing argument
  *Input:*
    ```python
    python python_proj.py createTask --database database --table tasks --description "Make dinner" --status "In Progress" --dueDate "04/05/2025"
    ```
  *Output:*
    ```python
    usage: python_proj.py createTask [-h] --database DATABASE --table TABLE --taskName TASKNAME --description DESCRIPTION --status {Complete,In Progress,On Hold,Not Started} [--dueDate DUEDATE]

    python_proj.py createTask: error: the following arguments are required: --taskName
    ```
-[x] createTask command with invalid date format
  *Input:*
    ```python
    python python_proj.py createTask --database database --table tasks --taskName "Make dinner" --description "Make dinner" --status "In Progress" --dueDate "0403"
    ```
  *Output:*
    ```python
    Invalid date format. Please enter date in MM/DD/YYYY format
    Exiting...
    ```

-[x] createTask command if task name already exists
  *Input:*
    ```python
    python python_proj.py createTask --database database --table tasks --taskName "Make dinner" --description "Make dinner" --status "In Progress" --dueDate "04/06/2025"
    ```
  *Output:*
    ```python
    The task 'Make dinner' already exists. Please create a unique task.
    Exiting...
    ```

<br/>

**Valid:**
-[x] createTask command with -h or --help
  *Input:*
    ```python
    python python_proj.py createTask -h
    ```
  *Ouput:*
    ```python
      usage: python_proj.py createTask [-h] --database DATABASE --table TABLE --taskName TASKNAME --description DESCRIPTION --status {Complete,In Progress,On Hold,Not Started} [--dueDate DUEDATE]

    options:
    -h, --help            show this help message and exit
    --database DATABASE   The database to which tasks can be created, removed, and/or modified
    --table TABLE         The table to which tasks can be created, removed, and/or modified
    --taskName TASKNAME   The name of the task
    --description DESCRIPTION
    The description of the task
    --status {Complete,In Progress,On Hold,Not Started}
    The status of the task
    --dueDate DUEDATE     The due date of the task
    ```

-[x] createTask command with database that doesn't exist yet
  *Input:*
    ```python
    python python_proj.py createTask --database database10 --table tasks --taskName "Make dinner" --description "Make dinner" --status "In Progress" --dueDate "04/06/2025"
    ```
  *Output:*
    ```python
    The database 'database2' does not exist.
    Would you like to create 'database2'? [Enter 'yes' or 'no']: <no>
    Exiting...
    ```

-[x] createTask command with table that doesn't exist yet but the database does
  *Input:*
    ```python
    python python_proj.py createTask --database database --table tasks2 --taskName "Make dinner" --description "Make dinner" --status "In Progress" --dueDate "04/06/2025"
    ```
  *Output:*
    ```python
    The table 'tasks3' does not exist within 'database.'
    Would you like to create 'tasks3' within 'database? [Enter 'yes' or 'no']: <yes>
    Creating table...
    Table 'tasks3' created within 'database.' Running commands...
    Task created.
    ```

-[x] createTask command with missing dueDate argument (not required -- valid input)
  *Input:*
    ```python
    python python_proj.py createTask --database database --table tasks --taskName "Make dinner" --description "Make dinner" --status "In Progress"
    ```
  *Output:*
    ```python
    Database 'database' and table 'tasks' found. Running commands...
    Task created.
    ```

-[x] createTask command with all arguments
  *Input:*
    ```python
    python python_proj.py createTask --database database --table tasks --taskName "Make dinner" --description "Make dinner" --status "In Progress" --dueDate "04/06/2025"
    ```
  *Output:*
    ```python
    Database 'database' and table 'tasks' found. Running commands...
    Task created.
    ```

<br/>
<br/>

### Update Task Name
**Errors:**
-[x] updateTaskName command with no options or arguments
  *Input:*
    ```python
    python python_proj.py updateTaskName
    ```
  *Output:*
    ```python
    usage: python_proj.py updateTaskName [-h] --database DATABASE --table TABLE --taskName TASKNAME --taskID TASKID
    python_proj.py updateTaskName: error: the following arguments are required: --database, --table, --taskName, --taskID
    ```

-[x] updateTaskName command with missing argument
  *Input:*
    ```python
    python python_proj.py updateTaskName --database database --table tasks
    ```
  *Output:*
    ```python
    usage: python_proj.py updateTaskName [-h] --database DATABASE --table TABLE --taskName TASKNAME --taskID TASKID
    python_proj.py updateTaskName: error: the following arguments are required: --taskName, --taskID
    ```

-[x] updateTaskName command if task name already exists
  *Input:*
    ```python
    python python_proj.py updateTaskName --database database --table tasks --taskName "Walk dog" --taskID 1
    ```
  *Output:*
    ```python
    The task 'Walk dog' already exists. Please create a unique task.
    Exiting...
    ```

<br/>

**Valid:**
-[x] updateTaskName command with -h or --help
  *Input:*
    ```python
    python python_proj.py updateTaskName -h
    ```
  *Ouput:*
    ```python
    usage: python_proj.py updateTaskName [-h] --database DATABASE --table TABLE --taskName TASKNAME --taskID TASKID

    options:
    -h, --help           show this help message and exit
    --database DATABASE  The database to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --table TABLE        The table to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --taskName TASKNAME  The name of the task; ensure this is in quotes
    --taskID TASKID      The number ID of the task (automatically assigned to task at creation)
    ```

-[x] updateTaskName command with database that doesn't exist yet
  *Input:*
    ```python
    python python_proj.py updateTaskName --database database2 --table tasks --taskName "Make dinner" --taskID 1
    ```
  *Output:*
    ```python
    The 'database2' does not exist. Able to create 'database2, but the task will not be created/updated.
    Continue? [Enter yes or no]: <yes>
    Creating database and table...
    Database 'database2' and table 'tasks' created. Exiting without task update/creation...
    ```

-[x] updateTaskName command with table that doesn't exist yet but the database does
  *Input:*
    ```python
    python python_proj.py updateTaskName --database database --table tasks5 --taskName "Make dinner" --taskID 1
    ```
  *Output:*
    ```python
    The table 'tasks5' does not exist. Able to create 'tasks5,' but the task will not be created/updated.
    Continue? [Enter yes or no]: yes
    Creating database and table...
    Table 'tasks5' created within database 'database'. Exiting without task update/creation...
    ```

-[x] updateTaskName command with all arguments
  *Input:*
    ```python
    python python_proj.py updateTaskName --database database --table tasks --taskName "Make dinner" --taskID 1
    ```
  *Output:*
    ```python
    Database 'database' and table 'tasks' found. Running commands...
    Task name updated.
    ```

<br/>
<br/>

### Update Description
**Errors:**
-[x] updateDescription command with no options or arguments
  *Input:*
    ```python
    python python_proj.py updateDescription
    ```
  *Output:*
    ```python
    usage: usage: python_proj.py updateDescription [-h] --database DATABASE --table TABLE --description DESCRIPTION [--taskID TASKID] [--taskName TASKNAME]
    python_proj.py updateDescription: error: the following arguments are required: --database, --table, --description
    ```

-[x] updateDescription command with missing argument
  *Input:*
    ```python
    python python_proj.py updateDescription --database database --table tasks
    ```
  *Output:*
    ```python
    usage: python_proj.py updateDescription [-h] --database DATABASE --table TABLE --description DESCRIPTION [--taskID TASKID] [--taskName TASKNAME]
    python_proj.py updateDescription: error: the following arguments are required: --description
    ```

<br/>

**Valid:**
-[x] updateDescription command with -h or --help
  *Input:*
    ```python
    python python_proj.py updateDescription -h
    ```
  *Ouput:*
    ```python
    usage: python_proj.py updateDescription [-h] --database DATABASE --table TABLE --description DESCRIPTION [--taskID TASKID] [--taskName TASKNAME]

    options:
    -h, --help            show this help message and exit
    --database DATABASE   The database to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --table TABLE         The table to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --description DESCRIPTION
    The description of the task; ensure this is in quotes
    --taskID TASKID       The number ID of the task (automatically assigned to task at creation)
    --taskName TASKNAME   The name of the task; ensure this is in quotes
    ```

-[x] updateDescription command with database that doesn't exist yet
  *Input:*
    ```python
    python python_proj.py updateDescription --database database2 --table tasks --taskName "Make dinner" --description "Need grocery list"
    ```
  *Output:*
    ```python
    The database 'database2' does not exist. Able to create 'database2, but the task will not be created/updated.
    Continue? [Enter yes or no]: <no>
    Exiting...
    ```

-[x] updateDescription command with table that doesn't exist yet but the database does
  *Input:*
    ```python
    python python_proj.py updateDescription --database database --table tasks6 --description "Need grocery list" --taskName "Make dinner"
    ```
  *Output:*
    ```python
    The table 'tasks6' does not exist. Able to create 'tasks6,' but the task will not be created/updated.
    Continue? [Enter yes or no]: <no>
    Exiting...
    ```

-[x] updateDescription command with all arguments
  *Input:*
    ```python
    python python_proj.py updateDescription --database database --table tasks --taskName "Make dinner" --description "Need grocery list"
    ```
  *Output:*
    ```python
    Database 'database' and table 'tasks' found. Running commands...
    Description updated.
    ```

<br/>
<br/>

### Update Status
**Errors:**
-[x] updateStatus command with no options or arguments
  *Input:*
    ```python
    python python_proj.py updateStatus
    ```
  *Output:*
    ```python
    usage: python_proj.py updateStatus [-h] --database DATABASE --table TABLE --status {Complete,In Progress,On Hold,Not Started} [--taskID TASKID] [--taskName TASKNAME]
    python_proj.py updateStatus: error: the following arguments are required: --database, --table, --status
    ```

-[x] updateStatus command with missing argument
  *Input:*
    ```python
    python python_proj.py updateStatus --database database --table tasks --taskName "Make dinner"
    ```
  *Output:*
    ```python
    usage: python_proj.py updateStatus [-h] --database DATABASE --table TABLE --status {Complete,In Progress,On Hold,Not Started} [--taskID TASKID] [--taskName TASKNAME]
    python_proj.py updateStatus: error: the following arguments are required: --status
    ```

<br/>

**Valid:**
-[x] updateStatus command with -h or --help
  *Input:*
    ```python
    python python_proj.py updateStatus -h
    ```
  *Ouput:*
    ```python
    usage: python_proj.py updateStatus [-h] --database DATABASE --table TABLE --status {Complete,In Progress,On Hold,Not Started} [--taskID TASKID] [--taskName TASKNAME]
    
    options:
    -h, --help            show this help message and exit
    --database DATABASE   The database to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --table TABLE         The table to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --status {Complete,In Progress,On Hold,Not Started}
    The status of the task; ensure this is in quotes
    --taskID TASKID       The number ID of the task (automatically assigned to task at creation)
    --taskName TASKNAME   The name of the task; ensure this is in quotes
    ```

-[x] updateStatus command with database that doesn't exist yet
  *Input:*
    ```python
    python python_proj.py updateStatus --database database2 --table tasks --taskName "Make dinner" --status "Complete"
  Output:
    The database 'database2' does not exist. Able to create 'database2, but the task will not be created/updated.
    Continue? [Enter yes or no]: <no>
    Exiting...
    ```

-[x] updateStatus command with table that doesn't exist yet but the database does
  *Input:*
    ```python
    python python_proj.py updateStatus --database database --table tasks6 --taskName "Make dinner" --status "Complete"
    ```
  *Output:*
    ```python
    The table 'tasks6' does not exist within 'database.' Able to create 'tasks6,' but the task will not be created/updated.
    Continue? [Enter yes or no]: <no>
    Exiting...
    ```

-[x] updateStatus command with all arguments
  *Input:*
    ```python
    python python_proj.py updateStatus --database database --table tasks --taskName "Make dinner" --status "Complete"
    ```
  *Output:*
    ```python
    Database 'database' and table 'tasks' found. Running commands...
    Status updated.
    ```

<br/>
<br/>

### Update Due Date
**Errors:**
-[x] updateDueDate command with no options or arguments
  *Input:*
    ```python
    python python_proj.py updateDueDate
    ```
  *Output:*
    ```python
    usage: python_proj.py updateDueDate [-h] --database DATABASE --table TABLE --dueDate DUEDATE [--taskID TASKID] [--taskName TASKNAME]
    python_proj.py updateDueDate: error: the following arguments are required: --database, --table, --dueDate
    ```

-[x] updateDueDate command with missing argument
  *Input:*
    ```python
    python python_proj.py updateDueDate --database database --table tasks --taskName "Make dinner"
    ```
  *Output:*
    ```python
    usage: python_proj.py updateDueDate [-h] --database DATABASE --table TABLE --dueDate DUEDATE [--taskID TASKID] [--taskName TASKNAME]
    python_proj.py updateDueDate: error: the following arguments are required: --dueDate
    ```

-[x] updateDueDate command with invalid date format
  *Input:*
    ```python
    python python_proj.py createTask --database database --table tasks --taskName "Make dinner" --dueDate "0403"
    ```
  *Output:*
    ```python
    Invalid date format. Please enter date in MM/DD/YYYY format
    Exiting...
    ```

<br/>

**Valid:**
-[x] updateDueDate command with -h or --help
  *Input:*
    ```python
    python python_proj.py updateDueDate -h
    ```
  *Ouput:*
    ```python
    usage: usage: python_proj.py updateDueDate [-h] --database DATABASE --table TABLE --dueDate DUEDATE [--taskID TASKID] [--taskName TASKNAME]

    options:
    -h, --help           show this help message and exit
    --database DATABASE  The database to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --table TABLE        The table to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --dueDate DUEDATE    The due date of the task; ensure this is in quotes and DD/MM/YYYY format
    --taskID TASKID      The number ID of the task (automatically assigned to task at creation)
    --taskName TASKNAME  The name of the task; ensure this is in quotes
    ```

-[x] updateDueDate command with database that doesn't exist yet
  *Input:*
    ```python
    python python_proj.py updateDueDate --database database2 --table tasks --taskName "Make dinner" --dueDate "05/05/2025"
    ```
  *Output:*
    ```python
    The database 'database2' does not exist. Able to create 'database2, but the task will not be created/updated.
    Continue? [Enter yes or no]: <no>
    Exiting...
    ```

-[x] updateDueDate command with table that doesn't exist yet but the database does
  *Input:*
    ```python
    python python_proj.py updateDueDate --database database --table tasks6 --taskName "Make dinner" --dueDate "05/05/2025"
    ```
  *Output:*
    ```python
    The table 'tasks6' does not exist within 'database.' Able to create 'tasks6,' but the task will not be created/updated.
    Continue? [Enter yes or no]: <no>
    Exiting...
    ```

-[x] updateDueDate command with all arguments
  *Input:*
    ```python
    python python_proj.py updateDueDate --database database --table tasks --taskName "Make dinner" --dueDate "05/05/2025"
    ```
  *Output:*
    ```python
    Database 'database' and table 'tasks' found. Running commands...
    Due date updated.
    ```

<br/>
<br/>

### Delete Task
**Errors:**
-[x] removeTask command with no options or arguments
  *Input:*
    ```python
    python python_proj.py removeTask
    ```
  *Output:*
    ```python
    usage: python_proj.py removeTask [-h] --database DATABASE --table TABLE [--taskName TASKNAME] [--taskID TASKID]
    python_proj.py removeTask: error: the following arguments are required: --database, --table
    ```

-[x] removeTask command with --database argument but no --table argument
  *Input:*
    ```python
    python python_proj.py removeTask --database database
    ```
  *Output:*
    ```python
    usage: python_proj.py removeTask [-h] --database DATABASE --table TABLE [--taskName TASKNAME] [--taskID TASKID]
    python_proj.py removeTask: error: the following arguments are required: --table
    ```

-[x] removeTask command with --table argument but no --database argument
  *Input:*
    ```python
    python python_proj.py removeTask --table tasks
    ```
  *Output:*
    ```python
    usage: python_proj.py removeTask [-h] --database DATABASE --table TABLE [--taskName TASKNAME] [--taskID TASKID]
    python_proj.py removeTask: error: the following arguments are required: --database
    ```

-[x] removeTask command without either --taskID or --taskName
  *Input:*
    ```python
    python python_proj.py removeTask --database database --table tasks
    ```
  *Output:*
    ```python
    Missing argument. Please provide --taskName or --taskID to remove task.
    Exiting...
    ```

<br/>

**Valid:**
-[x] removeTask command with -h or --help
  *Input:*
    ```python
    python python_proj.py removeTask -h
    ```
  *Output:*
    ```python
    usage: python_proj.py removeTask [-h] --database DATABASE --table TABLE [--taskName TASKNAME] [--taskID TASKID]

    options:
    -h, --help           show this help message and exit
    --database DATABASE  The database to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --table TABLE        The table to which tasks can be created, removed, and/or modified; ensure this is in quotes
    --taskName TASKNAME  The name of the task; ensure this is in quotes
    --taskID TASKID      The number ID of the task (automatically assigned to task at creation)
    ```

-[x] removeTask command with database that doesn't exist yet
  *Input:*
    ```python
    python python_proj.py removeTask --database database2 --table tasks --taskID 2
    ```
  *Output:*
    ```python
    The database 'database3' does not exist. Able to create 'database3, but there will be no task created for deletion.
    Continue? [Enter yes or no]: <no>
    Exiting...
    ```

-[x] removeTask command with table that doesn't exist yet but the database does
  *Input:*
    ```python
    python python_proj.py removeTask --database database --table tasks6 --taskID 2
    ```
  *Output:*
    ```python
    The table 'tasks6' does not exist within 'database.'
    Would you like to create 'tasks6' within 'database? [Enter 'yes' or 'no']: <no>
    Exiting...
    ```

-[x] removeTask command
  *Input:*
    ```python
    python python_proj.py removeTask --database database --table tasks --taskID 2
    ```
  *Output:*
    ```python
    Database 'database' and table 'tasks' found. Running commands...
    Task deleted.
    ```








                        
