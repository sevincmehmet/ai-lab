# JS'ten Python'a -> kafama takılanlar

JS'ten geliyorum, Python'da beni şaşırtan / yakan şeyleri buraya yazıyorum. Her hafta eklenecek.

---

## 1. "İzmir".lower() -> "izmir" DEĞİL

```python
"İzmir".lower()  # -> "i̇zmir"  (i + üstünde ayrı bi nokta karakteri)
"İzmir".lower() == "izmir"  # -> False 
```

- Türkçe büyük İ küçültülünce araya görünmez bi nokta ekliyo -> karşılaştırma tutmuyo
- comprehension'da İzmir filtresi boş liste döndü, sebebi buymuş
- çözüm -> önce elle değiştir sonra lower: `.replace("İ", "i").replace("I", "ı").lower()`
- şehir aramalarında kesin karşıma çıkar, unutma

## 2. round(8.5) -> 8 

```python
round(9.5)  # 10
round(8.5)  # 8  ???
```

- yarımları en yakın ÇİFT sayıya yuvarlıyo (banker's rounding)
- JS'te Math.round(8.5) -> 9, burda 8. fiyat hesabında dikkat

## 3. Built-in isimleri değişken yapma

```python
tuple = (1, 2, 3)   # artık tuple() fonksiyonu gitti 
sum = a + b         # artık sum() da gitti
```

- JS'te `Array = ...` yazmak gibi bi şey
- list, dict, set, tuple, sum, max, min, id, input -> bunlar YASAK isim
- dosya adı da aynı -> list.py, set.py açma, `_ornekleri` ekle

## 4. Parantez = tip

```python
[x for x in sayilar]        # liste -> sıra korunur
{x for x in sayilar}        # set -> tekrar yok, SIRA YOK
{x: x**2 for x in sayilar}  # sözlük
```

- çift sayılarda yanlışlıkla `{}` yazdım, sıra karıştı. liste sandım set çıktı :)

## 5. Comprehension'da if nereye yazılır

```python
[e["title"] for e in events if e["price"] == 0]                  # if SONDA -> filtreler
["Ücretsiz" if e["price"] == 0 else "Ücretli" for e in events]   # if BAŞTA -> değer seçer
```

- sonda olan eleman atıyo, başta olan her elemana bi değer veriyo
- JS'te `.filter().map()` diye 2 adım, burda tek satır

## 6. map/filter yerine comprehension

- JS refleksiyle `list(map(lambda ...))` yazdım, çalışıyo ama Python'cası comprehension
- filter + map = 2 satır, comprehension = 1 satır. daha okunaklı

## 7. Varsayılan argüman tuzağı

```python
def ekle(eleman, liste=[]):
    liste.append(eleman)
    return liste

ekle("a")  # ['a']
ekle("b")  # ['a', 'b']  ???  -> liste hafızada kalıyo
```

- varsayılan liste fonksiyon BİR KERE oluşurken yaratılıyo, her çağrıda aynı liste
- çözüm -> `liste=None` yap, içerde `if liste is None: liste = []`

## 8. Tipler çalışırken kontrol edilmiyo

```python
def sehir_basliklari(etkinlikler: list[dict], sehir: str) -> list[str]: ...
sehir_basliklari(events, 123)  # Python ses çıkarmıyo
```

- TypeScript'te derlerken patlar, burda tip sadece süs -> PyCharm uyarıyo o kadar
- yanlış tip verince hata ancak kod o satıra gelince patlıyo

## 9. `*` -> keyword-only

```python
def fiyat_hesapla(fiyat, *, indirim=0, kdv=0.20): ...
fiyat_hesapla(100, indirim=10)  # ✅
fiyat_hesapla(100, 10)          # ❌ TypeError: takes 1 positional argument but 2 were given
```

- `*`dan sonrakiler isimle verilmek ZORUNDA. 10 neydi indirim mi kdv mi karışmasın diye

## 10. `*` ve `**` ile paketten çıkarma

```python
toplam(*sayilar)                  # JS: toplam(...sayilar)
Event(**sozluk)                   # JS: { ...sozluk } gibi ama isimle eşliyo
```

- `**` alanları isimle eşlediği için sıra önemli değil

