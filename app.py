from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Define a list to store the book information
book_dict = [
    {"title": "Test",
     "author": "John Doe",
     "pages": "222",
     "classification": "fiction",
     "details": "test,test",
     "acquisition": "library"
    }
]

@app.route('/', methods=["GET", "POST"])
# homepage route
@app.route('/')
def index():
    return render_template('index.html', pageTitle="Add a book to my library", book= book_dict)

@app.route('/about', methods=["GET", 'POST'])
def about():
    return render_template('about.html', pageTitle="About the Developers")

@app.route('/add', methods=['POST'])
def add():
    print("inside add function")
    if request.method == 'POST':


        form = request.form


        # Get the book information from the form
        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        classification = form["classification"]
        details = form.getlist("details")
        acquisition = form["acquisition"]

        print(title)
        print(author)
        print(pages)
        print(classification)
        print(details)
        print(acquisition)


        details_string = ", ".join(details)

        book_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "classification": classification,
            "details": details_string,
            "acquisition": acquisition,
    }

        print(book_dict)
        book_dict.append(
            book_dict
        )
        print(book_dict)
        return redirect(url_for("index"))  
    else:
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)

