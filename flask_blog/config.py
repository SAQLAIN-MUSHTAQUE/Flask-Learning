from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='sqlite:///user.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587  # Use 587 for SSL
    MAIL_USE_TLS = True  # Set to False if using SSL
    MAIL_USE_SSL= False
    MAIL_USERNAME = os.getenv('EMAIL')
    MAIL_PASSWORD = os.getenv('PASSWORD')
