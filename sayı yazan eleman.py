import random
ADET = 100
DOSYA_ADI = "sayilar.txt"

def sayi_dosyasi_olustur():

    sayilar = list(range(1, ADET + 1))

    random.shuffle(sayilar)

    sayilar_str = [str(sayi) for sayi in sayilar]

    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        f.write(" ".join(sayilar_str))

    print(f"{DOSYA_ADI} dosyasına 1 ile {ADET} arasındaki sayılar karışık şekilde yazıldı.")

if __name__ == "__main__":
    sayi_dosyasi_olustur()
