import csv
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("pro108data.csv")
fig = ff.create_distplot([df["Avg Rating"]], ["Rating"], show_hist=False) 
fig.show() 