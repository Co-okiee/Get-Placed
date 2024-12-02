import PyPDF2
import docx
import re 

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
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return process_text(text)

def extract_keywords_from_doc(filepath):
    doc = docx.Document(filepath)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return process_text(text)


def process_text(text):
    # Define a list of common skills/keywords to look for
    skill_keywords = ['python', 'java', 'javascript', 'machine learning', 'deep learning', 'nlp', 'sql', 'c++', 'docker', 'html', 'css']

    # Split text into words
    words = text.split()
    # Use a simple match to detect skills in the text
    extracted_skills = [word.lower() for word in words if word.lower() in skill_keywords]
    
    # Return a set of extracted skills to remove duplicates
    return list(set(extracted_skills))
