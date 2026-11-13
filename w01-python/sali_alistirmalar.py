# SALI ALIŞTIRMALARI: fonksiyonlar, type hint, dataclass, modül, pytest
#
# Bölüm 1 ve 2 bu dosyada çözülür.
# Bölüm 3, 4 ve 5 için src/ai_lab/ ve tests/ altında yeni dosyalar açacaksın.
# Çalıştırmak için terminalde: uv run python w01-python/sali_alistirmalar.py


# --- BÖLÜM 1: *args, **kwargs, keyword-only ---

# 1) İstediğin kadar sayı alıp toplamını döndüren toplam() fonksiyonu yaz.
#    toplam(1, 2), toplam(5, 10, 15, 20) ve toplam() üçü de çalışsın.

# 2) etkinlik_ozeti(baslik, **detaylar) yaz. Önce başlığı, sonra her detayı
#    "anahtar: değer" şeklinde alt alta yazdırsın.
#    Örnek çağrı: etkinlik_ozeti("Duman Konseri", sehir="İzmir", fiyat=750)

# 3) fiyat_hesapla(fiyat, *, indirim=0, kdv=0.20) yaz. Önce indirim yüzdesini düş, sonra KDV ekle.
#    fiyat_hesapla(100, indirim=10) çalışsın.
#    fiyat_hesapla(100, 10) çağrısını dene: hangi hatayı veriyor, yorum satırına yaz. * ne işe yarıyor?

# 4) Değiştirilebilir varsayılan argüman tuzağı:
#    def ekle(eleman, liste=[]) yaz, elemanı listeye ekleyip listeyi döndürsün.
#    ekle("a"), ekle("b"), ekle("c") çağrılarını ayrı ayrı yazdır. Ne bekliyordun, ne oldu?
#    Sonra varsayılan değeri None yaparak düzelt.

# 5) Paketten çıkarma: sayılar listesini toplam()'a, bir sözlüğü de etkinlik_ozeti()'ne
#    tek tek yazmadan geçir (* ve ** ile).


# --- BÖLÜM 2: type hint ---

# 6) 1-4'teki bütün fonksiyonlara parametre ve dönüş tipi ekle.
#    İpucu: *args için tek elemanın tipi yazılır (*sayilar: float).

# 7) sehir_basliklari(etkinlikler, sehir) fonksiyonu yaz: verilen şehirdeki başlıkları döndürsün.
#    Tipleri list[dict], str ve list[str] olarak yaz.

# 8) ilk_ucretsiz(etkinlikler) yaz: ilk ücretsiz etkinliğin başlığını döndürsün, yoksa None.
#    Dönüş tipi: str | None

# 9) Bilerek yanlış tipte bir argümanla çağır (ör. sehir yerine sayı ver).
#    Python hata veriyor mu? PyCharm ne diyor? Yorum satırına yaz.
#    (TypeScript'ten farkı burada: tipler çalışırken kontrol edilmiyor.)


# --- BÖLÜM 3: dataclass → src/ai_lab/etkinlik.py ---

# 10) src/ai_lab/etkinlik.py dosyasını aç. Event adında bir dataclass yaz:
#     title, city, category, price, day alanları olsun. price varsayılan olarak 0.
# 11) Event'e ucretsiz_mi() metodu ekle (bool döndürsün).
# 12) Event'e ozet() metodu ekle: "Duman Konseri - İzmir (750 TL)" formatında, ücretsizse "(Ücretsiz)".
# 13) comprehension dosyasındaki events listesini src/ai_lab/veri.py'ye taşı.
#     Sözlük listesini tek satırda Event listesine çevir (** işine yarar).
# 14) frozen=True ile dene: bir etkinliğin fiyatını değiştirmeye çalış. Hangi hatayı aldın?
#     Tuple'daki "değiştirilemez" fikriyle bağlantısını yorum olarak yaz.


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
