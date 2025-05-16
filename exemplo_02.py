import requests
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=fXOvLdEiLmX1erJXXKc76fYGWNKrxXCaR5HN71w5"
response = requests.get(url)
print(response.json())