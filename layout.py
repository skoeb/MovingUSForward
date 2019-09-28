import dash
import dash_table
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

# --- Module Imports ---

# --- Layout ---
html_obj = html.Div([

    # Title - Row
    html.Div([
        html.Div([
            html.H1(
                'Moving US Forward',
                style={'font-family': 'Helvetica',
                    "margin-top": "0",
                    "margin-bottom": "0"},
            ),
            html.H4(
                "How increased access to drivers licenses under SB13-251 has improved the lives of Colorado's immigrant community.",
                style={'font-family': 'Helvetica',
                    'position':'left',
                    'width':'100%'},
            )],
        
        className='seven columns',
        ),

        html.A([
            html.Img(
                src="assets/MigrahackLogo.png",
                className='three columns',
                style={
                    'height': '11%',
                    'width': '11%',
                    'testAlign':'center',
                    'float':'right',
                    },
            )], href='https://coloradomigrahack.school.blog'),
    ],
    className='row',
    ),
    
    # -------------------------------------------------------
    # -------------------- Introduction ---------------------
    # -------------------------------------------------------
    html.Div([    
        # Spacer
        html.Div([
            html.Img(
                src='assets/spacer.png',
                className='twelve columns')
        ],
        className = 'twelve columns',
        style={'margin-left':'auto','margin-right':'auto'}
        ),

        # Title
        html.Div([
            html.H3(
                'Introduction:',
            )],
        className='twelve columns',
        style={'margin-top':0}),

        # Text
        html.Div([
            dcc.Markdown("""
                    The Philippines RPS is a legislative mandate requiring utilities to increase their use of renewable resources including
                    *“biomass, waste to energy technology, wind, solar, run-of-river, impounding hydropower sources that meet internationally accepted standards, ocean, hybrid systems, 
                    geothermal and other RE technologies that may be later identified by the DOE."* 
                    
                    The RPS requires all utilities to increase their utilization of renewable energy by 1% of their total energy sales (kWh) each year beginning in 2020, although this percentage can be increased in the future by the National Renewable Energy Board.
                    For many utilities, the lower costs and higher customer satisfaction with renewables is encouraging adoption above what the RPS requires. This calculator is designed to help utilities understand when they will need to procure additional renewable capacity, and how procuring additional renewables could result in cost savings.
                    Click through the tabs below to input data for your utility. More details about each input can be found by hovering your mouse over the circled question-mark symbols.
                    """.replace('  ', ''),
                    className='twelve columns',
            ),
        ]),
    ]),

    # -------------------------------------------------------
    # -------------------- Section 1 ------------------------
    # -------------------------------------------------------
    html.Div([    
        # Spacer
        html.Div([
            html.Img(
                src='assets/spacer.png',
                className='twelve columns')
        ],
        className = 'twelve columns',
        style={'margin-left':'auto','margin-right':'auto'}
        ),

        # Title
        html.Div([
            html.H3(
                'Section 1:',
            )],
        className='twelve columns',
        style={'margin-top':0}),

        # Text
        html.Div([
            dcc.Markdown("""
                    The Philippines RPS is a legislative mandate requiring utilities to increase their use of renewable resources including
                    *“biomass, waste to energy technology, wind, solar, run-of-river, impounding hydropower sources that meet internationally accepted standards, ocean, hybrid systems, 
                    geothermal and other RE technologies that may be later identified by the DOE."* 
                    
                    The RPS requires all utilities to increase their utilization of renewable energy by 1% of their total energy sales (kWh) each year beginning in 2020, although this percentage can be increased in the future by the National Renewable Energy Board.
                    For many utilities, the lower costs and higher customer satisfaction with renewables is encouraging adoption above what the RPS requires. This calculator is designed to help utilities understand when they will need to procure additional renewable capacity, and how procuring additional renewables could result in cost savings.
                    Click through the tabs below to input data for your utility. More details about each input can be found by hovering your mouse over the circled question-mark symbols.
                    """.replace('  ', ''),
                    className='twelve columns',
            ),
        ]),
    ]),

    # -------------------------------------------------------
    # ---------------------- Section 2 ----------------------
    # -------------------------------------------------------
    html.Div([    
        # Spacer
        html.Div([
            html.Img(
                src='assets/spacer.png',
                className='twelve columns')
        ],
        className = 'twelve columns',
        style={'margin-left':'auto','margin-right':'auto'}
        ),

        # Title
        html.Div([
            html.H3(
                'Section 2:',
            )],
        className='twelve columns',
        style={'margin-top':0}),

        # Text
        html.Div([
            dcc.Markdown("""
                    The Philippines RPS is a legislative mandate requiring utilities to increase their use of renewable resources including
                    *“biomass, waste to energy technology, wind, solar, run-of-river, impounding hydropower sources that meet internationally accepted standards, ocean, hybrid systems, 
                    geothermal and other RE technologies that may be later identified by the DOE."* 
                    
                    The RPS requires all utilities to increase their utilization of renewable energy by 1% of their total energy sales (kWh) each year beginning in 2020, although this percentage can be increased in the future by the National Renewable Energy Board.
                    For many utilities, the lower costs and higher customer satisfaction with renewables is encouraging adoption above what the RPS requires. This calculator is designed to help utilities understand when they will need to procure additional renewable capacity, and how procuring additional renewables could result in cost savings.
                    Click through the tabs below to input data for your utility. More details about each input can be found by hovering your mouse over the circled question-mark symbols.
                    """.replace('  ', ''),
                    className='twelve columns',
            ),
        ]),
    ]),


])

