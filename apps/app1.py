# -*- coding: utf-8 -*-
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
import dash_auth
import bcrypt


from app import app

pio.orca.config.executable = '/Users/Koala/.npm/bin/orca'

if os.path.exists('apps/ash.txt'):
    with open('ash.txt') as json_file:
        valid = json.load(json_file)


valid = [val for sublist in valid for val in sublist] 

valid1, valid2 = [list(tup) for tup in zip(*valid2)]

auth = dash_auth.BasicAuth(app,
    valid
)

external_stylesheets = ['/assets/code.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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

def changeImageSize(maxWidth, 
    maxHeight, 
    image):

    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage


d = datetime.datetime.now()
f = []
f.append(d)
f = str(f)
g = f.replace('[datetime.datetime(', '')
k = g[:4]
m = int(k)
bk2 = []
for i in range(1993, m+1):
    bk2.append(i)
with open('bk2.txt', 'w') as outfile:
    json.dump(bk2, outfile)

i = bk2[10]
j = bk2[11]

i1=bk2[0]
j2=bk2[-1]

app.layout = html.Div([
    html.Div([
    html.Br(),
    html.H1('Predict Lotto Ireland', style={ 'font-size': 100,  'margin-top': 15}, 
      className = "nine columns"),
    html.Img( src="/assets/lotto.png", className = 'three columns', style={'width': '15%', 'float': 'right', 'margin-right': 5,  'margin-top': -15}),
    ], className = "row"),
    html.Hr(),
    html.Br(),
    html.Div([
        dcc.Graph(id='lotto', style={'height': '60vh'}),
    ], className = "row"),
    html.Br(),
    html.Div([
        dcc.RangeSlider(
        marks={i: '{}'.format(i) for i in bk2},
        min=i1,
        max=j2,
        value=[i, j],
        id='slider',
        allowCross=False,
        className = 'ten columns offset-by-one')
    ], className='row'),
    html.Br(),
    html.Div(id='intermediate-value', style={'display': 'none'}),
    html.Div(id='intermediate-water', style={'display': 'none'}),
    html.Div(id='intermediate-lotto2', style={'display': 'none'}),
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
    html.Br(),
    html.Br(),
    html.Div([              
        dcc.Textarea(id='ball1', readOnly = True, rows=2, style={'width': '4.15%',  'height': 50, 'padding-bottom': 6, 'border-radius': 1, 'resize': 'none',  'font-size': 30, 'font-family': 'inherit'},
        className="one column offset-by-four"),
        dcc.Textarea(id='ball2', readOnly = True, rows=2, style={'width': '4.15%',  'height': 50, 'padding-bottom': 6, 'border-radius': 1, 'resize': 'none', 'font-size': 30, 'font-family': 'inherit',  'margin-left': 25},
        className="one column"),
        dcc.Textarea(id='ball3', readOnly = True, rows=2, style={'width': '4.15%',  'height': 50, 'padding-bottom': 6, 'border-radius': 1, 'resize': 'none', 'font-size': 30, 'font-family': 'inherit',  'margin-left': 25},
        className="one column"),
        dcc.Textarea(id='ball4', readOnly = True, rows=2, style={'width': '4.15%',  'height': 50, 'padding-bottom': 6, 'border-radius': 1, 'resize': 'none', 'font-size': 30, 'font-family': 'inherit',  'margin-left': 25},
        className="one column"),
        dcc.Textarea(id='ball5', readOnly = True, rows=2, style={'width': '4.15%',  'height': 50, 'padding-bottom': 6, 'border-radius': 1, 'resize': 'none', 'font-size': 30, 'font-family': 'inherit',  'margin-left': 25},
        className="one column"),
        dcc.Textarea(id='ball6', readOnly = True, rows=2, style={'width': '4.3333%',  'height': 50, 'padding-bottom': 6, 'border-radius': 1, 'resize': 'none', 'font-size': 30, 'font-family': 'inherit',  'margin-left': 25},
        className="one column"),
    ], className="row"),
    html.Br(),
    html.Div([
    html.Button(id='submit-button', n_clicks=0, children='Predict', className="two columns offset-by-eight"),
    ], className="row"),
    html.Br(),
    html.Div([
              html.Br(),
              html.Hr(id='footer'),
              html.Br(),
              html.Footer(
                    html.Center('Cataphysical Research Society - 2018.' ),
              ),
              html.Br(),
    ], className = "row"),
])

@app.callback(Output('intermediate-value', 'children'), [Input('slider', 'value')])
def update_graph(value):
    kx = value[0]
    ky = value[1]
    lendfi = []
    gg=[]
    sky = []
    if kx == ky:
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
    elif ky != kx:
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
    kx = slider[0]
    ky = slider[1]
    ze = list(range(kx, ky+1))
    ze0 = np.arange(1993, 1994)
    ze1 = np.arange(1994, 2006)
    ze2 = np.arange(2006, 2015)
    ze3 = np.arange(2015, 2020)
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
    g = (max(df))
    with open('water.txt', 'w') as outfile:
        return json.dump(g, outfile)
    
@app.callback(Output('lotto', 'figure'),
    [Input('intermediate-value', 'children')])
def make_graph3(intermediatevalue):
    with open('sky.txt', 'r') as json_file:
        sky = json.load(json_file)
    with open('water.txt') as json_file:
        cf = json.load(json_file)
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
        cmax= cf, 
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
    Input('intermediate-water', 'children')])
