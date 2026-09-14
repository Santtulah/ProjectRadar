import re

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


# Esikäännetään lauseke kerran globaalisti (huomaa IGNORECASE jo tässä vaiheessa)
COMPILED_PATTERN = re.compile('|'.join(map(re.escape, keywords)), re.IGNORECASE)
def is_relevant_decision(title: str, description: str) -> bool:

    title = title or ""
    description = description or ""

    title_and_description = f"{title} {description}"

    return bool(COMPILED_PATTERN.search(title_and_description))