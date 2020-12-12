# app.py

from flask import Flask, request  # import main Flask class and request object

import pandas as pd

app = Flask(__name__)  # create the Flask app


@app.route("/json", methods=["Post"])
def query_example():
    print(request.is_json)
    content = request.get_json()
    df_prefilter = pd.json_normalize(content)
    # keeping columns i want
    df = df_prefilter[
        ["x5", "x81", "x31", "x91", "x53", "x44", "x12", "x62", "x58", "x56"]
    ]
    print(df)
    return "request recieved"


app.run(debug=True, port=5000)  # run app in debug mode on port 5000
