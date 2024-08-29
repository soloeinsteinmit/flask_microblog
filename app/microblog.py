from flask import Flask
from routes import microblog
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# register the blueprint with the app
app.register_blueprint(microblog)
app.config.from_object(Config)
# Migration initialization
db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)

