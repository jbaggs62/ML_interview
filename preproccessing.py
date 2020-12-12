import pandas


def clean_final_dataset(dataframe):
    """
    cleaning final dataset based on cleaning that was done in notebook example
    """
    df["x12"] = df["x12"].str.replace("$", "")
    df["x12"] = df["x12"].str.replace(",", "")
    df["x12"] = df["x12"].str.replace(")", "")
    df["x12"] = df["x12"].str.replace("(", "-")
    df["x12"] = df["x12"].astype(float)
    df["x63"] = df["x63"].str.replace("%", "")
    df["x63"] = df["x63"].astype(float)
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
