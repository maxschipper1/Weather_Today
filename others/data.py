def get_data(location):
    import requests

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=d49e0468dfcac03773f5fc6090fe00a4".format(location)

    res = requests.get(url)

    data = res.json()

    main_weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temp = data["main"]["temp"] - 272.15
    temp_feeling = data["main"]["feels_like"] -272.15
    wind = data["wind"]["speed"]

    values = [main_weather, description, temp, temp_feeling, wind]

    return values

print(get_data("Stockholm"))