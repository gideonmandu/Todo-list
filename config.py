# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    HOST = 'http://127.0.0.1'
    PORT = 5000
    # Mongo DB options
    DB_HOST='http://127.0.0.1'
    DB_PORT=27017 
    DOC_CLASS= dict 
    TZ_AWARE=False 
    CON= True

class TestingConfig(Config):
    DEBUG = True
    HOST = 'http://127.0.0.1'
    PORT = 5000
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 8080

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY