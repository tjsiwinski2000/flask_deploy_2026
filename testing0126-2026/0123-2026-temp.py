import requests
import bs4
report=""
data = requests.get("https://text.npr.org")
soup = bs4.BeautifulSoup(data.text,"html.parser")
articles = soup.find_all(name = "a")
for article in articles:
    t=article.get_text()
    if len(t) > 30:
        report += t +"\n"
print(report)
     
     