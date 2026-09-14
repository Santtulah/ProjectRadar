import requests
from xml.etree import ElementTree as ET
from database import save_agenda
from utils import extract_date_from_title, extract_id_from_link
from classifier import is_relevant_decision



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

        id = extract_id_from_link(link)
        date_match = extract_date_from_title(title)
        date = date_match if date_match else None

        parsed_item = {
            'title': title,
            'link': link,
            'description': description,
            'id': id,
            'date': date,
            'is_relevant': is_relevant_decision(title, description)
        }
        parsed_items.append(parsed_item)
    
    return parsed_items


def run_etl():
    """Tämä on pääfunktio, joka hakee ja tallentaa päätökset tietokantaan."""
    print("Aloitetaan Kuopion päätösten haku...")
    rss_data = fetch_rss_data()

    if rss_data:
        parsed_data = parse_item_metadata(rss_data)
        for item in parsed_data:
            save_agenda(item)
    print("ETL-ajo suoritettu onnistuneesti!")

    



        





