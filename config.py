import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    DEBUG = True
    REPORTS_DIR = os.path.join(os.getcwd(), 'reports')

# Ensure the reports directory exists
if not os.path.exists(Config.REPORTS_DIR):
    os.makedirs(Config.REPORTS_DIR)
