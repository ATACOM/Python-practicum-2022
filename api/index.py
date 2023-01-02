from flask import Flask, render_template
import requests
import json
app = Flask(__name__,
            template_folder='Templates',
            static_url_path='',
            static_folder='static')

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

@app.route('/weather', methods=['GET', 'POST'])
def get_weather():

    if request.method == 'POST':
        city = request.form.get('city_name').capitalize()
        if len(city) == 0:
            return render_template('laiks.html', no_city="You should write the name of a city in the box")
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
            city + '&appid=60aa068482d6ddc251ae5f53570ac5fb&units=metric&mode=json'
        weather_data = requests.get(weather_url).json()
        if city in weather_data.values():
            return render_template('laiks_result.html', data=weather_data, city_name=city)
        else:
            return render_template('nav.html')

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
