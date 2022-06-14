from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
df = pd.read_csv('../assets/insurance.csv', sep=',')
