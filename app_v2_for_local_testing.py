"""
Dashboard main file
"""

from dash import Dash, dcc, html, Input, Output
import time
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import json


fleet_app_open = True





    
#---------- initialize fleet app
if fleet_app_open:
    from fleet_app_tab_for_local_testing import get_fleet_management_layout, register_fleet_management_callbacks  
    
#-------------- end


# Initialize the Dash app
## Adding meta labels to improve searchability via a search engine. 
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "description", "content": "IMAGINED Dashboard for Intermodal Analytics for Logistics Network Efficiency."},
        {"name": "keywords", "content": "IMAGINED, logistics, dashboard, ARPA-E, intermodal analytics, northwestern university"},
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ]
)

app.title = "IMAGINED Dashboard (Fleet Management component only)"
app._favicon = "favicon.ico"




#################################################

#register_fleet_management_callbacks(app)



app.layout = html.Div([

    html.Div([
        # Left Logo
        html.Img(src=app.get_asset_url("ARPA-E Subbrand_Awardee Logo-Light.png"),
                 style={"width": "250px", "height": "auto", "marginRight": "20px"}),

        # Title and Subtitle Container
        html.Div([
            html.H1("IMAGINED Dashboard (Beta - Fleet Management Component Only)", style={"margin": "0", "textAlign": "center"}),
            html.H2("Inter Modal Analytics for Logistics Network Efficiency",
                    style={"margin": "0", "fontSize": "18px", "color": "gray", "textAlign": "center"})
        ], style={"flex": "1", "textAlign": "center"}),  # Centers the text while allowing flex behavior

        # Right Logo (Duplicate of Left Logo)
        html.Img(src=app.get_asset_url("ARPA-E Subbrand_Awardee Logo-Light.png"),
                 style={"width": "250px", "height": "auto", "marginLeft": "20px"})
    ], style={"display": "flex", "alignItems": "center", "justifyContent": "space-between",
              "padding": "10px 20px", "width": "100%"}),

    # Tabs Section
    dcc.Tabs([
        
        dcc.Tab(label="Fleet Management", children=get_fleet_management_layout(app)),
        
    ])
], style={'fontFamily': 'Arial, Helvetica, sans-serif'})





register_fleet_management_callbacks(app)

if __name__ == "__main__":
    app.run_server( port=8052, debug=False)