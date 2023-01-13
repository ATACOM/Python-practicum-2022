# Python-practicum-2022
All mandatory tasks done!

# 1st week tasks:
1. Set up a development environment, e.g. Anaconda that includes all the necessary programs<br/>
https://www.anaconda.com/<br/>
2. Choose where to host the Flask app (local or hosted service, e.g., Heroku.com or similar)<br/>
https://www.heroku.com/<br/>
3. You will create a minimal Flask application for this assignment. Your application should<br/>
✅ have a route for /welcome, which responds with the string "welcome" <br/>
✅ have a route for /welcome/home, which responds with the string "welcome home" <br/>
✅ have a route for /welcome/back, which responds with the string "welcome back"<br/>
4. Optionally, you can share your code here: GitHub Python Practicum 2022<br/>

# 2nd week tasks:
✅ Get a weather report for a city of your liking via API call<br/>
✔️  API doc: https://openweathermap.org/current#name<br/>
✔️  API Key: 60aa068482d6ddc251ae5f53570ac5fb<br/>
✅ Create a route /weather which responds with received data<br/>
✔️  display city name and current temperature in Celsius<br/>
✔️  consider using a template to render and display data<br/>
✅ Optional task – let the user pick a city<br/>

# 3rd  week tasks:
✅ Get geographic coordinates for a city of your liking via an API call<br/>
✔️  API doc: https://openweathermap.org/api/geocoding-api<br/>
✅ Get historical data from dev.meteostat.net via one of these methods:<br/>
✔️  JSON API<br/>
✔️  Python library<br/>
✔️  Bulk data<br/>
✅ Display one year of temperature history - min., max., average<br/>
✔️  Use the graphical form of representation – matplotlib module<br/>
✅ Create a route /weather_history to display data<br/>
✔️  Show city name and chart with temperature data, including legend (names of axis, description of data)<br/>
✔️  In addition, separately display values for min., max. temperature, the date it was recorded, and the average temperature for the whole range.<br/>
✔️  Provide a download link for an Excel document with temperature data (raw data)<br/>
✔️  Provide a download link for a PDF document with a temperature chart (graphical data)<br/>
✅ Additional advanced task: Send notification of the temperature<br/>
✔️  Create a route /notification<br/>
✔️  Possible communication channels:<br/>
✔️ push notification via SIGNL4 or similar service: https://www.signl4.com/<br/>
e-mail notification<br/>
SMS message<br/>
✔️  Trigger the notification by:<br/>
Pushing a button on your webpage<br/>
Setting up a notification when a trigger temperature is reached<br/>

# 4th  week tasks:
Record each weather search in the log file<br/>
✔️  Log: Date, Time, City, Temperature<br/>
✅ Create a route /log to display data for the last 5 searches<br/>
✔️  Think about persistent data. The last 5 searches must be displayed even after flask is restarted<br/>
✅ Create a route /cities<br/>
✔️  Display the current list of cities of interest and their current temperature (updates on list change)<br/>
✔️  Let the user add the city to the list<br/>
✔️  Let the user change list entry (change city name)<br/>
✔️  Let the user delete the city from the list<br/>
✔️  Record add/change/delete events to log file<br/>
✔️  Let the user manually refresh the currently listed cities’ temperature data.<br/>
✔️  The current list and temperature must persist after the flask is restarted<br/>
✔️  Optional advanced task: implement this for multiple users (identified by login)<br/>
