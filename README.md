# Resume Analyzer
Resume Analyzer is a Python-based tool designed to help users analyze and rank resumes based on specific criteria. This project is particularly useful for recruiters and hiring managers who need to process large numbers of resumes efficiently.

## Features
- **Resume Parsing**: Extracts key information from resumes
- **Keyword Analysis**: Identifies relevant skills and qualifications
- **Ranking System**: Ranks resumes based on predefined criteria
- **Customizable**: Easily adapt to different job requirements
- **Logging**: Tracks requests and responses for better debugging and analysis


## Technologies Used
- **Spacy**: A library for natural language processing, used for resume parsing and analysis.
- **Transformers**: A library for state-of-the-art natural language processing models, potentially used for advanced text analysis.
- **OpenAI API**: If utilized, this would be for leveraging AI capabilities in analyzing resumes.
- **Logging**: Implemented for tracking request metadata and debugging.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/afra16181falakh/resume-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd resume-analyzer
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
1. Place your resumes in the `resumes` folder.
2. Run the analyzer:
   ```bash
   python resume_ranker.py
   ```
3. View the results in the `output` folder.

## Recent Updates
- Added logging functionality to track request metadata.
- Introduced a new endpoint for enhanced resume analysis.



