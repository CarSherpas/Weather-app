from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        api_key = '92841346f0caa84a872bd92299021efd'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        
        if response.get('main') is not None:
            weather_data = {
                'city': city,
                'temperature': round(response['main']['temp']),
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon']
            }
            return render_template('home.html', weather=weather_data)
        else:
            error_msg = 'City not found. Please try again.'
            return render_template('home.html', error=error_msg)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
