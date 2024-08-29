from flask import Flask
from routes import microblog

app = Flask(__name__)

# register the blueprint with the app
app.register_blueprint(microblog)

if __name__ == '__main__':
    app.run(debug=True)

