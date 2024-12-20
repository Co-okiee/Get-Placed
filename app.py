from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, Response
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from models import db, User, QuizResult
import os
import io
import random
import PyPDF2
import docx
import re
from datetime import datetime, timezone
import matplotlib
import matplotlib.pyplot as plt

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

# Allowed file extensions
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('quiz'))
        else:
            flash('Login failed. Check email or password.', 'danger')

    return render_template('login.html')

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
        ],
    }

    interview_questions = []
    for keyword in keywords:
        if keyword.lower() in quiz_data:
            interview_questions.extend([q['question'] for q in quiz_data[keyword.lower()]])
    return jsonify(interview_questions)

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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
