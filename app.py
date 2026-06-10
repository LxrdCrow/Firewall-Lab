from flask import Flask
from api.routes import bp

app = Flask(__name__)
app.register_blueprint(bp)

