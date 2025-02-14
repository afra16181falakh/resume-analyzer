from flask import Flask, request, jsonify
from resume_analyzer import analyze_resume
from resume_ranker import rank_resumes
import os

app = Flask(__name__)

# Define a constant for the upload folder
UPLOAD_FOLDER = 'uploads'

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define a function to handle file uploads
def handle_file_upload(file):
    # Save the file to the upload folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return file.filename

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    try:
        # Get the uploaded file
        file = request.files['file']
        # Handle the file upload
        filename = handle_file_upload(file)
        # Analyze the resume
        analysis = analyze_resume(filename)
        return jsonify({"message": "Resume uploaded and analyzed successfully", "analysis": analysis})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/upload-job-description', methods=['POST'])
def upload_job_description():
    try:
        # Get the job description text
        job_description = request.get_json()['job_description']
        # Handle the job description text
        return jsonify({"message": "Job description received", "job_description": job_description})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/rank-resumes', methods=['GET'])
def get_ranked_resumes():
    try:
        # Get the ranked resumes
        ranked_resumes = rank_resumes()
        return jsonify({"ranked_resumes": ranked_resumes})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    app.run(debug=True)
