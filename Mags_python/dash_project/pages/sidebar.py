import os

from dash import dcc, html
import dash_bootstrap_components as dbc

SIDESTYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "17rem",
    "padding": "2rem 1rem",
    "background-color": "#222222",
    "display": "flex",
    "flex-direction": "column",
    "justify-content": "space-between"
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

hidden = {
    "display": "none"
}

sidebar = html.Div([
    dcc.Location(id="url"),
    html.Div(
        [
            html.Div([
                html.H6("Analyze", className="display-3", style={'color': 'white'}),
                html.Hr(style={'color': 'white'}),
                dbc.Nav(
                    [
                        dbc.NavLink([html.Span("Histograms", style=span_flex),
                                     html.Div(dbc.Spinner(html.Div(id="page_hist_loading"), size="sm"), style=loader)],
                                    href="/hist", active="exact",
                                    style=navlink_flex),
                        dbc.NavLink([html.Span("Box-And-Whiskers", style=span_flex),
                                     html.Div(dbc.Spinner(html.Div(id="page_box_whisk_loading"), size="sm"),
                                              style=loader)],
                                    href="/box_whisk", active="exact",
                                    style=navlink_flex),
                        dbc.NavLink([html.Span("Scatter", style=span_flex),
                                     html.Div(dbc.Spinner(html.Div(id="page_scatter_loading"), size="sm"),
                                              style=loader)],
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
            ]),
            html.Div([
                dbc.FormText("File name / Separator", id="input_for_uploaded_file", style=hidden),
                dbc.Input(id="uploaded_file_info", size="sm", readonly=True, style=hidden),
                dbc.Button("Загрузить файл_2", id="upload_file_hidden", color="primary", n_clicks=0, size="sm", style=hidden)
            ])
        ],
        style=SIDESTYLE
    ),
    html.Div([
        html.Div(id="page-content", children=[], style=CONTSTYLE),
        # dbc.Alert("Выберите файл и разделитель!", id="alert_sidebar", color="warning", style=CONTSTYLE, is_open=True)
    ]),
    dbc.Button("Загрузить файл_1", id="upload_file_window_centered", color="primary", n_clicks=0, style=CONTSTYLE),
    dbc.Modal([
        dbc.ModalBody([
            dbc.FormText("File path", id="sidebar_formtext_path"),
            dbc.Input(id="sidebar_input_path", type="file", size="sm", valid=False),

            dbc.FormText("Separator", id="sidebar_formtext_symbol"),
            dbc.Input(id="sidebar_input_symbol", size="sm", valid=False)
        ]),
        dbc.ModalFooter(
            dbc.Button("Применить", id="upload_file_modal", color="primary", n_clicks=0, size="sm")
        )
    ], id="modal_window", centered=True, is_open=False)
])