## 11. Event vs event -> TEK HARF

```python
max(etkinlikler, key=lambda event: Event.price)  # ❌ hep 0 -> hep ilk eleman
max(etkinlikler, key=lambda event: event.price)  # ✅
```

- büyük E = sınıf (kalıp), varsayılan fiyatı 0
- küçük e = o anki etkinlik
- hata vermiyo, sessizce yanlış sonuç veriyo. kafayı yiyecektim, test yakaladı 

## 12. dataclass = TS interface + class

```python
@dataclass(frozen=True)
class Event:
    title: str
    price: int = 0
```

- alanlara `e["city"]` değil `e.city` -> sözlükten gelince karıştırıyosun
- `frozen=True` -> değiştirmeye çalışınca `FrozenInstanceError`. tuple'daki değiştirilemez olay

## 13. Import'ta src yazılmıyo

```python
from src.ai_lab.veri import events  # ❌ ModuleNotFoundError
from ai_lab.veri import events      # ✅
```

- src sadece klasör, paket adı ai_lab. JS'teki `@/lib/...` alias'ı gibi
- `__init__.py` = klasörün index.js'i
- `uv run ai-lab` -> pyproject.toml'daki `ai-lab = "ai_lab:main"` -> `__init__.py`'deki main()

## 14. Test yazmak sandığım kadar zor değilmiş

```python
def test_en_pahali_rock_festivali():
    sonuc = en_pahali(ETKINLIKLER)
    assert sonuc.title == "Rock Festivali"
```

- `test_` ile başla -> fonksiyonu çağır -> `assert` ile beklediğini söyle. bu kadar
- hata bekliyosan -> `with pytest.raises(ValueError):`
- önce kırmızı (test yaz) sonra yeşil (kodu düzelt) -> izmir küçük harf bonusunu böyle yaptım
- `uv run pytest -v`

## 15. `"a" and "b" in liste` -> ikisini birden KONTROL ETMİYO

```python
assert "Caz Akşamı" and "Seramik Atölyesi" in basliklar   # ❌ sadece Seramik'e bakıyo
# Python bunu şöyle okuyo: "Caz Akşamı" and ("Seramik Atölyesi" in basliklar)
# boş olmayan string her zaman True -> ilk kısım hiçbi şey test etmiyo, test yine yeşil

assert "Caz Akşamı" in basliklar          # ✅ ayrı ayrı yaz
assert "Seramik Atölyesi" in basliklar
```

- JS'te `"a" && arr.includes("b")` yazmakla aynı tuzak
- yeşil test != doğru test. test geçiyosa bi kere de bozup kırmızı yandığını gör

---

## 16. `"1" / 2` -> JS'te 0.5, Python'da TypeError

```python
"1" / 2        # ❌ TypeError: unsupported operand type(s) for /: 'str' and 'int'
int("1") / 2   # ✅ 0.5 -> çevirmeyi kendin yapıcaksın
```

- JS sessizce string'i sayıya çeviriyo (`"1" / 2 === 0.5`), Python tahmin etmiyo, hata veriyo
- iyi bi şey aslında: yanlış tip erken patlıyo, sessizce saçma sonuç üretmiyo
- dışardan gelen veri (input, form, API) string gelir -> önce `int()` / `float()`, hata ihtimali varsa `try/except ValueError`

---

## 17. try/catch vs try/except -> hata türünü yazıyosun

```python
try:
    sayi = int(metin)
except ValueError:          # JS'te catch (e) her şeyi yakalar, burda türünü seçiyosun
    print("sayı değil")
else:                       # JS'te yok -> hata ÇIKMAZSA çalışır
    print(sayi * 2)
finally:                    # JS'teki finally ile aynı -> her durumda çalışır
    print("bitti")
```

- `except Exception:` yazıp her şeyi yakalamak tuzak -> `NameError` gibi kendi yazım hatamı da yutuyo, "bir şeyler ters gitti" deyip geçiyo
- yakalıyosam en azından türünü ve mesajını bas: `print(f"{type(e).__name__}: {e}")`

---

## 18. Kendi exception'ım + ata ile yakalamak

