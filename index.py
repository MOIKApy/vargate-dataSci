import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib3
import json as js
urllib3.disable_warnings()  # Disables Certificate Warning

http = urllib3.PoolManager()
api = "https://api.iextrading.com/1.0"
call ="/tops?symbols=vktx,tmfc,nvda,xlk,aker,blok,bac,vktx,o"
## &format=csv use to turn file into csv
api_call = api + call

req = http.request('GET', api_call)

data_parsed = js.loads(req.data.decode('utf-8'))

stock_json = js.loads(req.data.decode('utf-8'))  # TURN PYTHON OBJ RESPONSE INTO JSON

print(stock_json)
