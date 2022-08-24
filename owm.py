import requests
import json

units = 'metric' #Celsius
lang = 'ru'
appid = 'OWM API key'
desc_content = {'01d': '☀', '02d': '🌥', '03d': '☁', '04d': '☁', '09d': '🌧', '10d': '🌦', '11d': '🌩', '13d': '🌨', '50d': '🌫',
                '01n': '🌓', '02n': '☁', '03n': '☁', '04n': '☁', '09n': '🌧', '10n': '🌧', '11n': '🌩', '13n': '🌨', '50n': '🌫'}

def show_data(city):
    try: #coordinates
        res = requests.get("http://api.openweathermap.org/data/2.5/weather?",
                params={'lon': city.longitude, 'lat': city.latitude,'units': units, 'lang': lang, 'appid': appid})
        return result(res)
    except:
        try: #city
            response = requests.get("http://api.openweathermap.org/data/2.5/weather?",
                params={'q': city, 'units': units, 'lang': lang, 'appid': appid})     
            return result(response)     
        except Exception as e:
            print(f"Error: {e}")
            return "Введены некорректные данные"
            pass
    
def result(response):
    result = ""
    data = response.json()
    result += (desc_content[data['weather'][0]['icon']]) + " " + str.capitalize(data['weather'][0]['description']) + "\n" #Description
    result += "🌡️ Температура: " + str(data['main']['temp']) + "°C\n" #Temperature
    #result += "⬇️" + str(data['main']['temp_min']) + "°C   " #Min temp
    #result += "⬆️" + str(data['main']['temp_max']) + "°C\n" #Max temp 
    result += "💧 Влажность: " + str(data['main']['humidity']) + "%\n" #Humidity      
    result += "💨 Скорость ветра: " + str(data['wind']['speed']) + " м/с" #Wind
    return result
        