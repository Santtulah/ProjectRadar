from utils import extract_date_from_title, extract_id_from_link
from classifier import is_relevant_decision
import datetime
import pytest

def test_date_extraction():
    # Testi dataa, joka sisältää päivämäärän otsikossa
    sample_title = "Kaupunginhallituksen kokous 10.09.2026"
    
    # Kutsutaan extract_date_from_title-funktiota
    extracted_date = extract_date_from_title(sample_title)
    
    # Määritellään odotettu päivämäärä, joka vastaa testidataa
    expected_date = datetime.date(2026, 9, 10)
    
    # Assert that the extracted date matches the expected date
    assert extracted_date == expected_date

def test_date_extraction_invalid_format():
    # Testi dataa, joka sisältää virheellisen päivämäärämuodon otsikossa
    sample_title = "Kaupunginhallituksen kokous 10/09/2026"
    
    extracted_date = extract_date_from_title(sample_title)
    
    # Varmista, että poimittu päivämäärä on None, jos muoto on virheellinen.
    assert extracted_date is None
def test_date_extraction_empty_string():
    # Testi dataa, joka on tyhjä merkkijono
    sample_title = ""
    
    extracted_date = extract_date_from_title(sample_title)
    
    # Varmista, että poimittu päivämäärä on None, jos otsikko on tyhjä.
    assert extracted_date is None

def test_is_relevant_decision_with_matching_keyword():
    title = "Kaupunginhallituksen kokous 10.09.2026"
    description = "Tässä kokouksessa käsitellään kaavamuutosta."
    
    # Kutsutaan is_relevant_decision-funktiota
    result = is_relevant_decision(title, description)
    
    # Varmista, että funktio palauttaa True, koska otsikko sisältää avainsanan "kaavamuutos"
    assert result is True

def test_is_relevant_decision_with_non_matching_keyword():
    title = "Kaupunginhallituksen kokous 10.09.2026"
    description = "Tässä kokouksessa käsitellään yleisiä asioita."
    
    # Kutsutaan is_relevant_decision-funktiota
    result = is_relevant_decision(title, description)
    
    # Varmista, että funktio palauttaa False, koska otsikko ei sisällä avainsanoja
    assert result is False

def test_extract_id_from_link():
    # Testi dataa, joka sisältää linkin, josta ID voidaan poimia
    sample_link = "https://www.kuopio.fi/paatokset?id=12345-67890"
    
    # Kutsutaan extract_id_from_link-funktiota
    extracted_id = extract_id_from_link(sample_link)
    
    # Määritellään odotettu ID, joka vastaa testidataa
    expected_id = "12345-67890"
    
    # Assert that the extracted ID matches the expected ID
    assert extracted_id == expected_id