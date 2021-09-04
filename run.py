from app import app
from config import DevelopmentConfig as dev

if __name__ == "__main__":
    app.run(debug=dev.DEBUG, port=dev.PORT, host=dev.HOST)