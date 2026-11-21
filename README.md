# ai-lab

12 haftalık LLM ve AI agent laboratuvarım. Frontend'den (React, Next.js, TypeScript) LLM tabanlı ürün geliştirmeye geçerken yaptığım bütün çalışmaları burada, haftalara göre topluyorum.

**Hedef:** "Bu hafta sonu İzmir'de ne yapsam?" diye sorulabilen, tool kullanan bir etkinlik asistanını sıfırdan yazmak ve ne kadar iyi çalıştığını eval ile ölçmek.

## Plan

| Faz | Haftalar | Konu | Durum |
|---|---|---|---|
| 1. Temeller | 1–3 | Python, LLM API, tool use, streaming arayüz, MCP | 🟡 devam ediyor |
| 2. Etkinlik asistanı | 4–7 | Kullanıcı görüşmeleri, ürün kararı, asistanın kendisi | ⚪ |
| 3. Eval ve ölçüm | 8–10 | Eval seti, önce/sonra karşılaştırması, tracing | ⚪ |
| 4. Paketleme | 11–12 | Vaka çalışması, demo | ⚪ |

## Haftalar

| Hafta | Klasör | Konu | Durum |
|---|---|---|---|
| 1 | [`w01-python`](w01-python) | Python temelleri: koleksiyonlar, comprehension, `*args/**kwargs`, type hint, dataclass, modüller, pytest, exception'lar, `with` / context manager, `async`/`await`, `asyncio.gather`, httpx, Pydantic (BaseModel, Field, validator), `pytest.mark.parametrize`, FastAPI (path/query parametreleri, `HTTPException`, `TestClient`) | ✅ |

## Yapı

```
ai-lab/
├── src/ai_lab/          # paket: haftalar boyunca büyüyecek etkinlik asistanı
│   ├── etkinlik.py      # Event modeli (dataclass)
│   ├── veri.py          # örnek etkinlik verisi
│   ├── arama.py         # şehir, fiyat, ücretsiz etkinlik araması
│   ├── hatalar.py       # EtkinlikHatasi, EtkinlikBulunamadi
│   ├── araclar.py       # zamanla(): süre ölçen context manager
│   ├── modeller.py      # Event modeli (Pydantic) + etkinlikleri_yukle()
│   ├── api.py           # FastAPI: /events, /events/{id}, /search
│   └── __init__.py      # main(): uv run ai-lab
├── data/                # events.json: 30 uydurma etkinlik
├── tests/               # pytest testleri
├── w01-python/          # haftalık alıştırmalar
└── notes/               # öğrendiklerim
```

## Çalıştırma

[uv](https://docs.astral.sh/uv/) gerekli.

```bash
uv sync              # bağımlılıkları kur
uv run ai-lab        # İzmir'deki etkinlikleri listeler
uv run pytest -v     # testleri çalıştırır
uv run fastapi dev src/ai_lab/api.py   # API'yi başlatır -> http://127.0.0.1:8000/docs
```

## API

| Endpoint | Açıklama |
|---|---|
| `GET /` | Sağlık kontrolü |
| `GET /events` | Bütün etkinlikler |
| `GET /events/{event_id}` | Tek etkinlik, yoksa 404 |
| `GET /search` | Filtreli arama: `city`, `category`, `from`, `to` (hepsi opsiyonel, büyük/küçük harf ve Türkçe `İ` duyarsız) |

Örnek: `/search?city=izmir&category=konser&from=2026-11-21&to=2026-12-01`

## Hafta 1'de öğrendiğim 3 şey

1. **Tip ipuçları Python'da iş yapıyor.** Pydantic ve FastAPI type hint'lere bakıp veriyi doğruluyor ve çeviriyor. `event_id: int` yazınca `/events/abc` isteği benim kodum hiç çalışmadan 422 dönüyor.
2. **Python sessizce geçiştirmiyor.** JS'te çalışıp yanlış sonuç veren şeyler (`"1" + 2`, `datetime` ile `date` karşılaştırmak) burada hata fırlatıyor. Bunları test yazarken değil, endpoint'i elle denerken yakaladım.
3. **Yeşil test her zaman doğru test değil.** `all([])` boş listede `True` dönüyor. Arama hiç sonuç döndürmese bile test geçiyordu, önce `len(veri) > 0` kontrolü ekledim.

## Notlar

- [JS'ten Python'a: kafama takılanlar](notes/js-vs-python.md): Türkçe `İ` ile `.lower()` tuzağı, varsayılan argüman tuzağı, `Event.price` ile `event.price` farkı, `await`'i unutunca ne olduğu, `gather` = `Promise.all`, Pydantic = Zod, Express vs FastAPI, 404 vs 422, `all([])` tuzağı gibi.
