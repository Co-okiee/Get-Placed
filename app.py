# <<<<<<< HEAD
# from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, Response
# =======
# from flask import Flask, jsonify, request, session
# >>>>>>> b98a9c89fe0aeffd2d478cdcd5e47c454f76fe38
# from flask_cors import CORS
# from flask_migrate import Migrate
# from werkzeug.utils import secure_filename
# from models import db, User, QuizResult
# import os
# <<<<<<< HEAD
# import io
# import random
# import PyPDF2
# import docx
# import re
# from datetime import datetime, timezone
# import matplotlib
# import matplotlib.pyplot as plt
# =======
# import mysql.connector
# from mysql.connector import Error
# from flask_bcrypt import Bcrypt
# import PyPDF2
# import docx
# import re
# from datetime import datetime
# import random
# import requests
# >>>>>>> b98a9c89fe0aeffd2d478cdcd5e47c454f76fe38
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, Response
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
from models import db, User, QuizResult
import os
import io
import random
import PyPDF2
import docx
import re
from datetime import datetime, timezone
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt
import pytz
import requests
import random


# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx'}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
db.init_app(app)
migrate = Migrate(app, db)

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
        'python', 'java', 'javascript', 'machine learning', 'deep learning',
        'sql', 'c++', 'docker', 'html', 'css', 'react', 'node.js', 'django'
    ]
    text = text.lower()
    extracted_skills = {keyword for keyword in skill_keywords if re.search(r'\b' + re.escape(keyword) + r'\b', text)}
    return list(extracted_skills)

# Routes for the application
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('User already registered. Please log in.', 'info')
            return redirect(url_for('login'))

        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')




# Route: Upload resume
# >>>>>>> b98a9c89fe0aeffd2d478cdcd5e47c454f76fe38


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

    keywords = extract_keywords(file_path)
    session['keywords'] = keywords
    return jsonify({'success': True, 'keywords': keywords})

@app.route('/api/interview-questions', methods=['POST'])
def get_interview_questions():
    data = request.get_json()
    keywords = data.get('keywords', session.get('keywords', []))
    if not keywords:
        return jsonify({"error": "No keywords provided."}), 400

    quiz_data = {
        'python': [
            {"question": "What is PEP 8?", "answer": "Code formatting guidelines"},
        ],
        'javascript': [
            {"question": "What is event bubbling?", "answer": "A way of propagating events"},
# =======
#         "python": [
#             {"question": "What is PEP 8, and why is it important?", "options": ["Code formatting guidelines", "An IDE", "A library", "A compiler"], "answer": "Code formatting guidelines"},
#         ],
#         "javascript": [
#             {"question": "What is event bubbling in JavaScript?", "options": ["A way of propagating events", "A sorting algorithm", "A method of debugging", "None of the above"], "answer": "A way of propagating events"},
# >>>>>>> b98a9c89fe0aeffd2d478cdcd5e47c454f76fe38
        ],
    }

    interview_questions = []
    for keyword in keywords:
        if keyword.lower() in quiz_data:
            interview_questions.extend([q['question'] for q in quiz_data[keyword.lower()]])
    return jsonify(interview_questions)

# <<<<<<< HEAD
# =======
# # Route: Fetch questions from MySQL
# @app.route('/questions/<quiz_type>', methods=['GET'])
# def fetch_quiz_questions(quiz_type):
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)
#         cursor.execute(f'SELECT * FROM {quiz_type}_quiz')
#         questions = cursor.fetchall()
#         cursor.close()
#         conn.close()
#         return jsonify(questions)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

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
# >>>>>>> b98a9c89fe0aeffd2d478cdcd5e47c454f76fe38
@app.route('/api/track-progress', methods=['GET'])
def track_progress():
    user_results = QuizResult.query.filter_by(user_id=session.get('user_id')).all()
    scores_by_quiz = {}
    for result in user_results:
        if result.quiz_type not in scores_by_quiz:
            scores_by_quiz[result.quiz_type] = []
        scores_by_quiz[result.quiz_type].append(result.score)

    weak_topics = [quiz for quiz, scores in scores_by_quiz.items() if sum(scores) / len(scores) < 2]
    total_correct_answers = sum(r.score for r in user_results)
    total_marks = len(user_results) * 5
    motivational_quotes = [
        "Keep pushing forward!", "Every effort counts!", "Believe in yourself!"
    ]

    return jsonify({
        "results": [{"quiz_type": r.quiz_type, "score": r.score, "date_taken": r.date_taken} for r in user_results],
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

@app.route('/arrays-quiz-questions', methods=['GET'])
def get_arrays_quiz_questions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM arrays_quiz')
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
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5001, debug=True)

# if __name__ == '__main__':
# <<<<<<< HEAD
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
# =======
#     app.run(host='0.0.0.0', port=5001, debug=True)

# >>>>>>> b98a9c89fe0aeffd2d478cdcd5e47c454f76fe38
