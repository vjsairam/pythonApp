from flask import Flask
import requests
import json
import boto3
import time

app = Flask(__name__)

AWS_REGION = "us-east-2"
S3_BUCKET_NAME = "pyweather_data"

s3_client = boto3.client("s3", region_name=AWS_REGION)
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "weather_data_"+timestr+".txt"

@app.route('/')
def index():
    return 'City required in URL request /{CITY}'

@app.route('/<city>')
def weather(city):
    locationEndpoint = 'https://www.metaweather.com/api/location/search/?query={}'.format(city)

    try:
        locationData = requests.get(locationEndpoint)
    except:
        return 'Metaweather service not available/reachable'

    if locationData.text == '[]':
        return 'Error: City not found'
    else:
        cityId = locationData.json()[0]["woeid"]

        weatherEndpoint = 'https://www.metaweather.com/api/location/{}'.format(cityId)
        weatherData = requests.get(weatherEndpoint).json()

        weather_data = []
        for date in weatherData['consolidated_weather']:
            weather_data.append({'date': date['applicable_date'], 'temperature': date['the_temp'], 'weather_state': date['weather_state_name']})
        ###Enable the below lines to write the data to a file and push it to S3    
        #with open(filename, 'x') as f:
        #    f.write(str(weather_data))
        #s3_client.upload_file(filename, S3_BUCKET_NAME, filename)
        return json.dumps(weather_data)
 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
