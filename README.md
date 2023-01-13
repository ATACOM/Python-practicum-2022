# Python-practicum-2022
All mandatory tasks done!<br/>

#Tasks was:<br/>
<br/>
#1st week:<br/>
1. Set up a development environment, e.g. Anaconda that includes all the necessary programs<br/>
https://www.anaconda.com/<br/>
2. Choose where to host the Flask app (local or hosted service, e.g., Heroku.com or similar)<br/>
https://www.heroku.com/<br/>
3. You will create a minimal Flask application for this assignment. Your application should<br/>
✅ have a route for /welcome, which responds with the string "welcome" <br/>
✅ have a route for /welcome/home, which responds with the string "welcome home" <br/>
✅ have a route for /welcome/back, which responds with the string "welcome back"<br/>
4. Optionally, you can share your code here: GitHub Python Practicum 2022<br/>
<br/>
#2nd week:<br/>
✅ Get a weather report for a city of your liking via API call<br/>
u  API doc: https://openweathermap.org/current#name<br/>
u  API Key: 60aa068482d6ddc251ae5f53570ac5fb<br/>
✅ Create a route /weather which responds with received data<br/>
u  display city name and current temperature in Celsius<br/>
u  consider using a template to render and display data<br/>
✅ Optional task – let the user pick a city<br/>
<br/>
#3rd  week.<br/>
✅ Get geographic coordinates for a city of your liking via an API call<br/>
u  API doc: https://openweathermap.org/api/geocoding-api<br/>
✅ Get historical data from dev.meteostat.net via one of these methods:<br/>
u  JSON API<br/>
u  Python library<br/>
u  Bulk data<br/>
✅ Display one year of temperature history - min., max., average<br/>
u  Use the graphical form of representation – matplotlib module<br/>
✅ Create a route /weather_history to display data<br/>
u  Show city name and chart with temperature data, including legend (names of axis, description of data)<br/>
u  In addition, separately display values for min., max. temperature, the date it was recorded, and the average temperature for the whole range.<br/>
u  Provide a download link for an Excel document with temperature data (raw data)<br/>
u  Provide a download link for a PDF document with a temperature chart (graphical data)<br/>
✅ Additional advanced task: Send notification of the temperature<br/>
u  Create a route /notification<br/>
u  Possible communication channels:<br/>
a push notification via SIGNL4 or similar service: https://www.signl4.com/<br/>
e-mail notification<br/>
SMS message<br/>
u  Trigger the notification by:<br/>
Pushing a button on your webpage<br/>
Setting up a notification when a trigger temperature is reached<br/>
<br/>
<br/>
#4th  week<br/>
Record each weather search in the log file<br/>
u  Log: Date, Time, City, Temperature<br/>
✅ Create a route /log to display data for the last 5 searches<br/>
u  Think about persistent data. The last 5 searches must be displayed even after flask is restarted<br/>
✅ Create a route /cities<br/>
u  Display the current list of cities of interest and their current temperature (updates on list change)<br/>
u  Let the user add the city to the list<br/>
u  Let the user change list entry (change city name)<br/>
u  Let the user delete the city from the list<br/>
u  Record add/change/delete events to log file<br/>
u  Let the user manually refresh the currently listed cities’ temperature data.<br/>
u  The current list and temperature must persist after the flask is restarted<br/>
u  Optional advanced task: implement this for multiple users (identified by login)<br/>
