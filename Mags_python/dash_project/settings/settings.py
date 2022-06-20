import os.path

from dash import Dash, Input, Output, State
import dash_bootstrap_components as dbc
from pandas import read_csv

from pages.sidebar import hidden

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


@app.callback(
    Output("sidebar_input_symbol", "value"),
    Output("sidebar_input_path", "value"),
    Input("modal_window", "is_open"),
    prevent_initial_call=True
)
def upload_button(_):
    return None, None


@app.callback(
    Output("modal_window", "is_open"),
    Input("upload_file_window_centered", "n_clicks"),
    prevent_initial_call=True
)
def upload_button(_n_clicks):
    return True


@app.callback(
    Output("sidebar_input_path", "valid"),
    Output("sidebar_input_symbol", "valid"),

    Output("input_for_uploaded_file", "style"),
    Output("uploaded_file_info", "style"),
    Output("upload_file_hidden", "style"),

    Input("upload_file_modal", "n_clicks"),
    State("sidebar_input_path", "value"),
    State("sidebar_input_symbol", "value"),
    prevent_initial_call=True
)
def input_file(_n_clicks, file, sep):
    if file and sep:
        print(file, sep, os.path.basename(file))
        return True, True, {}, {}, {}
    return False, False, hidden, hidden, hidden


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
