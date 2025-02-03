import sqlite3

# Create a connection to the database
def create_connection():
    conn = sqlite3.connect('tasks.db')
    return conn

# Create the tasks table
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            deadline TEXT,
            completed INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Add a task
def add_task(title, description, deadline):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, deadline) 
        VALUES (?, ?, ?)
    ''', (title, description, deadline))
    conn.commit()
    conn.close()

# Fetch all tasks
def fetch_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Mark a task as complete
def mark_completed(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
