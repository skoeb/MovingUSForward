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
                'moving US forward',
                style={'font-family': 'Helvetica',
                    "margin-top": "0",
                    "margin-bottom": "0",
                    'fontWeight':'700',
                    'fontSize':'105px',
                    'width':'60%',
                    'marginLeft':'15%'},
            ),
            html.H4(
                "How increased access to drivers licenses under SB13-251 has improved the lives of Colorado's immigrant community.",
                style={'font-family': 'Helvetica',
                    'position':'left',
                    'width':'100%',
                    # 'marginTop':'30%',
                    'marginLeft':'15%'
                },
            )
        ],
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
            )], href='https://coloradomigrahack.school.blog'
        ),
        html.Div([
            html.Img(
                src='assets/MainLogo_NoWords.png',
                className='twelve columns')],
            className = 'twelve columns',
            style={'marginLeft':'auto','marginRght':'auto'}
        ),
    ],
 
    className='row',
    style={
        'marginLeft':'auto',
        'marginRight':'auto',
        'height':'100vh',
        # 'backgroundColor':'#D3C9BD'
        }
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
        style={'marginLeft':'auto','marginRght':'auto'}
        ),

        # Text
        html.Div([
            dcc.Markdown("""
                    In 1999, Colorado law changed to bar some members of the immigrant community from obtaining a driver’s license. 
                    Then in 2006, the Colorado State General assembly approved SB90, which required police officers to report to Immigration
                    and Customs Enforcement (ICE) anyone arrested for a criminal offense that they *“reasonably believed”* might be in the U.S. 
                    without authorization.

                    A 2012 report by the Colorado Fiscal Institute found that Colorado spent $13 million per year to implement the so-called 
                    “Show Me Your Papers” law. The money was spent primarily on the detention of immigrants for committing traffic or other minor offenses.

                    """.replace('  ', ''),
                    className='eight columns offset-by-two'
            ),
        ]),
    ]),
    # Spacer
    html.Div([
        html.Img(
            src='assets/spacer.png',
            className='twelve columns')
    ],
    className = 'twelve columns',
    style={'marginLeft':'auto','marginRight':'auto'}
    ),

    # -------------------------------------------------------
    # -------------------- Section 1 ------------------------
    # -------------------------------------------------------
    html.Div([ 
        # html.Img(
        #     src="assets/denvermap.png",
        #     className='twelve columns',
        # )   
        html.Iframe(src="https://docs.google.com/presentation/d/e/2PACX-1vS2Ds7ZaV9USOQlklmCMLy2lzg6JPTaGfoiU_bruDkWzbg9XEepAEWEz8bYPhtgD5O_NFVQUKaoinZK/embed?start=false&loop=false&delayms=3000", style=dict(border=0), width="100%", height="800")
        # html.Iframe("""<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vS2Ds7ZaV9USOQlklmCMLy2lzg6JPTaGfoiU_bruDkWzbg9XEepAEWEz8bYPhtgD5O_NFVQUKaoinZK/embed?start=false&loop=false&delayms=3000" frameborder="0" width="auto" height="800" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>""")
    ]),


    html.Div([
        html.Img(
            src='assets/spacer.png',
            className='twelve columns')
        ],
        className = 'twelve columns',
        style={'marginLeft':'auto','marginRight':'auto'}
    ),
    html.Div([    
        # Text
        html.Div([
            dcc.Markdown("""

                    Is racial profiling present in our society? That is a question we asked 13 DU students. Most of them holding white identities. All of the students told us they believe that it is prevalent, 
                    however they have never thought about it. 

                    When we asked the students if they ever feared the reason of them being pulled over was because of the color of their skin, they all answered with “no” and “I’ve never thought about that, but no.” 
                    (Click the DU icon on the interactive map for a video of students’ responses).

                    After analyzing the data, we found that the four most white and the four most hispanic neighborhoods in Denver experience high disparity among police stops. 
                    The majority hispanic neighborhoods experience stops up to 4x the amount of their population, whereas the number of most white neighborhood stops 
                    reflect about half of the size of their population.

                    """.replace('  ', ''),
                    className='eight columns offset-by-two'
            ),
        ]),

        html.Div([
            html.Img(src='assets/neighborhood_percents.png'),
        ],
        className='eight columns offset-by-two',
        ),
    ]),
    # -------------------------------------------------------
    # ---------------------- Section 3 ----------------------
    # -------------------------------------------------------
    # Spacer
    html.Div([
        html.Img(
            src='assets/spacer.png',
            className='twelve columns')
        ],
        className = 'twelve columns',
        style={'margin-left':'auto','margin-right':'auto'}
    ),
    html.Div([    
        # Photo
        html.Div([
            html.Img(
                src="assets/janet.JPG",
                className='twelve columns',
            )],
            className='three columns',
            style={'marginTop':0}
        ),

        # Text
        html.Div([
            html.H3(
                '"Having a license does help you emotionally. I feel safer. And my children feel safer; they’re no longer scared."',
                style={"font-style":"italic"}
            ),
            html.H6(
                '-Jeanette Vizguerra,',
            ),
            html.H6(
                'driver\'s license recipient',
            )],
            className='nine columns'
        )],
        className = 'twelve columns',
        style={'marginTop':20},
    ),
    html.Div([    
        # Text
        html.Div([
            html.H3(
                '“I was involved in two car accidents that weren’t my fault. Luckily I had my license both times. I don’t want to even think about what would’ve happened if I didn’t have it.”',
                style={"font-style":"italic","text-align":"right"}
            ),
            html.H6(
                '-Pilar Carrillo,',
                style={"text-align":"right"}
            ),
            html.H6(
                'driver\'s license recipient',
                style={"textAlign":"right"}
            )],
            className='nine columns'
        ),
        # Photo
        html.Div([
            html.Img(
                src="assets/pilar1.jpg",
                className='twelve columns',
            )],
            className='three columns',
            style={'margin-top':0}
        )],
        className = 'twelve columns',
        style={'margin-top':20},
    ),
    html.Div([    
        # Photo
        html.Div([
            html.Img(
                src="assets/jose.jpg",
                className='twelve columns',
            )],
            className='three columns',
            style={'margin-top':0}
        ),

        # Text
        html.Div([
            html.H3(
                '"Many people have told me that now that they have a driver\'s license they have been able to buy a car, \
                take their children to the park; they no longer have to take them to school by foot under really cold weather conditions."',
                style={"font-style":"italic"}
            ),
            html.H6(
                '-José Ortiz,',
            ),
            html.H6(
                'activist',
            )],
            className='nine columns'
        )],
        className = 'twelve columns',
        style={'margin-top':20},
    ),
    # -------------------------------------------------------
    # ---------------------- Section pris 2nd part ----------------------
    # -------------------------------------------------------
    # Spacer
    html.Div([
        html.Img(
            src='assets/spacer.png',
            className='twelve columns')
        ],
        className = 'twelve columns',
        style={'marginLeft':'auto','marginRight':'auto'}
    ),
    html.Div([    
        # Text
        html.Div([
            dcc.Markdown("""

                    Undocumented immigrants were especially vulnerable to the effects of racial profiling. 

                    “[A traffic stop] perhaps meant getting a $150 ticket or going to court where unfortunately in some cases you would find immigration right outside,” 
                    said Jeanette Vizguerra, an activist who is currently seeking sanctuary in the First Unitarian Society of Denver Church to avoid being deported. 

                    In 2013, Colorado approved SB-251 or the Colorado Road and Community Safety Act, to increase access to driver’s licenses. By August of 2014, 
                    five Department of Motor Vehicle offices were implementing the program and offering 31 appointments per day, according to the I Drive Colorado campaign. 
                    The legislature later cut the program’s budget and the number of DMV offices participating in the program dropped to three.

                    Starting Jan. 1, 2019, The Eligibility Colorado Road And Community Safety Act extended the program by accepting Social Security Numbers to obtain 
                    the SB-251 driver’s licenses and by allowing SB-251 driver’s license renewal online.

                    Since its start, the SB-251 program has provided driver’s licenses, instruction permits, and identification cards to nearly 45,000 immigrants in Colorado.
                    
                    """.replace('  ', ''),
                    className='eight columns offset-by-two'
            ),
        ]),
    ]),
])

