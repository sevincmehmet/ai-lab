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
| 1 | [`w01-python`](w01-python) | Python temelleri: koleksiyonlar, comprehension, `*args/**kwargs`, type hint, dataclass, modüller, pytest | 🟡 |

## Yapı

```
ai-lab/
├── src/ai_lab/          # paket: haftalar boyunca büyüyecek etkinlik asistanı
│   ├── etkinlik.py      # Event modeli (dataclass)
│   ├── veri.py          # örnek etkinlik verisi
│   ├── arama.py         # şehir, fiyat, ücretsiz etkinlik araması
│   └── __init__.py      # main(): uv run ai-lab
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
```

## Notlar

- [JS'ten Python'a: kafama takılanlar](notes/js-vs-python.md): Türkçe `İ` ile `.lower()` tuzağı, varsayılan argüman tuzağı, `Event.price` ile `event.price` farkı gibi.
