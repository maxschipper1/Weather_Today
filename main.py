from flask import Flask, redirect, url_for, render_template, request
import data
import methods

app = Flask(__name__)
#states_of_wind = [ 
#                  "Light air", "Light breeze", "Gentle breeze", "Moderate breeze",
#                   "Fresh breeze", "Strong breeze", "Moderate gale", "Fresh gale", 
#                   "Strong gale", "Whole gale", "Storm", "Hurricane"]

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        location = request.form["location"]
        values = data.get_data(location)

        return render_template("second_page.html", weather=values[1], temp= round(values[2], 1), feel= round(values[3], 1), wind= values[4], dress=methods.dress(values[3]), wind_jacket= methods.wind_jacket(values[4]), rain_coat= methods.rain(values[0]), location= location )
    else:
        return render_template("start_page.html")

if __name__ == "__main__":
    app.run(debug=True)