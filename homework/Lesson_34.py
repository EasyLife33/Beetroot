#Task 1
import sqlite3

try:
    connection = sqlite3.connect('example_db.db')
    cursor = connection.cursor()
    print('Connected')
    get_data_query = "SELECT * FROM your_users"

    create_table_query = """CREATE TABLE IF NOT EXISTS my_users 
                                (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(255) NOT NULL)"""
    cursor.execute(create_table_query)
    print('Table created')

    rename_table_query = "ALTER TABLE my_users RENAME TO your_users"
    cursor.execute(rename_table_query)
    print('Table renamed')

    add_column_query = "ALTER TABLE your_users ADD COLUMN gender char(1)"
    cursor.execute(add_column_query)
    print('Column Added')

    users = [('Yura','Male'), ('Nazar','Male'), ('Ostap','Male')]

    for user in users:
        add_user_query = """INSERT INTO your_users (name, gender) VALUES (?, ?)"""
        cursor.execute(add_user_query, user)
    print('Rows added')
    cursor.execute(get_data_query)
    data = cursor.fetchall()
    print(data)

    update_query = "UPDATE your_users SET name='Olena' WHERE id = 1"
    cursor.execute(update_query)
    cursor.execute(get_data_query)
    data = cursor.fetchall()
    print(data)

    delete_query = "DELETE FROM your_users WHERE name = 'Ostap'"
    cursor.execute(delete_query)
    cursor.execute(get_data_query)
    data = cursor.fetchall()
    print(data)


except sqlite3.Error as e:
    print(e)
finally:
    cursor.execute('DROP TABLE your_users')
    print('Table droped')
    cursor.close()
    connection.close()
    print('CLOSED')


#Task 2
import sqlite3
import contextlib


@contextlib.contextmanager
def get_connection(db):
    conn = sqlite3.connect(db)
    try:
        yield conn
    finally:
        conn.close()
        if cursor:
            cursor.close


with get_connection('example_db.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT first_name as [First Name], last_name as [Last Name] FROM employees")
    data = cursor.fetchone()
    print(data)
    print()

    unique_dep_id_query = "SELECT DISTINCT department_id FROM employees"
    cursor.execute(unique_dep_id_query)
    data = cursor.fetchall()
    print(data)
    print()

    get_all_details_query = "SELECT * FROM employees ORDER BY first_name DESC"
    cursor.execute(get_all_details_query)
    data = cursor.fetchmany(size=5)
    for d in data:
        print(d)
    print()

    pf_query = "SELECT first_name, last_name, salary, (salary*0.12) as PF FROM employees"
    cursor.execute(pf_query)
    data = cursor.fetchmany(size=5)
    for d in data:
        print(d)
    print()

    min_max_query = "SELECT MIN(salary), MAX(salary) FROM employees"
    cursor.execute(min_max_query)
    data = cursor.fetchall()
    print(data)
    print()

    round_query = "SELECT first_name, last_name, ROUND(salary-salary*0.12, 2) as monthly_salary FROM employees"
    cursor.execute(round_query)
    data = cursor.fetchmany(size=5)
    for d in data:
        print(d)

