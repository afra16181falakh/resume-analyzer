import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    MODEL_NAME = "text-embedding-ada-002"
    BERT_MODEL = "bert-base-uncased"
    MAX_INPUT_LENGTH = 512
