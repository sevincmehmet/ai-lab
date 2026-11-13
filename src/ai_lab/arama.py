from ai_lab.etkinlik import Event

# 15) src/ai_lab/arama.py dosyasını aç, Event listesi alan şu fonksiyonları yaz (type hint'li):
#     - sehre_gore(etkinlikler, sehir) -> list[Event]
#     - ucretsizler(etkinlikler) -> list[Event]
#     - fiyat_araligi(etkinlikler, en_az, en_cok) -> list[Event]   (sınırlar dahil)
#     - en_pahali(etkinlikler) -> Event   (boş listede ne olmalı? Karar ver)

def sehre_gore(etkinlikler: list[Event], sehir: str) -> list[Event]:
    """Verilen şehirdeki etkinlikleri döndürür"""
    aranan = sehir.replace("İ", "i").replace("I", "ı").lower()
    return [
        event for event in etkinlikler 
        if event.city.replace("İ", "i").replace("I", "ı").lower() == aranan
    ]

def ucretsizler(etkinlikler: list[Event]) -> list[Event]:
    """Ücretsiz etkinlikleri döndürür."""
    return [event for event in etkinlikler if event.ucretsiz_mi()]

def fiyat_araligi(etkinlikler: list[Event], en_az:float, en_cok:float) -> list[Event]:
    """Belirtilen fiyat aralığındaki etkinlikleri döndürür (sınırlar dahil)."""
    return [event for event in etkinlikler if event.price>=en_az and event.price<=en_cok]

def en_pahali(etkinlikler: list[Event]) -> Event:
    """En pahalı etkinliği döndürür. Liste boşsa hata fırlatır."""
    
    if not etkinlikler:
        raise ValueError("Etkinlik listesi boş")

    return max(etkinlikler, key=lambda event: event.price)
