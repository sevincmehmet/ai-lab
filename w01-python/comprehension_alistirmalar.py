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

# 2) sayilar listesinden sadece çift olanları al.

# 3) Bütün etkinliklerin sadece başlıklarını (title) içeren bir liste oluştur.

# 4) Sadece İzmir'deki etkinliklerin başlıklarını al.

# 5) Ücretsiz (price == 0) etkinliklerin başlıklarını al.

# 6) Cumartesi günündeki konserlerin başlıklarını al (iki koşul).

# 7) kelimeler listesindeki her kelimeyi küçük harfe çevir.

# 8) Her etkinlik için "Başlık - Şehir" şeklinde bir metin listesi oluştur (f-string kullan).

# 9) Her etkinlik için fiyat 0 ise "Ücretsiz", değilse "Ücretli" yazan bir liste oluştur.
#    İpucu: koşul ifadesi (x if koşul else y) for'dan ÖNCE yazılır.


# --- DICT COMPREHENSION ---

# 10) {başlık: fiyat} şeklinde bir sözlük oluştur.

# 11) Sadece 500 TL'den pahalı etkinlikler için {başlık: fiyat} sözlüğü oluştur.

# 12) kelimeler listesinden {kelime: harf_sayısı} sözlüğü oluştur.


# --- SET COMPREHENSION ---

# 13) Etkinliklerin geçtiği şehirleri tekrar etmeyecek şekilde bir set olarak al.

# 14) Etkinlik kategorilerini set olarak al. Kaç farklı kategori var? (len)


# --- BİRLEŞTİR ---

# 15) Comprehension + sum() ile İstanbul'daki etkinliklerin toplam fiyatını hesapla.

# 16) Comprehension + max() ile en pahalı etkinliğin fiyatını bul.
#     Bonus: en pahalı etkinliğin BAŞLIĞINI bul (max'ın key parametresine bak).

# 17) {şehir: [o şehirdeki etkinlik başlıkları]} şeklinde bir sözlük oluştur.
#     İpucu: dict comprehension'ın içinde list comprehension kullanabilirsin.


# --- DÜZELT (önceki dosyalarda) ---

# A) Dictionary2.py: input() içinde virgül kullanılmış, f-string ile düzelt.
#    "if secim == '2'" satırını elif yap, 3 (öğrenci ekle) ve 0 (çıkış) seçeneklerini yaz.
# B) Tuple.py: "tuple = (...)" değişkeninin adını değiştir (built-in fonksiyonu eziyor).
# C) main.py: "sum = ..." değişkeninin adını değiştir; string birleştirmeleri f-string'e çevir.
# D) Set.py: "Birleşimde 3 bulunmaz" yorumunu düzelt.
# E) TodoApp.py: listeyi 1'den başlayarak numaralandır (enumerate'in 2. parametresi).
# F) Dosya adlarını snake_case yap: switch-match-case.py -> match_case.py, List.py -> list_ornekleri.py gibi.
#    (PyCharm'da sağ tık -> Refactor -> Rename)