```python
class EtkinlikHatasi(Exception):              # JS: class EtkinlikHatasi extends Error {}
    """Projedeki bütün hataların atası"""

class EtkinlikBulunamadi(EtkinlikHatasi):
    """Aranan şey yoksa"""

try:
    sehirde_ara(ETKINLIKLER, "Sivas")
except EtkinlikHatasi as e:                   # ata ile yakalayınca çocuklar da yakalanıyo
    print(f"Hata: {e}")
```

- içleri boş olabiliyo, docstring yeter, `pass`'e gerek yok
- testte: `with pytest.raises(EtkinlikBulunamadi, match="Sivas"):`

---

## 19. with = try/finally'nin kısa yolu

```python
with open("izmir.txt", "w", encoding="utf-8") as f:
    f.write("...")
print(f.closed)   # True -> blok bitince (hata çıksa bile) kendi kapattı
```

- `encoding="utf-8"` her zaman yaz -> İ, Ç, ş bozulmasın
- kendi context manager'ım: `@contextmanager` + `yield` -> yield'den öncesi girişte, `finally` çıkışta çalışıyo (`zamanla` böyle yazıldı, `ai_lab/araclar.py`)
- JS'te birebir karşılığı yok, en yakını `try { } finally { x.close() }` ya da yeni `using`

---

## 20. async: event loop'u ben başlatıyorum

```python
async def bekle(isim: str, sn: float) -> str:
    await asyncio.sleep(sn)
    return isim

asyncio.run(main())   # JS'te event loop hazır, Python'da asyncio.run olmadan HİÇBİR ŞEY çalışmaz
```

- `bekle("b", 1)` -> await'i unutunca `<coroutine object ...>` döner (JS'teki `Promise {<pending>}`)
- uyarı: `RuntimeWarning: coroutine 'bekle' was never awaited` -> içindeki kod hiç çalışmadı
- `async with httpx.AsyncClient() as client:` -> with'in async hali, client'ı iş bitince kapatıyo

---

## 21. gather = Promise.all

```python
sonuclar = await asyncio.gather(bekle("a", 1), bekle("b", 1), bekle("c", 1))
# ['a', 'b', 'c'] -> sıra korunuyo, hangisi önce biterse bitsin
```

- sıralı: toplam süre = sürelerin TOPLAMI (1+1+1 = 3 sn)
- paralel: toplam süre = EN UZUN sürenin kendisi (~1 sn)
- aslında aynı anda 3 iş yapmıyo: istek atıyo, cevabı beklerken diğerini atıyo -> beklemeler üst üste biniyo. JS event loop'uyla aynı
- o yüzden async API / LLM / DB gibi BEKLEME olan işte hızlandırır, hesaplama ağır işte hızlandırmaz
- gerçek ölçüm (httpbin delay/1 x3): sıralı 3.94 sn, paralel 1.53 sn

---

## 22. return_exceptions=True = Promise.allSettled

```python
sonuclar = await asyncio.gather(..., return_exceptions=True)
for sonuc in sonuclar:
    if isinstance(sonuc, Exception):
        print(f"hata: {type(sonuc).__name__}")
    else:
        print(f"başarılı: {sonuc.status_code}")
```

- normal gather: ilk hata hepsini patlatıyo, sağlam sonuçlar da kayboluyo (`Promise.all` gibi)
- `return_exceptions=True`: hata da listeye sonuç olarak giriyo, hiçbiri kaybolmuyo
- httpx 500'ü hata SAYMIYO -> `cevap.raise_for_status()` çağırmazsam normal cevap gibi döner
- `timeout=1` vermezsem varsayılan 5 sn -> delay/3 sorunsuz geçti, timeout yemedi
- LLM API'si tam bu iki şekilde patlıyacak: 5xx (`HTTPStatusError`) ve zaman aşımı (`TimeoutException`). ikisinin atası `httpx.HTTPError`

---

### Bonus
- satır sonuna `;` gerek yok
- string birleştirme yerine f-string -> `f"{isim} {yas} yaşında"` (JS template literal)
- değişken adları snake_case -> `yagmurlu_mu`, `yagmurluMu` değil
- `next((... for ...), None)` -> ilk eşleşeni bul, yoksa None. JS'teki `.find()`
