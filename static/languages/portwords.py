from bs4 import BeautifulSoup
import requests

#Be aware here that I used the dot notation to make the request object a TEXT object.
html_doc = requests.get("https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/BrazilianPortuguese_wordlist").text
soup = BeautifulSoup(html_doc, 'html.parser')

with open("portuguese.txt","w") as file:
    for link in soup.find_all('span'):
        if link.has_attr("lang"):
            file.write("{}\n".format(link.get_text()))
