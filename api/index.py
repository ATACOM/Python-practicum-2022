from flask import Flask, render_template
import requests
import json
app = Flask(__name__, template_folder='Templates', static_url_path='', static_folder='static')

#Main tasks

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    return 'welcome back'  

# For fun

# 1st page

@app.route('/')
def root():
    return """
    <h3>1st task links</h3>
    <p><b>Please use links below or type them by yourself:</b></p>
    <ul>
    <li><a href="https://weather-psi-nine.vercel.app/welcome">welcome</a></li>
    <li><a href="https://weather-psi-nine.vercel.app/welcome/home">welcome/home</a></li>
    <li><a href="https://weather-psi-nine.vercel.app/welcome/back">welcome/back</a></li>
    <li><a href="https://weather-psi-nine.vercel.app/weather">weather</a></li>
    </ul>
    """

#In case, if adress end with "/"

@app.route('/welcome/')
def welcome2():
    return 'welcome'

@app.route('/welcome/home/')
def welcome_home2():
    return 'welcome home'

@app.route('/welcome/back/')
def welcome_back2():
    return 'welcome back'

@app.route('/weather')
def weather():
    # Params
adress = 'https://api.openweathermap.org/data/2.5/weather'
appid = '60aa068482d6ddc251ae5f53570ac5fb'
units = 'metric'
city = 'Riga'

# Request
url = f"https://api.openweathermap.org/data/2.5/weather?appid={appid}&units={units}&q={city}"
response = requests.get(url)

# Parsing
temperature = response.json().get("main").get("temp")

#Print
print("Temperature in",city,"is",temperature,"°C")
    
    
    return 
