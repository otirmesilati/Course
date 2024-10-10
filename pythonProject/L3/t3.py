import requests

response = requests.get("https://youtube.com")
if response.status_code == 200:
    print("youtube")
