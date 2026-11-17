from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl, TypeAdapter, model_validator


class Event(BaseModel):
    id: int
    title: str = Field(min_length=1)
    city: str
    venue: str
    starts_at: datetime
    category: str
    price_min: int = Field(ge=0)
    price_max: int = Field(ge=0)
    url: HttpUrl

    @model_validator(mode="after")
    def fiyat_araligini_kontrol_et(self) -> Event:
        if self.price_max < self.price_min:
            raise ValueError("En yüksek fiyat en düşük fiyattan düşük olamaz")
        return self

    def ucretsiz_mi(self) -> bool:
        """Etkinlik ücretsiz mi (en yüksek fiyat 0 ise)."""
        return self.price_max == 0

    def ozet(self) -> str:
        """Örn: 'Duman Konseri - İzmir, KüçükSahne (750-1200 TL)' ya da '(Ücretsiz)'."""
        if self.ucretsiz_mi():
            fiyat = "Ücretsiz"
        else:
            fiyat = f"{self.price_min}-{self.price_max} TL"
        return f"{self.title} - {self.city}, {self.venue} ({fiyat})"


def etkinlikleri_yukle(yol: str = "data/events.json") -> list[Event]:
    adapter = TypeAdapter(list[Event])
    with open(yol, encoding="utf-8") as f:
        return adapter.validate_json(f.read())
