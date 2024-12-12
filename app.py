from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')





db_config = {
    'host': 'localhost',
    'user': 'root',        
    'password': 'Uikey@06',
    'database': 'users'    
}
@app.route('/users')
def users():
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, role FROM users")
    users_list = cursor.fetchall()

   
    cursor.close()
    conn.close()

    
    return render_template('users.html', users=users_list)

if __name__ == '__main__':
    app.run(debug=True)



