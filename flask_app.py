from flask import Flask,render_template
import requests
import json


app = Flask(__name__)

# data=[
#     {
#         'name':'Audrin',
#         'place': 'kaka',
#         'mob': '7736'
#     },
#     {
#         'name': 'Stuvard',
#         'place': 'Goa',
#         'mob' : '546464'
#     }
# ]

kp_index_url = 'https://services.swpc.noaa.gov/json/planetary_k_index_1m.json'
northern_hemisphere_image = 'https://services.swpc.noaa.gov/images/aurora-forecast-northern-hemisphere.jpg'

url = requests.get(kp_index_url)
text = url.text

data = json.loads(text)

@app.route("/")
def index():
    return render_template('index.html', image=northern_hemisphere_image, data=data)

if __name__ == '__main__':
    app.run(debug=True)
