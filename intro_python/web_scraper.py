import requests 
from bs4 import BeautifulSoup

url_string = "https://pokemondb.net/pokedex"
active_url = requests.get(url_string, headers = {'User-Agent': 'Mozilla/5.0'})
html = active_url.content

soup = BeautifulSoup(html, "html.parser")

panel_block = soup.select_one("nav.panel.panel-nav")
print("panel block html")
print(panel_block)
print("----------------------\n\n")

list = []
print("Pokedex titles on PokemonDB.net\n")
for links in panel_block.select("li"):
    a_tag = links.find("a", href = True)
    muted = links.find("small", class_= "text-muted")
    if a_tag and muted:
        href = a_tag["href"]
        title = a_tag.get_text(strip = True)
        region = muted.get_text(strip = True)
        print(f"{title}: {region}")
print("-----------------------\n\n")