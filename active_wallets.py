import requests
from collections import Counter
import json

# BASE RPC veya Basescan API ayarları
API_URL = "https://api.basescan.org/api"
API_KEY = "YOUR_BASESCAN_API_KEY"  # Kendi API anahtarınızı girin

def get_transactions(page=1, offset=100):
    params = {
        "module": "account",
        "action": "txlist",
        "address": "",  # Adres belirtmeyeceğiz, toplu tarama için başka endpoint gerekir
        "startblock": 0,
        "endblock": 99999999,
        "page": page,
        "offset": offset,
        "sort": "desc",
        "apikey": API_KEY
    }
    # Bu fonksiyon sadece örnek, gerçek toplu tarama için Dune Analytics veya özel bir API gerekir
    return []

def main():
    print("Base ağında en aktif cüzdanlar analiz ediliyor...")

    # Örnek: Hazır veriyle simülasyon
    addresses = [
        "0x111...", "0x222...", "0x111...", "0x333...", "0x222...", "0x111...", "0x444...",
        "0x555...", "0x333...", "0x222...", "0x666...", "0x777...", "0x333...", "0x888..."
    ]
    counter = Counter(addresses)
    most_common = counter.most_common(10)

    # Sonuçları kaydet
    with open("active_wallets.json", "w") as f:
        json.dump(most_common, f, indent=2)
    print("Sonuçlar active_wallets.json dosyasına kaydedildi.")

if __name__ == "__main__":
    main()