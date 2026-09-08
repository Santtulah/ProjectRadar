# 1. Valitaan kevyin mahdollinen Python-versio pohjaksi (käyttöjärjestelmäksi)
FROM python:3.11-slim

# 2. Asetetaan kansion nimi kontin sisällä, jonne koodit laitetaan
WORKDIR /app

# 3. Kopioidaan ENSIN vain requirements.txt (tämä nopeuttaa Dockerin toimintaa)
COPY requirements.txt .

# 4. Asennetaan Python-kirjastot kontin sisälle
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopioidaan KAIKKI loput koodit (api.py, database.py yms) kontin sisälle
COPY . .

# 6. Kerrotaan, että tämä kontti haluaa jutella ulkomaailman kanssa portin 8000 kautta
EXPOSE 8000

# 7. Komento, joka ajetaan kun kontti käynnistyy (vastaa sitä mitä aiemmin kirjoitit terminaaliin)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]