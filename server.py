"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html><a href = "/hello">Click me to go to Hello</a>Hi! This is the home page. Testing 123</html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""


    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>

        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          <input type = "radio" name="compliments" value="awesome">
          <label for="awesome">Awesome</label><br>
          <input type = "radio" name="compliments" value="terrific">
          <label for="terrific">Terrific</label><br>
          <input type = "radio" name="compliments" value="neato">
          <label for="neato">Neato</label><br>
          <input type = "radio" name="compliments" value="spectacular">
          <label for="spectacular">Spectacular</label><br>

          <br>
          <input type="submit" value="Submit">

        </form>


      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")


    compliment = request.args.get("compliments")


    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
