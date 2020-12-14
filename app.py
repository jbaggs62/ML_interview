# app.py
# import main Flask class and request object
from os import truncate
from flask import Flask, request, jsonify
import json
from flask.wrappers import Response
from numpy.lib.utils import info
import pandas as pd
from pandas.core.arrays import string_
from configs import final_fit, variables
import statsmodels.api as sm
import numpy as np
import logging


app = Flask(__name__)  # create the Flask app


@app.route("/json", methods=["Post"])
def query_example():
    try:
        print(request.is_json)
        content = request.get_json()
        df_prefilter = pd.json_normalize(content)
        if df_prefilter.empty:
            logging.warn("zero data on request")
        # keeping columns i want
        df = df_prefilter[
            ["x5", "x81", "x31", "x91", "x53", "x44", "x12", "x62", "x58", "x56"]
        ]

        def clean_final_dataset(dataframe):

            """
            cleaning final dataset based on cleaning that was done in notebook example
            """
            try:
                df["x12"] = df.x12.astype("string")
                df["x12"] = df["x12"].str.replace("$", "")
                df["x12"] = df["x12"].str.replace(",", "")
                df["x12"] = df["x12"].str.replace(")", "")
                df["x12"] = df["x12"].str.replace("(", "-")
                df["x12"] = df["x12"].astype("float")
                df["x62"] = df.x62.astype("string")
                df["x62"] = df["x62"].str.replace("%", "")
                df["x62"] = df["x62"].astype("float")
            except Exception:
                logging.exception("issue cleaning dataset")
            return df

        def create_final_dataset(dataframe):
            """
            function to create dataset with dummy variables and only the variables we want from our inital dataframe we create
            """
            try:
                #bringing in the variables we do not need to create dummy variables based on jupyternotebook
                df_final = df[["x12", "x44", "x53", "x56", "x62", "x91"]]
                df_final["x31_asia"] = [1 if x == "asia" else 0 for x in df["x31"]]
                df_final["x31_germany"] = [
                    1 if x == "germany" else 0 for x in df["x31"]
                ]
                df_final["x31_japan"] = [1 if x == "japan" else 0 for x in df["x31"]]
                df_final["x5_monday"] = [1 if x == "monday" else 0 for x in df["x5"]]
                df_final["x5_tuesday"] = [1 if x == "tuesday" else 0 for x in df["x5"]]
                df_final["x5_saturday"] = [
                    1 if x == "saturday" else 0 for x in df["x5"]
                ]
                df_final["x5_sunday"] = [1 if x == "sunday" else 0 for x in df["x5"]]
                df_final["x81_August"] = [1 if x == "August" else 0 for x in df["x81"]]
                df_final["x81_December"] = [
                    1 if x == "December" else 0 for x in df["x81"]
                ]
                df_final["x81_February"] = [
                    1 if x == "February" else 0 for x in df["x81"]
                ]
                df_final["x81_January"] = [
                    1 if x == "January" else 0 for x in df["x81"]
                ]
                df_final["x81_July"] = [1 if x == "July" else 0 for x in df["x81"]]
                df_final["x81_June"] = [1 if x == "June" else 0 for x in df["x81"]]
                df_final["x81_March"] = [1 if x == "March" else 0 for x in df["x81"]]
                df_final["x81_May"] = [1 if x == "May" else 0 for x in df["x81"]]
                df_final["x81_November"] = [
                    1 if x == "November" else 0 for x in df["x81"]
                ]
                df_final["x81_October"] = [
                    1 if x == "October" else 0 for x in df["x81"]
                ]
                df_final["x81_September"] = [
                    1 if x == "September" else 0 for x in df["x81"]
                ]
            except Exception:
                logging.exception("issue creating final dataset")
            return df_final

        # clean dataset
        df = clean_final_dataset(df)
        # create final dataset
        df_final = create_final_dataset(df)

        # export than report due to dimension issue this is a quick fix but needs further investigation down the road to increase peformance/ handle thousands of records due to potential storage limitations
        df_final.to_csv("df_final.csv")
        df_import = pd.read_csv("df_final.csv")

        # load in model
        model = sm.load("final_fit.pkl")

        # run predictions
        predictions = model.predict(df_import)

        # create response dataframe
        df_response = pd.DataFrame(predictions, columns=["phat"])
        df_response["business_outcome"] = [
            "event" if x > 0.75 else "not event" for x in df_response["phat"]
        ]
        df_response["variables"] = np.tile(variables, (len(df), 1)).tolist()
        print(df_response)

        # create json resposne and return so that each row in the dataframe is a return in order for easy processing of batch request with some logging
        response = df_response.to_json(orient="index")
    except Exception:
        logging.raiseExceptions("issue in main function")
    return response


# setting host and port to 1313
app.run(debug=False, host="0.0.0.0", port=1313)
