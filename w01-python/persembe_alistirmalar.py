# PERŞEMBE ALIŞTIRMALARI: Pydantic -> veriyi doğrulamak
#
# Pydantic = Python'un Zod'u. Dışarıdan gelen veriyi (JSON, API, LLM çıktısı)
# modele sokar: tip yanlışsa düzeltmeye çalışır, düzeltemezse ValidationError fırlatır.
# Hafta 2'de LLM'in döndürdüğü JSON'u tam olarak bununla doğrulayacaksın.
#
# Bölüm 1 ve 2 bu dosyada çözülür.
# Bölüm 3 ve 4 için src/ai_lab/modeller.py, data/events.json ve tests/test_modeller.py açacaksın.
# Çalıştırmak için terminalde: uv run python w01-python/persembe_alistirmalar.py
#
# Kural: dosya her an sonuna kadar ÇÖKMEDEN çalışmalı.
# Bilerek hata gösterdiğin satırları try/except ValidationError içine al.

from datetime import datetime

from pydantic import (
    BaseModel,
    Field,
    TypeAdapter,
    ValidationError,
    field_validator,
    model_validator,
)

from ai_lab.modeller import Event, etkinlikleri_yukle

# --- BÖLÜM 1: BaseModel temelleri ---

# 1) Kisi(BaseModel) yaz: isim: str, yas: int
#    Kisi(isim="Ali", yas=30) oluştur ve print et. Dataclass'tan farkı ne görünüyor?
print("--------------------- 1 ---------------------")


class Kisi(BaseModel):
    isim: str
    yas: int
    sehir: str | None = None


kisi = Kisi(isim="Ali", yas=24)
print(kisi)

# 2) Tip zorlama: Kisi(isim="Ali", yas="30") dene. yas ne oldu, tipi ne? (type(...) ile bak)
#    Sonra Kisi(isim="Ali", yas="otuz") dene -> ValidationError'ı yakala, print(e) ile mesajı oku.
#    (Dataclass bu ikisine de hiç ses çıkarmazdı. Hatırla: "tipler çalışırken kontrol edilmiyo" notun)
print("--------------------- 2 ---------------------")

kisi2 = Kisi(isim="Ali", yas="24")
print(kisi2)
print(
    type(kisi2.yas)
)  # -> <class 'int'>: Pydantic "24"ü int'e çevirdi (dataclass çevirmezdi)

try:
    Kisi(isim="Ali", yas="otuz")  # "otuz" int'e çevrilemez -> ValidationError
except ValidationError as e:
    print(f"HATA: {e}")


# 3) Eksik alan: Kisi(isim="Ali") dene, hatayı yakala.
#    e.errors() ne döndürüyor? İçinden "loc" ve "type" alanlarını bul.
print("--------------------- 3 ---------------------")
try:
    kisi3 = Kisi(isim="Mehmet")
except ValidationError as e:
    hatalar = e.errors()

    for hata in hatalar:
        print(f"Hatalı Alan (loc): {hata['loc']}")
        print(f"Hata Tipi (type): {hata['type']}")

# 4) Sözlükten model:  Kisi.model_validate({"isim": "Veli", "yas": 25})
#    Modelden sözlük:  .model_dump()
#    Modelden JSON:    .model_dump_json()      (JS'te JSON.stringify)
#    JSON'dan model:   Kisi.model_validate_json('{"isim": "Ayşe", "yas": 28}')   (JSON.parse + doğrulama)
print("--------------------- 4 ---------------------")
veri_sozlugu = {"isim": "Mehmet", "yas": 24, "sehir": None}
kisi_from_dict = Kisi.model_validate(veri_sozlugu)
print("1. Sözlükten Model:", kisi_from_dict)

sozluk_hali = kisi_from_dict.model_dump()
print("2. Modelden Sözlük:", sozluk_hali, type(sozluk_hali))

json_metni = kisi_from_dict.model_dump_json()
print("3. Modelden JSON:", json_metni, type(json_metni))

json_veri = '{"isim": "Ayşe", "yas": 28}'
kisi_from_json = Kisi.model_validate_json(json_veri)
print("4. JSON'dan Model:", kisi_from_json)

# 5) Opsiyonel alan: Kisi'ye sehir: str | None = None ekle.
#    sehir vermeden ve vererek iki kişi oluştur. model_dump()'ta ne görünüyor?
print("--------------------- 5 ---------------------")
kisi_yurt = Kisi(isim="Mehmet", yas=3, sehir="Trabzon")
kisi_yurtsuz = Kisi(isim="Dursun", yas=3, sehir=None)
print(kisi_yurt)
print(kisi_yurtsuz)

# 6) İç içe model: Adres(BaseModel) yaz (sehir, ilce). Kisi'nin bir alanı adres: Adres olsun.
#    Kisi.model_validate({"isim": "Ali", "yas": 30, "adres": {"sehir": "İzmir", "ilce": "Bornova"}})
#    İçteki sözlük kendiliğinden Adres'e dönüştü mü? (TS'te iç içe interface gibi, ama doğrulamalı)
print("--------------------- 6 ---------------------")


class Adres(BaseModel):
    sehir: str
    ilce: str


