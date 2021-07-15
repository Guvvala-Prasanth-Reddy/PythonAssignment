try:
    from main import app
    from flask_api import status
    import unittest
    import math
    import ast
except Exception as e:
    print("Some modules are missing {}".format(e))


class FlaskTest(unittest.TestCase):
    # test to ensure welcome page on 200_Ok response
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEquals(statuscode, 200)
        print(response.data)
        self.assertTrue(b'Welcome' in response.data)

    # invalid url must not return a 200 status code
    def test_invalid_url(self):
        tester = app.test_client(self)
        response = tester.get("/hello")
        self.assertNotEquals(response.status_code, status.HTTP_200_OK)

    # valid requests yields valid response
    def test_add_status(self):
        tester = app.test_client(self)
        response = tester.get("/calculator/add?a=2&b=3")
        statuscode = response.status_code
        self.assertEquals(statuscode, status.HTTP_200_OK)

    # response of REST call is JSON
    def test_add_content(self):
        tester = app.test_client(self)
        response = tester.get("/calculator/add?a=3&b=4")
        contenttype = response.content_type
        self.assertEquals(contenttype, "application/json")

    # validating the add function with original add function result
    def test_add_response(self):
        tester = app.test_client(self)
        response = tester.get("/calculator/add?a=7&b=3")
        self.assertEquals(str(ast.literal_eval(response.data.decode('utf-8')).get("result")), "10")

    # test to check equality between the log result from Rest Api and math.log(x)
    def test_logarithm_response(self):
        tester = app.test_client(self)
        response = tester.get("/calculator/log?value=16&base=4")
        print(type(response.data))
        self.assertEquals(str(math.log(16, 4)), str(ast.literal_eval(response.data.decode('utf-8')).get("result")))

    # proof checking the difference of dates functionality
    def test_date_diff_response(self):
        tester = app.test_client(self)
        response = tester.get("/calculator/datediff?date1=12/06/2012&date2=31/08/2012")
        self.assertEquals("-80", str(ast.literal_eval(response.data.decode('utf-8')).get("days")))

    # test to ensure correctness of date to day functionality
    def test_date_to_day(self):
        tester = app.test_client(self)
        response = tester.get("/calculator/dayfromdate?date=12/06/2012")
        self.assertEquals("Tuesday", ast.literal_eval(response.data.decode('utf-8')).get("day"))

    # test to compare objects returned by the x days after functionality and desired response
    def test_date_after_x_days(self):
        tester = app.test_client(self)
        response = tester.get("/calculator/dateafter?date=12/06/2012&days=20")
        self.assertEquals({
            "current date": "02/07/2012",
            "days added": "20",
            "previous date": "12/06/2012"
        }, ast.literal_eval(response.data.decode('utf-8')))


if __name__ == "__main__":
    unittest.main()
