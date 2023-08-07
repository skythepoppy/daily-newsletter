import requests
from send_email import send_email

api_key = 'bc0addffaf184d0c9d2263041c9511c0'
url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=bc0addffaf184d0c9d2263041c9511c0'


# creates request object type
request = requests.get(url)

# creates it into a dictionary
content = request.json()

# access article titles and description
body = ""
for article in content['articles']:
    if article["title"] and article["description"] is not None:
        body = "Subject: Today's News" + "\n" \
               + body + article['title'] + '\n' \
               + article['description'] + "\n" \
               + article['url'] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)