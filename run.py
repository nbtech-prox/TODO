from app import create_app
from dotenv import load_dotenv

load_dotenv('.flaskenv')
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
