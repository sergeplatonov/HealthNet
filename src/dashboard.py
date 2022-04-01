import json

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_reusable_components as drc
from dash.dependencies import Input, Output
import dash_cytoscape as cyto

app = dash.Dash(__name__)
server = app.server
app.title = 'Netzwerk Analyse'
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

# Load Data
with open('..\\input_data\\data.json', 'r') as f:
    elements = json.loads(f.read())

with open('..\\input_data\\style.json', 'r') as f:
    stylesheet = json.loads(f.read())

# Load extra layouts
cyto.load_extra_layouts()

app = dash.Dash(__name__)

# Define the tab styles
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

# ################################# APP LAYOUT ################################

app.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Landing Page', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Network Analysis', value='tab-2', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
])
# ################################# CALLBACKS ################################
@app.callback(Output('tabs-content-inline', 'children'),
              [Input('tabs-styled-with-inline', 'value')])


def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Welcome to Managed Care Dashboards!')
        ])
    elif tab == 'tab-2':
        return html.Div([

        html.Div(className='eight columns', children=[
            cyto.Cytoscape(
                id='cytoscape',
                elements=elements,
                stylesheet=stylesheet,
                style={
                    'width': '70%',
                    'height': '90%',
                    'position': 'absolute',
                    'left': 0,
                    'top': 80,
                    'z-index': 999

                },
                layout={
                    'name': "breadthfirst",
                  #   'idealEdgeLength': 100,
                  #   'nodeOverlap': 20,
                  #   'refresh': 20,
                  #  'fit': True,
                  #    'padding': 30,
                  #    'randomize': False,
                  #    'componentSpacing': 10000,
                  #    'nodeRepulsion': 4000,
                  #    'edgeElasticity': 100,
                  #    'nestingFactor': 1,
                  #    'gravity': 80,
                  #    'numIter': 1000,
                  #    'initialTemp': 200,
                  #    'coolingFactor': 0.95,
                  #    'minTemp': 1.0
                }
            )
        ]),

        html.Div(className='four columns', children=[
            dcc.Tabs(id='tabs',style={
                            'width': '30%',
                            'height': '90%',
                            'position': 'absolute',
                            'left': 1000,
                            'top': 0,
                            'z-index': 999

                        }, children=[
                dcc.Tab(label='Control Panel',style={
                            'width': '30%',
                            'height': '90%',
                            'position': 'absolute',
                            'left': 1000,
                            'top': 0,
                            'z-index': 999}, children=[
                    drc.NamedDropdown(
                        name='Layout',
                        id='dropdown-layout',
                        options=drc.DropdownOptionsList(
                            'random',
                            'grid',
                            'circle',
                            'concentric',
                            'breadthfirst',
                            'cose',
                            'cose-bilkent',
                            'dagre',
                            'cola',
                            'klay',
                            'spread',
                            'euler'
                        ),
                        value='grid',
                        style={
                            'width': '30%',
                            'height': '90%',
                            'position': 'absolute',
                            'left': 1000,
                            'top': 0,
                            'z-index': 999},
                        clearable=False
                    ),
                    drc.NamedRadioItems(
                        name='Expand',
                        id='radio-expand',
                        style={
                            'width': '30%',
                            'height': '90%',
                            'position': 'absolute',
                            'left': 1000,
                            'top': 0,
                            'z-index': 999},
                        options=drc.DropdownOptionsList(
                            'followers',
                            'following'
                        ),
                        value='followers'
                    )
                ]),

            ])
        ])
    ])

# ################################# RUN SERVER ################################

if __name__ == '__main__':
    app.run_server(debug=True)