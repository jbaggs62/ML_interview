# app.py
# import main Flask class and request object
from flask import Flask, request, jsonify
import json
from flask.wrappers import Response
import pandas as pd
from pandas.core.arrays import string_
from configs import final_fit, variables
import statsmodels.api as sm
import numpy as np


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

    def clean_final_dataset(dataframe):
        """
        cleaning final dataset based on cleaning that was done in notebook example
        """
        df["x12"] = df.x12.astype("string")
        df["x12"] = df["x12"].str.replace("$", "")
        df["x12"] = df["x12"].str.replace(",", "")
        df["x12"] = df["x12"].str.replace(")", "")
        df["x12"] = df["x12"].str.replace("(", "-")
        df["x12"] = df["x12"].astype("float")
        df["x62"] = df.x62.astype("string")
        df["x62"] = df["x62"].str.replace("%", "")
        df["x62"] = df["x62"].astype("float")
        return df

    def create_final_dataset(dataframe):
        """
        function to create dataset with dummy variables and only the variables we want from our inital dataframe we create
        """
        df_final = df[["x12", "x44", "x53", "x56", "x62", "x91"]]
        df_final["x31_asia"] = [1 if x == "asia" else 0 for x in df["x31"]]
        df_final["x31_germany"] = [1 if x == "germany" else 0 for x in df["x31"]]
        df_final["x31_japan"] = [1 if x == "japan" else 0 for x in df["x31"]]
        df_final["x5_monday"] = [1 if x == "monday" else 0 for x in df["x5"]]
        df_final["x5_tuesday"] = [1 if x == "tuesday" else 0 for x in df["x5"]]
        df_final["x5_saturday"] = [1 if x == "saturday" else 0 for x in df["x5"]]
        df_final["x5_sunday"] = [1 if x == "sunday" else 0 for x in df["x5"]]
        df_final["x81_August"] = [1 if x == "August" else 0 for x in df["x81"]]
        df_final["x81_December"] = [1 if x == "December" else 0 for x in df["x81"]]
        df_final["x81_February"] = [1 if x == "February" else 0 for x in df["x81"]]
        df_final["x81_January"] = [1 if x == "January" else 0 for x in df["x81"]]
        df_final["x81_July"] = [1 if x == "July" else 0 for x in df["x81"]]
        df_final["x81_June"] = [1 if x == "June" else 0 for x in df["x81"]]
        df_final["x81_March"] = [1 if x == "March" else 0 for x in df["x81"]]
        df_final["x81_May"] = [1 if x == "May" else 0 for x in df["x81"]]
        df_final["x81_November"] = [1 if x == "November" else 0 for x in df["x81"]]
        df_final["x81_October"] = [1 if x == "October" else 0 for x in df["x81"]]
        df_final["x81_September"] = [1 if x == "September" else 0 for x in df["x81"]]
        return df_final

    # clean dataset
    df = clean_final_dataset(df)
    # create final dataset
    df_final = create_final_dataset(df)
    df_final.to_csv("df_final.csv")
    df_import = pd.read_csv("df_final.csv")
    model = sm.load("final_fit.pkl")
    predictions = model.predict(df_import)
    df_response = pd.DataFrame(predictions, columns=["phat"])
    df_response["business_outcome"] = [
        "event" if x > 0.75 else "not event" for x in df_response["phat"]
    ]
    df_response["variables"] = np.tile(variables, (len(df), 1)).tolist()
    print(df_response)
    response = df_response.to_json(orient="index")
    return response


app.run(debug=True, port=5000)  # run app in debug mode on port 5000
