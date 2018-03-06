# IMPORTING PANDAS
import matplotlib.dates as matdates
# IMPORTING matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as matticker
# IMPORTING NUMPY
import numpy as np
import pandas as pd
# importing seaborn
import seaborn as sns
from matplotlib.finance import candlestick_ohlc as candles

# Importing Prophet
from fbprophet import Prophet

color = sns.color_palette()

# set up plotting inside a Jupyter notebook
%matplotlib inline

# Pandas options
pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999

# READING THE CSV WITH PANDAS
dfBitcoin = pd.read_csv("./data/bitcoin_price.csv", parse_dates=["Date"])
dfEtherium = pd.read_csv("./data/ethereum_price.csv", parse_dates=["Date"])
dfRipple = pd.read_csv("./data/ripple_price.csv", parse_dates=["Date"])


dfBitcoin.head()
# dfEtherium.head()
# dfRipple.head()

# Plots the Closing prices of bitcoins
dfBitcoin["Date_mplt"] = dfBitcoin["Date"].apply(
    lambda x: matdates.date2num(x))
fig, ax = plt.subplots(figsize=(12, 8))
sns.tsplot(dfBitcoin.Close.values, time=dfBitcoin.Date_mplt.values,
           alpha=0.8, color=color[3], ax=ax)
ax.xaxis.set_major_locator(matdates.AutoDateLocator())
ax.xaxis.set_major_formatter(matdates.DateFormatter('%Y.%m.%d'))
fig.autofmt_xdate()
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price in USD', fontsize=12)
plt.title("Closing Price Distribution of Bitcoin", fontsize=15)
plt.show()
# END

# Plotting using Candle Sticks
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid((1, 1), (0, 0))

temp_df = dfBitcoin[dfBitcoin["Date"] > '2017-01-01']
ohlc = []
for ind, row in temp_df.iterrows():
    ol = [row['Date_mplt'], row['Open'], row['High'],
          row['Low'], row['Close'], row['Volume']]
    ohlc.append(ol)

candles(ax1, ohlc, width=0.4, colorup="#77d879", colordown="#ad0000")
ax1.xaxis.set_major_formatter(matdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(matticker.MaxNLocator(10))

plt.xlabel("Date", fontsize=12)
plt.ylabel("Price in USD", fontsize=12)
plt.title("Candlestick chart for Bitcoin", fontsize=15)
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94,
                    top=0.90, wspace=0.2,  hspace=0)
plt.show()
# END

# ALLOWS FOR ANY COIN TO BE PLOTTED
DATA_FILE = "ethereum_price.csv"

coin_name = DATA_FILE.split("_")[0]
df = pd.read_csv("./data/" + DATA_FILE, parse_dates=['Date'])
df['Date_mplt'] = df['Date'].apply(lambda x: matdates.date2num(x))
fig, ax = plt.subplots(figsize=(12, 8))
sns.tsplot(df.Close.values, time=df.Date_mplt.values,
           alpha=0.8, color=color[2], ax=ax)
ax.xaxis.set_major_locator(matdates.AutoDateLocator())
ax.xaxis.set_major_formatter(matdates.DateFormatter('%Y.%m.%d'))
fig.autofmt_xdate()
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price in USD', fontsize=12)
plt.title("Closing Price Distribution of " + coin_name, fontsize=15)
plt.show()
# END


# GENERATING A HEATMAP
files_to_use = ["bitcoin_price.csv", "ethereum_price.csv", "ripple_price.csv"]

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

temp_df = df[cols_to_use]
corrmat = temp_df.corr(method="spearman")
fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(corrmat, vmax=1., square=True)
plt.title("Cryptocurrency Heat Map", fontsize=16)
plt.show()
# END


# Looking for the Future Prices
DATA_FILE = "ripple_price.csv"
df = pd.read_csv("./data/" + DATA_FILE,
                 usecols=["Date", "Close"], parse_dates=["Date"])
df.columns = ["ds", "y"]

p = Prophet()
p.fit(df)
future = p.make_future_dataframe(periods == 30)
forecast = p.predicts(future)
forecast[['ds, yhat, yhat_lower', 'yhat_upper']].tail()
