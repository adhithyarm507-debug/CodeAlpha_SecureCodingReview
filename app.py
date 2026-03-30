from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    if cursor.fetchone():
        return "Login Success"
    else:
        return "Login Failed"

app.run(debug=True)
