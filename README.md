# Python-practicum-2022
All mandatory tasks done!

#Tasks was:

#1st week:
1. Set up a development environment, e.g. Anaconda that includes all the necessary programs
https://www.anaconda.com/
2. Choose where to host the Flask app (local or hosted service, e.g., Heroku.com or similar)
https://www.heroku.com/
3. You will create a minimal Flask application for this assignment. Your application should
✅ have a route for /welcome, which responds with the string "welcome" 
✅ have a route for /welcome/home, which responds with the string "welcome home" 
✅ have a route for /welcome/back, which responds with the string "welcome back"
4. Optionally, you can share your code here: GitHub Python Practicum 2022

#2nd week:
✅ Get a weather report for a city of your liking via API call
u  API doc: https://openweathermap.org/current#name
u  API Key: 60aa068482d6ddc251ae5f53570ac5fb
✅ Create a route /weather which responds with received data
u  display city name and current temperature in Celsius
u  consider using a template to render and display data
✅ Optional task – let the user pick a city

#3rd  week.
✅ Get geographic coordinates for a city of your liking via an API call
u  API doc: https://openweathermap.org/api/geocoding-api
✅ Get historical data from dev.meteostat.net via one of these methods:
u  JSON API
u  Python library
u  Bulk data
✅ Display one year of temperature history - min., max., average
u  Use the graphical form of representation – matplotlib module
✅ Create a route /weather_history to display data
u  Show city name and chart with temperature data, including legend (names of axis, description of data)
u  In addition, separately display values for min., max. temperature, the date it was recorded, and the average temperature for the whole range.
u  Provide a download link for an Excel document with temperature data (raw data)
u  Provide a download link for a PDF document with a temperature chart (graphical data)
✅ Additional advanced task: Send notification of the temperature
u  Create a route /notification
u  Possible communication channels:
a push notification via SIGNL4 or similar service: https://www.signl4.com/
e-mail notification
SMS message
u  Trigger the notification by:
Pushing a button on your webpage
Setting up a notification when a trigger temperature is reached


#4th  week
Record each weather search in the log file
u  Log: Date, Time, City, Temperature
✅ Create a route /log to display data for the last 5 searches
u  Think about persistent data. The last 5 searches must be displayed even after flask is restarted
✅ Create a route /cities
u  Display the current list of cities of interest and their current temperature (updates on list change)
u  Let the user add the city to the list
u  Let the user change list entry (change city name)
u  Let the user delete the city from the list
u  Record add/change/delete events to log file
u  Let the user manually refresh the currently listed cities’ temperature data.
u  The current list and temperature must persist after the flask is restarted
u  Optional advanced task: implement this for multiple users (identified by login)
