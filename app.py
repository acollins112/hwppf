from flask import Flask, render_template, request, url_for 

app = Flask(__name__)

# Define a list to store the book information
books_dict = [
    {
    
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    print("inside add function")
    if request.method == "POST":
        form = request.form
    # Get the book information from the form
    title = form['title']
    author = form['author']
    pages = form['page_count']
    classification = form.getlist('classification')
    acquisition = form['acquisition']

    details_string= ", ".join() 

    add_book_dict = {
        "title": title,
        "author": author,
        "pages": pages,
        "classification": classification,
        "details": details_string,
        "acquisition": acquisition,
    }

    print(add_book_dict)
    books_dict.append(
        add_book_dict
    )

    # Add the book information to the list
    books_dict.append({
        'title': title,
        'author': author,
        'page_count': pages,
        'classification': classification,
        'acquisition': acquisition
    })

    # Render the table template with the book information
    return render_template('index.html', books=books_dict)
    

# about route
@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html', pageTitle="About the Developers")

if __name__ == '__main__':
    app.run(debug=True)