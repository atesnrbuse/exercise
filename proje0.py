# ÖĞRENCİ PERFORMANS ANALİZ SİSTEMİ
ogrenciler = []
ortalamalar = []
og_sayisi = int(input("kaç öğrenci var:"))

for i in range(og_sayisi):
    isim = input("isminiz: ")
    print(f"{i+1}. öğrenci: ",isim)
    notlar = []
    for i in range(3):
        not_gir = int(input(F"{i+1}. notunuz:"))
        notlar.append(not_gir)
        
    total = sum(notlar)
    ort = total / 3

    if ort >= 90: harf = "AA"
    elif ort >= 80: harf = "BA"
    elif ort >= 70: harf = "BB"
    elif ort >= 60: harf = "CB"
    elif ort >= 50: harf = "CC"
    else: harf = "FF"

    ogrenci ={
    "isim": isim,
    "notunuz": notlar,
    "not ortalamanız": ort,
    "harf notunuz": harf
    }

    ogrenciler.append(ogrenci)
    ortalamalar.append(ort)

en_basarili = ogrenciler[0]
en_basarisiz = ogrenciler[0]
toplam_ort = 0
for i in ogrenciler:
    toplam_ort += i["not ortalamanız"]
if i["not ortalamanız"] > en_basarili["not ortalamanız"]:
    en_basarili = i
if i["not ortalamanız"] < en_basarisiz["not ortalamanız"]:
    en_basarisiz = i

sinif_ortalamasi = toplam_ort / len(ogrenciler)

print("\n--- TÜM ÖĞRENCİLER ---" )
for ogr in ogrenciler:
    print(f"{ogr['isim']} → Ortalama:{ogr['not ortalamanız']} | Harf:{ogr['harf notunuz']}")

print(f"sınıf ortalaması: {sinif_ortalamasi}")
print(f"En Başarılı {en_basarili["isim"]} , {en_basarili["not ortalamanız"]}")
print(f"En Başarısız {en_basarisiz["isim"]} , {en_basarisiz["not ortalamanız"]}")

