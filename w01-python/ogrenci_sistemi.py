ogrenciler = {
    1001: {"ad": "Ali", "not": 85},
    1002: {"ad": "Ayşe", "not": 90},
    1003: {"ad": "Fırat", "not": 35},
}

while True:
    print("\n--- Öğrenci Sistemi ---")
    print("1) Öğrenci Görüntüle")
    print("2) Not Güncelle")
    print("3) Öğrenci Ekle")
    print("0) Çıkış")

    secim = input("Seçim: ")

    if secim == "1":
        no = int(input("Öğrenci no: "))
        if no in ogrenciler:
            print(f"Ad: {ogrenciler[no]['ad']}")
            print(f"Not: {ogrenciler[no]['not']}")
        else:
            print("Öğrenci bulunamadı")

    elif secim == "2":
        no = int(input("Öğrenci no: "))
        if no in ogrenciler:
            yeni_not = int(input(f"{ogrenciler[no]['ad']} adlı öğrencinin yeni notu: "))
            ogrenciler[no]["not"] = yeni_not
            print("Not güncellendi")
        else:
            print("Öğrenci bulunamadı")

    elif secim == "3":
        no = int(input("Yeni öğrenci no: "))
        if no in ogrenciler:
            print("Bu numarada bir öğrenci zaten var")
        else:
            ad = input("Ad: ")
            not_ = int(input("Not: "))
            ogrenciler[no] = {"ad": ad, "not": not_}
            print(f"{ad} eklendi")

    elif secim == "0":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim")
