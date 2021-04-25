import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experiencetemperature':2, 'pressure':9, 'hummidity':6})

print(r.json())
