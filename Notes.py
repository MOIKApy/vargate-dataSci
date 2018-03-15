'''
My Python Notes Learning Data Science

'''

# CALLS FIRST 5 ITEMS # cryptoMarket.head()

# CALSS LAST 5 ITEMS # cryptoMarket.tail()
#
# MANIPULATE ROWS # cryptoMarket.iloc[:5,]
#
# MANIPULATE COLUMNS # cryptoMarket.iloc[:5,1:9]
#
# CALL ROWS WITHS SPECIFIC COLUMNS # cryptoMarket.loc[:,["name","symbol","date","open","close","high","low","volume","market","close_ratio","spread"]]
#
# CALL SPECIFIC ROWN AND ID's
# cryptoMarket.loc[[1,2],["name","symbol","date"]]
#
# cryptoMarket["single column"]
#
# cryptoMarket[["search","many","columns"]]
#
# type(cryptoMarket["name"]) single column in a series
#
# cryptoMarket[["name","symbol","date","open","close","high","low","volume","market","close_ratio","spread"]]
#
# #Creating a Custom DF
# s1 = pd.Series([1,2])
# s2 = pd.Series(["Warren","James"])
# pd.DataFrame([s1,s2])
# frame = pd.DataFrame(
#     [[1,2],["warren","james"]],
#     index=["row1","row2"],
#     columns = ["column1", "column2"]
# )
# frame.loc["row1":"row2", "column1"]

# What I use to explore

# files_to_use = ["bitcoin_price.csv",
#                 "ethereum_price.csv", "ripple_price.csv"]
# Comparing Closing prices

# def comparing_all_three(e):
#
# cols_to_use = []
# for ind, file_name in enumerate(files_to_use):
#     coin_name = file_name.split("_")[0]
#     if ind == 0:
#         df = pd.read_csv("./data/" + file_name,
#                          usecols=["Date", "Close"], parse_dates=["Date"])
#         df.columns = ["Date", coin_name]
#     else:
#         temp_df = pd.read_csv("./data/" + file_name,
#                               usecols=["Date", "Close"], parse_dates=["Date"])
#         temp_df.columns = ["Date", coin_name]
#         df = pd.merge(df, temp_df, on="Date")
#     cols_to_use.append(coin_name)
# print(df.head())
#
#
# comparing_all_three(files_to_use)

# dfBitcoin.head()
# dfEtherium.head()
# dfRipple.head()

# Plots the Closing prices of bitcoins
# dfBitcoin["Date_mplt"] = dfBitcoin["Date"].apply(
#     lambda x: matdates.date2num(x))
# fig, ax = plt.subplots(figsize=(12, 8))
# sns.tsplot(dfBitcoin.Close.values, time=dfBitcoin.Date_mplt.values,
#            alpha=0.8, color=color[3], ax=ax)
# ax.xaxis.set_major_locator(matdates.AutoDateLocator())
# ax.xaxis.set_major_formatter(matdates.DateFormatter('%Y.%m.%d'))
# fig.autofmt_xdate()
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Price in USD', fontsize=12)
# plt.title("Closing Price Distribution of Bitcoin", fontsize=15)
# plt.show()
# END

# # Plots the Closing prices of ethereum
# dfEthereum["Date_mplt"] = dfEthereum["Date"].apply(
#     lambda x: matdates.date2num(x))
# fig, ax = plt.subplots(figsize=(12, 8))
# sns.tsplot(dfEthereum.Close.values, time=dfEthereum.Date_mplt.values,
#            alpha=0.8, color=color[3], ax=ax)
# ax.xaxis.set_major_locator(matdates.AutoDateLocator())
# ax.xaxis.set_major_formatter(matdates.DateFormatter('%Y.%m.%d'))
# fig.autofmt_xdate()
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Price in USD', fontsize=12)
# plt.title("Closing Price Distribution of Ethereum", fontsize=15)
# plt.show()
# # END
#
# # Plots the Closing prices of ripple
# dfRipple["Date_mplt"] = dfRipple["Date"].apply(
#     lambda x: matdates.date2num(x))
# fig, ax = plt.subplots(figsize=(12, 8))
# sns.tsplot(dfRipple.Close.values, time=dfRipple.Date_mplt.values,
#            alpha=0.8, color=color[3], ax=ax)
# ax.xaxis.set_major_locator(matdates.AutoDateLocator())
# ax.xaxis.set_major_formatter(matdates.DateFormatter('%Y.%m.%d'))
# fig.autofmt_xdate()
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Price in USD', fontsize=12)
# plt.title("Closing Price Distribution of Ripple", fontsize=15)
# plt.show()
# END

