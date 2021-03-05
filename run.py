from app import app
from config import DevelopmentConfig

if __name__ == "__main__":
    app.run(
        debug=DevelopmentConfig.DEBUG, 
        port=DevelopmentConfig.PORT, 
        host=DevelopmentConfig.HOST
        )