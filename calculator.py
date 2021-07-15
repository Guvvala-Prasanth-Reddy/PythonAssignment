import calendar
import math
import datetime
from flask import request, jsonify, Blueprint
from flask_api import status

app_file = Blueprint('app_file', __name__)

"""Name of every function except those contain date in their name depicts the mathematical operation
it performs
"""


@app_file.route("/calculator/add", methods=["GET"])
def add():
    try:
        a = request.args.get("a")
        b = request.args.get("b")
        result = int(a) + int(b)
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code


@app_file.route("/calculator/substract", methods=["GET"])
def substraction():
    global result
    try:
        a = request.args.get("a")
        b = request.args.get("b")
        result = int(a) - int(b)

    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code


@app_file.route("/calculator/multiply", methods=["GET"])
def multiplication():
    try:
        a = request.args.get("a")
        b = request.args.get("b")
        result = int(a) * int(b)
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code, 200


@app_file.route("/calculator/divide", methods=["GET"])
def division(a, b):
    try:
        a = request.args.get("a")
        b = request.args.get("b")
        result = int(a) / int(b)
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code


@app_file.route("/calculator/power", methods=["GET"])
def power():
    try:
        a = request.args.get("a")
        b = request.args.get("b")
        result = int(a) ** int(b)
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code


@app_file.route("/calculator/sin", methods=["GET"])
def sin():
    try:
        x = request.args.get("x")
        result = math.sin(x)
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code


@app_file.route("/calculator/cos", methods=["GET"])
def cos():
    try:
        x = request.args.get("x")
        result = math.cos(x)
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code


@app_file.route("/calculator/tan", methods=["GET"])
def tan():
    try:
        x = request.args.get("x")
        result = math.tan(x)
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code


@app_file.route("/calculator/log", methods=["GET"])
def logarithm():
    try:
        value = request.args.get("value")
        base = request.args.get("base")
        result = math.log(int(value), int(base))
        code = status.HTTP_200_OK
    except Exception as e:
        result = "make sure that you send data as value and base query parameters and cause is "+e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code


@app_file.route("/calculator/exp", methods=["GET"])
def exponent():
    try:
        x = request.args.get("x")
        result = math.exp(x)
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({"result": response}), code


@app_file.route("/calculator/datediff", methods=["GET"])
# method to calculate difference between two dates in days
def difference_between_dates():
    try:
        date1 = request.args.get("date1")
        date2 = request.args.get("date2")
        date_1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
        date_2 = datetime.datetime.strptime(date2, "%d/%m/%Y")
        result = date_1 - date_2
        result = result.days
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({
        "days": str(response)
    }), code


@app_file.route("/calculator/dayfromdate", methods=["GET"])
# method to convert current date to day in a week
def get_day_from_date():
    try:
        date1 = request.args.get("date")
        days_in_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = datetime.datetime.strptime(date1, "%d/%m/%Y").weekday()
        result = days_in_week[day_index]
        code = status.HTTP_200_OK
    except:
        result = "date  is missing in the params"
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({
        "day": str(response)
    }), code


@app_file.route("/calculator/dateafter", methods=["GET"])
# method to provide date after x days to the provided date
def get_date_after():
    try:
        date1 = request.args.get("date")
        print(request.args)
        days = int(request.args.get("days"))
        date_1 = datetime.datetime.strptime(date1, "%d/%m/%Y")
        result = (datetime.timedelta(days=days) + datetime.datetime.strptime(date1, "%d/%m/%Y")).date().__format__(
            "%d/%m/%Y")
        code = status.HTTP_200_OK
    except Exception as e:
        result = e.__cause__
        code = status.HTTP_400_BAD_REQUEST
    finally:
        response = result
    return jsonify({
        "current date": str(response),
        "previous date": str(date1),
        "days added": str(days)

    }), code
