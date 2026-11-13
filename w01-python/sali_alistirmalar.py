# SALI ALIŞTIRMALARI: fonksiyonlar, type hint, dataclass, modül, pytest
#
# Bölüm 1 ve 2 bu dosyada çözülür.
# Bölüm 3, 4 ve 5 için src/ai_lab/ ve tests/ altında yeni dosyalar açacaksın.
# Çalıştırmak için terminalde: uv run python w01-python/sali_alistirmalar.py

from ai_lab.etkinlik import Event
from ai_lab.veri import events
from ai_lab.veri import sayilar


# --- BÖLÜM 1: *args, **kwargs, keyword-only ---

# 1) İstediğin kadar sayı alıp toplamını döndüren toplam() fonksiyonu yaz.
#    toplam(1, 2), toplam(5, 10, 15, 20) ve toplam() üçü de çalışsın.
print("--------------------- 1 ---------------------")
def toplam(*args: float) -> float: 
    return sum(args)

print(toplam(1, 2))
print(toplam(5, 10, 15, 20))
print(toplam())

# 2) etkinlik_ozeti(baslik, **detaylar) yaz. Önce başlığı, sonra her detayı
#    "anahtar: değer" şeklinde alt alta yazdırsın.
#    Örnek çağrı: etkinlik_ozeti("Duman Konseri", sehir="İzmir", fiyat=750)
print("--------------------- 2 ---------------------")
def etkinlik_ozeti(baslik : str, **detaylar : str|int) -> dict: 
    return {baslik: detaylar}

print(etkinlik_ozeti("Duman Konseri", sehir="İzmir", fiyat=750))

# 3) fiyat_hesapla(fiyat, *, indirim=0, kdv=0.20) yaz. Önce indirim yüzdesini düş, sonra KDV ekle.
#    fiyat_hesapla(100, indirim=10) çalışsın.
#    fiyat_hesapla(100, 10) çağrısını dene: hangi hatayı veriyor, yorum satırına yaz. * ne işe yarıyor?
print("--------------------- 3 ---------------------")

def fiyat_hesapla(fiyat, *, indirim=0, kdv=0.20): 
    fiyat -= fiyat * (indirim/100)
    fiyat += fiyat * (kdv/100)
    return fiyat

print(fiyat_hesapla(100, indirim=10))
print(fiyat_hesapla(100, indirim=10, kdv=50))
# print(fiyat_hesapla(100, 10)) 
#Traceback (most recent call last):
  #File "/Users/dursunalisevinc/PycharmProjects/PythonProject1/w01-python/sali_alistirmalar.py", line 50, in <module>
   # print(fiyat_hesapla(100, 10))

# 4) Değiştirilebilir varsayılan argüman tuzağı:
#    def ekle(eleman, liste=[]) yaz, elemanı listeye ekleyip listeyi döndürsün.
#    ekle("a"), ekle("b"), ekle("c") çağrılarını ayrı ayrı yazdır. Ne bekliyordun, ne oldu?
#    Sonra varsayılan değeri None yaparak düzelt.
print("--------------------- 4 ---------------------")
def ekle(eleman, liste=[]): 
    liste.append(eleman)
    return liste

print(ekle('a')) # a
print(ekle('b')) # a, b
print(ekle('c')) # a, b, c -> Liste hafızada kalıyor 

def ekle_dogru(eleman, liste=None):
    if liste is None:
        liste = []
    liste.append(eleman)
    return liste

print(ekle_dogru('d')) # a
print(ekle_dogru('e')) # a, b
print(ekle_dogru('f')) # a, b, c -> Liste hafızada kalıyor 


# 5) Paketten çıkarma: sayılar listesini toplam()'a, bir sözlüğü de etkinlik_ozeti()'ne
#    tek tek yazmadan geçir (* ve ** ile).
print("--------------------- 5 ---------------------")
print(toplam(*sayilar))
ornek_sozluk = {"sehir": "İzmir", "fiyat": 750, "category": "konser"}
print(etkinlik_ozeti('Duman Konseri', **ornek_sozluk))

# --- BÖLÜM 2: type hint ---

# 6) 1-4'teki bütün fonksiyonlara parametre ve dönüş tipi ekle.
#    İpucu: *args için tek elemanın tipi yazılır (*sayilar: float).
print("--------------------- 6 ---------------------")
print(" Bölüm 1' deki fonksiyonlara eklendi ")

# 7) sehir_basliklari(etkinlikler, sehir) fonksiyonu yaz: verilen şehirdeki başlıkları döndürsün.
#    Tipleri list[dict], str ve list[str] olarak yaz.
print("--------------------- 7 ---------------------")
def sehir_basliklari(etkinlikler: list[dict], sehir:list[str]) -> list[str]: 
    return {etkinlik["title"] for etkinlik in etkinlikler}

