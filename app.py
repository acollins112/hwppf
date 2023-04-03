from flask import Flask, flash, render_template, request, url_for, redirect

app = Flask(__name__)

# Define a list to store the book information
book_dict = [
    {"Title": "Test",
     "Author": "John Doe",
     "Pages": "222",
     "Classification": "fiction",
     "Details": "test,test",
     "Acquisition": "library"
    }
]

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', pageTitle="Add a book to my library", book= book_dict)

@app.route('/about', methods=["GET", 'POST'])
def about():
    return render_template('about.html', pageTitle="About the Developers")

@app.route('/add', methods=['POST'])
def add():
    print("Add book")
    if request.method == 'POST':
            
        form =request.form

        # Get the book information from the form
        Title = form["Title"]
        Author = form["Author"]
        Pages = form["Pages"]
        Classification = form["Classification"]
        Details = form.getlist("Details")
        Acquisition = form["Acquisition"]

        print(Title)
        print(Author)
        print(Pages)
        print(Classification)
        print(Details)
        print(Acquisition)


        Details_string = ", ".join(Details)

        book_dict = {
            "Title": Title,
            "Author": Author,
            "Pages": Pages,
            "Classification": Classification,
            "Details": Details_string,
            "Acquisition": Acquisition,
    }

        print(book_dict)
        book_dict.append(
            book_dict
        )
        print(book_dict)

        flash(
            "The book ;" + Title + " has been added to the database.",
            "success",
        )
        return redirect(url_for("index"))  
    else:
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)

