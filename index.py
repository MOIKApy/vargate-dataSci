import sqlite3 as sql3  # Importing SQLITE

import matplotlib.dates as matdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
import seaborn as sns
from pandas.tools.plotting import table

# from gears.clean import clean

db = 'cryptoGG'
con = sql3.connect('./db/cryptoGG.db')
color = sns.color_palette()

# set up plotting inside a Jupyter notebook
%matplotlib inline

# Pandas options
pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999

# Files Uploaded to the DB
files = ["bitcoin_price.csv", "ethereum_price.csv", "ripple_price.csv"]

# File Container
cols = []
for i, file_name in enumerate(files):
    data = file_name.split(".")[0]

    if i == 0:
        df = pd.read_csv(
            "./data/" + file_name,
            usecols=["Date", "Close"],
            parse_dates=["Date"])
        df.columns = ["Date", data]
        # df.head()
    else:
        temp_df = pd.read_csv(
            "./data/" + file_name,
            usecols=["Date", "Close"],
            parse_dates=["Date"])
        temp_df.columns = ["Date", data]
        df = pd.merge(df, temp_df, on=["Date"])
        # df.head()
    cols.append(data)

# Use to see if csv are mergedprior to aql upload
# df.head()


def run_query(query):
    return pd.read_sql_query(query, db)


df.to_sql(db, con, schema=None, if_exists='replace',
          index=False, index_label=None, chunksize=None, dtype=None)

sql = """
SELECT Date,
bitcoin_price AS 'Bitcoin Close',
ethereum_price AS 'Ethereum Close',
ripple_price AS 'Ripple Close'
FROM cryptoGG
WHERE Date>='2017-01-01 00:00:00'
"""

df = pd.read_sql(sql, con)

# Heat Mapp


def heatmap(e):
    corrmat = df.corr(method="spearman")
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(corrmat, vmax=1.0, square=True)
    plt.title("Cryptocurrency Heat Map: January 1st, 2017 - Present", fontsize=16)
    plt.show()


# Create a Pie Chart
def close_avg(e):
    bitcoin_avg = df['Bitcoin Close'].mean()
    ethereum_avg = df['Ethereum Close'].mean()
    ripple_avg = df['Ripple Close'].mean()

    labels = ['Bitcoin', 'Ethereum', 'Ripple']
    values = [bitcoin_avg, ethereum_avg, ripple_avg]
    colors = ['gold', 'yellowgreen', 'red']
    explode = (0, 0, 0.1)  # explode 1st slice

    # Plot
    plt.pie(values, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.title(
        "Cryptocurrency Close Average: January 1st, 2017 - Present", fontsize=16)
    plt.show()


# Function Calls


# Creates Heat Map
heatmap(df)
# Creates Pie Chart of Close Avg
close_avg(df)
