# -*- coding: utf-8 -*-
import flask
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame
import numpy as np
import numpy as nd
import numpy.ma as ma
import plotly.plotly as py
from plotly.graph_objs import *
import  plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import datetime
import json
import ast
import os
import plotly.io as pio
from PIL import Image, ImageFile
import base64
import random
import bcrypt
import time

pio.orca.config.executable = '/Users/Koala/.npm/bin/orca'

external_stylesheets = ['/assets/code.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

_app_route = '/dash-core-components/logout_button'

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()

    # Adds new node containing 'data' to the end of the linked list.
    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        with open('ash.txt', 'w') as outfile:
            return json.dump(elems, outfile)

    # Returns the length (integer) of the linked list.
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total         

    # Returns the value of the node at 'index'. 
    def get(self,index):
        if index>=self.length() or index<0: # added 'index<0' post-video
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index: return cur_node.data
            cur_idx+=1

d = datetime.datetime.now()
f = []
f.append(d)
f = str(f)
g = f.replace('[datetime.datetime(', '')
k = g[:4]
m = int(k)
bk3 = []
for i in range(1993, m+1):
    bk3.append(i)
with open('bk2.txt', 'w') as outfile:
    json.dump(bk3, outfile)
    
def signed():
    td = datetime.datetime.now()
    td = str(td)
    cleantd = td.replace('[datetime.datetime(', '')
    sign= bcrypt.hashpw(cleantd.encode('utf-8'), bcrypt.gensalt()) 
    encoded = base64.b64encode(sign)
    s1 = encoded.decode('ascii')
    s2 = s1[74:]
    s3 = s1[67:74]
    s4 = s1[60:67]
    s5 = s1[54:60]
    s6 = s1[47:54]
    s7 = s1[40:47]
    s8 = s1[34:40]
    s9 = s1[27:34]
    s10 = s1[20:27]
    s11 = s1[14:20]
    s12 = s1[64:70]
    with open('keys.txt') as inFile:
        try: 
             tet = json.load(inFile)
        except ValueError: 
             tet = []
    tet.append( '{}.txt'.format(s2))
    tet.append('{}.txt'.format(s3))
    tet.append('{}.txt'.format(s4))
    tet.append('{}.txt'.format(s5))
    tet.append('{}.txt'.format(s6))
    tet.append('{}.txt'.format(s7))
    tet.append('{}.txt'.format(s8))
    tet.append('{}.txt'.format(s9))
    tet.append('{}.txt'.format(s10))
    tet.append('{}.txt'.format(s11))
    tet.append('{}.txt'.format(s12))
    with open('keys.txt', 'w') as outfile:
        tet = json.dump(tet, outfile)
    return(s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12)



ftd = signed()
(s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12) = ftd

def rem():
    skies =  '{}.txt'.format(s7)
    fire =  '{}.txt'.format(s8)
    rains =  '{}.txt'.format(s10)
    air = '{}.txt'.format(s2)
    earth = '{}.txt'.format(s6)
    water =  '{}.txt'.format(s11)
    clicks11 = '{}.txt'.format(s4)
    clicks22 = '{}.txt'.format(s5)
    wind = '{}.txt'.format(s9)
    outseg = '{}.txt'.format(s3)
    indexd = [skies, fire, rains, air, earth, water, clicks11, clicks22, wind, outseg]
    if os.path.exists(air):
        os.remove(air)
    if os.path.exists(skies):
        os.remove(skies)
    if os.path.exists(fire):
        os.remove(fire)
    if os.path.exists(rains):
        os.remove(rains)
    if os.path.exists(earth):
        os.remove(earth)
    if os.path.exists(water):
        os.remove(water)
    if os.path.exists(clicks11):
        os.remove(clicks11)
    if os.path.exists(clicks22):
        os.remove(clicks22)
    if os.path.exists(wind):
        os.remove(wind)
    if os.path.exists(outseg):
        os.remove(clicks22)
    with open('keys.txt') as json_file:
        tet = json.load(json_file)
    for c in indexd:
        try:
            kkg = tet.index(c)
            del tet[kkg]
            with open('keys.txt', 'w') as outfile:
                 return json.dump(tet, outfile)
        except ValueError:
            return 'all files deleted'

def imagerem():
    gyh=[]
    for i in range(1, 47):
        x = 'images/base' + str(bk3[-1]) + '-' + str(i) + '.png'
        gyh.append(x)
        for j in gyh:
            if os.path.exists(j):
                os.remove(j)
    return 'Images deleted'

def keyrem():
    with open('keys.txt') as json_file:
        tet = json.load(json_file)
    for i in tet:
        DAYS = 2
        removed = 0
        time_in_secs = 39
        if os.path.exists(i):
            try:
                oldest_file = min(i, key=os.path.getctime)
            except FileNotFoundError:
                return 'key removed'
            if oldest_file <= time_in_secs:
                os.remove(oldest_file)
            kkg = tet.index(oldest_file)
            del tet[kkg]
            with open('keys.txt', 'w') as outfile:
                 json.dump(tet, outfile)
            removed += 1
    return 'key removed'

# Create a login route
@app.server.route('/custom-auth/login', methods=['POST'])
def route_login():
    data = flask.request.form
    dtime = datetime.datetime.now()
    dtime = str(dtime)
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        flask.abort(401)

    # Return a redirect with
    rep = flask.redirect(_app_route)

    # Here we just store the given username in a cookie.
    # Actual session cookies should be signed or use a JWT token.
    rep = flask.redirect(_app_route)
    rep.set_cookie('custom-auth-session', '', expires=0)
    return rep

# create a logout route
@app.server.route('/custom-auth/logout', methods=['POST'])
def route_logout():
    # Redirect back to the index and remove the session cookie.
    rep = flask.redirect(_app_route)
    rep.set_cookie('custom-auth-session', '', expires=0)
    return rep



app.config['suppress_callback_exceptions'] = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
ImageFile.LOAD_TRUNCATED_IMAGES = True

server = app.server

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
    <head>
    <meta charset="utf-8">

    <title>Plotto: Predict Lotto Ireland</title>
        {%favicon%}
        {%css%}

    </head>
    <body>
        {%app_entry%}
    <footer>
        {%config%}
        {%scripts%}
        {%renderer%}
    </footer>
    </body>
</html>
'''

login_form = html.Div([
    html.Form([
        dcc.Input(id='user', placeholder='  username', name='username', style={'height': 32, 'border': '1px solid black', 'resize': 'none',  'font-size': 'inherit'}),
        dcc.Input(id='pw', placeholder='password', name='password', type='password', style={'margin-left': 25}),
        html.Button('Login', type='submit',  style={'margin-left': 25})
    ], action='/custom-auth/login', method='post')
])

def changeImageSize(maxWidth, 
    maxHeight, 
    image):

    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage

i = bk3[22]
j = bk3[-1]

i1=bk3[0]

app.layout = html.Div([
    html.Div([
    dcc.Store(id='memory'),
    html.Br(),
    html.H1('Predict Lotto Ireland', style={ 'font-size': 100,  'margin-top': 15}, 
      className = "nine columns"),
    html.Img( src="/assets/lotto.png", className = 'three columns', style={'width': '15%', 'float': 'right', 'margin-right': 5, 'z-index': 1, 'margin-top': -15}),
    ], className = "row"),
    html.Hr(),
    html.Div([
        html.H3('Log In', className="six columns offset-by-one", style={'margin-top': 0}), 
        html.Div(id='custom-auth-frame', style={'float': 'right'}),
    ], className = "row"),
    html.Hr(),
    html.Div([
        html.H3('Plotto Results Visualiser', className="eleven columns offset-by-one"), 
    ], className = "row"),
    html.Div([
        html.P('This graph lets you see all of the Irish Lotto results from the year 1993 to present. Use the slider to select the range and then rotate the graph to gain different perspectives on the information. The earliest year of the slider below is used in calculating the graphs further down.', className="ten columns offset-by-one"),
    ], className = "row"),
    html.Div([
        dcc.Graph(id='lotto', style={'height': '60vh'}),
    ], className = "row"),
    html.Br(),
    html.Div([
        dcc.RangeSlider(
        marks={i: '{}'.format(i) for i in bk3},
        min=i1,
        max=j,
        value=[i, j],
        id='slider',
        allowCross=False,
        className = 'ten columns offset-by-one')
    ], className='row'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(),
    html.Div([
        html.H3('Plotto Predict', className="eleven columns offset-by-one"), 
    ], className = "row"),
    html.Div([
        html.P('This app helps to take the drudgery and indecision out of choosing lottery numbers and provides a statistically greater chance of winning than your average ‘quick pick’. Push the \'Predict\' button to increase your chances of winning the Lotto.', className="ten columns offset-by-one"),
    ], className = "row"),
    html.Br(),
    html.Div([              
        dcc.Textarea(id='ball1', readOnly = True, rows=2, style={'width': '33.3333%',  'height': 50, 'padding-bottom': 6, 'border-radius': 1, 'resize': 'none',  'font-size': 30, 'font-family': 'inherit', 'text-align': 'center'},
        className="one column offset-by-four"),
    ], className="row"),
    html.Br(),
    html.Div([
    html.Button(id='submit-button', n_clicks=0, children='Predict', className="two columns offset-by-eight"),
    ], className="row"),
    html.Div(id='intermediate-value', style={'display': 'none'}),
    html.Div(id='intermediate-water', style={'display': 'none'}),
    html.Div(id='intermediate-lotto2', style={'display': 'none'}),
    html.Div(id='intermediate-auth', style={'display': 'none'}),
    html.Hr(),
    html.Div([
        html.H3('Statistical Analysis', className="eleven columns offset-by-one"), 
    ], className = "row"),
    html.Div([
        html.P('These two graphs return statistics based off of results from both the upper and lower graphs. The graph on the right shows the distribution of results, for a single initial (or base-ball) for that entire year. The same search determine the results of the graph on the left. This graph shows the percentages of numbers, for each of the six balls drawn in order. These are arranged on a per ball basis and are determined by the slider in the lower graph. So, if the slider in the lower graph is set to \'2\', the first ball will read \'100%\', because all of the first balls are \'2\'. Each of the other balls will display different numbers, which are the results that all share the first ball in common.', className="ten columns offset-by-one"),
    ], className = "row"),
    html.Br(),
    html.Div([
        dcc.Graph(id='lotto3', style={'height': '60vh'},
        className="six columns"),
        html.Img(id='lotto2', style={'height': '60vh', 'margin-left': 14, 'margin-top': 14}, className="six columns"),
        dcc.RadioItems(id = 'radio',
            options=[
                {'label': '1', 'value': '1'},
                {'label': '2', 'value': '2'},
                {'label': '3', 'value': '3'},
                {'label': '4', 'value': '4'},
                {'label': '5', 'value': '5'},
                {'label': '6', 'value': '6'},
            ],
            value='2',
            labelStyle={'display': 'inline-block', 'margin-left': 35,  'margin-top': -50},
        className="five columns offset-by-one"),
    ], className="row"),
    html.Hr(),
    html.Div([
        html.H3('Lowest Base Result', className="eleven columns offset-by-one"), 
    ], className = "row"),
    html.Div([
        html.P('The slider on this graph allows you to determine the lowest number result of the Lottery result. If the slider is set to \'1\', all of the lottery results that have \'1\' as their lowest number will be displayed.', className="ten columns offset-by-one"),
    ], className = "row"),
    html.Br(),
    html.Div([
        html.Div(
        dcc.Graph(id='lotto4', style={'height': '60vh'})),
    ], className='row'),
        html.Div([
        dcc.Slider(
        marks={i: '{}'.format(i) for i in range(1, 43)},
        min=1,
        max=42,
        id='slider2',
        value=1,
        className = 'ten columns offset-by-one')
    ], className='row'),
    html.Br(),
    html.Div(id='intermediate-value2', style={'display': 'none'}),
    html.Div(id='inter-zone', style={'display': 'none'}),
    html.Div(id='inter-ball', style={'display': 'none'}),
    html.Div(id='inter-ball2', style={'display': 'none'}),
    html.Div(id='inter-user', style={'display': 'none'}),
    html.Div(id='inter-med1', style={'display': 'none'}),
    html.Br(),
    html.Hr(),
    html.Div([
        html.H3('Plotto Lowest Result Predict', className="eleven columns offset-by-one"), 
    ], className = "row"),
    html.Div([
        html.P('Push the \'Predict\' button to calculate based on the lowest order result.', className="ten columns offset-by-one"),
    ], className = "row"),
    html.Br(),
    html.Div([              
        dcc.Textarea(id='ball2', readOnly = True, rows=2, style={'width': '33.3333%',  'height': 50, 'padding-bottom': 6, 'border-radius': 1, 'resize': 'none',  'font-size': 30, 'font-family': 'inherit', 'text-align': 'center'},
        className="one column offset-by-four"),
    ], className="row"),
    html.Br(),
    html.Div([
    html.Button(id='submit-button2', n_clicks=0, children='Predict', className="two columns offset-by-eight"),
    ], className="row"),
    html.Hr(),
    html.Div([
        html.H3('Stochastic Analysis', className="eleven columns offset-by-one"), 
    ], className = "row"),
    html.Div([
        html.P('This aspect of Predict Lotto attempts to do the impossible i.e. use Machine Learning to predict random numbers.', className="ten columns offset-by-one"),
    ], className = "row"),
    html.Br(),
    html.Div([
        html.Div(
        dcc.Graph(id='lotto5', style={'height': '70vh'}, className="ten columns offset-by-one")),
    ], className='row'),
    html.Div([
        html.H3('Stochastic Predict', className="eleven columns offset-by-one"), 
    ], className = "row"),
    html.Div([
        html.P('This function attempts to predict the range of numbers that the next draw will appear in, using Machine Learning methods. This section is still under development', className="ten columns offset-by-one"),
    ], className = "row"),
    html.Br(),
    html.Div([              
        dcc.Textarea(id='ball3', readOnly = True, rows=2, style={'width': '33.3333%',  'height': 50, 'padding-bottom': 6, 'border-radius': 1, 'resize': 'none',  'font-size': 30, 'font-family': 'inherit', 'text-align': 'center'},
        className="one column offset-by-four"),
    ], className="row"),
    html.Br(),
    html.Div([
    html.Button(id='submit-button3', n_clicks=0, children='Predict', className="two columns offset-by-eight"),
    ], className="row"),
    html.Hr(),
    html.Br(),
    html.Div([
        html.H3('Result History and Statistics', className="eleven columns offset-by-one"), 
    ], className = "row"),
    html.Div([
        html.Div(id='table-container', className= "five columns offset-by-one", style={'margin-top': 20}),
    ], className='row'),
    html.Div(id='intermediate-delog', style={'display': 'none'}),
    html.Div(id='intermediate-delog2', style={'display': 'none'}),
    dcc.ConfirmDialog(
        id='confirm',
        message='Your session has timed out. Reload to continue using Plotto Predict',
    ),
    html.Br(),
    html.Div([
              html.Br(),
              html.Hr(id='footer'),
              html.Br(),
              html.Footer(
                    html.Center('Cataphysical Research Society - 2019.' ),
              ),
              html.Br(),
    ], className = "row"),
])


@app.callback(Output('intermediate-auth', 'children'),
              [Input('custom-auth-frame', 'id')])
def dynamic_layout(_):
    session_cookie = flask.request.cookies.get('custom-auth-session')
    print(session_cookie)
    if session_cookie == None:
        return login_form

@app.callback(Output('custom-auth-frame', 'children'),
              [Input('intermediate-auth', 'children')])
def dynamic_layout2(_):
    session_cookie = flask.request.cookies.get('custom-auth-session')
    if not session_cookie:
        # If there's no cookie we need to login.
        return login_form
    return html.Div([
        html.Div('Hello {}'.format(session_cookie)), dcc.LogoutButton(logout_url='/custom-auth/logout')
    ], className="row")


@app.callback(Output('intermediate-value', 'children'), [Input('slider', 'value')])
def update_graph(value):
    skies =  '{}.txt'.format(s7)
    fire =  '{}.txt'.format(s8)
    rains =  '{}.txt'.format(s10)
    with open('bk2.txt') as json_file:
        bk3 = json.load(json_file)
    kx = value[0]
    ky = value[1]
    lendfi = []
    gg=[]
    sky = []
    if kx == bk3[22] and ky == bk3[-1]:
        i = bk3[22]
        j = bk3[-1]
        newlist1 = []
        bx = []
        for x in range(i, j):
            bx.append(x)
        bz = []
        i = 0
        for i in bx:
            while len(bz) <= len(bx)-1:
                gb = "https://www.irishlottery.com/archive-"
                kz = gb + str(i)
                bz.append(kz)
                i += 1
        for c in bz:
            url = c
            print(url)
            html = urlopen(url)
        
            soup = BeautifulSoup(html, 'lxml')
        
            # Get the title
            table = soup.findAll('table')[0] 
            df = pd.read_html(str(table))
            df= (df[0].to_json(orient='split'))
            df = pd.read_json(df, orient='split')
            lendf = (len(df))
            i = 1
            while i <= lendf-1:
                df1 = df.loc[[i], 'Draw Result:'].tolist()
                clean = str(df1)
                clean = clean.replace("\'", "")
                clean = clean.replace(" ", ", ")
                clean = clean.replace("list(", "")
                clean = clean.replace(")", "")
                newlist = 'clean = ' + clean
                exec(newlist)
                newlist1.append(clean)
                i += 1
        sky = str(newlist1)
        sky = sky.replace("\'[\'[", "[[")
        sky = sky.replace("]\']\'", "]]")
        sky = sky.replace("\'[", "[")
        sky = sky.replace("]\'", "]")
        newlist1 = ast.literal_eval(sky)
        sky = newlist1[:]
        kivy = len(sky)
        with open('sky1.txt') as json_file:
            sky1 = json.load(json_file)
        kivy2 = len(sky1)
        if kivy != kivy2:
            with open('sky1.txt', 'w') as outfile:
                json.dump(sky, outfile)
            with open('sky.txt', 'w') as outfile:
                return json.dump(sky, outfile)
        else:
            with open('sky.txt', 'w') as outfile:
                return json.dump(sky, outfile) 
    elif kx == ky:
        gb = "https://www.irishlottery.com/archive-"
        kz = gb + str(kx)
        url = kz
        print(url)
        html = urlopen(url)

        soup = BeautifulSoup(html, 'lxml')

        # Get the title
        table = soup.findAll('table')[0] 
        df = pd.read_html(str(table))
        df= (df[0].to_json(orient='split'))

        df = pd.read_json(df, orient='split')
        lendf = len(df)
        gg.append(lendf)
        i = 1
        while i <= lendf -1:
            df1 = df.loc[[i], 'Draw Result:'].tolist()
            clean = str(df1)
            clean = clean.replace("\'", "")
            clean = clean.replace(" ", ", ")
            clean = clean.replace("list(", "")
            clean = clean.replace(")", "")
            newlist = 'clean = ' + clean
            exec(newlist)
            sky.append(clean)
            i += 1
    else:
        bx = []
        for i in range(kx, (ky+1)):
            bx.append(i)
        bz = []
        i = 0
        for i in bx:
            while len(bz) <= len(bx)-1:
                gb = "https://www.irishlottery.com/archive-"
                kz = gb + str(i)
                bz.append(kz)
                i += 1
        for c in bz:
            url = c
            print(url)
            html = urlopen(url)
    
            soup = BeautifulSoup(html, 'lxml')
    
            # Get the title
            table = soup.findAll('table')[0] 
            df = pd.read_html(str(table))
            df= (df[0].to_json(orient='split'))
            df = pd.read_json(df, orient='split')
            lendf = (len(df))
            gg.append(lendf)
            i = 1
            while i <= lendf-1:
                df1 = df.loc[[i], 'Draw Result:'].tolist()
                clean = str(df1)
                clean = clean.replace("\'", "")
                clean = clean.replace(" ", ", ")
                clean = clean.replace("list(", "")
                clean = clean.replace(")", "")
                newlist = 'clean = ' + clean
                exec(newlist)
                sky.append(clean)
                i += 1
    with open('rain.txt', 'w') as outfile:
        json.dump(gg, outfile)
    sky = str(sky)
    sky = sky.replace("\'[\'[", "[[")
    sky = sky.replace("]\']\'", "]]")
    sky = sky.replace("\'[", "[")
    sky = sky.replace("]\'", "]")
    sky = ast.literal_eval(sky)
    sky=sky[:]
    with open('sky.txt', 'w') as outfile:
        return json.dump(sky, outfile)

@app.callback(Output('intermediate-water', 'children'),
    [Input('intermediate-value', 'children'),
    Input('slider', 'value')])
def make_graph1(intermediatevalue, slider):
    water = '{}.txt'.format(s11)
    kx = slider[0]
    ky = slider[1]
    d = datetime.datetime.now()
    f = []
    f.append(d)
    f = str(f)
    g = f.replace('[datetime.datetime(', '')
    k = g[:4]
    m = int(k)
    ze = list(range(kx, ky+1))
    ze0 = np.arange(1993, 1994)
    ze1 = np.arange(1994, 2006)
    ze2 = np.arange(2006, 2015)
    ze3 = np.arange(2015, m+1)
    ze = np.array(ze)
    df = []
    for i in ze0:
        el = [ze == i]
        xc = np.any(el)
        if xc:
            df.append(39)
    for i in ze1:
        el = [ze == i]
        xc = np.any(el)
        if xc:
            df.append(42)
    for i in ze2:
        el = [ze == i]
        xc = np.any(el)
        if xc:
            df.append(45)
    for i in ze3:
        el = [ze == i]
        xc = np.any(el)
        if xc:
            df.append(47)
    topg = (max(df))
    with open('water.txt', 'w') as outfile:
        return json.dump(topg, outfile)
    
@app.callback(Output('lotto', 'figure'),
    [Input('intermediate-value', 'children'),
    Input('intermediate-water', 'children'),
    Input('slider', 'value')])
def make_graph3(intermediatevalue, intermediatewater, value):
    skies =  '{}.txt'.format(s7)
    water =  '{}.txt'.format(s11)
    with open('bk2.txt') as json_file:
        bk3 = json.load(json_file)
    kx = value[0]
    ky = value[1]
    if kx == bk3[22] and ky == bk3[-1]:
        with open('sky1.txt', 'r') as json_file:
            sky1 = json.load(json_file)
        sky1 = sky1[::-1]
        trace1 = dict(
            type="surface",
            z=sky1,
            hoverinfo='z',
            lighting={
                "ambient": 0.80,
                "diffuse": 0.80,
                "fresnel": 4,
                "roughness": 50,
                "specular": 3,
            },
            autocolorscale= False, 
            cauto= False, 
            cmax= 47, 
            colorscale= [
                [0, "#313131"], [0.0625, "#3d019d"], [0.125, "#3810dc"], [0.1875, "#2d47f9"], [0.25, "#2593ff"], [0.3125, "#2adef6"], [0.375, "#60fdfa"], [0.4375, "#aefdff"], [0.5, "#f3f3f1"], [0.5625, "#fffda9"], [0.625, "#fafd5b"], [0.6875, "#f7da29"], [0.75, "#ff8e25"], [0.8125, "#f8432d"], [0.875, "#d90d39"], [0.9375, "#97023d"], [1, "#313131"]], 
            showscale=True,
            scene="scene",
            colorbar= {
                "x": 1.1, 
                "y": 0.43999999999999995, 
                "lenmode": "fraction", 
                "thickness": 31, 
                "thicknessmode": "pixels", 
                "xanchor": "right"
              }, 
        )
        data = [trace1]
        layout = dict(
            autosize=True,
            font=dict(
                size=12,
                color="#CCCCCC",
            ),
            margin=dict(
                t=5,
                l=50,
                b=50,
                r=5,
            ),
            hovermode='closest',
            scene=dict(
                aspectmode="manual",
                aspectratio=dict(x=2, y=5, z=1.5),
                camera=dict(eye=dict(x=-3.4, y=0, z=0)), center=dict(x=0, y=0, z=0), up=dict(x=0, y=0, z=1)),
                xaxis={
                    "showgrid": True,
                    "title": "",
                    "type": "category",
                    "zeroline": False,
                    "categoryorder": 'array',
                    "categoryarray": list(reversed(g))
                },
                yaxis={
                    "showgrid": True,
                    "title": "",
                    "type": "date",
                    "zeroline": False,
                },
            )
        
        figure = dict(data=data, layout=layout)
        # py.iplot(figure)
        return figure
    else:
        with open('sky.txt', 'r') as json_file:
            sky = json.load(json_file)
        with open('water.txt', 'r') as json_file:
            topg = json.load(json_file)
        sky = sky[::-1]
        trace1 = dict(
            type="surface",
            z=sky,
            hoverinfo='z',
            lighting={
                "ambient": 0.80,
                "diffuse": 0.80,
                "fresnel": 4,
                "roughness": 50,
                "specular": 3,
            },
            autocolorscale= False, 
            cauto= False, 
            cmax= topg, 
            colorscale= [
                [0, "#313131"], [0.0625, "#3d019d"], [0.125, "#3810dc"], [0.1875, "#2d47f9"], [0.25, "#2593ff"], [0.3125, "#2adef6"], [0.375, "#60fdfa"], [0.4375, "#aefdff"], [0.5, "#f3f3f1"], [0.5625, "#fffda9"], [0.625, "#fafd5b"], [0.6875, "#f7da29"], [0.75, "#ff8e25"], [0.8125, "#f8432d"], [0.875, "#d90d39"], [0.9375, "#97023d"], [1, "#313131"]], 
            showscale=True,
            scene="scene",
            colorbar= {
                "x": 1.1, 
                "y": 0.43999999999999995, 
                "lenmode": "fraction", 
                "thickness": 31, 
                "thicknessmode": "pixels", 
                "xanchor": "right"
              }, 
        )
        data = [trace1]
        layout = dict(
            autosize=True,
            font=dict(
                size=12,
                color="#CCCCCC",
            ),
            margin=dict(
                t=5,
                l=50,
                b=50,
                r=5,
            ),
            hovermode='closest',
            scene=dict(
                aspectmode="manual",
                aspectratio=dict(x=2, y=5, z=1.5),
                camera=dict(eye=dict(x=-3.4, y=0, z=0)), center=dict(x=0, y=0, z=0), up=dict(x=0, y=0, z=1)),
                xaxis={
                    "showgrid": True,
                    "title": "",
                    "type": "category",
                    "zeroline": False,
                    "categoryorder": 'array',
                    "categoryarray": list(reversed(g))
                },
                yaxis={
                    "showgrid": True,
                    "title": "",
                    "type": "date",
                    "zeroline": False,
                },
            )
        
        figure = dict(data=data, layout=layout)
        # py.iplot(figure)
        return figure

@app.callback(Output('intermediate-value2', 'children'),
    [Input('intermediate-value', 'children'),
    Input('slider2', 'value'),
    Input('slider', 'value'),
    Input('intermediate-water', 'children')])
def make_graph4(intermediatevalue, value, slider, intermediatewater):
    skies =  '{}.txt'.format(s7)
    fire =  '{}.txt'.format(s8)
    earth = '{}.txt'.format(s6)
    water = '{}.txt'.format(s11)
    with open('bk2.txt') as json_file:
        bk3 = json.load(json_file)
    kx = slider[0]
    ky = slider[1]
    if  kx == bk3[22] and ky == bk3[-1]:
        with open('sky1.txt', 'r') as json_file:
            sky = json.load(json_file)
    else:
        with open('sky.txt') as json_file:
            sky = json.load(json_file)
    with open('water.txt') as json_file:
        g = json.load(json_file)
    sky2 = [val for sublist in sky for val in sublist] 
    ball1 = sky2[::7]
    ball1 = np.array(ball1)
    balls=[]
    for i in range(1, 7):
        ball = sky2[i::7]
        balls.append(ball)
    balls=np.array(balls)
    rollerball=[]
    elimin8 = [ball1 != value]
    mask = np.ma.masked_array(ball1, elimin8)
    roll=[x for x in mask if x is not None]
    roll = roll.count(value)
    clean = [value]*roll
    rollerball.append(clean)
    lenball=[]
    percentball=[]
    for i in balls:
        mask2 = np.ma.masked_array(i, elimin8)
        ball2 = mask2.tolist()
        roll2=[x for x in ball2 if x is not None]
        for j in list(range((value+1), g+1)):
            roll5 = roll2.count(j)
            percentball.append(roll5)
        while len(lenball) < 1:
            roll4=len(roll2)
            lenball.append(roll4)
        rollerball.append(roll2)
    x = lenball[0]
    lenpercentball = g - value
    percentball = np.array(percentball).reshape(lenpercentball, 6)
    percentball = percentball.tolist()
    with open('fire.txt', 'w') as outfile:
        json.dump(percentball, outfile)
    roller = np.concatenate(rollerball, axis=0)
    roller = np.array(roller).reshape(7, x)
    roller = np.rot90(roller, 1)
    roller = np.array(roller).tolist()
    with open('earth.txt', 'w') as outfile:
        return json.dump(roller, outfile)

@app.callback(Output('lotto3', 'figure'),
    [Input('intermediate-value', 'children'),
    Input('slider2', 'value'),
    Input('radio', 'value'),
    Input('slider', 'value'),
    Input('intermediate-water', 'children')])
def make_graph2(intermediatevalue, value, radio, slider, intermediatewater):
    skies =  '{}.txt'.format(s7)
    water = '{}.txt'.format(s11)
    with open('bk2.txt') as json_file:
        bk3 = json.load(json_file)
    kx = slider[0]
    ky = slider[1]
    if kx == bk3[22] and ky == bk3[-1]:
        with open('sky1.txt', 'r') as json_file:
            sky = json.load(json_file)
    else:
        with open('sky.txt') as json_file:
            sky = json.load(json_file)
    with open('water.txt') as json_file:
        g = json.load(json_file)
    sky2 = [val for sublist in sky for val in sublist] 
    ball1 = sky2[::7]
    ball1 = np.array(ball1)
    balls=[]
    for i in range(1, 7):
        ball = sky2[i::7]
        balls.append(ball)
    balls=np.array(balls)
    rollerball=[]
    elimin8 = [ball1 != value]
    mask = np.ma.masked_array(ball1, elimin8)
    roll=[x for x in mask if x is not None]
    roll = roll.count(value)
    clean = [value]*roll
    rollerball.append(clean)
    xk = list(range((value), g+1))
    for i in balls:
        mask2 = np.ma.masked_array(i, elimin8)
        ball2 = mask2.tolist()
        roll2=[x for x in ball2 if x is not None]
        rollerball.append(roll2)
    percentball=[]
    if radio == '1':
        rollerball = rollerball[0]
        for j in xk:
            roll5 = rollerball.count(j)
            percentball.append(roll5)
    elif radio == '2':
        rollerball = rollerball[1]
        for j in xk:
            roll5 = rollerball.count(j)
            percentball.append(roll5)
    elif radio == '3':
        rollerball = rollerball[2]
        for j in xk:
            roll5 = rollerball.count(j)
            percentball.append(roll5)
    elif radio == '4':
        rollerball = rollerball[3]
        for j in xk:
            roll5 = rollerball.count(j)
            percentball.append(roll5)
    elif radio == '5':
        rollerball = rollerball[4]
        for j in xk:
            roll5 = rollerball.count(j)
            percentball.append(roll5)
    else:
        rollerball = rollerball[5]
        for j in xk:
            roll5 = rollerball.count(j)
            percentball.append(roll5)
    data = go.Pie(values= percentball[:],  labels= [i for i in xk]),
    fig = Figure(data=data)
    return fig


@app.callback(Output('lotto2', 'src'),
    [Input('intermediate-value2', 'children'),
    Input('slider2', 'value'),
    Input('slider', 'value')])
def make_graph5(intermediatevalue2, value, slider):
    rains =  '{}.txt'.format(s10)
    water = '{}.txt'.format(s11)
    earth = '{}.txt'.format(s6)
    kx = slider[0]
    with open('earth.txt') as json_file:
        earth = json.load(json_file)
    if not os.path.exists('images'):
        os.mkdir('images')
    with open('water.txt') as json_file:
        cf = json.load(json_file)
    with open('rain.txt', 'r') as json_file:
        rain = json.load(json_file)
    earth = earth[::-1]
    rain = rain[0]
    rain = rain//7
    earth2 = earth[:rain]
    cal = len(earth2)
    earth = np.array(earth2).reshape(cal, 7)
    earth = earth.tolist()
    with open('bk2.txt') as json_file:
        bk3 = json.load(json_file)
    if kx == bk3[22]:
        image_filename = 'images/base2015-' + str(value) + '.png'
        if os.path.exists(image_filename):
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())    
            return 'data:image/png;base64,{}'.format(encoded_image.decode())
        else:    
            ylist = earth[0]
            xlist = iter(range(1, 8))
            xlist = list(xlist)
            data = go.Scatter(
                 x = xlist,
                 y = ylist
            ),
            layout = dict(
                title = "Initial Ball:" + str(value) + "| Year: 2015",
                paper_bgcolor= "#ffffff",
                plot_bgcolor= "rgb(208, 248, 255)",
                autosize=True,
                font=dict(
                    size=12,
                    color="#CCCCCC",
                ),
                margin=dict(
                    t=50,
                    l=50,
                    b=50,
                    r=5,
                ),
                hovermode='closest',
                xaxis={
                    "showgrid": True,
                    "title": "Position",
                    "type": "category",
                },
                yaxis={
                    "range": [0, cf+2],
                    "showgrid": True,
                    "title": "Number",
                },
            )
            fig = dict(data=data, layout=layout)
            pio.write_image(fig, 'images/base2015-' + str(value) + '.png')
            del earth[0]
            xc = iter(range(0, len(earth)))
            i = 0
            for i in list(xc):
                for val in (earth):
                    while i <= len(earth)-1:
                        data = go.Scatter(
                             x = xlist,
                             y = earth[i],
                        ),
                        layout = dict(
                            title = "Initial Ball:" + str(value) + "| Year: 2015",
                            paper_bgcolor= "rgb(255, 255, 255)",
                            autosize=True,
                            font=dict(
                                size=12,
                                color="#CCCCCC",
                            ),
                            margin=dict(
                                t=50,
                                l=50,
                                b=50,
                                r=5,
                            ),
                            hovermode='closest',
                            xaxis={
                                "showgrid": False,
                                "title": "Position",
                                "type": "category",
                            },
                            yaxis={
                                "range": [0, cf +2],
                                "showgrid": False,
                                "title": "Number",
                            },
                        )
                        fig = dict(data=data, layout=layout)
                        newfile = 'images/fig0.png'
                        pio.write_image(fig, newfile)
                        image1 = Image.open('images/base2015-' + str(value) + '.png')
                        image2 = Image.open(newfile)
                        
                        image3 = changeImageSize(800, 500, image1)
                        image4 = changeImageSize(800, 500, image2)
                        
                        # Make sure images got an alpha channel
                        image5 = image3.convert("RGBA")
                        image6 = image4.convert("RGBA")
                        datas = image6.getdata()
                        
                        newData = []
                        for item in datas:
                            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                                newData.append((255, 255, 255, 0))
                            else:
                                newData.append(item)
                                
                        image6.putdata(newData)
                        background = image5
                        foreground = image6
                        
                        background.paste(foreground, (0, 0), foreground)
                        background.save('images/base2015-' + str(value) + '.png', compress_level=1)
                        i+=1
            image_filename = 'images/base' + str(kx) + '-' + str(value) + '.png'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())    
            return 'data:image/png;base64,{}'.format(encoded_image.decode())

    else:
        if os.path.exists('images/base' + str(kx) + '-' + str(value) + '.png'):
            image_filename = 'images/base' + str(kx) + '-' + str(value) + '.png'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())    
            return 'data:image/png;base64,{}'.format(encoded_image.decode())
        else:    
            ylist = earth[0]
            xlist = iter(range(1, 8))
            xlist = list(xlist)
            data = go.Scatter(
                 x = xlist,
                 y = ylist
            ),
            layout = dict(
                title = "Initial Ball:" + str(value) + "| Year:" + str(kx),
                paper_bgcolor= "#ffffff",
                plot_bgcolor= "rgb(208, 248, 255)",
                autosize=True,
                font=dict(
                    size=12,
                    color="#CCCCCC",
                ),
                margin=dict(
                    t=50,
                    l=50,
                    b=50,
                    r=5,
                ),
                hovermode='closest',
                xaxis={
                    "showgrid": True,
                    "title": "Position",
                    "type": "category",
                },
                yaxis={
                    "range": [0, cf+2],
                    "showgrid": True,
                    "title": "Number",
                },
            )
            fig = dict(data=data, layout=layout)
            pio.write_image(fig, 'images/base' +str(kx)  + '-' + str(value) + '.png')
            del earth[0]
            xc = iter(range(0, len(earth)))
            i = 0
            for i in list(xc):
                for val in (earth):
                    while i <= len(earth)-1:
                        data = go.Scatter(
                             x = xlist,
                             y = earth[i],
                        ),
                        layout = dict(
                            title = "Initial Ball:" + str(value) + "| Year:" + str(kx),
                            paper_bgcolor= "rgb(255, 255, 255)",
                            autosize=True,
                            font=dict(
                                size=12,
                                color="#CCCCCC",
                            ),
                            margin=dict(
                                t=50,
                                l=50,
                                b=50,
                                r=5,
                            ),
                            hovermode='closest',
                            xaxis={
                                "showgrid": False,
                                "title": "Position",
                                "type": "category",
                            },
                            yaxis={
                                "range": [0, cf +2],
                                "showgrid": False,
                                "title": "Number",
                            },
                        )
                        fig = dict(data=data, layout=layout)
                        newfile = 'images/fig0.png'
                        pio.write_image(fig, newfile)
                        image1 = Image.open('images/base' + str(kx) + '-' + str(value) + '.png')
                        image2 = Image.open(newfile)
                        
                        image3 = changeImageSize(800, 500, image1)
                        image4 = changeImageSize(800, 500, image2)
                        
                        # Make sure images got an alpha channel
                        image5 = image3.convert("RGBA")
                        image6 = image4.convert("RGBA")
                        datas = image6.getdata()
                        
                        newData = []
                        for item in datas:
                            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                                newData.append((255, 255, 255, 0))
                            else:
                                newData.append(item)
                                
                        image6.putdata(newData)
                        background = image5
                        foreground = image6
                        
                        background.paste(foreground, (0, 0), foreground)
                        background.save('images/base' + str(kx) + '-' + str(value) + '.png', compress_level=1)
                        i+=1
        image_filename = 'images/base' + str(kx) + '-' + str(value) + '.png'
        encoded_image = base64.b64encode(open(image_filename, 'rb').read())    
        return 'data:image/png;base64,{}'.format(encoded_image.decode())

@app.callback(Output('lotto4', 'figure'),
    [Input('intermediate-value2', 'children')])
def make_graph6(intermediatevalue2):
    water = '{}.txt'.format(s11)
    earth = '{}.txt'.format(s6)
    with open('earth.txt') as json_file:
        roller = json.load(json_file)
    with open('water.txt') as json_file:
        cf = json.load(json_file)
    if len(roller) == 1:
        roller = roller * 2
    else:
        roller = roller
    trace1 = dict(
        type="surface",
        z=roller,
        hoverinfo='z',
        lighting={
            "ambient": 0.80,
            "diffuse": 0.80,
            "fresnel": 4,
            "roughness": 50,
            "specular": 3,
        },
        autocolorscale= False, 
        cauto= False, 
        cmax= cf, 
        colorscale= [
            [0, "#440154"], [0.1111111111111111, "#482878"], [0.2222222222222222, "#3e4989"], [0.3333333333333333, "#31688e"], [0.4444444444444444, "#26828e"], [0.5555555555555556, "#1f9e89"], [0.6666666666666666, "#35b779"], [0.7777777777777778, "#6ece58"], [0.8888888888888888, "#b5de2b"], [1, "#fde725"]], 

        showscale=True,
        scene="scene",
        colorbar= {
            "x": 1.1, 
            "y": 0.43999999999999995, 
            "lenmode": "fraction", 
            "thickness": 31, 
            "thicknessmode": "pixels", 
            "xanchor": "right"
          }, 
    )
    data = [trace1]
    layout = dict(
        autosize=True,
        font=dict(
            size=12,
            color="#CCCCCC",
        ),
        margin=dict(
            t=5,
            l=50,
            b=50,
            r=5,
        ),
        hovermode='closest',
        scene=dict(
            aspectmode="manual",
            aspectratio=dict(x=2, y=5, z=1.5),
            camera=dict(eye=dict(x=-3.4, y=0, z=0)), center=dict(x=0, y=0, z=0), up=dict(x=0, y=0, z=1)),
            xaxis={
                "showgrid": True,
                "title": "",
                "type": "category",
                "zeroline": False,
                "categoryorder": 'array',
            },
            yaxis={
                "showgrid": True,
                "title": "",
                "type": "date",
                "zeroline": False,
            },
        )
    
    figure = dict(data=data, layout=layout)
    # py.iplot(figure)
    return figure


@app.callback(Output('inter-ball', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('inter-ball', 'children')])
def update_output(nclicks, interball):
    nclicks = int(nclicks)
    clicks11 = '{}.txt'.format(s4)
    clicks22 = '{}.txt'.format(s5)
    if nclicks == 0:
        with open('clicks11.txt', 'w') as outfile:
            json.dump(nclicks, outfile)
        with open('clicks22.txt', 'w') as outfile:
            json.dump(nclicks, outfile)
    nclicks2 = nclicks % 2
    if nclicks2 == 1:
        with open('clicks22.txt', 'w') as outfile:
            json.dump(nclicks2, outfile)
    if nclicks2 == 0 and nclicks > 1:
        with open('clicks11.txt', 'w') as outfile:
            json.dump(nclicks2, outfile)
    with open('clicks22.txt') as json_file:
        clicks2 = json.load(json_file)
    with open('clicks11.txt') as json_file:
        clicks = json.load(json_file)
    if clicks != clicks2: 
        with open('sky.txt') as json_file:
            mist = json.load(json_file)
        mist=mist[::-1]
        cage = (mist[34:])
        cage2 = [val for sublist in cage for val in sublist]
        balls = []
        for i in range(0, 6):
            ball = cage2[i::6]
            balls.append(ball)
        ball =  balls[0]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball1 = ball[k]
        out = []
        out.append(ball1)
        
        ball =  balls[1]
        ball = [y for y in ball if y != ball1]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball2 = ball[k]
        out.append(ball2)
        
        ball =  balls[2]
        jc = [y for y in ball if y != ball1]
        ball = [y for y in jc if y != ball2]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball3 = ball[k]
        out.append(ball3)

        ball =  balls[3]
        jc = [y for y in ball if y != ball1]
        jd = [y for y in jc if y != ball2]
        ball = [y for y in jd if y != ball3]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball4 = ball[k]
        out.append(ball4)
        
        ball =  balls[4]
        jc = [y for y in ball if y != ball1]
        jd = [y for y in jc if y != ball2]
        je = [y for y in jd if y != ball3]
        ball = [y for y in je if y != ball4]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball5 = ball[k]
        out.append(ball5)
        
        ball =  balls[5]
        jc = [y for y in ball if y != ball1]
        jd = [y for y in jc if y != ball2]
        je = [y for y in jd if y != ball3]
        jf = [y for y in je if y != ball4]
        ball = [y for y in jf if y != ball5]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball6 = ball[k]
        out.append(ball6)
        out = sorted(out)
        if out[4] == 46:
            out[5] = 47
        elif out[3] == 45:
            out[4] = 46
            out[5] = 47
        elif out[2] == 44:
            out[3] = 45
            out[4] = 46
            out[5] = 47
        elif out[1] == 43:
            out[2] = 44
            out[3] = 45
            out[4] = 46
            out[5] = 47
        with open('out.txt', 'w') as outfile:
            return json.dump(out, outfile)


@app.callback(Output('ball1', 'value'),
              [Input('inter-ball', 'children')])
def update_output(interball):
    with open('out.txt') as json_file:
        out = json.load(json_file)
    clean=str(out)
    clean = clean.replace(',', '  ')
    clean = clean.replace('[', '')
    clean = clean.replace(']', '')
    return clean


@app.callback(Output('inter-ball2', 'children'),
              [Input('submit-button2', 'n_clicks')],
              [State('inter-ball2', 'children')])
def update_output(nclicks, interball2):
    nclicks = int(nclicks)
    if nclicks == 0:
        with open('clicks33.txt', 'w') as outfile:
            json.dump(nclicks, outfile)
        with open('clicks44.txt', 'w') as outfile:
            json.dump(nclicks, outfile)
    nclicks2 = nclicks % 2
    if nclicks2 == 1:
        with open('clicks44.txt', 'w') as outfile:
            json.dump(nclicks2, outfile)
    if nclicks2 == 0 and nclicks > 1:
        with open('clicks33.txt', 'w') as outfile:
            json.dump(nclicks2, outfile)
    with open('clicks44.txt') as json_file:
        clicks2 = json.load(json_file)
    with open('clicks33.txt') as json_file:
        clicks = json.load(json_file)
    if clicks != clicks2: 
        with open('earth.txt') as json_file:
            mist = json.load(json_file)
        cage=mist[::-1]
        cage2 = [val for sublist in cage for val in sublist]
        balls = []
        for i in range(0, 7):
            ball = cage2[i::7]
            balls.append(ball)
        ball =  balls[0]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball1 = ball[k]
        out = []
        out.append(ball1)
        
        ball =  balls[1]
        ball = [y for y in ball if y != ball1]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball2 = ball[k]
        out.append(ball2)
        
        ball =  balls[2]
        jc = [y for y in ball if y != ball1]
        ball = [y for y in jc if y != ball2]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball3 = ball[k]
        out.append(ball3)

        ball =  balls[3]
        jc = [y for y in ball if y != ball1]
        jd = [y for y in jc if y != ball2]
        ball = [y for y in jd if y != ball3]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball4 = ball[k]
        out.append(ball4)
        
        ball =  balls[4]
        jc = [y for y in ball if y != ball1]
        jd = [y for y in jc if y != ball2]
        je = [y for y in jd if y != ball3]
        ball = [y for y in je if y != ball4]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball5 = ball[k]
        out.append(ball5)
        
        ball =  balls[5]
        jc = [y for y in ball if y != ball1]
        jd = [y for y in jc if y != ball2]
        je = [y for y in jd if y != ball3]
        jf = [y for y in je if y != ball4]
        ball = [y for y in jf if y != ball5]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball6 = ball[k]
        out.append(ball6)
        out = sorted(out)
        if out[4] == 46:
            out[5] = 47
        elif out[3] == 45:
            out[4] = 46
            out[5] = 47
        elif out[2] == 44:
            out[3] = 45
            out[4] = 46
            out[5] = 47
        elif out[1] == 43:
            out[2] = 44
            out[3] = 45
            out[4] = 46
            out[5] = 47
        with open('out2.txt', 'w') as outfile:
            return json.dump(out, outfile)


@app.callback(Output('ball2', 'value'),
              [Input('inter-ball2', 'children')])
def update_output(interball2):
    with open('out2.txt') as json_file:
        out = json.load(json_file)
    clean=str(out)
    clean = clean.replace(',', '  ')
    clean = clean.replace('[', '')
    clean = clean.replace(']', '')
    return clean



@app.callback(Output('lotto5', 'figure'),
    [Input('intermediate-value', 'children')])
def make_graph5(intermediatevalue):
    with open('sky1.txt') as json_file:
        sky = json.load(json_file)
    y = sky[-37:-1]
    c = []
    for i in y:
        g = sum(i)
        c.append(g) 
    data = go.Scatter(
      y = c,
      marker= dict(
        color = "rgb(178, 10, 28)", 
        symbol = "square"
      ), 
    ),
    layout = dict(
      autosize = True, 
      plot_bgcolor = "rgb(255, 251, 198)", 
      showlegend =  False, 
      title = "Stochastic Analysis", 
      xaxis= {
        "autorange": True, 
        "range": [-1.7517458100558658, 30.751745810055866], 
        "title": {"text": "time"}
      }, 
      yaxis= {
        "autorange": True, 
        "range": [108.03752039151712, 259.96247960848285], 
        "title": {"text": "aggregated results"}, 
        "type": "linear"
      }
    )
    figure = dict(data=data, layout=layout)
    # py.iplot(figure)
    return figure
    
@app.callback(Output('inter-med1', 'children'),
              [Input('submit-button3', 'n_clicks')],
              [State('inter-med1', 'children')])
def update_output(nclicks, intermed1):
    nclicks = int(nclicks)
    if nclicks == 0:
        with open('clicks55.txt', 'w') as outfile:
            json.dump(nclicks, outfile)
        with open('clicks66.txt', 'w') as outfile:
            json.dump(nclicks, outfile)
    nclicks2 = nclicks % 2
    if nclicks2 == 1:
        with open('clicks66.txt', 'w') as outfile:
            json.dump(nclicks2, outfile)
    if nclicks2 == 0 and nclicks > 1:
        with open('clicks55.txt', 'w') as outfile:
            json.dump(nclicks2, outfile)
    with open('clicks66.txt') as json_file:
        clicks2 = json.load(json_file)
    with open('clicks55.txt') as json_file:
        clicks = json.load(json_file)
    if clicks != clicks2: 
        with open('sky1.txt') as json_file:
            sky = json.load(json_file)
        y = sky[-36:-1]
        c = []
        for i in y:
            g = sum(i)
            c.append(g)      
        ko = max(i for i in c)    
        p = min(i for i in c)    
        q = len(c)    
        o = sum(c)
        f = o//q    
        gg = ko-p
        fg = gg//3
        gh = p+fg
        jk = gh+fg
        kl=[]
        for v in c:
            if p >= v <= gh:
                kl.append(-1)
            elif gh >= v <= jk:
                kl.append(0)
            else:
                kl.append(+1)
        x1 = np.array(kl).reshape(7, 5)
        x2 = np.array(kl).reshape(5, 7)
        kl.append(2)
        x3 = np.array(kl).reshape(6, 6)    
        x5 = np.arange(3,52).reshape(7, 7)    
        x5[0,2]= x3[0,2]
        x5[0,3]= x3[0,3]
        x5[0,4]= x1[0,4]
        if x5[0,4]==0 and x2[0,4] == 1:
            x5[0,4]=10
        elif x5[0,4]==1 and x2[0,4] == 0:
            x5[0,4]=10
        elif x5[0,4]==-1 and x2[0,4] == 0:
            x5[0,4]=-10
        elif x5[0,4]==0 and x2[0,4] == -1:
            x5[0,4]=-10
        elif x5[0,4]==1 and x2[0,4] == -1:
            x5[0,4]=-11
        elif x5[0,4]==-1 and x2[0,4] == 1:
            x5[0,4]=-11
        x5[0,5]= x3[0,5]
        x5[0,6]= x2[0,6]
        x5[1,1]= x1[1,1]
        if x5[1,1]==0 and x3[1,1] == 1:
            x5[1,1]=10
        elif x5[1,1]==1 and x3[1,1] == 0:
            x5[1,1]=10
        elif x5[1,1]==-1 and x3[1,1] == 0:
            x5[1,1]=-10
        elif x5[1,1]==0 and x3[1,1] == -1:
            x5[1,1]=-10
        elif x5[1,1]==1 and x3[1,1] == -1:
            x5[1,1]=-11
        elif x5[1,1]==-1 and x3[1,1] == 1:
            x5[1,1]=-11
        x5[1,2]= x2[1,2]
        if x5[1,2]==0 and x3[1,2] == 1:
            x5[1,2]=10
        elif x5[1,2]==1 and x3[1,2] == 0:
            x5[1,2]=10
        elif x5[1,2]==-1 and x3[1,2] == 0:
            x5[1,2]=-10
        elif x5[1,2]==0 and x3[1,2] == -1:
            x5[1,2]=-10
        elif x5[1,2]==1 and x3[1,2] == -1:
            x5[1,2]=-11
        elif x5[1,2]==-1 and x3[1,2] == 1:
            x5[1,2]=-11
        x5[1,4]= x1[1,4]
        x5[1,5]= x3[1,5]
        x5[1,6]= x2[1,6]
        x5[2,0]= x2[2,0]
        x5[2,2]= x3[2,2]
        x5[2,3]= x1[2,3]
        if x5[2,3]==0 and x3[2,3] == 1:
            x5[2,3]=10
        elif x5[2,3]==1 and x3[2,3] == 0:
            x5[2,3]=10
        elif x5[2,3]==-1 and x3[2,3] == 0:
            x5[2,3]=-10
        elif x5[2,3]==0 and x3[2,3] == -1:
            x5[2,3]=-10
        elif x5[2,3]==1 and x3[2,3] == -1:
            x5[2,3]=-11
        elif x5[2,3]==-1 and x3[2,3] == 1:
            x5[2,3]=-11
        x5[2,4]= x1[2,4]
        x5[2,5]= x2[2,5]
        if x5[2,5]==0 and x3[2,5] == 1:
            x5[2,5]=10
        elif x5[2,5]==1 and x3[2,5] == 0:
            x5[2,5]=10
        elif x5[2,5]==-1 and x3[2,5] == 0:
            x5[2,5]=-10
        elif x5[2,5]==0 and x3[2,5] == -1:
            x5[2,5]=-10
        elif x5[2,5]==1 and x3[2,5] == -1:
            x5[2,5]=-11
        elif x5[2,5]==-1 and x3[2,5] == 1:
            x5[2,5]=-11
        x5[2,6] = x2[2,6]
        x5[3,1]= x3[3,1]
        x5[3,2]= x3[3,2]
        x5[3,4]= x1[3,4]
        x5[3,5]= x3[3,5]
        x5[3,6]= x2[3,6]
        x5[4,0]= x1[4,0]
        x5[4,1]= x2[4,1]
        x5[4,2]= x3[4,2]
        x5[4,3]= x3[4,3]
        x5[4,4]= x1[4,4]
        x5[4,5]= x3[4,5]
        x5[4,6]= x2[4,6]
        x5[5,1]= x3[5,1]
        x5[5,2]=  x1[5,2]
        if x5[5,2]==0 and x3[5,2] == 1:
            x5[5,2]=10
        elif x5[5,2]==1 and x3[5,2] == 0:
            x5[5,2]=10
        elif x5[5,2]==-1 and x3[5,2] == 0:
            x5[5,2]=-10
        elif x5[5,2]==0 and x3[5,2] == -1:
            x5[5,2]=-10
        elif x5[5,2]==1 and x3[5,2] == -1:
            x5[5,2]=-11
        elif x5[5,2]==-1 and x3[5,2] == 1:
            x5[5,2]=-11
        x5[5,4]= x1[5,4]
        x5[6,4]=  x1[6,4]
        x5[0,0] = x5[0,6]
        x5[0,1] = x5[0,5]
        x5[1,0] = x5[1,6]
        x5[2,1] = x5[2,5]
        x5[3,0] = x5[3,6]
        x5[3,1] = x5[3,6]
        x5[6,6] = x5[0,6]
        x5[5,5] = x5[1,5]
        x5[6,5] = x5[0,5]
        x5[5,6] = x5[1,6]
        x5[5,0] = x5[5,6]
        x5[6,0] = x5[0,0]
        x5[6,1] = x5[0,1]
        x5[6,2] = x5[0,2]
        x5[6,3] = x5[0,3]
        x5[6,5] = x5[0,5]
        
        gh3 = x5.tolist()
        gh1 = [val for sublist in gh3 for val in sublist] 
        gh2 = gh1[-9:]
        gh3 = gh2[0]
        if gh3 == -1:
            x = list(range(p, gh+1))
        elif gh3 == 0:
            x = list(range(gh, jk+1))
        else:
            x = list(range(jk, ko+1))
                
        cage3 = [val for sublist in y for val in sublist] 
        
        def calrange():
            balls = []
            for i in range(0, 6):
                ball = cage3[i::6]
                balls.append(ball)
            ball =  balls[5]
            lenball = len(ball)
            k = random.randint(0, lenball-1)
            ball1 = ball[k]
            out = []
            out.append(ball1)
            
            ball =  balls[4]
            ball = [y for y in ball if y != ball1]
            lenball = len(ball)
            k = random.randint(0, lenball-1)
            ball2 = ball[k]
            out.append(ball2)
            
            ball =  balls[3]
            jc = [y for y in ball if y != ball1]
            ball = [y for y in jc if y != ball2]
            lenball = len(ball)
            k = random.randint(0, lenball-1)
            ball3 = ball[k]
            out.append(ball3)
        
            ball =  balls[2]
            jc = [y for y in ball if y != ball1]
            jd = [y for y in jc if y != ball2]
            ball = [y for y in jd if y != ball3]
            lenball = len(ball)
            k = random.randint(0, lenball-1)
            ball4 = ball[k]
            out.append(ball4)
            
            ball =  balls[1]
            jc = [y for y in ball if y != ball1]
            jd = [y for y in jc if y != ball2]
            je = [y for y in jd if y != ball3]
            ball = [y for y in je if y != ball4]
            lenball = len(ball)
            k = random.randint(0, lenball-1)
            ball5 = ball[k]
            out.append(ball5)
            
            ball =  balls[0]
            jc = [y for y in ball if y != ball1]
            jd = [y for y in jc if y != ball2]
            je = [y for y in jd if y != ball3]
            jf = [y for y in je if y != ball4]
            ball = [y for y in jf if y != ball5]
            lenball = len(ball)
            k = random.randint(0, lenball-1)
            ball6 = ball[k]
            out.append(ball6)
            out = sorted(out)
            dsf = sum(out)
            if dsf in x:
                return dsf
            else:
                ds = calrange()
        
        ds = calrange()
        print(ds)
        with open('out3.txt', 'w') as outfile:
            return json.dump(ds, outfile)
    

@app.callback(Output('ball3', 'value'),
              [Input('inter-med1', 'children')])
def update_output(intermed1):
    with open('out3.txt') as json_file:
        out = json.load(json_file)
    clean=str(out)
    clean = clean.replace(',', '  ')
    clean = clean.replace('[', '')
    clean = clean.replace(']', '')
    return clean


if __name__ == '__main__':
    app.run_server(debug=True)