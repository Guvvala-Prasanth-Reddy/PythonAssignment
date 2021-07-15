# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import flask
from calculator import app_file
from flask_api import status

app = flask.Flask(__name__)
app.register_blueprint(app_file)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def welcome():
    return '''<h1> Welcome to Rest API ''', status.HTTP_200_OK


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    welcome()
app.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
