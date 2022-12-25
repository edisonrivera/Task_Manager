import sqlite3
from typing import List
import datetime
from model import ToDo

conn = sqlite3.connect('Tasks.db')
c = conn.cursor()


def create_table():
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            task text,
            category text,
            date_added text,
            date_completed text,
            status integer,
            position integer
        )    
    """)

create_table()

def insert_task(toDo: ToDo):
    c.execute("SELECT count(*) FROM tasks")
    count = c.fetchone()[0]
    toDo.position = count if count else 0 
    with conn:
        c.execute('INSERT INTO tasks VALUES(:task, :category, :date_added, :date_completed, :status, :position)', 
        {'task': toDo.task, 'category': toDo.category, 'date_added': toDo.date_added, 'date_completed': toDo.date_completed
        , 'status': toDo.status, 'position': toDo.position})


def get_tasks() -> List[ToDo]:
    c.execute("SELECT * FROM tasks")
    results = c.fetchall()
    tasks = []

    for result in results:
        tasks.append(ToDo(*result))

    return tasks

def delete_task(position):
    c.execute("SELECT COUNT(*) FROM tasks")
    count = c.fetchone()[0]

    with conn:
        c.execute("DELETE FROM tasks WHERE position=:position", {'position': position})
        for pos in range (position+1, count):
            change_position(pos, pos-1, False)


def change_position(old_position: int, new_position: int, commit=True):
    c.execute("UPDATE tasks SET position=:new_position WHERE position=:old_position", {'new_position': new_position, 'old_position': old_position})
    if commit:
        conn.commit()


def update_task(position: int, task: str, category: str):
    with conn:
        if task is not None and category is not None:
            c.execute("UPDATE tasks SET task=:task, category=:category WHERE position=:position", {
                'position' : position, 'task': task, 'category': category
            })

        elif task is not None:
            c.execute("UPDATE tasks SET task=:task WHERE position=:position", {'position' : position, 'task': task})
        
        elif category is not None:
            c.execute("UPDATE tasks SET category=:category WHERE position=:position", {
                'position' : position, 'category': category
            })


def complete_task(position: int):
    with conn:
        c.execute("UPDATE tasks SET status = 2, date_completed =:date_completed WHERE position=:position", {'position': position, 'date_completed': datetime.datetime.now().strftime("%d/%m/%Y")})