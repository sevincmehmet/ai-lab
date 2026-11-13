from dataclasses import dataclass

@dataclass(frozen=True)
class Event:
    title: str
    city: str
    category: str
    day: str
    price: int = 0  # price varsayılan olarak 0 verildi

    def ucretsiz_mi(self) -> bool:
        """Etkinlik ücretsiz mi kontrol eder (True/False döner)."""
        return self.price == 0

    def ozet(self) -> str:
        """Etkinliğin özet metnini döndürür."""
        if self.ucretsiz_mi():
            return f"{self.title} - {self.city} (Ücretsiz)"
        else:
            return f"{self.title} - {self.city} ({self.price} TL)"