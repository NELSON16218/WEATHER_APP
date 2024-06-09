from flask import Flask, render_template, request
import requests
app= Flask(__name__)

def get_weather_data(city):
   APY_KEY = "6530db6f1031a09258a34de1ed8831c4"
   url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid={APY_KEY}'
   r = requests.get(url).json()
   return r

@app.route("/", methods=['POST','GET'])
def hello():
  if request.method == 'POST':
     ciudad = str(request.form.get('txtciudad') )
     data=get_weather_data(ciudad)
     return render_template('index.html', context = data)
  else:
     return render_template('index.html')

@app.route("/CV_Nelson")
def Nelson():
    return render_template("curriculum.html")


if __name__== '__main__':
    app.run(debug = True)
    