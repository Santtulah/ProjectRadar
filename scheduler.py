import time
from fetch_rss_data import run_etl

RUN_INTERVAL = 86400  # 24 tuntia sekunteina

print(f"Worker käynnistetty! Data haetaan {RUN_INTERVAL} sekunnin välein.")

while True:
    try:
        run_etl()
    except Exception as e:
        print(f"Virhe ETL-prosessissa: {e}")

    print(f"Worker menee nukkumaan. Seuraava herätys {RUN_INTERVAL} sekunnin kuluttua.")
    time.sleep(RUN_INTERVAL)