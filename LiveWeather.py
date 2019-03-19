import requests, json 

api_key = "5bef21214a0df068f1566e469e0ba750"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ") 

 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 


response = requests.get(complete_url) 


x = response.json() 


if x["cod"] != "404": 

	
	y = x['main'] 

	
	current_temperature = y["temp"]-273


	current_pressure = y["pressure"] 

	
	current_humidity = y["humidity"] 
	z = x["weather"] 
	weather_description = z[0]["description"] 

	print(" Temperature (in celsius) = " +
					str(current_temperature) +
		"\n Atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n Humidity (in percentage) = " +
					str(current_humidity) +
		"\n Description = " +
					str(weather_description)) 

else: 
	print(" City Not Found ") 

