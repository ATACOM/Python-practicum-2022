from flask import Flask, render_template, request, send_file, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import pandas as pd
import openpyxl
import os
from datetime import datetime, date
from meteostat import Point, Daily
import matplotlib.pyplot as plt




app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "log.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.Text) 
    datums = db.Column(db.DateTime)
    temperature = db.Column(db.REAL)

def whattemp(city):
    adress = 'https://api.openweathermap.org/data/2.5/weather'
    appid = '60aa068482d6ddc251ae5f53570ac5fb'
    units = 'metric'
    url = f"{adress}?appid={appid}&units={units}&q={city}"
    response = requests.get(url)
    temperature = response.json().get("main").get("temp")
    return temperature

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.Text)
    temp = db.Column(db.REAL)

class Citieslog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.Text) 
    datums = db.Column(db.DateTime)
    action = db.Column(db.Text) 

def create_cities(text):
    cities = Cities(city=text, temp=whattemp(text))
    db.session.add(cities)
    db.session.commit()
    db.session.refresh(cities)

def create_citieslog(city,datums,action):
    citieslog = Citieslog(city=city,action=action,datums=datums)
    db.session.add(citieslog)
    db.session.commit()
    db.session.refresh(citieslog)

def create_log(city,temperature,datums):
    note = Note(city=city,temperature=temperature,datums=datums)
    db.session.add(note)
    db.session.commit()
    db.session.refresh(note)

def read_log():
    return db.session.query(Note).order_by(Note.id.desc()).limit(5).all()

def read_logcities():
    return db.session.query(Citieslog).order_by(Citieslog.id.desc()).all()

def read_cities():
    return db.session.query(Cities).all()

def update_cities(city_id, text):
    db.session.query(Cities).filter_by(id=city_id).update({
        "city": text,
        "temp" : whattemp(text)        
    })
    db.session.commit()


def delete_cities(city_id):
    db.session.query(Cities).filter_by(id=city_id).delete()
    db.session.commit()


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

@app.route("/weather",methods=["POST", "GET"])
def weather():
    title = 'Weather'
    if request.method == "POST":
        city=request.form["city"]
        return redirect(url_for("weatherdata",city=city, title=title))
    else:
        name=request.args.get("city")
        return render_template("_city_weather.html", title=title)

@app.route("/weatherdata/<city>")
def weatherdata(city):
    # Params
    title = 'Weather'
    adress = 'https://api.openweathermap.org/data/2.5/weather'
    appid = '60aa068482d6ddc251ae5f53570ac5fb'
    units = 'metric'
    
    # Request
    url = f"{adress}?appid={appid}&units={units}&q={city}"
    response = requests.get(url)
    # Parsing 
    temperature = response.json().get("main").get("temp")
    datums = datetime.now()
    content = f"Temperature in {city} is {temperature} °C"
    create_log(city,temperature,datums)
    return render_template('_root.html', title=title, content=content)
    

@app.route('/log')
def log():
    # Params
    title = 'Log'
    logdata = read_log()
    return render_template('_log.html', title=title, content=logdata)


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
    title = 'Weather history'
    city = 'Riga'
    adress = 'http://api.openweathermap.org/geo/1.0/direct?limit=1'
    appid = '60aa068482d6ddc251ae5f53570ac5fb'
    
    # Request
    url = f"{adress}&q={city}&appid={appid}"
    req=requests.get(url)
    response = req.json()
    lat = (response[0]['lat'])
    lon = (response[0]['lon'])

    # Set time period
    start = datetime(2022, 1, 1)
    end = datetime(2022, 12, 31)
    
    # Create Point for Riga, LV
    riga = Point(lat, lon)
    
    # Get daily data for 2018
    data = Daily(riga, start, end)
    data = data.fetch()
    
    # Plot line chart including average, minimum and maximum temperature
    data.plot(y=['tavg', 'tmin', 'tmax'])
    plt.title("Temperature in " + city)
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.legend(['Average', 'Minimum', 'Maximum'])
    
    #Save result charts
    plt.savefig('static/chart.png')
    plt.savefig('static/chart.pdf')

    #Save result excel and csv files
    df = pd.DataFrame(data).reset_index()
    df["time"] = df["time"].dt.date
    df.to_excel("static/dataframe.xlsx")
    maxtempdate = df.loc[df.tmax == df.tmax.max(), "time"].item()
    avgtemp = df["tavg"].mean().round(decimals=2)
    mintempdate = df.loc[df.tmin == df.tmin.min(), "time"].item()
    maxtemp=df["tmax"].max()
    mintemp=df["tmin"].min()

    statistika = f"Mean temperature in {city} was {avgtemp} °C, min temperature {mintemp} °C was in {mintempdate}, max temperature {maxtemp} °C was in {maxtempdate}."

    return render_template('_weatherhistory.html', title=title, city=city, stat=statistika)

@app.route('/static/chart.pdf')
def downloadpdf ():
    path = "static/chart.pdf"
    return send_file(path, as_attachment=True)

@app.route('/static/dataframe.xlsx')
def downloadxlsx ():
    path = "static/dataframe.xlsx"
    return send_file(path, as_attachment=True)

@app.route("/cities", methods=["POST", "GET"])
def cities():
    title = 'Cities'
    if request.method == "POST":
        create_cities(request.form['text'])
        create_citieslog(city=request.form['text'],datums=datetime.now(),action='ADD')
    return render_template("_cities.html", table=read_cities(), title=title)

@app.route("/cities/edit/<city_id>", methods=["POST", "GET"])
def edit_cities(city_id):
    if request.method == "POST":
        update_cities(city_id, text=request.form['text'])
        create_citieslog(city=request.form['text'],datums=datetime.now(),action='UPDATE')
    elif request.method == "GET":
        cityname = Cities.query.filter_by(id=city_id).first()
        create_citieslog(city=cityname.city,datums=datetime.now(),action='DELETE')
        delete_cities(city_id)
    return redirect("/cities", code=302)


@app.route('/logcities')
def logcities():
    # Params
    title = 'Log Cities'
    logdata = read_logcities()
    return render_template('_logcities.html', title=title, content=logdata)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

