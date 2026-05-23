import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students(name, age, course) VALUES (?, ?, ?)",
            (name, age, course)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)