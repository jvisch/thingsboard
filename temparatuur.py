import requests
import time
import random
from datetime import datetime, timezone, timedelta

# ThingsBoard instellingen
TB_HOST = "http://localhost:8080"
ACCESS_TOKEN = "id8rv89upm207075mxrg"  # Vervang dit met het access token van je device

# Aantal berichten
AANTAL_BERICHTEN = 100
INTERVAL_SECONDEN = 120


def stuur_temperatuur(temperatuur: float, tijdstip_ms: int):
    url = f"{TB_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"
    payload = {
        "ts": tijdstip_ms,
        "values": {
            "temperature": temperatuur
        }
    }
    print(payload)
    response = requests.post(url, json=payload, timeout=5)
    return response.status_code


def main():
    print(f"Versturen van {AANTAL_BERICHTEN} temperatuurberichten naar ThingsBoard...")
    start = datetime.now(timezone.utc) - timedelta(hours=8)
    for i in range(AANTAL_BERICHTEN):
        nu = start + timedelta(seconds=(i*INTERVAL_SECONDEN))
        tijdstip_ms = int(nu.timestamp() * 1000)
        temperatuur = round(random.uniform(18.0, 26.0), 2)

        status = stuur_temperatuur(temperatuur, tijdstip_ms)
        print(f"[{nu.strftime('%Y-%m-%d %H:%M:%S')}] Temperatuur: {temperatuur}°C  →  HTTP {status}")
        print('- '* 40)

    print("Klaar.")


if __name__ == "__main__":
    main()
