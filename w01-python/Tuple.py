# Tuple = Değiştirilemez olayı da o zaten.. 

# renkler = ("kırmızı", "yeşil", "mavi") # değişmeyen verilerdir örn haftanın günleri gibi
# print(renkler[0])
# print(renkler)

# gunler = ("pzt", "sl", "çrş", "prş", "cm", "cmr", "pzr")
# gunler[1] = "prş" # hatalıdır değişmemelidir -> verinin yanlışlıkla değişmemesi için vardır
# print(gunler)

# t1 = (10, 20, 30)
# t2 = 10, 20, 30
# t3 = (5,) # -> Tek eleman olsa bile sonuan virgül koy -> virgül koyarsan tuple olur
# t4 = ("python",)

# diller = ("python", "C", "Java")

# for dil in diller:
#     print(dil)   

# a1 = (1, 2, 3)
# a2 = (4, 5)

# yeni = a1+a2 # Birleştirilebilir 
# print(yeni)

# tekrar = a2*2
# print("tekrar ", tekrar)


# koordinat = (10, 20)
# x, y = koordinat

# print(x,y)


# ogrenci = ("Aram", 24, "Bilgisayar Mühendisi")
# isim, yas, bolum = ogrenci

# print(f"{isim}, {yas} yaşında, {bolum}")


renkler = ("beyaz", "bordo", "mavi")

renkler_listesi = list(renkler)
print(renkler_listesi)

renkler_listesi.append("sarı")
print(renkler_listesi)


renkler = tuple(renkler_listesi) # => Yeni bir tuple oluşturur eskisinden farklıdır.

import sys

liste = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(liste)) # 104 -> daha esnektir 
print(sys.getsizeof(tuple)) # 88 -> tuple daha az yer kaplar -> daha hızlıdır 


def hesapla(a, b): 
    return a+b, a*b

toplam, carpim = hesapla(2, 5)
print(toplam, carpim)