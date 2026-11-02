
def hitung_total(data):
    total = 0

    for nilai in data:
        total += nilai

    return total


def hitung_rata_rata(data):
    total = hitung_total(data)
    rata_rata = total / len(data)

    return rata_rata


nilai_mahasiswa = [80, 90, 70]

hasil = hitung_rata_rata(nilai_mahasiswa)

print("Data nilai:", nilai_mahasiswa)
print("Rata-rata:", hasil)
