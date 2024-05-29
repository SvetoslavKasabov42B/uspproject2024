from flask import Flask
from models import db, setup_db

app = Flask(__name__)
setup_db(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
