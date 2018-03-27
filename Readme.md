# Python Data Science Project for Code Louisville
###### Please Run in Jupyter Notebook or py index.py
###### Installed Python from www.anaconda.com
###### Please install these packages before running:
- jupyter notebook
- sqlite3
- matplotlib.dates
- matplotlib.pyplot
- numpy
- pandas
- plotly.graph_objs
- plotly.plotly
- seaborn
- from pandas.tools.plotting import table

###### Database
- All Data is Stored in:
  - db/cryptoGG.db

### Current question I am Trying to Answer?
###### How well have Bitcoin, Ethereum, and Ripple been performing from January 1st to Present?
- To find this information I downloaded a few CSV from the kaggle website and began by merging the files into one data frame using a similar column, "Date". I then viewed the .head() of the new Data Frame to see if the files merged correctly and to note the new names of the columns. ex: "Close_x being file 1", "Close_y being file2", and "Close being file 3". After double checking my DF I then upload it to my SQLite Database which is updated each run. For each figure the DB is cleaned for comparison. This project contains a few sample results of the data I was able to gather.

- Figures used:
  - Heatmap
  - Pie Chart
