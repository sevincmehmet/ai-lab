from ai_lab.arama import en_pahali, sehre_gore
from ai_lab.etkinlik import Event
from ai_lab.veri import events


def main() -> None:
    etkinlikler = [Event(**e) for e in events]

    # print("İzmir'deki etkinlikler:")
    # for etkinlik in sehre_gore(etkinlikler, "İzmir"):
    #     print(" -", etkinlik.ozet())

    # print("İstanbul'daki etkinlikler:")
    # for etkinlik in sehre_gore(etkinlikler, "İstanbul"):
    #     print("-", etkinlik.ozet())
    
    print(en_pahali(etkinlikler))
    # Diğer fonksiyonları yazınca burada dene, örneğin:
    # from ai_lab.arama import ucretsizler   (bunu dosyanın en üstüne taşı)
    # print("Ücretsizler:", [e.title for e in ucretsizler(etkinlikler)])
