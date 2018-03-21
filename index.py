import sqlite3 as sql3  # Importing SQLITE

import matplotlib.dates as matdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

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


class heat_map():
    # File Container
    cols = []

    for i, file_name in enumerate(files):
        data = file_name.split(".")[0]

        if i == 0:
            df = pd.read_csv("./data/" + file_name,
                             usecols=["Date", "Close"], parse_dates=["Date"])
            df.columns = ["Date", data]
            # df.head()
        else:
            temp_df = pd.read_csv("./data/" + file_name,
                                  usecols=["Date", "Close"], parse_dates=["Date"])
            temp_df.columns = ["Date", data]
            df = pd.merge(df, temp_df, on=["Date"])
            # df.head()
        cols.append(data)
    # Use to see if csv are mergedprior to aql upload
    # df.head()

    # Populats Database

    def run_query(query):
        return pd.read_sql_query(query, db)

    df.to_sql(db, con, schema=None, if_exists='replace',
              index=False, index_label=None, chunksize=None, dtype=None)
    # Query
    sql = """
    SELECT Date,
    bitcoin_price AS 'Bitcoin Close',
    ethereum_price AS 'Ethereum Close',
    ripple_price AS 'Ripple Close'
    FROM cryptoGG
    WHERE Date>='2017-01-05 00:00:00'
    """

    df = pd.read_sql(sql, con)
    print(df)
    # Heat Map

    def heatmap(e):
        # GENERATING A HEATMAP
        corrmat = df.corr(method="spearman")
        fig, ax = plt.subplots(figsize=(10, 10))
        sns.heatmap(corrmat, vmax=1., square=True)
        plt.title("Cryptocurrency Heat Map: Close Jan 2017 - Present", fontsize=16)
        plt.show()
        # END

    heatmap(df)

# Pie Chart
# Coins Close, which Coin had the highest Avg From Jan. 1st 2017-Present.
