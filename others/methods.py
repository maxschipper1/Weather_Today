def dress(temp):
    if temp <= 0:
        return "really warm"
    elif 10 > temp >= 0:
        return "warm"
    elif 20 > temp >= 10:
        return "kind of warm, like a hoodie"
    elif temp >= 20:
        return "lightly"

def wind_jacket(wind):
    if wind >= 8:
        return "and use a wind blocking jacket"
    else:
        return ""

def rain(rain):
    if rain == "Rain":
        return "and remeber to bring a raincoat!"
    else:
        return ""

def type_of_wind(wind):
    if wind <= 0.5:
        return "No wind"
    elif 0.5 < wind <= 1.5:
        return "Light air"
    elif 1.5 < wind <= 3:
        return "a Light breeze"
    elif 3 < wind <= 5:
        return "a Gentle breeze"
    elif 5 < wind <= 8:
        return "a Moderate breeze"
    elif 8 < wind <= 10.5:
        return "a Fresh breeze"
    elif 10.5 < wind <= 13.5:
        return "a Strong breeze"
    elif 13.5 < wind <= 16.5:
        return "a Moderate gale"
    elif 16.5 < wind <= 20:
        return "a Fresh gale"
    elif 20 < wind <= 23.5:
        return "a Strong gale"
    elif 23.5 < wind <= 27.5:
        return "a Whole gale"
    elif 27.5< wind <= 31.5:
        return "a Storm"
    elif 31.5 < wind:
        return "a Hurricane"

print(type_of_wind(10))

    