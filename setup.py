# imports
from flask import Flask, jsonify, request, make_response
import pandas as pd
import numpy as np
import sklearn
import pickle
import json
from configs import variables, Final_Model
from make_json_test_file import json_object

# initialize Flask
app = Flask(__name__)


@app.route("/predictions", methods=["GET"])
def callback(request_id, response, exception):
    if exception is not None:
        print(format(request_id, exception))
    else:
        print(
            format(
                response.get("x12")
                .get("x31_asia")
                .get("x31_germany")
                .get("x31_japan")
                .get("x44")
                .get("x53")
                .get("x56")
                .get("x58")
                .get("x5_monday")
                .get("x5_saturday")
                .get("x5_sunday")
                .get("x5_tuesday")
                .get("x62")
                .get("x81_August")
                .get("x81_December")
                .get("x81_February")
                .get("x81_January")
                .get("x81_July")
                .get("x81_June")
                .get("x81_March")
                .get("x81_May")
                .get("x81_November")
                .get("x81_October")
                .get("x81_September")
                .get("x91")
            )
        )


batch = service.new_batch_http_request(callback=callback)
for row in student_emails:
    student = {"userId": student_email}
    request = service.courses().students().create(courseId=course_id, body=student)
    batch.add(request, request_id=student_email)
batch.execute(http=http)

print("Printing each JSON Decoded Object")
for student in studentsList:
    print(student["id"], student["name"], student["class"], student["email"])


def predictions():
    data = request.get_json()
    df = pd.DataFrame(data["data"])
    data_all_x_cols = cols
    response = {"data": [], "prediction_label": {"survived": 1, "not survived": 0}}
    response["data"] = list(predictions)
    return make_response(jsonify(response), 200)
