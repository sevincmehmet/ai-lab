# isim = input("İsminiz nedir? ")
# yemek= input("Sevdiğiniz Yemek Nedir? ")
#
# print(isim + " " +yemek + " seviyormuş king")


# isim = "mehmet"
# yas = 24
#
# print(isim + " " + str(yas) + " Yaşında")

# x = 5
# y = 9
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(x%y)
# print(x**y)


# number1 = int(input("1. Sayıyı gir: "))
# number2 = int(input("2. Sayıyı gir: "))
#
# sum = number1 + number2
#
# print("Sayılarınızın toplamı: " + str(sum))



# import math

# print(math.sqrt(5))
# print(min(0,5,4))
# print(max(0,5,2,1))
# print(round(9.5)) # yuvarlama
# print(abs(-9)) # mutlak değer

#
# name = "Mehmet' in"
# name2 = """ Mehmet' in büyük yüreği
# aslkmasfn slak """
#
# print(name2)
# print(name)
# print(name2[1])
# print(name[-1])
# print(name[-5:-1])
# print(len(name))


#
# isim = "meHMet"
# print(isim)
# print(isim.title())
# print(isim.upper())
# print(isim.lower())
# print(isim.find("e")) #Büyğük küçük harf duyarlı -> bulamayınca -1 döner
# print(isim.replace("HM","hm"))



# yagmurluMu = False
# gunesliMi = False
#
# if yagmurluMu:
#     print("Ceketini Giy")
# elif gunesliMi:
#     print("Güneş Gözlüğünü Tak")
# else :
#     print("Çık Knk")


#
# ehliyet = False
# araba = True
#
# if ehliyet and araba :
#     print("Sür")
# if ehliyet or araba :
#     print("az kaldı king")
# else:
#     print("Kullanamazsın knk")

# if ehliyet and not araba :
#     print("araba alınca kullanırsın")
# elif araba and not ehliyet:
#     print("ehliyet al king")


# sıcaklık = 32
# if sıcaklık > 30 :
#     print("Klima Aç")
# elif sıcaklık<0 :
#     print("Bu ne soğuk abi")
# else:
#     print("Klima kapat")



# yas = int(input("Yaşınız"))
# okul = False
#
# if not okul and yas>18 :
#     print("Askere Gidebilir")
# else:
#     print("Daha var aslanım")


# i = 1
# while(i <= 1000):
#     print(i);
#     i = i + 1


# isciler = ["Mehmet", "Dursun", "Gökdeniz", "Mustafa"]
# print(isciler)
# print(isciler[0:2])


# Döngüler

# for i in range(1, 10) :
#     if i == 5: 
#         continue
#     print(i)


# for i in range(1, 6):
#     for j in range(1,6):
#         print(i, "x", j, "=", i*j)

#     print("-------------")    



# sifre = "pythonadamdır"
# giris = ""

# while giris != sifre : 
#     giris = input("Şifreyi giriniz: ")

# print("Giriş Başarılı!!!")



# def selamla(isim): 
#     print("Sa", isim)

# selamla("Mehmet")




# def topla(a, b) : 
#     return a+b

# def yazdır(sonuc):
#     print("Sonuç: ", str(sonuc)) 

# deger = topla(14, 22)
# yazdır(deger)



# def faktoriyel(n): 
#     sonuc = 1
#     for i in range(1, n+1):
#         sonuc *= i 
#     return sonuc

# sayi = int(input("Bir sayı girin: "))

# print(sayi, "sayısının faktoriyeli: ", faktoriyel(sayi))