import time


def oku_sayilar(dosya_adi: str):

    with open(dosya_adi, "r", encoding="utf-8") as f:
        veri = f.read()


    veri = veri.replace(",", " ")
    parcalar = veri.split()

    sayilar = [int(p) for p in parcalar]
    return sayilar


def bubble_sort(liste):

    a = liste.copy()
    n = len(a)

    karsilastirma = 0
    yer_degistirme = 0

    basla = time.perf_counter()

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            karsilastirma += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                yer_degistirme += 1

    bitis = time.perf_counter()
    sure = bitis - basla
    toplam_adim = karsilastirma + yer_degistirme

    istatistik = {
        "algoritma": "Bubble Sort",
        "karsilastirma": karsilastirma,
        "yer_degistirme": yer_degistirme,
        "toplam_adim": toplam_adim,
        "sure_saniye": sure
    }

    return a, istatistik


def selection_sort(liste):

    a = liste.copy()
    n = len(a)

    karsilastirma = 0
    yer_degistirme = 0

    basla = time.perf_counter()

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            karsilastirma += 1
            if a[j] < a[min_index]:
                min_index = j


        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            yer_degistirme += 1

    bitis = time.perf_counter()
    sure = bitis - basla
    toplam_adim = karsilastirma + yer_degistirme

    istatistik = {
        "algoritma": "Selection Sort",
        "karsilastirma": karsilastirma,
            "yer_degistirme": yer_degistirme,
        "toplam_adim": toplam_adim,
        "sure_saniye": sure
    }

    return a, istatistik


def rapor_yaz(rapor_adi,
              orijinal_liste,
              bubble_sirali, bubble_istatistik,
              selection_sirali, selection_istatistik):

    with open(rapor_adi, "w", encoding="utf-8") as f:
        f.write("SIRALAMA ALGORITMALARI PROJESI RAPORU\n")
        f.write("=====================================\n\n")

        f.write(f"Orijinal liste : {orijinal_liste}\n\n")

        f.write("1) Bubble Sort Sonucu\n")
        f.write("---------------------\n")
        f.write(f"Sıralanmış liste   : {bubble_sirali}\n")
        f.write(f"Karşılaştırma sayısı : {bubble_istatistik['karsilastirma']}\n")
        f.write(f"Yer değiştirme sayısı: {bubble_istatistik['yer_degistirme']}\n")
        f.write(f"Toplam adım         : {bubble_istatistik['toplam_adim']}\n")
        f.write(f"Süre (saniye)       : {bubble_istatistik['sure_saniye']:.8f}\n\n")

        f.write("2) Selection Sort Sonucu\n")
        f.write("------------------------\n")
        f.write(f"Sıralanmış liste   : {selection_sirali}\n")
        f.write(f"Karşılaştırma sayısı : {selection_istatistik['karsilastirma']}\n")
        f.write(f"Yer değiştirme sayısı: {selection_istatistik['yer_degistirme']}\n")
        f.write(f"Toplam adım         : {selection_istatistik['toplam_adim']}\n")
        f.write(f"Süre (saniye)       : {selection_istatistik['sure_saniye']:.8f}\n\n")

        f.write("3) Karşılaştırma\n")
        f.write("---------------\n")


        if bubble_istatistik["toplam_adim"] < selection_istatistik["toplam_adim"]:
            f.write("Adım sayısı açısından daha verimli algoritma: Bubble Sort\n")
        elif bubble_istatistik["toplam_adim"] > selection_istatistik["toplam_adim"]:
            f.write("Adım sayısı açısından daha verimli algoritma: Selection Sort\n")
        else:
            f.write("Adım sayısı açısından her iki algoritma da eşit verimlidir.\n")


        if bubble_istatistik["sure_saniye"] < selection_istatistik["sure_saniye"]:
            f.write("Süre açısından daha hızlı algoritma        : Bubble Sort\n")
        elif bubble_istatistik["sure_saniye"] > selection_istatistik["sure_saniye"]:
            f.write("Süre açısından daha hızlı algoritma        : Selection Sort\n")
        else:
            f.write("Süre açısından her iki algoritma da eşittir.\n")


def main():

    giris_dosya_adi = input("Sayı listesini içeren .txt dosyasının adını girin (ör: sayilar.txt): ")


    sayilar = oku_sayilar(giris_dosya_adi)
    print("Okunan liste:", sayilar)


    bubble_sirali, bubble_istatistik = bubble_sort(sayilar)
    selection_sirali, selection_istatistik = selection_sort(sayilar)


    rapor_adi = "siralama_raporu.txt"
    rapor_yaz(
        rapor_adi,
        sayilar,
        bubble_sirali, bubble_istatistik,
        selection_sirali, selection_istatistik
    )

    print(f"\nİŞLEM TAMAM. Rapor dosyası: {rapor_adi}")


if __name__ == "__main__":
    main()
