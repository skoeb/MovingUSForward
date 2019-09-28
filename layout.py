import dash
import dash_table
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

# --- Module Imports ---
import resources
import layout

# --- Layout ---
html_obj = html.Div([

# Title - Row
    html.Div([
        html.H1(
            'Moving US Forward',
            style={'font-family': 'Helvetica',
                "margin-top": "25",
                "margin-bottom": "0"},
            className='nine columns',
        ),
        html.A([
            html.Img(
                src="assets/MigrahackLogo.png",
                className='two columns',
                style={
                    'height': '20%',
                    'width': '20%',
                    'float': 'right',
                    'position': 'relative',
                    'padding-top': 10,
                    'padding-right': 0
                },
            )], href='https://coloradomigrahack.school.blog'),

        html.H4(
            'A decision support tool for renewable energy planning for utilities.',
            style={'font-family': 'Helvetica',
                'position':'left',
                'width':'100%'},
            className='twelve columns',
        )
    ],
    className='row',
    ),
])