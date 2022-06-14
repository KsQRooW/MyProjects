import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output

from pages.page_3 import page_3
from pages.page_2 import page_2
from pages.page_1 import page_1
from settings import app, df
from models.sidebar import sidebar

app.layout = sidebar


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def pagecontent(pathname):
    if pathname == "/page1":
        return page_1

    elif pathname == "/page2":
        return page_2

    elif pathname == "/page3":
        return page_3


@app.callback(
    Output(component_id='output_graph', component_property='figure'),
    [Input(component_id='demo_drop', component_property='value')]
)
def update_output(value):
    if value == 'children':
        h = df.groupby(['children'], as_index=False, sort=False)['age'].count()
    elif value == 'charges':
        h = df.groupby(['charges'], as_index=False, sort=False)['age'].count()
    elif value == 'bmi':
        h = df.groupby(['bmi'], as_index=False, sort=False)['age'].count()
    fig = px.bar(h, x=value, y="age", labels={"age": "Count"})
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
