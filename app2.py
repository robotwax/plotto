# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_dangerously_set_inner_html
import os
import json
import numpy as np
import bcrypt
import base64


external_stylesheets = ['/assets/code.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config['suppress_callback_exceptions'] = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

server = app.server

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
    <head>
    <meta charset="utf-8">

    <title>Plotto: Predict Lotto Ireland: PayZone</title>
        {%favicon%}
        {%css%}

    </head>
    <body background="/assets/plotto-bg3.png">
        {%app_entry%}
    <footer>
        {%config%}
        {%scripts%}
        {%renderer%}
    </footer>
    </body>
</html>
'''

gs = '''<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="DM5U9PZVPAT5S">
<table>
<tr><td><input type="hidden" name="on0" value="One Time Payment">One Time Payment</td></tr><tr><td><select name="os0">
	<option value="Price">Price €4.50 EUR</option>
</select> </td></tr>
</table>
<input type="hidden" name="currency_code" value="EUR">
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynowCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>
'''

app.layout = html.Div([
    html.Div([
    html.Br(),
    html.H1('Predict Lotto Ireland', style={ 'font-size': 100,  'margin-top': 15}, 
      className = "nine columns"),
    html.Img( src="/assets/lotto.png", className = 'three columns', style={'width': '15%', 'float': 'right', 'margin-right': 5,  'margin-top': -15}),
    ], className = "row"),
    html.Hr(),
    html.Br(),
    html.Br(),
    html.Div([
        html. Textarea('''Legend has it, that there is patterns in the numbers of Irish Lottery draws. The 'Plotto' App intends to exploit those patterns using computer science, a range of analytical tools, and a Dash of magic. And all for less than the price of a lottery ticket. This app helps to take the drudgery and indecision out of choosing lottery numbers and provides a statistically greater chance of winning than your average ‘quick pick’.
        
        **Play Lotto & Play to Win.**''',  className= "four columns offset-by-one", readOnly=True, style={'resize': 'none', 'height': 220}),
        html.Div(className="two columns"),
        html.Div(dash_dangerously_set_inner_html.DangerouslySetInnerHTML(gs), className="three columns offset-by-three", style={'margin-top': 100}),
    ], className = "row"),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
              html.Br(),
              html.Br(),
              html.Footer(
                    html.Center('Cataphysical Research Society - 2019.' ),
              ),
              html.Br(),
    ], className = "row"),
])

if __name__ == '__main__':
    app.run_server(debug=True)
