import requests

api_key = 'bc0addffaf184d0c9d2263041c9511c0'
url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=bc0addffaf184d0c9d2263041c9511c0'


request = requests.get(url)     # creates request object type
content = request.json()    # creates it into a dictionary
for article in content['articles']:
    print(article['title'])
    print(article['description'])
