from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from flask_bcrypt import Bcrypt
import pytz


app = Flask(__name__)
bcrypt = Bcrypt(app)

CORS(app)  # Enable CORS for all routes

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Ruzan',
        database='get_placed'
    )

@app.route('/questions', methods=['GET'])
def get_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM quiz')  # Ensure this matches the correct table
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/arrays-quiz-questions', methods=['GET'])
def get_arrays_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM arrays_quiz')  # New table for arrays quiz
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/matrices-quiz-questions', methods=['GET'])
def get_matrices_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM matrix_quiz')  # New table for arrays quiz
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/verbal-ability-quiz-questions', methods=['GET'])
def get_verbal_ability_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT passage, question, option1, option2, option3, option4, answer,explanation FROM verbal_ability_questions LIMIT 8")
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/save_verbal_score', methods=['POST'])
def save_verbal_score():
    data = request.json
    user_id = data.get('user_id')
    score = data.get('score')
    topic = data.get('topic')

    if user_id is None or score is None or topic is None:
        return jsonify({"error": "User ID, score, and topic are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO verbal_score (user_id, score, date, topic) VALUES (%s, %s, NOW(), %s)', (user_id, score, topic))
        conn.commit()
        return jsonify({"message": "Score saved successfully!"}), 201
    except Exception as e:
        conn.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


@app.route('/save-score', methods=['POST'])
def save_score():
    data = request.get_json()
    score_value = data.get('score')
    user_id = data.get('user_id')  # Get the user ID
    
    ist_timezone = pytz.timezone('Asia/Kolkata')
    date_value = data.get('date', datetime.now(ist_timezone).isoformat())
    if score_value is None or user_id is None:  # Check for user ID
        return jsonify({"error": "Invalid data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO scores (score, user_id, date) VALUES (%s, %s, %s)', (score_value, user_id, date_value))
        conn.commit()
        return jsonify({"message": "Score saved successfully!"}), 201
    except Exception as e:
        conn.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# User signup route
# User signup route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    username = data.get('username')
    password = data.get('password')

    if name is None or username is None or password is None:
        return jsonify({"error": "Name, username, and password are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        # Check if the username already exists
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')  # Hash the password

        cursor.execute('INSERT INTO users (name, username, password) VALUES (%s, %s, %s)', (name, username, hashed_password))
        conn.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Error as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()




@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return jsonify({"error": "Username and password are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user:
            # Use check_password_hash to verify the password
            if bcrypt.check_password_hash(user['password'], password):
                return jsonify({"message": "Login successful!", "username": user['username'], "user_id": user['user_id'],"name": user['name']}), 200
            else:
                return jsonify({"error": "Invalid username or password"}), 401
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:  # Catch all exceptions
        print("An error occurred during login:", str(e))  # Log the error
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500
    finally:
        cursor.close()
        conn.close()




if __name__ == '__main__':
    app.run(debug=True)