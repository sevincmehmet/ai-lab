"""

ogrenciler = {
    1001: {"ad":"Ali", "not": 85 },
    1002: {"ad":"Ayşe", "not": 90 },
    1003: {"ad":"Fırat", "not": 35 }
}

while True :
    print("\n--- Öğrenci Sistemi --- ")
    print("1) Öğrenci Görüntüle")
    print("2) Not Güncelle")
    print("3) Öğrenci Ekle")
    print("0) Çıkış")

    secim = input("Seçim: ")

    if secim == "1": 
        no = int(input("Öğrenci no: "))
        if no in ogrenciler: 
            print("Ad: ", ogrenciler[no]["ad"])
            print("Not: ", ogrenciler[no]["not"])
        else: 
            print("Öğrenci bulunamadı")

    if secim == "2": 
        no = int(input("Öğrenci no: "))
        if no in ogrenciler: 
            newnote = int(input(ogrenciler[no]["ad"], " adlı öğrencinin yeni notu: "))
            ogrenciler[no]["not"] = newnote
            print("not güncel")

            """