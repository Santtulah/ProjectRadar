# Kuopio Decisions - ETL Pipeline & API (Work in Progress)

Tämä projekti on ETL-putki, joka hakee, luokittelee ja tallentaa Kuopion kaupungin rakennus- ja hankepäätöksiä julkisesta RSS-syötteestä.

Tavoitteena on rakentaa täysin automatisoitu ja testattu dataputki, joka kerää hajallaan olevan datan yhteen paikkaan ja jakelee sen myöhemmin rakennettavalle käyttöliittymälle.

## Nykytilanne (Mitä on jo tehty)

- **Mikropalveluarkkitehtuuri:** Järjestelmä on kontitettu ja se koostuu kolmesta Docker-palvelusta (Python Worker, FastAPI, MySQL).
- **Modulaarinen koodi:** I/O-operaatiot ja ydinlogiikka (regex-luokittelu, datan jäsennys) on eriytetty puhtaisiin apufunktioihin testattavuuden parantamiseksi.
- **CI/CD & Laadunvarmistus:** Ydinlogiikka on katettu Pytest-yksikkötesteillä.

## Tulevat ominaisuudet (Roadmap)

- **Frontend / Visualisointi:** Uuden Streamlit-kontin rakentaminen datan visualisointia varten.
- **Pilvi-infra (Deployment):** Koko järjestelmän vieminen julkiseen pilveen (esim. Render/AWS).
- **Lopullinen dokumentaatio:** Tarkat asennusohjeet ja API-dokumentaatio toisia kehittäjiä varten.
