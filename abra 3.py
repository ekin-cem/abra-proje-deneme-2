import time

dosya_adi = input("Sayıların olduğu .txt dosyasının adını yaz (örnek: sort.txt): ")

def sayilari_oku(dosya_adi):
    f = open(dosya_adi, "r")
    metin = f.read()
    f.close()

    metin = metin.replace(",", " ")

    parcalar = metin.split()

    sayilar = []
    for p in parcalar:
        sayilar.append(int(p))

    return sayilar


def bubble_sort(liste):
    a = liste[:]  # orijinali bozmamak için kopya
    n = len(a)
    adim = 0

    baslangic = time.time()

    for i in range(n - 1):
        for j in range(n - 1 - i):
            adim += 1  # karşılaştırma
            if a[j] > a[j + 1]:
                # yer değiştirme (swap)
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                adim += 1  # swap için de 1 adım sayalım

    bitis = time.time()
    sure = bitis - baslangic
    return a, adim, sure


def selection_sort(liste):
    a = liste[:]
    n = len(a)
    adim = 0

    baslangic = time.time()

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            adim += 1  # karşılaştırma
            if a[j] < a[min_index]:
                min_index = j

        if min_index != i:
            temp = a[i]
            a[i] = a[min_index]
            a[min_index] = temp
            adim += 1  # swap için 1 adım daha

    bitis = time.time()
    sure = bitis - baslangic
    return a, adim, sure



sayilar = sayilari_oku(dosya_adi)

bubble_sirali, bubble_adim, bubble_sure = bubble_sort(sayilar)
selection_sirali, selection_adim, selection_sure = selection_sort(sayilar)

print("Orijinal liste:", sayilar)
print("Bubble sort sonucu:", bubble_sirali)
print("Selection sort sonucu:", selection_sirali)

print("\nBubble sort -> Adım:", bubble_adim, "  Süre:", bubble_sure, "saniye")
print("Selection sort -> Adım:", selection_adim, "  Süre:", selection_sure, "saniye")

rapor_adi = "rapor.txt"
f = open(rapor_adi, "w")

f.write("SIRALAMA ALGORITMALARI RAPORU\n\n")

f.write("Orijinal liste:\n")
f.write(str(sayilar) + "\n\n")

f.write("Bubble sort sonucu:\n")
f.write(str(bubble_sirali) + "\n")
f.write("Adim sayisi: " + str(bubble_adim) + "\n")
f.write("Gecen sure (saniye): " + str(bubble_sure) + "\n\n")

f.write("Selection sort sonucu:\n")
f.write(str(selection_sirali) + "\n")
f.write("Adim sayisi: " + str(selection_adim) + "\n")
f.write("Gecen sure (saniye): " + str(selection_sure) + "\n\n")

if bubble_sure < selection_sure:
    f.write("Zamana göre daha hızlı: BUBBLE SORT\n")
elif selection_sure < bubble_sure:
    f.write("Zamana göre daha hızlı: SELECTION SORT\n")
else:
    f.write("İki algoritmanın süresi de neredeyse aynı.\n")

if bubble_adim < selection_adim:
    f.write("Adım sayısına göre daha az işlem yapan: BUBBLE SORT\n")
elif selection_adim < bubble_adim:
    f.write("Adım sayısına göre daha az işlem yapan: SELECTION SORT\n")
else:
    f.write("Adım sayıları neredeyse aynı.\n")

f.close()

print("\nRapor", rapor_adi, "dosyasına yazıldı.")
