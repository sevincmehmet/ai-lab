# CUMA ALIŞTIRMALARI: FastAPI -> etkinlik verisini API olarak sun

FastAPI = Express + Zod + Swagger'ın tek pakette, tiplerden otomatik üretilmiş hali.
- Express'te `req.params.id` alıp elle `parseInt` + kontrol yaparsın.
  FastAPI'de fonksiyon parametresine `id: int` yazarsın, çeviri + doğrulama + 422 hatası otomatik.
- Dönüş tipini Pydantic model verirsen JSON'a kendisi çevirir.
- `/docs` adresinde Swagger arayüzü kendiliğinden oluşur, tek satır yazmadan.

Bu sefer kod `.py` alıştırma dosyasında değil, gerçek uygulamada:
- `src/ai_lab/api.py`   -> FastAPI uygulaması
- `tests/test_api.py`  -> endpoint testleri

Kural aynı: kodu sen yazıyorsun, Claude kontrol + ipucu veriyor.
Görevleri bitirdikçe bu dosyada `[ ]` -> `[x]` yap.

---

## BÖLÜM 1: Kurulum ve ilk endpoint

- [x] **1)** Kur: `uv add "fastapi[standard]"`
      (`[standard]` = uvicorn sunucusu + `fastapi` komutu da gelsin. npm'deki "peer dependency'leri de kur" gibi)

- [x] **2)** `src/ai_lab/api.py` aç:
      ```python
      app = FastAPI(title="ai-lab etkinlik API")
      ```
      `GET /` -> `{"mesaj": "çalışıyor"}` döndüren bir endpoint yaz.
      Express'teki `app.get("/", (req, res) => res.json({...}))` ile karşılaştır: `res.json` yok, dict'i **return** etmen yeterli.

- [x] **3)** Çalıştır: `uv run fastapi dev src/ai_lab/api.py`
      Tarayıcıda `http://127.0.0.1:8000/` ve `http://127.0.0.1:8000/docs` aç.
      `dev` = nodemon gibi, dosyayı kaydedince kendini yeniden başlatır.

---

## BÖLÜM 2: Etkinlik endpoint'leri

Etkinlikleri dosyanın başında bir kere yükle: `ETKINLIKLER = etkinlikleri_yukle()` (Perşembe'deki fonksiyon).

- [x] **4)** `GET /events` -> 30 etkinliğin hepsi.
      Dönüş tipini yaz: `-> list[Event]`. `/docs`'ta "Schemas" kısmına bak, Event modelin orada mı?

- [x] **5)** `GET /events/{event_id}` -> tek etkinlik.
      Path parametresi: `def etkinlik_getir(event_id: int) -> Event:`
      (Express'te `/events/:id`, burada `{event_id}`. Fonksiyondaki parametre adı birebir aynı olmalı.)

- [x] **6)** Bulunamazsa **404**: `raise HTTPException(status_code=404, detail="Etkinlik bulunamadı")`
      Dikkat: `return` değil, `raise`. Çarşamba'daki exception mantığı.
      İpucu: "ilk eşleşeni bul, yoksa None" -> notlarındaki `next(..., None)` tam burada lazım.

- [x] **7)** 422'yi gör: tarayıcıda `/events/abc` aç. Hiç kod yazmadan ne döndü? Hata gövdesini oku.
      Perşembe'deki `e.errors()` çıktısına benziyor mu? (`loc`, `type`, `msg`)
      Sonra `/events/999` aç -> bu sefer 404. **İki durumun farkını bir cümleyle yaz** (yorum satırı olarak).

---

## BÖLÜM 3: Arama endpoint'i

- [x] **8)** `GET /search` -> query parametreleri: `city`, `category`, `from`, `to` (hepsi opsiyonel).
      Opsiyonel query parametresi: `city: str | None = None`
      (Express'te `req.query.city`. Burada fonksiyon parametresi, ve path'te `{}` yoksa FastAPI onu query sayar.)

- [x] **9)** Önce sadece `city` ve `category` filtrelerini yaz.
      Büyük/küçük harf: `?city=izmir` de `İzmir`'i bulsun. Salı'daki `İ` + `.lower()` tuzağını hatırla (notlarda var).

- [x] **10)** Tarih filtresi. **Tuzak:** `from` Python'da ayrılmış kelime (`from x import y`), parametre adı olamaz.
       Çözüm: `Query` ile takma ad:
       ```python
       baslangic: datetime | None = Query(default=None, alias="from")
       ```
       `to` için de aynısını yap (`to` ayrılmış kelime değil, ama ikisi tutarlı olsun).
       URL `/search?from=2026-11-21T00:00:00` olarak kalır, Python tarafında `baslangic` diye kullanırsın.
       `/search?from=yarın` dene -> ne döndü?

- [x] **11)** Filtreler birlikte çalışsın: `/search?city=İzmir&category=konser` iki koşulu birden uygulamalı.
       İpucu: listeyi adım adım daralt (`sonuc = ETKINLIKLER`, sonra her filtre için `if city: sonuc = [...]`).

---

## BÖLÜM 4: Testler (TestClient)

`TestClient` = Supertest. Sunucuyu ayağa kaldırmadan istek atarsın.
```python
from fastapi.testclient import TestClient
from ai_lab.api import app

client = TestClient(app)
cevap = client.get("/events")
cevap.status_code   # 200
cevap.json()        # list[dict]
```

- [x] **12)** `tests/test_api.py` aç. En az 5 test:
       - `/events` 30 etkinlik döndürüyor
       - `/events/1` doğru etkinliği döndürüyor (title kontrolü)
       - `/events/999` -> 404
       - `/events/abc` -> 422
       - `/search?city=...` sadece o şehrin etkinliklerini döndürüyor (**her** sonucun city'si doğru mu?)
       Bonus: `/search` için `parametrize` kullan (Perşembe'deki gibi).

- [x] **13)** Çalıştır: `uv run pytest -v` -> hepsi yeşil (26 eski + yenileri).

---

## KAPANIŞ

- [x] **14)** `notes/js-vs-python.md`'ye ekle (bu sefer **sen** yaz 🙂):
       Express vs FastAPI, path/query parametresi, `return` vs `res.json`, `raise HTTPException`,
       404 vs 422 farkı, `from` ayrılmış kelime tuzağı, TestClient = Supertest.

- [x] **15)** README: nasıl çalıştırılır (`uv run fastapi dev ...`), endpoint listesi, bu hafta öğrendiğin 3 şey.

- [x] **16)** Kontrol: `uv run pytest -v` yeşil, `/docs`'tan her endpoint'i bir kere dene.
       Bitince haber ver, kontrol edelim, sonra commit + push. **Hafta 1 biter.** 🎉
