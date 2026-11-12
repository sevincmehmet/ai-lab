tasks = []

while True:
    print(""" 
        1- Ekle
        2- Listele
        3- Sil
        4- Çıkış 
      """)

    secim = input("Secim: ")

    if secim == "1":
        gorev = input("Yeni todo elemanı: ")
        tasks.append(gorev)

    elif secim == "2":
        for i, task in enumerate(tasks):
            print(i, "-", task)

    elif secim == "3":
        silinecek = int(input("Silinecek görev numarası: "))
        if 0 <= silinecek < len(tasks):
            tasks.pop(silinecek)
        else:
            print("Geçersiz numara.")

    elif secim == "4":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Lütfen 1 ile 4 arasında geçerli bir seçim yapın.")
