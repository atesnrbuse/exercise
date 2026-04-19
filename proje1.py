# Akıllı Harcama Takipçisi
def harcama_takip():
    gün_sayisi = int(input("kaç gün harcama girdin:"))
    harcamalar = []
    for i in range(gün_sayisi):
        harcama = float(input(f"{i+1}. gün harcaması:"))
        harcamalar.append(harcama)
    toplam = sum(harcamalar)
    ortalama = toplam/gün_sayisi
    bütce = float(input("toplam bütçen ne kadar:"))
    if toplam > bütce:
        durum = "bütçeyi aştın"
    else:
        durum = "bütçe kontrol altında"
    print("toplam harcama:", toplam)
    print("günlük ortalama:", ortalama)
    print(durum)
harcama_takip()



