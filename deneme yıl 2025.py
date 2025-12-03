import json
import time

def oku_json_dosyasi(dosya_adi):

    with open(dosya_adi, "r", encoding="utf-8") as f:
        veri = json.load(f)
    return veri

def yaz_json_dosyasi(dosya_adi, veri):

    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)

def listeleri_kumeye_cevir(veri):

    liste1 = veri.get("liste1", [])
    liste2 = veri.get("liste2", [])

    kume1 = set(liste1)
    kume2 = set(liste2)

    return kume1, kume2

def kume_islemleri(kume1, kume2):

    sonuc = {}


    basla = time.perf_counter()
    birlesim = kume1 | kume2
    bitis = time.perf_counter()
    sonuc["birlesim"] = {
        "sonuc": sorted(list(birlesim)),
        "sure": bitis - basla
    }


    basla = time.perf_counter()
    kesisim = kume1 & kume2
    bitis = time.perf_counter()
    sonuc["kesisim"] = {
        "sonuc": sorted(list(kesisim)),
        "sure": bitis - basla
    }


    basla = time.perf_counter()
    fark_1_2 = kume1 - kume2
    bitis = time.perf_counter()
    sonuc["fark_liste1_liste2"] = {
        "sonuc": sorted(list(fark_1_2)),
        "sure": bitis - basla
    }


    basla = time.perf_counter()
    fark_2_1 = kume2 - kume1
    bitis = time.perf_counter()
    sonuc["fark_liste2_liste1"] = {
        "sonuc": sorted(list(fark_2_1)),
        "sure": bitis - basla
    }

    return sonuc

def main():

    giris_dosya_adi = input("Girdi JSON dosyasının adını giriniz (ör: veri.json): ")


    try:
        veri = oku_json_dosyasi(giris_dosya_adi)
    except FileNotFoundError:
        print("Hata: Dosya bulunamadı!")
        return
    except json.JSONDecodeError:
        print("Hata: Dosya geçerli bir JSON formatında değil!")
        return


    kume1, kume2 = listeleri_kumeye_cevir(veri)


    sonuc_verisi = kume_islemleri(kume1, kume2)


    cikti_dosya_adi = input("Sonuçların yazılacağı JSON dosyasının adını giriniz (ör: sonuc.json): ")


    yaz_json_dosyasi(cikti_dosya_adi, sonuc_verisi)

    print(f"İşlem tamamlandı. Sonuçlar '{cikti_dosya_adi}' dosyasına yazıldı.")

if __name__ == "__main__":
    main()
