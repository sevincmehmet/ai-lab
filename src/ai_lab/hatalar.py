class EtkinlikHatasi(Exception):
    """Etkinlik yönetimi sırasında oluşan genel hatalar."""


class EtkinlikBulunamadi(EtkinlikHatasi):
    """Aranan etkinlik sistemde bulunamadığında fırlatılan hata."""
