###### CALLS FIRST 5 ITEMS # cryptoMarket.head()

CALSS LAST 5 ITEMS # cryptoMarket.tail()

MANIPULATE ROWS # cryptoMarket.iloc[:5,]

MANIPULATE COLUMNS # cryptoMarket.iloc[:5,1:9]

CALL ROWS WITHS SPECIFIC COLUMNS # cryptoMarket.loc[:,["name","symbol","date","open","close","high","low","volume","market","close_ratio","spread"]]

CALL SPECIFIC ROWN AND ID's
cryptoMarket.loc[[1,2],["name","symbol","date"]]

cryptoMarket["single column"]

cryptoMarket[["search","many","columns"]]

type(cryptoMarket["name"]) single column in a series

cryptoMarket[["name","symbol","date","open","close","high","low","volume","market","close_ratio","spread"]]

#Creating a Custom DF
s1 = pd.Series([1,2])
s2 = pd.Series(["Warren","James"])
pd.DataFrame([s1,s2])
frame = pd.DataFrame(
    [[1,2],["warren","james"]],
    index=["row1","row2"],
    columns = ["column1", "column2"]
)
frame.loc["row1":"row2", "column1"]
