secim = int(input("Bir sayı seç: "))

match secim: 
    case 1: 
        print("Seçtiğin sayı 1 mi?")
    case 2: 
        print("Seçtiğin sayı 2 mi?")
    case 3: 
        print("Seçtiğin sayı 3 mü?")
    case _:
        print("Ne seçtin :( ")
