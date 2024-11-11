import plotly.express as px
import pandas as pd
import sys
import argparse

parser = argparse.ArgumentParser("python fosscostplots.py")
parser.add_argument("--type", choices=['Incremental Cost', 'Cumulative Cost'], help='Select column to plot', type=str)
args = parser.parse_args()
try:
    df = pd.read_csv("input.csv")
except (FileNotFoundError, pd.errors.ParserError, pd.errors.EmptyDataError, pd.errors.IntCastingNaNError):
    print('Missing input csv file or errors in file')
    sys.exit()
except Exception as e:
    print(f'Weird error: {e}')
    sys.exit()
try:
    fig = px.line(df, x='Date', y=args.type)
    fig.write_html('plot.html')
except Exception as e:
    print(f'Wrong column names or other problems: {e}')
    sys.exit()


