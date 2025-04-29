from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/about")
def about():
    return "This is about page"

@app.route("/html")
def html_page():
    return "<h1>Welcome to Flask</h1><p>This is a paragraph.</p>"


if __name__ == "__main__":
    app.run(debug=True)