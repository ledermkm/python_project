import sqlite3
import re
from datetime import datetime


# CREATE DATABASE AND TABLE (if applicable)
def createTable(database, table):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
            
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table} (
        taskID INTEGER PRIMARY KEY AUTOINCREMENT,
        taskName TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL,
        dueDate REAL)
    ''')
    conn.commit()
    return conn, cursor

# VALIDATE IF TABLE EXISTS
def validTable(database, table):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,))
    result = cursor.fetchone()
    return result is not None


# VALIDATE DUE DATE FORMAT:
def validDate(date):
    reg = r"^(0[1-9]|1[0-2])/([0-2][0-9]|3[01])/([0-9]{4})$"
    if not re.match(reg, date):
        print("Invalid date format. Please enter date in MM/DD/YYYY format")
        print("Exiting...")
        exit(1)
    else:
        return date


# VALIDATE IF TASK ALREADY EXISTS:
def checkExist(database, table, taskName):
    conn, cursor = createTable(database, table)

    cursor.execute(f"SELECT 1 FROM {table} where taskName = ? LIMIT 1", (taskName,))
    check = cursor.fetchone()
    return check is not None

# SELECT ALL:
def selectAll(database, table):
    conn, cursor = createTable(database, table)

    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    print(rows)


# CREATE A TASK:
def createTask(database, table, taskName, description, dueDate, status):
    conn, cursor = createTable(database, table)

    cursor.execute('''INSERT INTO tasks
        (taskName, description, dueDate, status) VALUES (?, ?, ?, ?)''',
        (taskName, description, dueDate, status)
    )
    conn.commit()

# TEST:
#createTask("Complete Task", "This task needs completing", "4/15/2025", "Complete")


# UPDATE TASK NAME:
def updateTaskName(database, table, taskName, taskID):
    conn, cursor = createTable(database, table)

    cursor.execute('''UPDATE tasks
        SET taskName = ? WHERE taskID = ?''',
        (taskName, taskID)
    )
    conn.commit()

# TEST:
#updateTaskName("Remove Task", 1)


# UPDATE TASK DESCRIPTION:
def updateDescription(database, table, description, taskID, taskName):
    conn, cursor = createTable(database, table)

    cursor.execute('''UPDATE tasks
        SET description = ? WHERE taskID = ? OR taskName = ?''',
        (description, taskID, taskName)
    )
    conn.commit()

# TEST:
#updateDescription("Remove Task", 1, None)


# UPDATE STATUS:
def updateStatus(database, table, status, taskID, taskName):
    conn, cursor = createTable(database, table)

    cursor.execute('''UPDATE tasks
        SET status = ? WHERE taskID = ? OR taskName = ?''',
        (status, taskID, taskName)
    )
    conn.commit()

# TEST:
#updateStatus("Complete", None, "Remove Task")


# UPDATE DUE DATE:
def updateDueDate(database, table, dueDate, taskID, taskName):
    conn, cursor = createTable(database, table)

    date = datetime.strptime(dueDate, "%m/%d/%Y")
    dueDate = date.strftime("%Y-%m-%d")
    cursor.execute('''UPDATE tasks
        SET dueDate = ? WHERE taskID = ? OR taskName = ?''',
        (dueDate, taskID, taskName)
    )
    conn.commit()

# TEST:
#updateDueDate("05/05/2025", 1, None)


# DELETE TASK
def removeTask(database, table, taskID, taskName):
    conn, cursor = createTable(database, table)

    cursor.execute('''DELETE FROM tasks
        WHERE taskID = ? OR taskName = ?''',
        (taskID, taskName)
    )
    conn.commit()

# TEST:
#removeTask(1, None)