
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    hasil = total - diskon

    print("Total belanja:", total)
    print("Persentase diskon:", persen)
    print("Jumlah diskon:", diskon)

    return hasil


hasil_akhir = hitung_diskon(200000, 10)

print("Total setelah diskon:", hasil_akhir)