class KisiNested(BaseModel):
    isim: str
    yas: int
    sehir: str | None = None
    adres: Adres


veri_nested = {"isim": "Ali", "yas": 30, "adres": {"sehir": "İzmir", "ilce": "Bornova"}}

kisi_nested = KisiNested.model_validate(veri_nested)
print("İç İçe Model Çıktısı:", kisi_nested)
print("Adres Alanının Tipi:", type(kisi_nested.adres))

# --- BÖLÜM 2: Field ve validator ---

# 7) Field ile kural koy:  from pydantic import Field
#    Urun(BaseModel): ad: str = Field(min_length=2), fiyat: int = Field(ge=0)
#    Urun(ad="A", fiyat=10) ve Urun(ad="Kalem", fiyat=-5) dene. Hata mesajları ne diyor?
#    (Zod'daki z.string().min(2), z.number().min(0) ile aynı)
print("--------------------- 7 ---------------------")


class Urun(BaseModel):
    ad: str = Field(min_length=2)
    fiyat: float = Field(ge=0)


try:
    Urun(ad="A", fiyat=10)
except ValidationError as e:
    hatalar = e.errors()
    for hata in hatalar:
        print(hata)

try:
    Urun(ad="Kalem", fiyat=-5)
except ValidationError as e:
    hatalar = e.errors()
    for hata in hatalar:
        print(hata)


# 8) Tarih: from datetime import datetime
#    Seans(BaseModel): baslik: str, baslangic: datetime
#    Seans(baslik="Konser", baslangic="2026-11-21T20:00:00") -> baslangic'in tipi ne oldu?
#    Sonra baslangic="yarın akşam" dene. Ne oldu?
print("--------------------- 8 ---------------------")


class Seans(BaseModel):
    baslik: str
    baslangic: datetime


try:
    seans = Seans(
        baslik="konser", baslangic="2026-11-21T20:00:00"
    )  # -> başlangıç' ın tipi dateTime oldu
    print(seans)
    seans_yarin_aksam = Seans(baslik="Yarınki konser :)", baslangic="yarın akşam")
    print("seans_yarin_aksam : ", seans_yarin_aksam)
except ValidationError as e:
    hatalar = e.errors()
    for hata in hatalar:
        print(hata)

# 9) field_validator: tek bir alanı kendi kuralınla kontrol et / düzelt.
#    from pydantic import field_validator
#    Sehirli(BaseModel): sehir: str
#    @field_validator("sehir") ile: baştaki/sondaki boşlukları sil, boşsa ValueError fırlat.
#    Sehirli(sehir="  İzmir  ").sehir -> "İzmir" olmalı. Sehirli(sehir="   ") -> hata.
#    İpucu: validator @classmethod olur ve düzeltilmiş değeri RETURN etmek zorunda.
print("--------------------- 9 ---------------------")


class Sehirli(BaseModel):
    sehir: str

    @field_validator(
        "sehir"
    )  # -> Otomatik olarak dışardan yanlış gelen veriyi düzenler
    @classmethod
    def sehir_temizle_ve_kontrol_et(cls, sehir: str):
        sehir = sehir.strip()
        if not sehir:
            raise ValueError("Şehir adı boş olamaz!")
        return sehir


print(Sehirli(sehir=" İzmir   ").sehir)

try:
    print(Sehirli(sehir="    ").sehir)
except ValidationError as e:
    hatalar = e.errors()
    for hata in hatalar:
        print(hata)


# 10) model_validator: İKİ alanı birlikte kontrol et.
#     from pydantic import model_validator
#     Aralik(BaseModel): en_az: int, en_cok: int
#     @model_validator(mode="after") ile: en_cok < en_az ise ValueError fırlat.
#     Aralik(en_az=100, en_cok=50) -> hata.  İpucu: mode="after"da self gelir, sonunda return self.
print("--------------------- 10 ---------------------")


class Aralik(BaseModel):
    en_az: int
    en_cok: int

    @model_validator(mode="after")
    def kontrol_et(self: Aralik) -> Aralik:
        if self.en_cok < self.en_az:
            raise ValueError("en çok değeri en az değerinden daha küçük olamaz!")
        return self


try:
    dogru_aralik = Aralik(en_az=50, en_cok=100)
    print(f"dogru aralik: {dogru_aralik}")

    yanlis_aralik = Aralik(en_az=100, en_cok=50)
    print(f"yanlis aralik: {yanlis_aralik}")
except ValidationError as e:
    hatalar = e.errors()
    for hata in hatalar:
        print(hata)

# --- BÖLÜM 3: Gerçek Event modeli -> src/ai_lab/modeller.py ---

