sayilar = [20, 10, 50, 40]
isimler = ["ali", "ayşe", "mehmet", "aram"]
karisik = [10, "python", True, 3.14]

# print(isimler)
# isimler.append("ali")
# print(isimler)
# isimler.insert(1, "deniz")
# print(isimler)
# isimler.remove("mehmet")
# print(isimler)
# isimler.pop()
# print(isimler)

# print(sayilar)
# print("boyut: ", len(sayilar))
# print("toplam: ",  sum(sayilar))
# print("max: ", max(sayilar))
# print("min: ", min(sayilar))
# sayilar.sort()
# print("Sıralı Liste: ", sayilar)
# sayilar.reverse()
# print("Ters Çevir: ", sayilar)
# print(sayilar)

# for index, isim in enumerate(isimler): 
#     print(index, ":", isim)


# LİSTE KOPYALANMADI
# isimlerX = isimler
# isimlerX.remove("aram")
# print(isimler)

# LİSTE KOPYALANDI
isimlerX = isimler.copy()
isimlerX.remove("aram")
print(isimler)
print(isimlerX)