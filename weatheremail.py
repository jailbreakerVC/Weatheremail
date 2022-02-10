import requests, json
import smtplib
import getpass

smtp_object=smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()

email=getpass.getpass('Gib ID: ')
password=getpass.getpass('Password pls')
print(smtp_object.login(email,password))
from_address=input("Enter From Address")

people=[[]]

for person in people:
	print(person[0],"lives in ",person[1],"email id is",person[2])

api_key = input("Enter API KEY")
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
for person in people:
	print('\n')
	print("OUTPUT FOR ",person[0])
	city_name = person[1]
	
# get method of requests module
# return response object
	response = requests.get(complete_url)
# json method of response object
# convert json format data into
# python format data
	x = response.json()
	if x["cod"] != "404":
		y = x["main"]
		current_temperature = y["temp"]
		celcius=current_temperature-273
		current_pressure = y["pressure"]
		current_humidity = y["humidity"]
		z = x["weather"]
		weather_description = z[0]["description"]
		print(" Temperature (in celcius) = " +
						str(celcius) +
			"\n atmospheric pressure (in hPa unit) = " +
						str(current_pressure) +
			"\n humidity (in percentage) = " +
						str(current_humidity) +
			"\n description = " +
						str(weather_description))
		values =str(weather_description)+"  temp="+str(celcius)+"  humidity="+str(current_humidity)
		#print("WEATHER: \n the Temperature is: \n",str(celcius),"The pressure is \n",str(current_pressure),"\nThe temperature is \n",str(current_humidity),"\nDescription of weather \n",str(weather_description))
	else:
		print("City Not Found ")
		values="City not found"
	
	to_address=person[2]
	subject="WEATHER REPORT"
	message=values
	msg="subject: "+subject+"\n"+message
	smtp_object.sendmail(from_address,to_address,msg)	
