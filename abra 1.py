import json
import time

dosya_adi = input("JSON dosyasının adını yaz (örn: veri.json): ")

with open(dosya_adi, "r", encoding="utf-8") as f:
    veri = json.load(f)

liste1 = veri["liste1"]
liste2 = veri["liste2"]

kume1 = set(liste1)
kume2 = set(liste2)

sonuclar = {}

baslama_zamani = time.time()
birlesim = kume1.union(kume2)
bitis_zamani = time.time()
gecen_sure = bitis_zamani - baslama_zamani

sonuclar["birlesim"] = {
    "sonuc": list(birlesim),
    "sure_saniye": gecen_sure
}

baslama_zamani = time.time()
kesisim = kume1.intersection(kume2)
bitis_zamani = time.time()
gecen_sure = bitis_zamani - baslama_zamani

sonuclar["kesisim"] = {
    "sonuc": list(kesisim),
    "sure_saniye": gecen_sure
}

baslama_zamani = time.time()
fark1 = kume1.difference(kume2)
bitis_zamani = time.time()
gecen_sure = bitis_zamani - baslama_zamani

sonuclar["fark_kume1_eksi_kume2"] = {
    "sonuc": list(fark1),
    "sure_saniye": gecen_sure
}

baslama_zamani = time.time()
fark2 = kume2.difference(kume1)
bitis_zamani = time.time()
gecen_sure = bitis_zamani - baslama_zamani

sonuclar["fark_kume2_eksi_kume1"] = {
    "sonuc": list(fark2),
    "sure_saniye": gecen_sure
}

cikis_dosyasi = "sonuclar.json"

with open(cikis_dosyasi, "w", encoding="utf-8") as f:
    json.dump(sonuclar, f, ensure_ascii=False, indent=4)

print("İşlem bitti! Sonuçlar", cikis_dosyasi, "dosyasına yazıldı.")