# 11) src/ai_lab/modeller.py aç, Pydantic Event yaz. Alanlar (yol haritasındaki gibi):
#       id: int
#       title: str              -> boş olamaz (min_length=1)
#       city: str
#       venue: str              -> mekan adı
#       starts_at: datetime
#       category: str
#       price_min: int          -> ge=0 (negatif olamaz)
#       price_max: int          -> ge=0
#       url: HttpUrl            -> from pydantic import HttpUrl ("abc" verirsen ne olur?)
#                                  örnek: https://example.com/etkinlik/1
#     Kurallar:
#       - price_max >= price_min olmalı (model_validator, 10'daki gibi)
#     Metodlar (eski Event'tekiler, yeni alanlara göre):
#       - ucretsiz_mi() -> price_max == 0
#       - ozet() -> "Duman Konseri - İzmir, KüçükSahne (750-1200 TL)" / "(Ücretsiz)"
#     NOT: eski src/ai_lab/etkinlik.py'ye DOKUNMA, salı/çarşamba dosyaları ve testler onu kullanıyor.
#     Yeni modeli Cuma FastAPI'de kullanacağız.
print("--------------------- 11 ---------------------")
try:
    konser = Event(
        id=1,
        title="Konser",
        city="Trabzon",
        venue="Akyazı Stadyumu",
        starts_at="2026-11-21T20:00:00",
        category="Konser",
        price_min=1000,
        price_max=20000,
        url="https://example.com/etkinlik/1",
    )
    print(konser)
except ValidationError as e:
    hatalar = e.errors()
    for hata in hatalar:
        print(hata)

# 12) Burada import et ve bir Event oluştur. ozet()'ünü bas, model_dump_json() ile JSON'unu bas.
print("--------------------- 12 ---------------------")
print(konser.ozet())
print(konser.model_dump_json())  # starts_at -> ISO string, url -> düz string

ucretsiz = Event(
    id=2,
    title="Açık Hava Sineması",
    city="Ankara",
    venue="Gençlik Parkı",
    starts_at="2026-11-22T19:00:00",
    category="Sinema",
    price_min=0,
    price_max=0,
    url="https://example.com/etkinlik/2",
)
print(ucretsiz.ozet())


# --- BÖLÜM 4: 30 etkinlik + bozuk veri testleri ---

# 13) data/events.json dosyası: 30 etkinlik, Event modeline uygun bir JSON listesi.
#     TAMAMEN UYDURMA olsun (repo public -> gerçek platform verisi YOK).
#     Gerçekçi görünsün ama uydurma: farklı şehirler, kategoriler, birkaç ücretsiz (0-0) etkinlik.
#     url'ler için https://example.com/etkinlik/1 gibi adresler kullan (example.com bu iş için ayrılmış).
print("--------------------- 13 ---------------------")
print("Eklendi")

# 14) events.json'u oku ve hepsini tek seferde doğrula:
#       from pydantic import TypeAdapter
#       adapter = TypeAdapter(list[Event])
#       with open("data/events.json", encoding="utf-8") as f:
#           etkinlikler = adapter.validate_json(f.read())
#     Kaç etkinlik geldi? En pahalısı hangisi? (max(..., key=...))
#     (Çarşamba'daki with + encoding="utf-8" burada işe yarıyor)
print("--------------------- 14 ---------------------")
adapter = TypeAdapter(list[Event])
with open("data/events.json", encoding="utf-8") as f:
    etkinlikler = adapter.validate_json(f.read())

print(f"{len(etkinlikler)} adet etkinlik var")
en_pahali_etkinlik = max(etkinlikler, key=lambda event: event.price_max)
print(f"En pahalı etkinlik özeti: {Event.ozet(en_pahali_etkinlik)}")


# 15) Bu yüklemeyi src/ai_lab/modeller.py'ye fonksiyon yap:
#       def etkinlikleri_yukle(yol: str = "data/events.json") -> list[Event]
print("--------------------- 15 ---------------------")
print("Tamamlandı")
etkinlikler = etkinlikleri_yukle()
print(len(etkinlikler))

# 16) tests/test_modeller.py aç. Bozuk veri testleri (yol haritası: "Pydantic hangisini yakalıyor?"):
#       - geçerli bir Event oluşuyor
#       - eksik alan          -> ValidationError
#       - yanlış tarih        -> ValidationError  (starts_at="32 Kasım")
#       - negatif fiyat       -> ValidationError
#       - price_max < min     -> ValidationError
#       - bozuk url           -> ValidationError
#       - fiyat "750" string  -> HATA DEĞİL, 750'ye dönüşüyor (bunu da test et!)
#       - etkinlikleri_yukle() 30 etkinlik döndürüyor
#     İpucu: with pytest.raises(ValidationError):
#     Çalıştır: uv run pytest -v   (9 eski + 8 yeni = 17 yeşil olmalı)
print("--------------------- 16 ---------------------")
print("Tamamlandı")

# --- KAPANIŞ ---

# 17) notes/js-vs-python.md'ye ekle:
#     Pydantic = Zod, dataclass vs BaseModel (doğrulama var/yok), tip zorlama ("30" -> 30),
#     model_validate_json = JSON.parse + doğrulama, field_validator vs model_validator.
print("--------------------- 17 ---------------------")
print("Notlar alındı")

# 18) Kontrol:
#       uv run pytest -v                                   (17 yeşil)
#       uv run python w01-python/persembe_alistirmalar.py  (sonuna kadar çökmeden)
#     Bitince bana haber ver, kontrol edelim. Sonra commit + push.
print("--------------------- 18 ---------------------")
print("Tamamlandı")
