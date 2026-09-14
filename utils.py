
import re
import datetime

def extract_date_from_title(title: str):

    date_match = re.search(r'(\d{2}\.\d{2}\.\d{4})', title) if title else None
    try:
        date = datetime.datetime.strptime(date_match.group(1), '%d.%m.%Y').date() if date_match else None
    except ValueError:
        date = None
    return date

def extract_id_from_link(link: str):
    id = re.search(r'id=(\d+-\d+)', link) if link else None
    return id.group(1) if id else None