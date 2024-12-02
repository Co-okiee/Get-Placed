# from flask import Flask, request, render_template, jsonify, redirect, url_for, session
# from werkzeug.utils import secure_filename
# import os
# from func import extract_keywords

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # For session management
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'docx'}

# # Ensure the upload folder exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Allowed file types
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# # Questions based on keywords (you can extend this list)
# questions = {
#     "java": [
#         "What are the main features of Java?",
#         "Can you explain the concept of OOP in Java?",
#         "What is the difference between JDK, JRE, and JVM?"
#     ],
#     "python": [
#         "What is PEP 8, and why is it important?",
#         "Explain the concept of decorators in Python.",
#         "How does Python handle memory management?"
#     ],
#     "c++": [
#         "What are the main differences between C and C++?",
#         "Can you explain the concept of pointers in C++?",
#         "What is a constructor in C++?"
#     ],
#     "javascript": [
#         "What is the difference between var, let, and const?",
#         "Can you explain how prototypal inheritance works?",
#         "What is a closure in JavaScript?"
#     ],
#     "sql": [
#         "What is the difference between INNER JOIN and OUTER JOIN?",
#         "Can you explain normalization and denormalization?",
#         "How do you optimize SQL queries?"
#     ],
#     "html": [
#         "What is the purpose of the DOCTYPE declaration?",
#         "How do you create a table in HTML?",
#         "What are semantic HTML elements?"
#     ],
#     "css": [
#         "What is the box model in CSS?",
#         "How do you center a block element in CSS?",
#         "What are CSS preprocessors, and why would you use them?"
#     ],
#     "git": [
#         "What is the difference between git merge and git rebase?",
#         "How do you resolve a merge conflict in Git?",
#         "What is a Git branch?"
#     ],
#     "react": [
#         "What are components in React?",
#         "Can you explain the virtual DOM?",
#         "What is the purpose of state and props in React?"
#     ],
#     "machine learning": [
#         "What is the difference between supervised and unsupervised learning?",
#         "Can you explain overfitting and underfitting?",
#         "What are some common algorithms used in machine learning?"
#     ],
#     # Add more technologies and related questions here
# }

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'resume' not in request.files:
#         return jsonify({'error': 'No file part'}), 400

#     file = request.files['resume']

#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         try:
#             # Extract keywords from the resume
#             keywords = extract_keywords(filepath)

#             # Store keywords in the session for later use
#             session['keywords'] = keywords

#             # Redirect to the video capture page
#             return redirect(url_for('capture_video'))

#         except Exception as e:
#             return jsonify({'error': f'Error processing the file: {str(e)}'}), 500

#     return jsonify({'error': 'Unsupported file type. Please upload a PDF or Word document.'}), 400

# @app.route('/capture-video')
# def capture_video():
#     # Get the keywords from the session
#     keywords = session.get('keywords', [])

#     # Prepare questions based on extracted keywords
#     interview_questions = []
#     for keyword in keywords:
#         if keyword.lower() in questions:
#             interview_questions.extend(questions[keyword.lower()])

#     return render_template('video_capture.html', questions=interview_questions)

# if __name__ == '__main__':
#     app.run(debug=True)
