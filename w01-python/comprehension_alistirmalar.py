# COMPREHENSION ALIŞTIRMALARI
# Her görevin altına tek satırlık bir comprehension yaz ve print et.
# for döngüsü + append kullanma; amaç tek satırda çözmek.
events = [
    {"title": "Duman Konseri", "city": "İzmir", "category": "konser", "price": 750, "day": "cumartesi"},
    {"title": "Stand-up Gecesi", "city": "İstanbul", "category": "komedi", "price": 400, "day": "cuma"},
    {"title": "Çocuk Tiyatrosu", "city": "İzmir", "category": "tiyatro", "price": 0, "day": "pazar"},
    {"title": "Caz Akşamı", "city": "Ankara", "category": "konser", "price": 300, "day": "cumartesi"},
    {"title": "Seramik Atölyesi", "city": "İzmir", "category": "atölye", "price": 550, "day": "pazar"},
    {"title": "Hamlet", "city": "İstanbul", "category": "tiyatro", "price": 250, "day": "perşembe"},
    {"title": "Açık Hava Sineması", "city": "Ankara", "category": "sinema", "price": 0, "day": "cuma"},
    {"title": "Rock Festivali", "city": "İstanbul", "category": "konser", "price": 1200, "day": "cumartesi"},
]

sayilar = [3, 8, 15, 22, 7, 10, 41, 6]
kelimeler = ["python", "React", "llm", "Agent", "api", "TypeScript"]


# --- LIST COMPREHENSION ---

# 1) sayilar listesindeki her sayının karesini içeren bir liste oluştur.
print("----------------1----------------")
kareler = [sayi ** 2 for sayi in sayilar]
print(kareler)
kareler2 = list(map(lambda x: x**2, sayilar))
print(kareler2)
kareler_compherehesion = {x: x**2 for x in sayilar}
print(kareler_compherehesion)

# 2) sayilar listesinden sadece çift olanları al.
print("----------------2----------------")
cift = list(filter(lambda x: x%2 == 0, sayilar))
cift_compherehesion = {x for x in sayilar if x%2 == 0}
print(cift)
print(cift_compherehesion)

# 3) Bütün etkinliklerin sadece başlıklarını (title) içeren bir liste oluştur.
print("----------------3----------------")
event_titles = list(map(lambda event :  event["title"], events))
event_titles_compherehesion = [event["title"] for event in events]
print(event_titles)
print(event_titles_compherehesion)

# 4) Sadece İzmir'deki etkinliklerin başlıklarını al.
print("----------------4----------------")
izmir_events = list(filter(lambda event: event["city"] == "İzmir", events))  # .lower() kullanma: "İzmir".lower() -> "i̇zmir"
print(izmir_events)
izmir_event_titles = [event["title"] for event in events if event["city"] == "İzmir"]
print(izmir_event_titles)

# 5) Ücretsiz (price == 0) etkinliklerin başlıklarını al.
print("----------------5----------------")
free_events = list(filter(lambda event: event["price"] == 0 , events))
free_events_title = list(map(lambda event: event["title"], free_events))
free_events_comp = [event["title"] for event in events if event["price"] == 0]
print(free_events_title)
print(free_events_comp)

# 6) Cumartesi günündeki konserlerin başlıklarını al (iki koşul).
print("----------------6----------------")
cmrts_konserleri = list(filter(lambda event: event["day"] == "cumartesi" and event["category"] == "konser", events))
cmrts_konserleri_comp = [event["title"] for event in events if event["day"] == "cumartesi" and event["category"] == "konser"]
print(cmrts_konserleri)
print(cmrts_konserleri_comp)

# 7) kelimeler listesindeki her kelimeyi küçük harfe çevir.
print("----------------7----------------")
kucuk_kelimeler = list(map(lambda kelime: kelime.lower(), kelimeler))
kucuk_kelimeler_comp = [kelime.lower() for kelime in kelimeler]
print(kucuk_kelimeler)
print(kucuk_kelimeler_comp)

# 8) Her etkinlik için "Başlık - Şehir" şeklinde bir metin listesi oluştur (f-string kullan).
print("----------------8----------------")
title_city = list(map(lambda event: f"{event["title"]} - {event["city"]}", events))
title_city_comp = [f"{event["title"]} - {event["city"]}" for event in events ]
print(title_city)
print(title_city_comp)
# 9) Her etkinlik için fiyat 0 ise "Ücretsiz", değilse "Ücretli" yazan bir liste oluştur.
#    İpucu: koşul ifadesi (x if koşul else y) for'dan ÖNCE yazılır.
print("----------------9----------------")
ucret_durumu = list(map(lambda event: "Ücretsiz" if event["price"] == 0 else "Ücretli", events))
print(ucret_durumu)

# --- DICT COMPREHENSION ---

# 10) {başlık: fiyat} şeklinde bir sözlük oluştur.
events_prices = {event["title"] : event["price"] for event in events}
print(events_prices)

# 11) Sadece 500 TL'den pahalı etkinlikler için {başlık: fiyat} sözlüğü oluştur.
# besyuz_ustu = list(filter(lambda event : event["price"]>500 , events))
# baslik_fiyat = {event["title"] : event["price"] for event in besyuz_ustu}
baslik_fiyat = {event["title"]: event["price"] for event in events if event["price"] > 500}
print(baslik_fiyat)

# 12) kelimeler listesinden {kelime: harf_sayısı} sözlüğü oluştur.
sozluk = {kelime : len(kelime) for kelime in kelimeler}
print(sozluk)

# --- SET COMPREHENSION ---

# 13) Etkinliklerin geçtiği şehirleri tekrar etmeyecek şekilde bir set olarak al.
sehirler = {event["city"] for event in events}
print(sehirler)

# 14) Etkinlik kategorilerini set olarak al. Kaç farklı kategori var? (len)
kategoriler = {event["category"] for event in events}
print(kategoriler)
print("Kategori sayısı:", len(kategoriler))

# --- BİRLEŞTİR ---

# 15) Comprehension + sum() ile İstanbul'daki etkinliklerin toplam fiyatını hesapla.
# İçerideki kısım sadece İstanbul'daki fiyatları seçer, sum() ise hepsini toplar
toplam_istanbul_fiyati = sum(event["price"] for event in events if event["city"] == "İstanbul")
print(toplam_istanbul_fiyati)

# 16) Comprehension + max() ile en pahalı etkinliğin fiyatını bul.
#     Bonus: en pahalı etkinliğin BAŞLIĞINI bul (max'ın key parametresine bak).
en_pahali_etkinlik_fiyati = max(event["price"] for event in events)
# 1. Adım: key parametresine lambda vererek EN PAHALI ETKİNLİĞİN KENDİSİNİ (bütün sözlüğü) buluyoruz
en_pahali_etkinlik_sozlugu = max(events, key=lambda event: event["price"])

# 2. Adım: Bulduğumuz sözlüğün içinden sadece başlığı (title) çekiyoruz
en_pahali_baslik = en_pahali_etkinlik_sozlugu["title"]
print(en_pahali_baslik)
print(en_pahali_etkinlik_fiyati)

# 17) {şehir: [o şehirdeki etkinlik başlıkları]} şeklinde bir sözlük oluştur.
#     İpucu: dict comprehension'ın içinde list comprehension kullanabilirsin.
sehir_etkinlikleri = {
    event["city"]: [ e["title"] for e in events if e["city"] == event["city"]] 
    for event in events
}

print(sehir_etkinlikleri)
