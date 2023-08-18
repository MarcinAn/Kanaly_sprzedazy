import dash_core_components as dcc
import dash_html_components as html


def render_tab(df):

    layout = html.Div(
        [
            html.H1("Kanały sprzedaży", style={"text-align": "center"}),
            html.Div(
                [
                    dcc.Dropdown(
                        id="prod_dropdown-canal",
                        options=[
                            {"label": prod_cat, "value": prod_cat}
                            for prod_cat in df["Store_type"].unique()
                        ],
                        value=df["Store_type"].unique()[0],
                    ),
                    html.Div([dcc.Graph(id="bar-sales-canal")]),
                    html.Div([dcc.Graph(id="bar-sales-country-canal")]),
                    html.Div([dcc.Graph(id="bar-sales-gender-canal")]),
                ]
            ),
        ]
    )
    return layout
