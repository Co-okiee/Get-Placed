from flask import Flask, jsonify, request, session
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import mysql.connector
from mysql.connector import Error
from flask_bcrypt import Bcrypt
import PyPDF2
import docx
import re
from datetime import datetime
import random
import requests

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)
app.secret_key = 'your_secret_key'

# Upload configurations
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# MySQL Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Ruzan',
        database='get_placed'
    )

# Allowed file types for resume upload
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Keyword extraction functions
def extract_keywords(filepath):
    ext = filepath.split('.')[-1].lower()
    if ext == 'pdf':
        return extract_keywords_from_pdf(filepath)
    elif ext in ['doc', 'docx']:
        return extract_keywords_from_doc(filepath)
    else:
        raise ValueError("Unsupported file format")

def extract_keywords_from_pdf(filepath):
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''.join([page.extract_text() for page in reader.pages])
    return process_text(text)

def extract_keywords_from_doc(filepath):
    doc = docx.Document(filepath)
    text = ''.join([para.text for para in doc.paragraphs])
    return process_text(text)

def process_text(text):
    skill_keywords = [
        'python', 'java', 'javascript', 'machine learning', 'sql',
        'c++', 'html', 'css', 'git', 'react', 'node.js', 'django'
    ]
    text = text.lower()
    extracted_skills = set([keyword for keyword in skill_keywords if re.search(r'\b' + re.escape(keyword) + r'\b', text)])
    return list(extracted_skills)

# Route: Upload resume
@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({'success': False, 'error': 'No file uploaded.'})

    file = request.files['resume']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file.'})

    if not allowed_file(file.filename):
        return jsonify({'success': False, 'error': 'Invalid file type.'})

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Extract keywords and store in session
    keywords = extract_keywords(file_path)
    session['keywords'] = keywords

    return jsonify({'success': True, 'keywords': keywords})

# Route: Fetch interview questions
@app.route('/api/interview-questions', methods=['POST'])
def get_interview_questions():
    data = request.get_json()
    keywords = data.get('keywords', session.get('keywords', []))
    if not keywords:
        return jsonify({"error": "No keywords provided."}), 400

    quiz_data = {
        "python": [
            {"question": "What is PEP 8, and why is it important?", "options": ["Code formatting guidelines", "An IDE", "A library", "A compiler"], "answer": "Code formatting guidelines"},
        ],
        "javascript": [
            {"question": "What is event bubbling in JavaScript?", "options": ["A way of propagating events", "A sorting algorithm", "A method of debugging", "None of the above"], "answer": "A way of propagating events"},
        ],
    }

    interview_questions = []
    for keyword in keywords:
        if keyword.lower() in quiz_data:
            interview_questions.extend([q['question'] for q in quiz_data[keyword.lower()]])
    return jsonify(interview_questions)

# Route: Fetch questions from MySQL
@app.route('/questions/<quiz_type>', methods=['GET'])
def fetch_quiz_questions(quiz_type):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'SELECT * FROM {quiz_type}_quiz')
        questions = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(questions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Track progress
@app.route('/api/track-progress', methods=['GET'])
def track_progress():
    user_results = [
        {"quiz_type": "python", "score": 4, "time_taken": 3.2, "date_taken": datetime.now()},
        {"quiz_type": "javascript", "score": 3, "time_taken": 5.0, "date_taken": datetime.now()},
    ]
    scores_by_quiz = {}
    for result in user_results:
        if result['quiz_type'] not in scores_by_quiz:
            scores_by_quiz[result['quiz_type']] = []
        scores_by_quiz[result['quiz_type']].append(result['score'])

    weak_topics = [quiz for quiz, scores in scores_by_quiz.items() if sum(scores) / len(scores) < 2]
    total_correct_answers = sum(r['score'] for r in user_results)
    total_marks = len(user_results) * 5
    motivational_quotes = [
        "Keep pushing forward!", "Every effort counts!", "Believe in yourself!"
    ]
    return jsonify({
        "results": user_results,
        "weak_topics": weak_topics,
        "quote": random.choice(motivational_quotes),
        "total_correct_answers": total_correct_answers,
        "total_marks": total_marks
    })

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
    app.run(host='0.0.0.0', port=5001, debug=True)

