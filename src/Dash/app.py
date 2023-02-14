import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output


def dash_graph(donnees):

    app = dash.Dash(__name__)

    category = ["homophob", "racist", "sexist",
                "religion", "insult"]

    indicateurs_WOEID = ["Paris", "London", "New York"]

    colors = {
        'background': '#FFFFFF',
        'text': '#006182',
        'fond_graphique': '#E6E6E6'
    }
    # df est le dataframe utilisé pour faire le graphique (notes des différentes tendances twitter)

    datae = []
    for k in range(3):
        datae.append([])
        for i in range(5):
            datae[k].append(go.Bar(x=donnees[k][i]["tendances"],
                                   y=donnees[k][i]["notes"], name=category[i]))
    # mise en page de l'app

    # Header + affichage du graphe
    app.layout = html.Div([html.Div(style={'backgroundColor': colors['background']}, children=[html.Div(
        className="app-header",
        children=[
            html.Div('État des tendances Twitter',
                     className="app-header--title"), html.Img(src="/assets/tousantiinsultes.png", width='300px')
        ]
    ),

        # menu déroulant au-dessus de l'histogramme
        html.Div([
            dcc.Dropdown(
                id='loca',
                options=[{'label': i, 'value': i} for i in indicateurs_WOEID],
                value='London'
            )]),

        dcc.Graph(id='histo_tend')
    ]),


        # Bas de la page
        html.Div([
            html.Div(
                children=[html.Div("Description", className="app-desc"),
                          html.Div("Cette application permet de visualiser la part d'insultes dans les différentes tendances de twitter. Pour chaque sujet en tendance, l'application compte le nombre d'insultes (pondéré en fonction de la vulgarité) pour cent tweets.",
                                   className="app-desc--corps")
                          ]
            )
        ]), html.Div(children=[html.Div('Antoine Dieu, Etienne Lefranc, Ambroise Marché, Matthieu Scharffe, Quentin Echasseriau, Lisa Lupi – Coding weeks 2021', className="app-footer")])])

    # callback

    @app.callback(
        Output("histo_tend", 'figure'),
        [Input('loca', 'value')]
    )
    def update_graph(valeur):
        if valeur == 'Paris':
            fig = go.Figure(data=datae[0], layout=go.Layout(barmode='stack'))
        elif valeur == "London":
            fig = go.Figure(data=datae[1], layout=go.Layout(barmode='stack'))
        elif valeur == 'New York':
            fig = go.Figure(data=datae[2], layout=go.Layout(barmode='stack'))
        return fig

    app.run_server(debug=True, use_reloader=False)
