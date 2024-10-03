from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import mysql.connector

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

if __name__ == '__main__':
    app.run(debug=True)
