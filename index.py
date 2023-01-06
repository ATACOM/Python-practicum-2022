from flask import Flask, render_template, request
import requests
import json
import pandas as pd
import openpyxl
from datetime import datetime, date
from meteostat import Point, Daily
app = Flask(__name__)

@app.route('/')
def home():
    # Params
    title = 'Home'
    content = ''
    return render_template('_root.html', title=title, content=content)

@app.route('/welcome')
def welcome():
    # Params
    title = 'Welcome'
    content = 'Welcome'
    return render_template('_root.html', title=title, content=content)

@app.route('/welcome/home')
def welcome_home():
    # Params
    title = 'Welcome home'
    content = 'Welcome home'
    return render_template('_root.html', title=title, content=content)

@app.route('/welcome/back')
def welcome_back():
    # Params
    title = 'Welcome back'
    content = 'Welcome back'
    return render_template('_root.html', title=title, content=content)

@app.route('/weather')
def weather():
    # Params
    title = 'Weather'
    adress = 'https://api.openweathermap.org/data/2.5/weather'
    appid = '60aa068482d6ddc251ae5f53570ac5fb'
    units = 'metric'
    city = 'Riga'
    # Request
    url = f"{adress}?appid={appid}&units={units}&q={city}"
    response = requests.get(url)
    # Parsing 
    Temperature = response.json().get("main").get("temp")
    content = f"Temperature in {city} is {Temperature} °C"
    return render_template('_root.html', title=title, content=content)

@app.route('/coords')
def coords():
    # Params
    title = 'Coords'
    adress = 'http://api.openweathermap.org/geo/1.0/direct?limit=100'
    appid = '60aa068482d6ddc251ae5f53570ac5fb'
    city = 'Riga'
    # Request
    url = f"{adress}&q={city}&appid={appid}"
    req=requests.get(url)
    response = req.json()
    thislist = []
    for item in response:
        country = (item['country'])
        state = (item['state'])
        lat = (item['lat'])
        lon = (item['lon'])
        coords = f"{lat},{lon} ({country}, {state})"
        thislist.append(coords)
    return render_template('_coord.html', title=title, content=thislist, city=city)


@app.route('/weather_history')
def weather_history():
    # Load bulk data
    url="https://bulk.meteostat.net/v2/hourly/10637.csv.gz"
    df = pd.read_csv(url, compression='gzip', header=0, sep=' ', quotechar='"', error_bad_lines=False)
    df.to_excel(r'dataframe.xlsx', index=False)  
    return
