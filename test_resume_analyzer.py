import unittest
from resume_analyzer import analyze_resume, extract_education, extract_experience

class TestResumeAnalyzer(unittest.TestCase):
    def test_analyze_resume(self):
        resume_text = """
        John Doe
        Python developer with experience in machine learning and data analysis.
        """
        result = analyze_resume(resume_text)
        self.assertIsNotNone(result['name'])
        self.assertIn("python", result['skills'])
        self.assertIn("machine learning", result['skills'])
        self.assertIn("data analysis", result['skills'])

    def test_extract_education(self):
        resume_text = """
        John Doe
        Bachelor of Science in Computer Science from University of Example.
        """
        education_info = extract_education(resume_text)
        self.assertIn("Bachelor of Science in Computer Science from University of Example.", education_info)

    def test_extract_experience(self):
        resume_text = """
        John Doe
        Worked at Example Corp as a Software Engineer for 3 years.
        """
        experience_info = extract_experience(resume_text)
        self.assertIn("Worked at Example Corp as a Software Engineer for 3 years.", experience_info)

if __name__ == '__main__':
    unittest.main()
