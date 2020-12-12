import pandas
from post.py import df


def create_final_dataset():
    """
    function to create dummy variables and drop nondummies 
    """
    df_final=pd.DataFrame()
    df_final[x12]=df[x12]
    df_final[x31_asia]=[1 if x=='asia' else 0 for x in df[x31]]
    df_final[x31_germany]=[1 if x=='germany' else 0 for x in df[x31]]
    df_final[x31_japan]=[1 if x=='japan' else 0 for x in df[x31]]
    df_final[x44]=df[x44]
    df_final[x53]=df[x53]
    df_final[x56]=df[x56]
    df_final[x5_monday]=[1 if x="monday" else 0 for x in df[x5]]
    df_final[x5_tuesday]=[1 if x="tuesday" else 0 for x in df[x5]]
    df_final[x5_saturday]=[1 if x="saturday" else 0 for x in df[x5]]
    df_final[x5_sunday]=[1 if x="sunday" else 0 for x in df[x5]]
    df_final[x62]=df_final[x62]
    df_final[x81_Augst]=[1 if x='August' else 0 for x in df[x81]]
    df_final[x81_Augst]=[1 if x='August' else 0 for x in df[x81]]