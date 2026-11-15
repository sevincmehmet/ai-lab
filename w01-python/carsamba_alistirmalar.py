# ÇARŞAMBA ALIŞTIRMALARI: hatalar, kendi exception'ın, with, async/await
#
# Bölüm 1, 3 ve 4 bu dosyada çözülür.
# Bölüm 2 için src/ai_lab/ ve tests/ altında dosya açacaksın.
# Çalıştırmak için terminalde: uv run python w01-python/carsamba_alistirmalar.py
#
# Kural: dosya her an sonuna kadar ÇÖKMEDEN çalışmalı.
# Bilerek hata gösterdiğin satırları ya try/except içine al ya da yorum satırı yap.

import asyncio
import time

import httpx

from ai_lab.araclar import zamanla
from ai_lab.arama import en_pahali, sehirde_ara
from ai_lab.etkinlik import Event
from ai_lab.hatalar import EtkinlikBulunamadi, EtkinlikHatasi
from ai_lab.veri import events

ETKINLIKLER = [Event(**e) for e in events]


# --- BÖLÜM 1: try / except / else / finally ---

# 1) int("abc") satırını try/except içine al. ValueError'ı yakala ve
#    "Bu bir sayı değil" yazdır. JS'teki try/catch'ten farkı: hatanın TÜRÜNÜ yazıyorsun.
print("--------------------- 1 ---------------------")
try:
    int("abc")
except ValueError:
    print("Bu bir sayı değil ")

# 2) sayi_al(metin: str) -> int | None yaz.
#    Sayıya çevrilebiliyorsa sayıyı döndürsün, çevrilemiyorsa None.
#    Dene: sayi_al("42"), sayi_al("kırk iki"), sayi_al("")
print("--------------------- 2 ---------------------")


def sayi_al(metin: str) -> int | None:
    try:
        return int(metin)
    except ValueError:
        return None


print(sayi_al("12"))
print(sayi_al("mehmet"))


# 3) bol(a, b) yaz. İki ayrı except bloğu olsun:
#    - ZeroDivisionError -> "Sıfıra bölünmez"
#    - TypeError         -> "Sayı vermelisin"
#    Dene: bol(10, 2), bol(10, 0), bol(10, "2")
print("--------------------- 3 ---------------------")


