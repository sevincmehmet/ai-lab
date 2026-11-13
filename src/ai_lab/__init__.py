from ai_lab.etkinlik import Event
from ai_lab.veri import events

# 15. görevde arama.py'ye sehre_gore'yi yazınca bu satırı aç:
# from ai_lab.arama import sehre_gore


def main() -> None:
    etkinlikler = [Event(**e) for e in events]

    # sehre_gore hazır olunca alttaki satırı şöyle değiştir:
    # for etkinlik in sehre_gore(etkinlikler, "İzmir"):
    for etkinlik in etkinlikler:
        print(etkinlik.ozet())
