# Valitaan kevyin mahdollinen Python-versio pohjaksi (käyttöjärjestelmäksi)
FROM python:3.11-slim

# Asetetaan kansion nimi kontin sisällä, jonne koodit laitetaan
WORKDIR /app

# Kopioidaan ENSIN vain requirements.txt (tämä nopeuttaa Dockerin toimintaa)
COPY requirements.txt .

# Asennetaan Python-kirjastot kontin sisälle
RUN pip install --no-cache-dir -r requirements.txt

# Kopioidaan KAIKKI loput koodit kontin sisälle
COPY . .

# Kerrotaan, että tämä kontti haluaa jutella ulkomaailman kanssa portin 8080 kautta
EXPOSE 8080

# Määritellään suoritettava komento ja oikea tiedostopolku
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py", "--server.port=8080", "--server.address=0.0.0.0"]