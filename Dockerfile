# Valitaan kevyin mahdollinen Python-versio pohjaksi (käyttöjärjestelmäksi)
FROM python:3.11-slim

# Asetetaan kansion nimi kontin sisällä, jonne koodit laitetaan
WORKDIR /app

# opioidaan ENSIN vain requirements.txt (tämä nopeuttaa Dockerin toimintaa)
COPY requirements.txt .

# Asennetaan Python-kirjastot kontin sisälle
RUN pip install --no-cache-dir -r requirements.txt

# Kopioidaan KAIKKI loput koodit (api.py, database.py yms) kontin sisälle
COPY . .

# Kerrotaan, että tämä kontti haluaa jutella ulkomaailman kanssa portin 8000 kautta
EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]