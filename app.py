from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Works!</h1>"

#Handling error by creating instance


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
