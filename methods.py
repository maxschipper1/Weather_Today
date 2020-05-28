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