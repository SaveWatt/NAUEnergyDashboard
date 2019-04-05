import requests

def day1():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=ec447c97b1d6b713f803898111798f50'
    city = 'Flagstaff'
    r = requests.get(url.format(city)).json()

    city_weather = {
        'temperature': r['list'][0]['main']['temp'],
        'description': r['list'][0]['weather'][0]['description'],
        'icon': r['list'][0]['weather'][0]['icon']
    }
    return city_weather

def day2():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=ec447c97b1d6b713f803898111798f50'
    city = 'Flagstaff'
    r = requests.get(url.format(city)).json()

    city_weather = {
        'temperature': r['list'][8]['main']['temp'],
        'description': r['list'][8]['weather'][0]['description'],
        'icon': r['list'][8]['weather'][0]['icon']
    }
    return city_weather

def day3():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=ec447c97b1d6b713f803898111798f50'
    city = 'Flagstaff'
    r = requests.get(url.format(city)).json()

    city_weather = {
        'temperature': r['list'][16]['main']['temp'],
        'description': r['list'][16]['weather'][0]['description'],
        'icon': r['list'][16]['weather'][0]['icon']
    }
    return city_weather
