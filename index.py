import sqlite3  # Importing SQLITE3

import matplotlib
import matplotlib.dates as matdates
import matplotlib.pyplot as plt
import matplotlib.ticker as matticker
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.finance import candlestick_ohlc as candles

db = 'cryptoGG'
con = sqlite3.connect('./db/cryptoGG.db')
color = sns.color_palette()

# set up plotting inside a Jupyter notebook
%matplotlib inline

# Pandas options
pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999

# READING THE CSV WITH PANDAS
# dfBitcoin = pd.read_csv("./data/bitcoin_price.csv", parse_dates=["Date"])
# dfEthereum = pd.read_csv("./data/ethereum_price.csv", parse_dates=["Date"])
# dfRipple = pd.read_csv("./data/ripple_price.csv", parse_dates=["Date"])
files_to_use = ["bitcoin_price.csv",
                "ethereum_price.csv", "ripple_price.csv"]
cols_to_use = []
for ind, file_name in enumerate(files_to_use):
    coin_name = file_name.split("_")[0]
    if ind == 0:
        df = pd.read_csv("./data/" + file_name,
                         usecols=["Date", "Close"], parse_dates=["Date"])
        df.columns = ["Date", coin_name]
    else:
        temp_df = pd.read_csv("./data/" + file_name,
                              usecols=["Date", "Close"], parse_dates=["Date"])
        temp_df.columns = ["Date", coin_name]
        df = pd.merge(df, temp_df, on="Date")
    cols_to_use.append(coin_name)
df.head()


def run_query(query):
    return pd.read_sql_query(query, db)


df.to_sql(db, con, schema=None, if_exists='fail',
          index=True, index_label=None, chunksize=None, dtype=None)
