import dash
import dash_core_components as dcc
import dash_html_components as html

# Inicialize a aplicação Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div(children=[
    html.H1(children='Meu Dashboard'),

    html.Div(children='''
        Aqui está um gráfico simples.
    '''),

    # Gráfico de exemplo
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Grupo 1'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Grupo 2'},
            ],
            'layout': {
                'title': 'Gráfico de Barras Simples'
            }
        }
    )
])

# Executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
