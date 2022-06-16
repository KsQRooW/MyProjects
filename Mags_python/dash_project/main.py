import plotly.express as px
from dash.dependencies import Input, Output
from pages import *
from settings import app, df
from models import sidebar, hist, dist
import warnings
warnings.filterwarnings("ignore")

app.layout = sidebar


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def pagecontent(pathname):
    if pathname == "/page1":
        return page_1

    elif pathname == "/page2":
        return page_2

    elif pathname == "/page3":
        return page_3

    elif pathname == "/page4":
        return page_4


@app.callback(
    Output('output_graph', 'figure'),
    [Input('demo_drop', 'value')]
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


@app.callback(
    [Output('graph_4_1', 'figure'),
     Output('graph_4_2', 'figure'),
     Output('graph_4_3', 'figure'),
     Output('graph_4_4', 'figure')],
    [Input('page4_drop', 'value')]
)
def swapper(value):
    if value == 'Histogram':
        res = hist(df, ['age', 'bmi', 'children', 'charges']).plots
        return res
    elif value == 'Distplot':
        res = dist(df, ['age', 'bmi', 'children', 'charges']).plot
        return res


if __name__ == '__main__':
    app.run_server(debug=True)
