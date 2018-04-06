import os
from dotenv import load_dotenv

load_dotenv()

JINKENS_URL = os.getenv('JINKENS_URL')
JINKENS_JOB = os.getenv('JINKENS_JOB')
JINKENS_USER = os.getenv('JINKENS_USER')
JINKENS_PASS = os.getenv('JINKENS_PASS')
HTTP_TIMEOUT = os.getenv('HTTP_TIMEOUT') if os.getenv('HTTP_TIMEOUT')!=None else 15

