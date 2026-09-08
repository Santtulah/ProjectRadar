import requests
from xml.etree import ElementTree as ET
# from bs4 import BeautifulSoup
import re
import datetime
from database import get_db_connection, save_agenda


keywords = [
    # Projects / development
    "hanke",
    "hankesuunnitelma",
    "hankekokonaisuus",
    "kehittämishanke",
    "kehittämisprojekti",
    "projekti",
    "kehittäminen",
    "kehittämistoimenpide",
    "toteutussuunnitelma",
    "toimenpideohjelma",
    "investointi",
    "investointihanke",
    "rakennushanke",
    "rakentaminen",
    "rakennuttaminen",

    # Procurement
    "hankinta",
    "hankintapäätös",
    "hankintamenettely",
    "hankintaprosessi",
    "kilpailutus",
    "tarjouskilpailu",
    "tarjouspyyntö",
    "tarjous",
    "toimittaja",
    "palveluhankinta",
    "tavarahankinta",
    "urakka",
    "urakkatarjous",
    "urakkasopimus",

    # Contracts / agreements
    "sopimus",
    "sopimusluonnos",
    "sopimuksen tekeminen",
    "sopimuksen hyväksyminen",
    "yhteistyösopimus",
    "palvelusopimus",
    "hankintasopimus",
    "puitejärjestely",
    "puitesopimus",
    "käyttösopimus",
    "aiesopimus",

    # Planning / construction
    "asemakaava",
    "asemakaavan",
    "yleiskaava",
    "kaavamuutos",
    "kaavoitus",
    "kaavaehdotus",
    "kaavaluonnos",
    "suunnittelu",
    "suunnitteluhanke",
    "rakennuslupa",
    "infrastruktuuri",
    "kunnallistekniikka",
    "katusuunnitelma",
    "liikennesuunnitelma",
    "yleissuunnitelma",

    # Money / investment
    "määräraha",
    "lisämääräraha",
    "talousarvio",
    "talousarviomuutos",
    "investointimääräraha",
    "investointiohjelma",
    "investointisuunnitelma",
    "rahoitus",
    "rahoituspäätös",
    "rahoitushakemus",
    "avustus",
    "hankemääräraha",

    # Future / preparation
    "suunnitelma",
    "suunnitteilla",
    "suunnitellaan",
    "valmistelu",
    "valmistellaan",
    "käynnistäminen",
    "käynnistää",
    "käynnistetään",
    "toteuttaminen",
    "toteuttaa",
    "toteutetaan",
    "tuleva",
    "tulevaisuudessa",
    "esitys",
    "ehdotus",
    ]

def fetch_rss_data():
    rss_url = "https://kuopio.oncloudos.com/cgi/DREQUEST.PHP?page=rss/meetingitems&show=30"

    

    try:
        response = requests.get(rss_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        root = ET.fromstring(response.content)

        items = []

        for item in root.findall('.//item')[:5]:
            data = {
                'title': item.findtext('title'),
                'link': item.findtext('link'),
                'description': item.findtext('description')
            }
            items.append(data)
        return items
                
    except Exception as e:
        print(f"An error occurred while fetching RSS feed: {e}")
        return []

def parse_item_metadata(items: list):

    parsed_items = []

    for item in items:
        title = item.get('title', 'No Title')
        link = item.get('link', 'No Link')
        description = item.get('description', 'No Description')

        id = re.search(r'id=(\d+-\d+)', link) if link else None
        date_match = re.search(r'(\d{2}\.\d{2}\.\d{4})', title) if title else None
        try:
            date = datetime.datetime.strptime(date_match.group(1), '%d.%m.%Y').date() if date_match else None
        except ValueError:
            date = None

        parsed_item = {
            'title': title,
            'link': link,
            'description': description,
            'id': id.group(1) if id else None,
            'date': date,
            'is_relevant': is_relevant_decision(title, description)
        }
        parsed_items.append(parsed_item)
    
    return parsed_items



# Esikäännetään lauseke kerran globaalisti (huomaa IGNORECASE jo tässä vaiheessa)
COMPILED_PATTERN = re.compile('|'.join(map(re.escape, keywords)), re.IGNORECASE)
def is_relevant_decision(title: str, description: str) -> bool:

    title = title or ""
    description = description or ""

    title_and_description = f"{title} {description}"

    return bool(COMPILED_PATTERN.search(title_and_description))


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    rss_data = fetch_rss_data()

    if rss_data:
        parsed_data = parse_item_metadata(rss_data)

        for item in parsed_data:
            save_agenda(item)



        





