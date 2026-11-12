ogrenci = {
    "ad" : "Mehmet", 
    "yas" : 24, 
    "bolum" : "Bilgisayar Mühendisi"
}
print(ogrenci)
print(ogrenci["ad"])
print(ogrenci.get("bolum"))
print(ogrenci.get("okul"))
print(ogrenci.get("okul", "bilinmiyor"))

ogrenci["okul"] = "Sivas Cumhuriyet Üni." 
print(ogrenci)