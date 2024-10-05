from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import mysql.connector
from datetime import datetime

app = Flask(__name__)
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

@app.route('/save-score', methods=['POST'])
def save_score():
    data = request.get_json()
    score_value = data.get('score')
    date_value = data.get('date', datetime.utcnow().isoformat())  # Default to current time

    if score_value is None:
        return jsonify({"error": "Invalid data"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO scores (score, date) VALUES (%s, %s)', (score_value, date_value))
        conn.commit()
        return jsonify({"message": "Score saved successfully!"}), 201
    except Exception as e:
        conn.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
