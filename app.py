from flask import Flask, render_template, request

app = Flask(__name__)

# homepage route
@app.route('/')
def index():
    return render_template('index.html')

# add route
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    # process the data here
    return 'Data received: {} - {}'.format(name, email)

# about route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)