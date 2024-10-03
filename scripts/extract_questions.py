import os
from docx import Document
import json

def extract_questions(file_path):
    doc = Document(file_path)
    questions = []
    for para in doc.paragraphs:
        if para.text.strip():
            questions.append(para.text.strip())
    return questions

def process_word_files(directory):
    all_questions = []
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            file_path = os.path.join(directory, filename)
            questions = extract_questions(file_path)
            all_questions.append({
                'filename': filename,
                'questions': questions
            })
    return all_questions

def save_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    questions_data = process_word_files('../word_files')  # Folder where Word files are stored
    save_to_json(questions_data, '../data/questions.json')  # Save JSON to data folder