def bol(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "2. parametre sıfır olamaz."
    except TypeError:
        return "Sayı girin"


print(bol("a", "b"))
print(bol("1", 2))
print(bol(4, 2))
print(bol(4, 0))


# 4) else ve finally: try / except / else / finally bloklarının hepsine print koy.
#    Bir kere hatasız, bir kere hatalı çalıştır. Hangi bloklar hangi sırayla çalıştı? Yorum olarak yaz.
#    (JS'te else bloğu yok. Python'da else = "hata çıkmadıysa çalış".)
print("--------------------- 4 ---------------------")
try:
    print("try bloğu çalıştı")
except ValueError:
    print("except bloğu çalıştı")
else:
    print("else bloğu çalıştı")
finally:
    print("finally bloğu çalıştı")

print("\n--- 2. SENARYO: Hatalı Çalıştırma ---")

try:
    print("1. try bloğu çalıştı (Hata aranıyor...)")
    sonuc = 10 / 0  # ZeroDivisionError hatası patlatıyoruz!
except ZeroDivisionError:
    print("2. except bloğu çalıştı (Hata yakalandı!)")
else:
    print("else bloğu çalıştı")
finally:
    print("3. finally bloğu çalıştı (Her koşulda çalışırım)")

# not : hata varsa else bloğuna girmiyor -> else bloğu oldu da hata kodu çalışmazsa diye var ..
# başarılı olunca yapılacak işi try'a değil else'e koyuyoruz

# 5) en_pahali([]) çağır, ValueError'ı "as e" ile yakala ve print(f"Hata: {e}") yazdır.
#    e'nin içinde ne var? Salı günü raise ederken yazdığın mesaj mı?
print("--------------------- 5 ---------------------")
try:
    print(en_pahali([]))
except ValueError as e:
    print(f"Hata: {e}")  # -> Etkinlik Listesi boş raise mesajı geldi


# 6) Tuzak: her şeyi yakalamak.
#    try içinde bilerek bir isim hatası yap (ör. var olmayan bir değişkeni yazdır: print(etkinlikk))
#    ve "except Exception:" ile yakalayıp "bir şeyler ters gitti" yazdır.
#    Neden kötü bir fikir? Asıl hatayı nasıl gizledi? Yorum olarak yaz.
print("--------------------- 6 ---------------------")
# Kötü hali: ne olduğunu söylemiyor, asıl hatayı (NameError) gizliyor
try:
    print(degisken)
except Exception:
    print("Birşeyler ters gitti")

# Doğrusu: yine yakala ama hatanın türünü ve mesajını göster
try:
    print(degisken)
except Exception as e:
    print(f"Beklenmeyen hata: {type(e).__name__}: {e}")

# --- BÖLÜM 2: kendi exception'ın → src/ai_lab/hatalar.py ---

# 7) src/ai_lab/hatalar.py dosyasını aç, iki sınıf yaz:
#    - EtkinlikHatasi(Exception)            -> projedeki bütün hataların atası
#    - EtkinlikBulunamadi(EtkinlikHatasi)   -> aranan şey yoksa
#    İçleri boş olabilir. Tek satırlık docstring yeter, pass yazmana gerek kalmaz.
#    (JS'teki: class EtkinlikBulunamadi extends Error {})
print("--------------------- 7 ---------------------")
print("Tamamlandı")

# 8) src/ai_lab/arama.py'ye sehirde_ara(etkinlikler, sehir) -> list[Event] ekle:
#    sehre_gore'yi çağırsın, sonuç boşsa raise EtkinlikBulunamadi(f"{sehir} için etkinlik yok").
#    Dikkat: sehre_gore'yi DEĞİŞTİRME. "Sivas'ta boş liste döner" testi hâlâ geçmeli.
#    Burada dene: sehirde_ara(ETKINLIKLER, "Sivas") -> yakala, mesajı yazdır.
print("--------------------- 8 ---------------------")
# sehirde_ara(ETKINLIKLER, "Sivas") # Hata mesajı -> ai_lab.hatalar.EtkinlikBulunamadi: Sivas şehrinde etkinlik bulunamadı olarak çalıştı
print("Tamamlandı")
try:
    sehirde_ara(ETKINLIKLER, "Sivas")
except EtkinlikBulunamadi as e:
    print(f"Hata: {e}")


# 9) Aynı çağrıyı bu sefer "except EtkinlikHatasi" ile yakala (yani atayla).
#    Yine yakalandı mı? Neden? Yorum olarak yaz.
#    (İleride asistan tek bir except EtkinlikHatasi ile projedeki bütün hataları yakalayabilecek.)
print("--------------------- 9 ---------------------")
try:
    sehirde_ara(ETKINLIKLER, "Sivas")
except EtkinlikHatasi as e:
    print(f"Hata: {e}")
# Yine yakalandı: EtkinlikBulunamadi, EtkinlikHatasi'ndan türediği için o da bir EtkinlikHatasi.
# except, hatanın kendi sınıfını VEYA atalarını yakalar (JS'te instanceof'un ata sınıfa da true dönmesi gibi).
# Bu sayede ileride tek bir "except EtkinlikHatasi" projedeki bütün kendi hatalarımızı yakalar.


# 10) tests/test_arama.py'ye 2 test ekle:
#     - sehirde_ara İzmir'de 3 etkinlik döndürüyor
#     - sehirde_ara Sivas'ta EtkinlikBulunamadi fırlatıyor
#       İpucu: with pytest.raises(EtkinlikBulunamadi, match="Sivas"):
#     Çalıştır: uv run pytest -v   (9 yeşil olmalı)
print("--------------------- 10 ---------------------")
print("Tamamlandı")

# --- BÖLÜM 3: with ve context manager ---

# 11) with open(..., "w", encoding="utf-8") ile w01-python/izmir.txt dosyasına
#     İzmir'deki etkinliklerin ozet()'lerini alt alta yaz. Sonra with open(...) ile okuyup ekrana bas.
#     izmir.txt'yi .gitignore'a ekle (çıktı dosyası, repoya girmesin).
#     Neden encoding="utf-8"? "İzmir" ve "Çocuk Tiyatrosu" yüzünden.
print("--------------------- 11 ---------------------")
dosya_yolu = "w01-python/izmir.txt"

izmir_etkinlikleri = sehirde_ara(ETKINLIKLER, "izmir")

with open(dosya_yolu, "w", encoding="utf-8") as f:  # ->write
    f.writelines(etkinlik.ozet() + "\n" for etkinlik in izmir_etkinlikleri)

with open(dosya_yolu, "r", encoding="utf-8") as f:  # -> read
    print(f.read())

# 12) with bloğundan çıktıktan sonra print(f.closed) yazdır. Ne çıktı?
#     with = try/finally'nin kısa yolu: blok bitince (hata çıksa bile) dosyayı kendi kapatıyor.
print("--------------------- 12 ---------------------")
print(f.closed)  # True çıktı kapanmış

# 13) Kendi context manager'ını yaz: zamanla(etiket)
#     from contextlib import contextmanager
#     @contextmanager ile, time.perf_counter() kullanarak. Kullanımı:
#         with zamanla("uyku"):
#             time.sleep(0.5)
#     Çıktı: "uyku: 0.50 sn"
#     İpucu: yield'den önce başlangıcı al, yield'i try/finally içine koy, finally'de süreyi yazdır.
print("--------------------- 13 ---------------------")

with zamanla("uyku"):
    time.sleep(0.5)  # -> Burdaki fonksiyonun kaç saniye çalıştığını yazar.

# 14) zamanla'yı src/ai_lab/araclar.py'ye taşı ve buraya import et.
#     Bölüm 4'te süre ölçmek için bunu kullanacaksın.
print("--------------------- 14 ---------------------")
print("Tamamlandı")

# --- BÖLÜM 4: async / await ---

# 15) async def bekle(isim: str, sn: float) -> str yaz:
#     await asyncio.sleep(sn) yapsın, sonra isim döndürsün.
#     async def sirali() yaz: bekle("a", 1), bekle("b", 1), bekle("c", 1) sırayla await etsin.
#     asyncio.run(sirali()) ile çalıştır, zamanla ile ölç. Kaç saniye sürdü?
#     (JS'ten fark: event loop'u sen başlatıyorsun. asyncio.run olmadan hiçbir şey çalışmaz.)
print("--------------------- 15 ---------------------")


async def bekle(isim: str, sn: float) -> str:
    """Bekleme fonksiyonu"""
    await asyncio.sleep(sn)
    return isim


def sync_bekle(isim: str) -> str:
    """sync bekleme fonksiyonu burda beklemeden geçmesi lazım"""
    return isim


async def sirali():
    """Sıralı çalıştırma için"""
    print(await bekle("a", 1))
    print(await bekle("b", 1))
    print(sync_bekle("c"))  # c bekleme durumunda olmamasına rağmen a ve b' yi bekledi
    print(await bekle("c", 1))


with zamanla("sıralı_islem"):
    asyncio.run(sirali())

# 16) async def paralel() yaz: aynı üç bekle'yi asyncio.gather(...) ile aynı anda çalıştırsın.
#     Ne kadar sürdü? gather ne döndürdü, sıra korundu mu?
#     (asyncio.gather = Promise.all)
print("--------------------- 16 ---------------------")


async def paralel():
    # Üçünü aynı anda başlatıyoruz (JS'teki Promise.all gibi)
    sonuclar = await asyncio.gather(bekle("a", 1), bekle("b", 1), bekle("c", 1))
    print(f"Gather'ın döndürdüğü: {sonuclar}")


with zamanla("paralel_islem"):
    asyncio.run(paralel())

# 17) Tuzak: await'i unut. sirali() içinde bir bekle(...) çağrısının başındaki await'i sil.
#     Ne döndü? Terminalde hangi uyarı çıktı? Yorum olarak yaz, sonra await'i geri koy.
#     (JS'te await'i unutunca Promise gelir. Burada da benzer bir şey var.)
print("--------------------- 17 ---------------------")
# print(bekle("b", 1))
# -> <coroutine object bekle at 0x...> basar (JS'teki Promise {<pending>} gibi)
# -> RuntimeWarning: coroutine 'bekle' was never awaited
# Çağrılabiliyor ama içindeki kod HİÇ çalışmıyor: await etmezsen bekleme de olmuyor.
print("Tamamlandı")

# 18) Gerçek istek. Önce terminalde: uv add httpx
#     import httpx  (dosyanın en üstüne)
#     https://httpbin.org/delay/1 adresi 1 saniye bekleyip cevap veriyor.
#     httpx.AsyncClient ile bu adrese 3 istek at:
#       - önce sırayla (3 ayrı await)
#       - sonra asyncio.gather ile
#     İkisini de zamanla ile ölç, her cevabın status_code'unu yazdır.
#     İpucu: async with httpx.AsyncClient() as client:
#                cevap = await client.get(url)
#     (async with = with'in async hali. Client'ı iş bitince kendi kapatıyor.)
print("--------------------- 18 ---------------------")


async def sirali_istekler():
    url = "https://httpbin.org/delay/1"
    async with httpx.AsyncClient() as client:
        r1 = await client.get(url)
        print(f"Sıralı 1 -> Status: {r1.status_code}")

        r2 = await client.get(url)
        print(f"Sıralı 2 -> Status: {r2.status_code}")

        r3 = await client.get(url)
        print(f"Sıralı 3 -> Status: {r3.status_code}")


# 2. SENARYO: Paralel İstek Atma (Üçü aynı anda başlar, toplam ~1 sn sürer)
async def paralel_istekler():
    url = "https://httpbin.org/delay/1"
    async with httpx.AsyncClient() as client:
        # 3 isteği aynı anda gather içine atıyoruz
        cevaplar = await asyncio.gather(
            client.get(url), client.get(url), client.get(url)
        )

        for r in cevaplar:
            print(f"Paralel -> Status: {r.status_code}")


# --- Çalıştırma ve Ölçüm Kısmı ---

print("--- 1. Sıralı İstekler Başlıyor ---")
with zamanla("Sıralı Toplam Süre"):
    asyncio.run(sirali_istekler())

print("--- 2. Paralel İstekler Başlıyor ---")
with zamanla("Paralel Toplam Süre"):
    asyncio.run(paralel_istekler())

# 19) Hatalar + async: https://httpbin.org/status/500 adresine istek at,
#     cevap.raise_for_status() çağır, httpx.HTTPStatusError'ı yakala, durum kodunu yazdır.
#     Sonra https://httpbin.org/delay/3 adresine timeout=1 ile istek at, httpx.TimeoutException'ı yakala.
#     (Hafta 2'de LLM API'si tam olarak bu iki şekilde patlayacak: 5xx hata ve zaman aşımı.)
print("--------------------- 19 ---------------------")


async def gorev_19():
    async with httpx.AsyncClient() as client:
        # 1. Kısım: 500 Hatası ve raise_for_status
        try:
            url_500 = "https://httpbin.org/status/500"
            cevap = await client.get(url_500)
            cevap.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(f"Yakalandı! HTTP Durum Kodu: {e.response.status_code}")

        # 2. Kısım: Timeout (Zaman Aşımı) Hatası
        try:
            url_timeout = "https://httpbin.org/delay/3"
            await client.get(url_timeout, timeout=1.0)
        except httpx.TimeoutException:
            print("Yakalandı! İstek zaman aşımına uğradı (TimeoutException).")


with zamanla("gorev_19 süre"):
    asyncio.run(gorev_19())

# 20) Bonus: gather'a bir sağlam, bir 500 dönen ve bir zaman aşımına düşen istek ver.
#     Önce normal çalıştır: ne oldu? Sonra return_exceptions=True ekle: sonuç listesinde ne var?
#     Her sonucu isinstance(sonuc, Exception) ile kontrol edip ayrı ayrı yazdır.
print("--------------------- 20 ---------------------")


async def getir(
    client: httpx.AsyncClient, url: str, timeout: float = 5
) -> httpx.Response:
    """İstek at, 4xx/5xx gelirse hata fırlat (httpx 500'ü kendiliğinden hata saymıyo)"""
    cevap = await client.get(url, timeout=timeout)
    cevap.raise_for_status()
    return cevap


URL_SAGLAM = "https://httpbin.org/delay/1"
URL_500 = "https://httpbin.org/status/500"
URL_TIMEOUT = "https://httpbin.org/delay/3"


# a) normal gather -> ilk patlayan hata her şeyi patlatıyo, sağlam isteğin sonucu da çöpe gidiyo
async def gorev_20_a():
    async with httpx.AsyncClient() as client:
        try:
            cevaplar = await asyncio.gather(
                getir(client, URL_SAGLAM),
                getir(client, URL_500),
                getir(client, URL_TIMEOUT, timeout=1),
            )
            print(cevaplar)  # buraya hiç gelmiyo
        except httpx.HTTPError as e:
            # HTTPError hem HTTPStatusError'ın hem TimeoutException'ın atası -> ikisini de yakalar
            print(f"a) gather patladı: {type(e).__name__}")


# b) return_exceptions=True -> hata fırlatmıyo, hatayı da sonuç listesine koyuyo (JS'teki Promise.allSettled)
async def gorev_20_b():
    async with httpx.AsyncClient() as client:
        sonuclar = await asyncio.gather(
            getir(client, URL_SAGLAM),
            getir(client, URL_500),
            getir(client, URL_TIMEOUT, timeout=1),
            return_exceptions=True,
        )

    for sonuc in sonuclar:
        if isinstance(sonuc, Exception):
            print(f"b) hata: {type(sonuc).__name__}")
        else:
            print(f"b) başarılı: {sonuc.status_code}")


with zamanla("gorev_20_a süre"):
    asyncio.run(gorev_20_a())

with zamanla("gorev_20_b süre"):
    asyncio.run(gorev_20_b())

# a) çıktı: HTTPStatusError -> 500 ilk geldi, gather hemen patladı. sağlam isteğin 200'ü kayboldu
# b) çıktı: başarılı: 200 / hata: HTTPStatusError / hata: ReadTimeout -> sıra korundu, hiçbiri kaybolmadı
# Agent 3 aracı aynı anda çağırıp biri patlarsa -> b) ile diğer ikisinin sonucunu kullanmaya devam ederim


# --- KAPANIŞ ---

# 21) notes/js-vs-python.md'ye bugün öğrendiklerini ekle:
#     try/catch vs try/except (hata türü yazmak), else bloğu, except Exception tuzağı,
#     kendi exception sınıfı + ata ile yakalamak, with = try/finally,
#     asyncio.run, gather = Promise.all, await'i unutunca ne oluyor.
print("--------------------- 21 ---------------------")
print("Tamamlandı")


# 22) Kontrol:
#       uv run pytest -v                                    (9 yeşil)
#       uv run python w01-python/carsamba_alistirmalar.py   (sonuna kadar çökmeden)
#     Bitince bana haber ver, kontrol edelim. Sonra commit + push.
print("--------------------- 22 ---------------------")
print("Tamamlandı")
