import pytest
from pydantic import ValidationError

from ai_lab.modeller import Event, etkinlikleri_yukle

ETKINLIKLER = etkinlikleri_yukle()

GECERLI = {
    "id": 1,
    "title": "Test Konseri",
    "city": "İzmir",
    "venue": "Liman Sahnesi",
    "starts_at": "2026-11-20T21:00:00",
    "category": "konser",
    "price_min": 100,
    "price_max": 200,
    "url": "https://example.com/etkinlik/1",
}


def test_gecerli_event_olusuyor():
    e = Event(**GECERLI)
    assert e.title == "Test Konseri"
    assert e.price_max == 200


@pytest.mark.parametrize("silinecek_alan", GECERLI.keys())
def test_eksik_alan_hata_verir(silinecek_alan):
    veri = {**GECERLI}
    del veri[silinecek_alan]  # -> sırayla her alanı dener
    with pytest.raises(ValidationError):
        Event(**veri)


def test_yanlis_tarih_hata_verir():
    veri = {**GECERLI}
    veri["starts_at"] = "Yarın"
    with pytest.raises(ValidationError):
        Event(**veri)


def test_max_negatif_fiyat_hata_verir():
    veri = {**GECERLI}
    veri["price_max"] = -1
    with pytest.raises(ValidationError):
        Event(**veri)


def test_min_negatif_fiyat_hata_verir():
    veri = {**GECERLI}
    veri["price_min"] = -1
    with pytest.raises(ValidationError):
        Event(**veri)


def test_max_min_kucuk_hata_verir():
    veri = {**GECERLI}
    veri["price_min"] = 300
    veri["price_max"] = 100
    with pytest.raises(ValidationError):
        Event(**veri)


def test_bozuk_url_hata_verir():
    veri = {**GECERLI}
    veri["url"] = "Mehmetin sitesi"
    with pytest.raises(ValidationError):
        Event(**veri)


def test_string_fiyat_int_e_donusur():
    veri = {**GECERLI, "price_min": "50"}
    event = Event(**veri)
    assert event.price_min == 50
    assert isinstance(event.price_min, int)


def test_etkinlikleri_yukle():
    assert len(ETKINLIKLER) == 30
