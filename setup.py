# imports
from flask import Flask, jsonify, request, make_response
import pandas as pd
import numpy as np
import sklearn
import pickle
import json
from configs import variables, Final_Model

# initialize Flask
app = Flask(__name__)


@app.route("/predictions", methods=["GET"])
def callback(request_id, response, exception):
    if exception is not None:
        print(format(request_id, exception))
        "x5_monday", "x5_saturday", "x5_sunday", "x5_tuesday", "x62", "x81_August", "x81_December", "x81_February", "x81_January", "x81_July", "x81_June", "x81_March", "x81_May", "x81_November", "x81_October", "x81_September", "x91"
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
            )
        )


batch = service.new_batch_http_request(callback=callback)
for student_email in student_emails:
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
