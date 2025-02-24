from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_analyzer import analyze_resume
from resume_ranker import rank_resumes
import os

app = Flask(__name__)

# Initialize CORS
CORS(app)

# Define a constant for the upload folder
UPLOAD_FOLDER = 'uploads'

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize global variable for job description
job_description_global = ""

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
    except KeyError:
        return jsonify({"error": "No file part in the request"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_analyzer import analyze_resume
from resume_ranker import rank_resumes
import os

app = Flask(__name__)

# Initialize CORS
CORS(app)

# Define a constant for the upload folder
UPLOAD_FOLDER = 'uploads'

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize global variable for job description
job_description_global = ""

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
    except KeyError:
        return jsonify({"error": "Job description not provided"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_analyzer import analyze_resume
from resume_ranker import rank_resumes
import os

app = Flask(__name__)

# Initialize CORS
CORS(app)

# Define a constant for the upload folder
UPLOAD_FOLDER = 'uploads'

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize global variable for job description
job_description_global = ""

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
    except KeyError:
        return jsonify({"error": "Resumes not provided"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/upload-job-description', methods=['POST'])
def upload_job_description():
    try:
        # Get the job description text
        job_description = request.get_json()['job_description']
        # Store the job description in a global variable
        global job_description_global
        job_description_global = job_description
        return jsonify({"message": "Job description received", "job_description": job_description})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/rank-resumes', methods=['POST'])
def get_ranked_resumes():
    try:
        # Get the ranked resumes
        resumes = request.get_json()['resumes']
        ranked_resumes = rank_resumes(resumes, job_description_global)
        return jsonify({"ranked_resumes": ranked_resumes, "message": "Resumes ranked successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
