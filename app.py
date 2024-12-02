from flask import Flask, request, jsonify, session
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import PyPDF2
import docx
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'

# Upload configurations
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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

# Quiz data
quiz_data = {
    "python": [
        {"question": "What is PEP 8, and why is it important?", "options": ["Code formatting guidelines", "An IDE", "A library", "A compiler"], "answer": "Code formatting guidelines"},
        {"question": "Explain the concept of decorators in Python.", "options": ["A special type of function", "A module", "A loop", "An IDE"], "answer": "A special type of function"},
    ],
    "javascript": [
        {"question": "What is event bubbling in JavaScript?", "options": ["A way of propagating events", "A sorting algorithm", "A method of debugging", "None of the above"], "answer": "A way of propagating events"},
        {"question": "What is the purpose of closures in JavaScript?", "options": ["To create classes", "To manage state in functions", "To handle async calls", "To modify prototypes"], "answer": "To manage state in functions"},
    ],
}

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

    interview_questions = []
    for keyword in keywords:
        if keyword.lower() in quiz_data:
            interview_questions.extend([q['question'] for q in quiz_data[keyword.lower()]])
    return jsonify(interview_questions)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)