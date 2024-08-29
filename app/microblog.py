from flask import Flask
from routes import microblog
from config import Config

app = Flask(__name__)

# register the blueprint with the app
app.register_blueprint(microblog)
app.config.from_object(Config)

if __name__ == '__main__':
    app.run(debug=True)

