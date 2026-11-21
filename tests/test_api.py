import pytest
from fastapi.testclient import TestClient

from ai_lab.api import app, tr_lower

client = TestClient(app)


# --- ÖRNEK 1: basit durum kodu + gövde kontrolü ---
def test_events_liste_donduruyor():
    cevap = client.get("/events")

    assert cevap.status_code == 200
    veri = cevap.json()  # JSON -> Python list[dict]
    assert isinstance(veri, list)
    assert len(veri) > 0


# --- ÖRNEK 2: hata durumu (olmayan id -> 404) ---
def test_olmayan_etkinlik_404():
    cevap = client.get("/events/99999")

    assert cevap.status_code == 404
    assert cevap.json()["detail"] == "Etkinlik Bulunamadı"


def test_id_ile_etkinlik_donduruyor():
    cevap = client.get("/events/1")

    assert cevap.status_code == 200
    veri = cevap.json()
    assert veri["id"] == 1


def test_yanlis_id_tipi():
    cevap = client.get("/events/abc")

    assert cevap.status_code == 422


def test_sehir_arama():
    cevap = client.get("/search?city=izmir")

    assert cevap.status_code == 200
    veri = cevap.json()

    # for v in veri:
    #     assert tr_lower(v["city"]) == "izmir"
    assert len(veri) > 0
    assert all(tr_lower(v["city"]) == "izmir" for v in veri)


def test_tarih_kelime_hata_vermeli():
    cevap = client.get("/search?from=yarın")

    assert cevap.status_code == 422


@pytest.mark.parametrize(
    "query_string, beklenen_sehir, beklenen_kategori",
    [
        ("?city=izmir", "izmir", None),
        ("?city=İZMİR&category=konser", "izmir", "konser"),
        ("?from=2026-11-21&to=2026-12-01", None, None),
    ],
)
def test_search_parametrize(query_string, beklenen_sehir, beklenen_kategori):
    cevap = client.get(f"/search{query_string}")

    assert cevap.status_code == 200
    veri = cevap.json()

    assert len(veri) > 0

    if beklenen_sehir is not None:
        assert all(tr_lower(v["city"]) == beklenen_sehir for v in veri)

    if beklenen_kategori is not None:
        assert all(tr_lower(v["category"]) == beklenen_kategori for v in veri)
