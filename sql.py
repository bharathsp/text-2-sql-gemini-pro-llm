import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('student.db')

# Create a cursor object to insert, update, delete, and query data
cursor = connection.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name VARCHAR(25) NOT NULL,
        class VARCHAR(25),
        marks INT
    )
''')

# Insert sample data
cursor.execute('''
    INSERT INTO students (name, class, marks) VALUES
    ('John Doe', '10th Grade', 85),
    ('Jane Smith', '9th Grade', 78),
    ('Michael Brown', '11th Grade', 92),
    ('Emily Davis', '8th Grade', 88),
    ('David Wilson', '10th Grade', 67),
    ('Sarah Johnson', '12th Grade', 95),
    ('Robert Taylor', '9th Grade', 81),
    ('Laura Anderson', '10th Grade', 73),
    ('James Thomas', '8th Grade', 90),
    ('Anna Moore', '11th Grade', 84),
    ('Chris Miller', '12th Grade', 76),
    ('Olivia Clark', '9th Grade', 82),
    ('Daniel Lewis', '10th Grade', 65),
    ('Sophia Hall', '11th Grade', 97),
    ('Liam Young', '12th Grade', 71),
    ('Isabella King', '9th Grade', 89),
    ('Ethan Wright', '8th Grade', 75),
    ('Mia Scott', '10th Grade', 91),
    ('Noah Green', '11th Grade', 88),
    ('Ava Adams', '12th Grade', 83),
    ('William Baker', '9th Grade', 77),
    ('Charlotte Gonzalez', '8th Grade', 86),
    ('Lucas Perez', '10th Grade', 79),
    ('Amelia Campbell', '11th Grade', 94),
    ('Mason Turner', '12th Grade', 68),
    ('Harper Mitchell', '9th Grade', 87),
    ('Elijah Carter', '8th Grade', 72),
    ('Evelyn Roberts', '10th Grade', 90),
    ('Benjamin Phillips', '11th Grade', 85),
    ('Abigail Evans', '12th Grade', 93),
    ('Logan Parker', '9th Grade', 80),
    ('Ella Edwards', '8th Grade', 88),
    ('Alexander Collins', '10th Grade', 66),
    ('Grace Stewart', '11th Grade', 79),
    ('Jacob Sanchez', '12th Grade', 84),
    ('Chloe Morris', '9th Grade', 81),
    ('Matthew Rogers', '8th Grade', 89),
    ('Zoe Reed', '10th Grade', 92),
    ('Henry Cook', '11th Grade', 78),
    ('Lily Morgan', '12th Grade', 87),
    ('Jack Bell', '9th Grade', 74),
    ('Ella Murphy', '8th Grade', 95),
    ('Sebastian Bailey', '10th Grade', 70),
    ('Victoria Rivera', '11th Grade', 88),
    ('Samuel Cooper', '12th Grade', 90),
    ('Scarlett Richardson', '9th Grade', 76),
    ('David Cox', '8th Grade', 82),
    ('Layla Howard', '10th Grade', 91),
    ('Owen Ward', '11th Grade', 85),
    ('Hannah Torres', '12th Grade', 89)
''')

data = cursor.execute('SELECT * FROM students').fetchall()

for row in data:
    print(row)

# Commit changes and close the connection
connection.commit()
connection.close()