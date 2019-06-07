from flask import Flask
from flask_cors import CORS
from extensions import db
from modern_api import api_blueprint

app = Flask(__name__)
app.config.from_object('config')
CORS(app)
db.init_app(app)
with app.test_request_context():
    db.create_all()
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)