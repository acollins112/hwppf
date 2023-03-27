from flask import Flask, render_template, request

app = Flask(__name__)

# list to store form data
data_list = []

# homepage route
@app.route('/')
def index():
    return render_template('index.html')

# add route
@app.route('/add', methods=['POST'])
def add():
    # process form data
    name = request.form['name']
    email = request.form['email']
    
    # create dictionary and add to list
    data_dict = {'name': name, 'email': email}
    data_list.append(data_dict)

    # return success message
    return 'Data added successfully!'

# about route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)