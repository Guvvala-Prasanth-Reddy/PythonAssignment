
import flask
from calculator import app_file
from flask_api import status

app = flask.Flask(__name__)
app.register_blueprint(app_file)
app.config["DEBUG"] = True

#Home method
@app.route("/", methods=["GET"])
def welcome():
    return '''<h1> Welcome to Rest API ''', status.HTTP_200_OK



if __name__ == '__main__':
    welcome()
app.run()

