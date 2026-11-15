import time
from contextlib import contextmanager


@contextmanager  # yield'li fonksiyonu with ile kullanılabilir yapar
def zamanla(etiket: str):
    baslangic = time.perf_counter()

    try:
        yield
    finally:
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"{etiket}: {sure:.2f} sn")
