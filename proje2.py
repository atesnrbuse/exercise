# MİNİ GÖREV YÖNETİM SİSTEMİ

gorevler = []
def gorev_ekle():
    gorev = input("Yeni görev: ")
    gorevler.append(gorev)
    print("Görev eklendi!")
def gorevleri_goster():
    if len(gorevler) == 0:
        print("Hiç görev yok.")
    else:
        for i, gorev in enumerate(gorevler):
            print(f"{i+1}.{gorev}")
def gorev_sil():
    gorevleri_goster()
    if len(gorevler) == 0:
        return
    silinecek = int(input("Silmek istediğin görev numarası: "))
    if 1 <= silinecek <= len(gorevler):
        gorevler.pop(silinecek - 1)
        print("Görev Silindi!")
    else:
        print("Geçersiz Seçim!")
def menu():
    while True:
        print("\n--- GÖREV YÖNETİMİ ---")
        print("1. Görev Ekle")
        print("2. Görevleri Göster")
        print("3. Görev sil")
        print("4. Çıkış")
        secim = input("Seçim: ")
        if secim == "1":
            gorev_ekle()
        elif secim == "2":
            gorevleri_goster()
        elif secim == "3":
            gorev_sil()
        elif secim == "4":
            break
        else:
            print("Hatalı seçim!")
menu()








