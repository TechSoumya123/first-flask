from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)


# Create a route decorator
# @app.route('/about')
# def index():
#     return "<h1>Hello World!</h1>"

@app.route('/')
def index():
    first_name = "John"
    stuff = "This is <Strong>Bold</Strong> Text"
    list1 = ["one", "two", "three"]
    return render_template("index.html", first_name=first_name, stuff=stuff, list1=list1)


# @app.route('/user/<name>')
# def user(name):
#     return "<h1>Hello {}</h1>".format(name)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


if __name__ == "__main__":
    app.run(debug=True)