def make_graph4(intermediatevalue, value, intermediatewater):
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
    Input('intermediate-water', 'children')])
def make_graph2(intermediatevalue, value, radio, intermediatewater):
    with open('sky.txt') as json_file:
        sky = json.load(json_file)
    with open('water.txt') as json_file:
        g = json.load(json_file)
    sky2 = [val for sublist in sky for val in sublist] 
    ball1 = sky2[::7]
    ball1 = np.array(ball1)
    balls=[]
    for i in range(1, 6):
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
    print(percentball)
    data = go.Pie(values= percentball[:],  labels= [i for i in xk]),
    fig = Figure(data=data)
    return fig

@app.callback(Output('lotto2', 'src'),
    [Input('intermediate-value2', 'children'),
    Input('slider2', 'value'),
    Input('slider', 'value')])
def make_graph5(intermediatevalue2, value, slider):
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
    kx = slider[0]
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
    with open('earth.txt') as json_file:
        roller = json.load(json_file)
    with open('water.txt') as json_file:
        cf = json.load(json_file)
    trace1 = dict(
        type="surface",
        opacity = 0.75,
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
    with open('bk2.txt') as json_file:
        bk2 = json.load(json_file)
    bk = bk2[22:]
    nclicks = int(nclicks)
    if nclicks == 0:
        with open('clicks.txt', 'w') as outfile:
            json.dump(nclicks, outfile)
        with open('clicks2.txt', 'w') as outfile:
            json.dump(nclicks, outfile)
    nclicks2 = nclicks % 2
    if nclicks2 == 1:
        with open('clicks2.txt', 'w') as outfile:
            json.dump(nclicks2, outfile)
    if nclicks2 == 0 and nclicks > 1:
        with open('clicks.txt', 'w') as outfile:
            json.dump(nclicks2, outfile)
    with open('clicks2.txt') as json_file:
        clicks2 = json.load(json_file)
    with open('clicks.txt') as json_file:
        clicks = json.load(json_file)
    bz = []
    mist = []
    gg = []
    if clicks != clicks2: 
        for i in bk:
            while len(bz) <= len(bk)-1:
                gb = "https://www.irishlottery.com/archive-"
                kz = gb + str(i)
                bz.append(kz)
                i += 1
        for c in bz:
            url = c
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
                mist.append(clean)
                i += 1
        mist = str(mist)
        mist = mist.replace("\'[\'[", "[[")
        mist = mist.replace("]\']\'", "]]")
        mist = mist.replace("\'[", "[")
        mist = mist.replace("]\'", "]")
        mist = ast.literal_eval(mist)
        mist=mist[::-1]
        print(mist)
        cage = (mist[34:])
        cage2 = [val for sublist in cage for val in sublist]
        balls = []
        for i in range(0, 6):
            ball = cage2[i::7]
            balls.append(ball)
        ball =  balls[0]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball1 = ball[k]
        out = []
        out.append(ball1)
        
        ball =  balls[1]
        [y for y in ball if y != ball1]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball2 = ball[k]
        out.append(ball2)
        
        ball =  balls[2]
        [y for y in ball if y != ball1]
        [y for y in ball if y != ball2]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball3 = ball[k]
        out.append(ball3)

        ball =  balls[3]
        [y for y in ball if y != ball1]
        [y for y in ball if y != ball2]
        [y for y in ball if y != ball3]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball4 = ball[k]
        out.append(ball4)
        
        ball =  balls[4]
        [y for y in ball if y != ball1]
        [y for y in ball if y != ball2]
        [y for y in ball if y != ball3]
        [y for y in ball if y != ball4]
        lenball = len(ball)
        k = random.randint(0, lenball-1)
        ball5 = ball[k]
        out.append(ball5)
        
        ball =  balls[5]
        [y for y in ball if y != ball1]
        [y for y in ball if y != ball2]
        [y for y in ball if y != ball3]
        [y for y in ball if y != ball4]
        [y for y in ball if y != ball5]
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


@app.callback(Output('ball1', 'value'),
              [Input('inter-ball', 'children')])
def update_output(interball):
    with open('out2.txt') as json_file:
        out = json.load(json_file)
    out = out[0]
    return out
    
@app.callback(Output('ball2', 'value'),
              [Input('inter-ball', 'children')])
def update_output(interball):
    with open('out2.txt') as json_file:
        out = json.load(json_file)
    out = out[1]
    return out

@app.callback(Output('ball3', 'value'),
              [Input('inter-ball', 'children')])
def update_output(interball):
    with open('out2.txt') as json_file:
        out = json.load(json_file)
    out = out[2]
    return out
    
@app.callback(Output('ball4', 'value'),
              [Input('inter-ball', 'children')])
def update_output(interball):
    with open('out2.txt') as json_file:
        out = json.load(json_file)
    out = out[3]
    return out

@app.callback(Output('ball5', 'value'),
              [Input('inter-ball', 'children')])
def update_output(interball):
    with open('out2.txt') as json_file:
        out = json.load(json_file)
    out = out[4]
    return out

@app.callback(Output('ball6', 'value'),
              [Input('inter-ball', 'children')])
def update_output(interball):
    with open('out2.txt') as json_file:
        out = json.load(json_file)
    out = out[5]
    return out





if __name__ == '__main__':
    app.run_server(debug=True)