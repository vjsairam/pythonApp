# Weather Service Frontend
Simple flask app that calls the [weather service backend](../weather-svc) and formats the data in an HTML table.  
Listens on port `5002` and takes a city argument in the URL `/{CITY}`. 

Example: `http://host:5002/toronto`

The weather service backend URL can be set with the environment variable `WEATHER_SVC_URL`. If not present, it defaults to `http://localhost:5003`.

#### Note
If running as a docker container, the internal dns name can be used as the service URL:  
`docker run -d -p 5002:5002 -e WEATHER_SVC_URL=http://host.docker.internal:5003 --name weather-frontend weather_frontend`