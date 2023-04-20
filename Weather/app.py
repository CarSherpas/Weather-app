import requests
from datetime import datetime
from flask import Flask, render_template, request

API_KEY = '92841346f0caa84a872bd92299021efd'  # Replace with your OpenWeatherMap API key

app = Flask(__name__)

@app.template_filter('timestamp_to_datetime')
def timestamp_to_datetime(value):
    return datetime.utcfromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S')

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    weather_data = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        
        if weather_data is None:
            error = 'Error: Could not fetch weather data. Please try again.'

    return render_template('index.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
