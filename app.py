
# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(__name__)

# # Initialize the database
# def init_db():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             age INTEGER NOT NULL,
#             occupation TEXT NOT NULL,
#             salary INTEGER NOT NULL,
#             email TEXT NOT NULL UNIQUE,
#             password TEXT NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         occupation = request.form['occupation']
#         salary = request.form['salary']
#         email = request.form['email']
#         password = request.form['password']
        
#         # Store user data in the database
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO users (name, age, occupation, salary, email, password)
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (name, age, occupation, salary, email, password))
#         conn.commit()
#         conn.close()
        
#         return redirect(url_for('login'))
#     return render_template('register.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Simple authentication
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (username, password))
#         user = cursor.fetchone()
#         conn.close()
        
#         if user:
#             return render_template('index.html')
#         else:
#             return "Invalid credentials, please try again."
#     return render_template('login.html')

# @app.route('/invest')
# def invest():
#         return render_template('invest.html')

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            occupation TEXT NOT NULL,
            salary INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        occupation = request.form['occupation']
        salary = request.form['salary']
        email = request.form['email']
        password = request.form['password']
        
        # Store user data in the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, age, occupation, salary, email, password)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, age, occupation, salary, email, password))
        conn.commit()
        conn.close()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Simple authentication
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return render_template('index.html')
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

from flask import jsonify

@app.route('/get_salary_data')
def get_salary_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT salary FROM users")  # Adjust table and column names as needed
    data = cursor.fetchall()
    conn.close()
    
    # Extract salary values into a list
    salaries = [row[0] for row in data]
    
    return jsonify(salaries)




@app.route('/invest')
def invest():
    return render_template('invest.html')

@app.route('/page3fin')
def page3():
    return render_template('page3fin.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/Welcome')
def Welcome():
    return render_template('Welcome.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/welcome2')
def welcome2():
    return render_template('welcome2.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/page6')
def page6():
    return render_template('page6.html')

@app.route('/page7')
def page7():
    return render_template('page7.html')

@app.route('/page8')
def page8():
    return render_template('page8.html')

@app.route('/page9')
def page9():
    return render_template('page9.html')

@app.route('/page10')
def page10():
    return render_template('page10.html')


@app.route('/page11')
def page11():
    return render_template('page11.html')


@app.route('/bank')
def bank():
    return render_template('bank.html')

@app.route('/Bonds')
def Bonds():
    return render_template('Bonds.html')

@app.route('/Stocks')
def Stocks():
    return render_template('Stocks.html')

@app.route('/govern')
def govern():
    return render_template('govern.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

@app.route('/KnowStocks')
def KnowStocks():
    return render_template('KnowStocks.html')

@app.route('/tax')
def tax():
    return render_template('tax.html')





if __name__ == '__main__':
    init_db()
    app.run(debug=True)