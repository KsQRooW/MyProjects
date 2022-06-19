from dash import Dash
import dash_bootstrap_components as dbc
from pandas import read_csv

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
df = read_csv('../assets/insurance.csv', sep=',')
df_no_cat = df.copy()

changer_sex = {'female': 1, 'male': 2}
df_no_cat['sex'] = df['sex'].map(lambda x: changer_sex[x])

changer_smoker = {'no': 1, 'yes': 2}
df_no_cat['smoker'] = df['smoker'].map(lambda x: changer_smoker[x])

changer_region = {'northeast': 1, 'southwest': 2, 'northwest': 3, 'southeast': 4}
df_no_cat['region'] = df['region'].map(lambda x: changer_region[x])


changer = {
    'sex': list(changer_sex),
    'smoker': list(changer_smoker),
    'region': list(changer_region)
}
