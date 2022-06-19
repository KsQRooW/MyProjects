from dash import dcc, html
import dash_bootstrap_components as dbc

SIDESTYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#222222",
}

CONTSTYLE = {
    "margin-left": "18rem",
    "margin-right": "3rem",
    "padding": "2rem 1rem",
}

loader = {
    "width": "1rem"
}

navlink_flex = {
    "display": "flex",
    "alignItems": "center"
}

span_flex = {
    "flexGrow": "1"
}

sidebar = html.Div([
    dcc.Location(id="url"),
    html.Div(
        [
            html.H6("Analyze", className="display-3", style={'color': 'white'}),
            html.Hr(style={'color': 'white'}),
            dbc.Nav(
                [
                    dbc.NavLink([html.Span("Histograms", style=span_flex),
                                 html.Div(dbc.Spinner(html.Div(id="page_hist_loading"), size="sm"), style=loader)],
                                href="/hist", active="exact",
                                style=navlink_flex),
                    dbc.NavLink([html.Span("Box-And-Whiskers", style=span_flex),
                                 html.Div(dbc.Spinner(html.Div(id="page_box_whisk_loading"), size="sm"), style=loader)],
                                href="/box_whisk", active="exact",
                                style=navlink_flex),
                    dbc.NavLink([html.Span("Scatter", style=span_flex),
                                 html.Div(dbc.Spinner(html.Div(id="page_scatter_loading"), size="sm"), style=loader)],
                                href="/scatter", active="exact",
                                style=navlink_flex),
                    dbc.NavLink([html.Span("Bar", style=span_flex),
                                 html.Div(dbc.Spinner(html.Div(id="page_bar_loading"), size="sm"), style=loader)],
                                href="/bar", active="exact",
                                style=navlink_flex),
                    dbc.NavLink([html.Span("Statistic", style=span_flex),
                                 html.Div(dbc.Spinner(html.Div(id="page_stat_loading"), size="sm"), style=loader)],
                                href="/stat", active="exact",
                                style=navlink_flex),
                    # dbc.DropdownMenu(
                    #             [dbc.DropdownMenuItem("age/bmi/charges"),
                    #              dbc.DropdownMenuItem("sex/region/children/smoker")],
                    #             label="Histograms",
                    #             nav=True
                    #         ),
                    # dbc.NavLink("The effect", href="/page2", active="exact"),
                    # dbc.NavLink("Thanks", href="/page3", active="exact"),
                    # dbc.NavLink("Histograms", href="/page4", active="exact"),
                ],
                vertical=True, pills=True),
        ],
        style=SIDESTYLE
    ),
    html.Div(id="page-content", children=[], style=CONTSTYLE)
])
