
from re import X
import csv, pandas as pd, matplotlib.pyplot as plt
from os import system

def HydroBill():
    system("cls")

    csv_data = 

    df = pd.read_csv(csv.dumps(csv_data['Time Period'])) # df : Data Frame
    print(df)

    ax = df.plot.bar(
        x='Time Period',
        y='Amount ($)',
        rot=0,
        legend=False
    )
    ax.set_title('Hydro Bill 2021', fontsize=20)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Amount($)', fontsize=14)
    ax.invert_xaxis()
    plt.show()


HydroBill()




# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# https://api.opencovid.ca/timeseries
# https://github.com/andrew-davis4/HydroBill