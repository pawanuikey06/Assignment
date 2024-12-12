from flask import Flask, render_template, request, redirect, url_for,flash
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


# USERS 
@app.route('/users')
def users():
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email, role FROM users")
    users_list = cursor.fetchall()

   
    cursor.close()
    conn.close()

    
    return render_template('users.html', users=users_list)




# NEW USERS
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        
        conn =mysql.connector.connect(**db_config)
        cursor =conn.cursor()

        query = "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, role))
        conn.commit()

        cursor.close()
        conn.close()
        
        
        return redirect(url_for('users'))
    
    return render_template('new_user.html')



# Getting Specific Users By there ID
@app.route('/users/<int:id>')
def user_detail(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor= conn.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (id,))
        user = cursor.fetchone() 
        cursor.close()
        conn.close()

        if user:
            
            return render_template('user_detail.html', user=user)
        else:
            flash('User not found', 'error')
            return redirect(url_for('users')) 

    except mysql.connector.Error as err:
        flash(f"Error: {err}", 'error')
        return redirect(url_for('users'))



if __name__ == '__main__':
    app.run(debug=True)



