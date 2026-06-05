import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.config['MYSQL_HOST'] = os.getenv("DB_HOST")
app.config['MYSQL_USER'] = os.getenv("DB_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("DB_NAME")

mysql = MySQL(app)

@app.route('/')
def index():
    search_query = request.args.get('search', '').strip()
    cur = mysql.connection.cursor()
    
    # 1. Fetch filtered or total student records
    if search_query:
        query = "SELECT * FROM students WHERE name LIKE %s OR department LIKE %s ORDER BY id DESC"
        cur.execute(query, (f"%{search_query}%", f"%{search_query}%"))
    else:
        cur.execute("SELECT * FROM students ORDER BY id DESC")
    students = cur.fetchall()
    
    # 2. Compute live dashboard metrics using SQL aggregations
    cur.execute("SELECT COUNT(*), AVG(marks), MAX(marks) FROM students")
    stats_raw = cur.fetchone()
    
    stats = {
        "total": stats_raw[0] if stats_raw[0] else 0,
        "avg_marks": round(stats_raw[1], 1) if stats_raw[1] else 0,
        "top_score": stats_raw[2] if stats_raw[2] else 0
    }
    
    cur.close()
    return render_template('index.html', students=students, stats=stats, search_query=search_query)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name'].strip()
        dept = request.form['department'].strip()
        marks = request.form['marks']
        attendance = request.form['attendance']

        if not name or not dept or not marks or not attendance:
            flash("All fields are strictly required.", "danger")
            return redirect(url_for('add_student'))

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO students (name, department, marks, attendance) VALUES (%s, %s, %s, %s)",
            (name, dept, marks, attendance)
        )
        mysql.connection.commit()
        cur.close()
        
        flash(f"Record for {name} has been securely enrolled.", "success")
        return redirect(url_for('index'))
        
    return render_template('add_student.html')

@app.route('/delete/<int:id>')
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    
    flash("Student record successfully deleted from the registry.", "dark")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)