# Plotting using Candle Sticks
# fig = plt.figure(figsize=(12, 8))
# ax1 = plt.subplot2grid((1, 1), (0, 0))
#
# temp_df = dfBitcoin[dfBitcoin["Date"] > '2017-01-01']
# ohlc = []
# for ind, row in temp_df.iterrows():
#     ol = [row['Date_mplt'], row['Open'], row['High'],
#           row['Low'], row['Close'], row['Volume']]
#     ohlc.append(ol)
#
# candles(ax1, ohlc, width=0.4, colorup="#77d879", colordown="#ad0000")
# ax1.xaxis.set_major_formatter(matdates.DateFormatter('%Y-%m-%d'))
# ax1.xaxis.set_major_locator(matticker.MaxNLocator(10))
#
# plt.xlabel("Date", fontsize=12)
# plt.ylabel("Price in USD", fontsize=12)
# plt.title("Candlestick chart for Bitcoin", fontsize=15)
# plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94,
#                     top=0.90, wspace=0.2,  hspace=0)
# plt.show()
# END

# ALLOWS FOR ANY COIN TO BE PLOTTED

# DATA_FILE = "consolidated_coin_data.csv"
#
# coin_name = DATA_FILE.split("_")[0]
# df = pd.read_csv("./data/" + DATA_FILE, parse_dates=['Date'])
# # df['Date_mplt'] = df['Date'].apply(lambda x: matdates.date2num(x))
# df.head()
#
#
# fig, ax = plt.subplots(figsize=(12, 8))
# sns.tsplot(df.Close.values, time=df.Date_mplt.values,
#            alpha=0.8, color=color[2], ax=ax)
# ax.xaxis.set_major_locator(matdates.AutoDateLocator())
# ax.xaxis.set_major_formatter(matdates.DateFormatter('%Y.%m.%d'))
# fig.autofmt_xdate()
# plt.xlabel('Date', fontsize=12)
# plt.ylabel('Price in USD', fontsize=12)
# plt.title("Closing Price Distribution of " + coin_name, fontsize=15)
# plt.show()

# END

# GENERATING A HEATMAP
# files_to_use = ["bitcoin_price.csv", "ethereum_price.csv", "ripple_price.csv"]
#
# cols_to_use = []
# for ind, file_name in enumerate(files_to_use):
#     coin_name = file_name.split("_")[0]
#     if ind == 0:
#         df = pd.read_csv("./data/" + file_name,
#                          usecols=["Date", "Close"], parse_dates=["Date"])
#         df.columns = ["Date", coin_name]
#     else:
#         temp_df = pd.read_csv("./data/" + file_name,
#                               usecols=["Date", "Close"], parse_dates=["Date"])
#         temp_df.columns = ["Date", coin_name]
#         df = pd.merge(df, temp_df, on="Date")
#     cols_to_use.append(coin_name)
# df.head()
#
# temp_df = df[cols_to_use]
# corrmat = temp_df.corr(method="spearman")
# fig, ax = plt.subplots(figsize=(10, 10))
# sns.heatmap(corrmat, vmax=1., square=True)
# plt.title("Cryptocurrency Heat Map", fontsize=16)
# plt.show()
# END

# READING THE CSV WITH PANDAS
# dfBitcoin = pd.read_csv("./data/bitcoin_price.csv", parse_dates=["Date"])
# dfEthereum = pd.read_csv("./data/ethereum_price.csv", parse_dates=["Date"])
# dfRipple = pd.read_csv("./data/ripple_price.csv", parse_dates=["Date"])
