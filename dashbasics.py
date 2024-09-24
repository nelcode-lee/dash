import dash
from dash import dcc
from dash import html


app = dash.Dash()

colors = {'background': '1111111', text: '#7fdbff'}
colors



app.layout = html.Div(children=[
    html.H1('Hello Dash', style ={'textAlign': 'center',
                                  'color':colors['text']}),


    dcc.Graph(id='example',
        figure=={'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor':['background'],
                'paper_bgcolor':colors['background'],
                'font':{'color':colors['text']}
                'title': 'Dash Data Visualization'
            }
        }
    )
], style = {'background':colors['background']})

if __name__ == '__main__':
    app.run_server()
