from datetime import date

from fastapi import FastAPI, HTTPException, Query

from ai_lab.modeller import Event, etkinlikleri_yukle

app = FastAPI(title="ai-lab etkinlik API")

ETKINLIKLER = etkinlikleri_yukle()


def tr_lower(metin: str) -> str:
    """Türkçe I/İ dönüşümünü bozmadan küçük harfe çevirir."""
    return metin.replace("İ", "i").replace("I", "ı").lower()


@app.get("/")
def root() -> dict[str, str]:
    return {"mesaj": "çalışıyor"}


@app.get("/events")
def get_events() -> list[Event]:
    return ETKINLIKLER


@app.get("/search")
def search(
    city: str | None = None,
    category: str | None = None,
    from_date: date | None = Query(default=None, alias="from"),
    to: date | None = None,
) -> list[Event]:
    """Query parametrelerine göre etkinlikleri filtreler."""
    sonuclar = ETKINLIKLER

    if city is not None:
        sonuclar = [e for e in sonuclar if tr_lower(e.city) == tr_lower(city)]

    if category is not None:
        sonuclar = [e for e in sonuclar if tr_lower(e.category) == tr_lower(category)]

    if from_date is not None:
        sonuclar = [e for e in sonuclar if e.starts_at.date() >= from_date]

    if to is not None:
        sonuclar = [e for e in sonuclar if e.starts_at.date() <= to]

    return sonuclar


@app.get("/events/{event_id}")
def get_event_by_id(event_id: int) -> Event:
    """Id değerine göre etkinlik getirir"""
    event = next((e for e in ETKINLIKLER if e.id == event_id), None)

    if event is None:
        raise HTTPException(status_code=404, detail="Etkinlik Bulunamadı")
    return event