print(sehir_basliklari(events, ["İzmir", "İstanbul"]))

# 8) ilk_ucretsiz(etkinlikler) yaz: ilk ücretsiz etkinliğin başlığını döndürsün, yoksa None.
#    Dönüş tipi: str | None
print("--------------------- 8 ---------------------")
def ilk_ucretsiz(etkinlikler: list[dict]) -> str | None:
    return next((etkinlik["title"] for etkinlik in etkinlikler if etkinlik["price"] == 0), None)

print(ilk_ucretsiz(events))

# 9) Bilerek yanlış tipte bir argümanla çağır (ör. sehir yerine sayı ver).
#    Python hata veriyor mu? PyCharm ne diyor? Yorum satırına yaz.
#    (TypeScript'ten farkı burada: tipler çalışırken kontrol edilmiyor.)
print("--------------------- 9 ---------------------")
# ilk_ucretsiz("etkinlikler") # TypeError: string indices must be integers, not 'str'

# --- BÖLÜM 3: dataclass → src/ai_lab/etkinlik.py ---

# 10) src/ai_lab/etkinlik.py dosyasını aç. Event adında bir dataclass yaz:
#     title, city, category, price, day alanları olsun. price varsayılan olarak 0.
print("--------------------- 10 ---------------------")

# 11) Event'e ucretsiz_mi() metodu ekle (bool döndürsün).
# 12) Event'e ozet() metodu ekle: "Duman Konseri - İzmir (750 TL)" formatında, ücretsizse "(Ücretsiz)".
# 13) comprehension dosyasındaki events listesini src/ai_lab/veri.py'ye taşı.
#     Sözlük listesini tek satırda Event listesine çevir (** işine yarar).
print("--------------------- 13 ---------------------")
# events: list[Event] = [Event(**item) for item in events_dict]
# ilk_nesne = Event(**events[0])
# print(ilk_nesne.ucretsiz_mi())
# print(ilk_nesne.ozet())
events: list[Event] = [Event(**item) for item in events]
for event in events :
    print(event.ozet())

# 14) frozen=True ile dene: bir etkinliğin fiyatını değiştirmeye çalış. Hangi hatayı aldın?
#     Tuple'daki "değiştirilemez" fikriyle bağlantısını yorum olarak yaz.
print("--------------------- 14 ---------------------")
for event in events:
    event.price = 0 #  -> Frozen varsayılan False hepsini değiştirdi :) 
    print(event.ozet())

# --- BÖLÜM 4: modül → src/ai_lab/arama.py ---

# 15) src/ai_lab/arama.py dosyasını aç, Event listesi alan şu fonksiyonları yaz (type hint'li):
#     - sehre_gore(etkinlikler, sehir) -> list[Event]
#     - ucretsizler(etkinlikler) -> list[Event]
#     - fiyat_araligi(etkinlikler, en_az, en_cok) -> list[Event]   (sınırlar dahil)
#     - en_pahali(etkinlikler) -> Event   (boş listede ne olmalı? Karar ver)
# 16) src/ai_lab/__init__.py içindeki main() fonksiyonunda veri.py ve arama.py'den import yap,
#     İzmir'deki etkinliklerin ozet()'lerini yazdır.
#     Çalıştır: uv run ai-lab


# --- BÖLÜM 5: pytest → tests/test_arama.py ---

# 17) Proje kökünde tests/test_arama.py aç, en az 5 test yaz:
#     - İzmir'de 3 etkinlik dönüyor
#     - Olmayan bir şehirde boş liste dönüyor
#     - 2 ücretsiz etkinlik var
#     - fiyat_araligi sınır değerleri dahil ediyor (ör. 300-550 aralığında 300 ve 550 de gelmeli)
#     - en_pahali boş listede senin karar verdiğin davranışı gösteriyor (hata ise pytest.raises)
#     Çalıştır: uv run pytest
# 18) Bir testi bilerek boz, pytest'in hata çıktısını oku, sonra düzelt.
# 19) Bonus: sehre_gore(etkinlikler, "izmir") da İzmir'i bulsun. Önce testini yaz (kırmızı),
#     sonra fonksiyonu düzelt (yeşil). Dikkat: "İzmir".lower() tuzağı burada da var.


# --- KAPANIŞ ---

# 20) notes/js-vs-python.md dosyasını aç, şimdiye kadar öğrendiğin farkları yaz:
#     .lower() ve İ, round(8.5), built-in isimleri ezme, [] / {} / {k: v},
#     if sonda (filtre) ve başta (değer seçer), varsayılan argüman tuzağı, tiplerin çalışırken kontrol edilmemesi.
# 21) Bitince bana haber ver, kontrol edip commit'leyeyim.
