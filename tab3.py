import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

def render_tab(df):
    sorting_order = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    grouped =  df[df['total_amt']>0].groupby([df['tran_date'].dt.day_name(),'Store_type'])['total_amt'].sum().round(2).unstack()
    grouped.index = pd.CategoricalIndex(grouped.index, categories=sorting_order, ordered=True)
    grouped = grouped.sort_index()
    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(x=grouped.index,y=grouped[col],name=col,hoverinfo='text',
        hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]))
    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Kanały sprzedaży',barmode='stack',legend=dict(x=0,y=-0.5)))
    
    layout = html.Div([html.H1('Kanały sprzedaży',style={'text-align':'center'}),
                        html.Div([html.Div([dcc.Graph(id='pie-prod-cat',figure=fig)]),
                        html.Div([dcc.Dropdown(id='prod_dropdown-canal',
                                    options=[{'label':prod_cat,'value':prod_cat} for prod_cat in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    html.Div([dcc.Graph(id='bar-sales-country-canal')],style={'height':'50%'})]),
                                    html.Div([dcc.Graph(id='bar-sales-gender-canal')],style={'height':'50%'})])])
    return layout