from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from flask_bcrypt import Bcrypt
import pytz
import requests
from bs4 import BeautifulSoup
#from transformers import pipeline
#summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)  # Enable CORS for all routes

# Pre-trained summarizer model from HuggingFace
#summarizer = pipeline("summarization")

# MySQL Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Ruzan',
        database='get_placed'
    )


# Existing API endpoints for questions and user handling
@app.route('/questions', methods=['GET'])
def get_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM quiz')
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/api/aptitude-questions', methods=['GET'])
def fetch_aptitude_questions():
    try:
        # URL for iMocha API
        api_url = "https://apiv3.imocha.io/v3/tests"
        headers = {
            'Authorization': 'Bearer YOUR_API_KEY'  # Replace with your iMocha API key
        }
        
        # Making a request to the iMocha API
        response = requests.get(api_url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Return the JSON response to the frontend
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to fetch questions"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/arrays-quiz-questions', methods=['GET'])
def get_arrays_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM arrays_quiz')
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/algo-quiz-questions', methods=['GET'])
def get_algo_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM algo_quiz')
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/os-quiz-questions', methods=['GET'])
def get_os_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM os_quiz')
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/dbms-quiz-questions', methods=['GET'])
def get_dbms_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM dbms_quiz')
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/oops-quiz-questions', methods=['GET'])
def get_oops_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM oops_quiz')
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/apt-quiz-questions', methods=['GET'])
def get_apt_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM apt_quiz')
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/cnt-quiz-questions', methods=['GET'])
def get_cnt_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM cnt_quiz')
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

@app.route('/systemd-quiz-questions', methods=['GET'])
def get_systemd_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM systemd_quiz')
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)



@app.route('/verbal-ability-quiz-questions', methods=['GET'])
def get_verbal_ability_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT passage, question, option1, option2, option3, option4, answer, explanation FROM verbal_ability_questions LIMIT 8")
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(questions)

# Save verbal score
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

# Save score for other quizzes
@app.route('/save-score', methods=['POST'])
def save_score():
    data = request.get_json()
    score_value = data.get('score')
    user_id = data.get('user_id')

    ist_timezone = pytz.timezone('Asia/Kolkata')
    date_value = data.get('date', datetime.now(ist_timezone).isoformat())
    if score_value is None or user_id is None:
        return jsonify({"error": "Invalid data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO scores (score, user_id, date) VALUES (%s, %s, %s)', (score_value, user_id, date_value))
        conn.commit()
        return jsonify({"message": "Score saved successfully!"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/get-scores', methods=['GET'])
def get_scores():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = '''
            SELECT score, topic, date 
            FROM scores 
            WHERE user_id = %s 
            ORDER BY date ASC
        '''
        cursor.execute(query, (user_id,))
        scores = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify({'scores': scores}), 200
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

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
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            return jsonify({"error": "Username already exists"}), 400
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        cursor.execute('INSERT INTO users (name, username, password) VALUES (%s, %s, %s)', (name, username, hashed_password))
        conn.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except Error as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# User login route
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
            if bcrypt.check_password_hash(user['password'], password):
                return jsonify({"message": "Login successful!", "username": user['username'], "user_id": user['user_id'], "name": user['name']}), 200
            else:
                return jsonify({"error": "Invalid username or password"}), 401
        else:
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True) 
