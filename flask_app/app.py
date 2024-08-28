from flask import Flask, render_template

app = Flask(__name__)

# getting data from html file and displaying it on webpage
app.add_url_rule('/images/<path:filename>', endpoint='images', view_func=app.send_static_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thename/<name>')
def identity(name):
    return render_template('who.html', name="Bro", to=name)

@app.route('/whereami')
def whereami():
    return 'Ghana'

# making the it dynamic to accept inputs
@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)

if __name__ == '__main__':
    app.run(debug=True)
