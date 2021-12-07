
from PIL import Image

resim = Image.open("cihat.jpg")

print(resim.format,resim.size,resim.mode)
Image._show(resim)

print("""
İŞLEM SEÇİN:

1.RESMİ İSTEDİĞİN AÇIDA DÖNDÜR
2.RESMİ İSTEDİĞİN BOYUTTA KIRP
ÇIKMAK İÇİN "q"YA BASIN.
""")

while True:
    işlem = input("İşleminizi Seçin:")

    if (işlem == "q"):
        print("İşlem Sonlandırılıyor...")
        break

    elif (işlem == "1"):
        açı = int(input("Döndürmek İstediğiniz Açıyı Giriniz:"))
        print("İşlem Yapılıyor...")
        resim.rotate(açı).save("cihat2.jpg")
        resim = Image.open("cihat2.jpg")
        Image._show(resim)

    elif (işlem == "2"):
        koordinat1 = int(input("Kırpılcak Alanı Belirtiniz(x0):"))
        koordinat2 = int(input("Kırpılcak Alanı Belirtiniz(y0):"))
        koordinat3 = int(input("Kırpılcak Alanı Belirtiniz(x1):"))
        koordinat4 = int(input("Kırpılcak Alanı Belirtiniz(y1):"))
        print("İşlem Yapılıyor...")
        koordinatlar = (koordinat1, koordinat2, koordinat3, koordinat4)
        resim.crop(koordinatlar).save("kırpılacakcihat.jpg")
        resim2 = Image.open("kırpılacakcihat.jpg")
        Image._show(resim2)

    else:
        print("Geçersiz İşlem!")










