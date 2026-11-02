
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0

    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"

    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x

    return tertinggi


# Data utama
nilai = [80, 60, 90, 70]

print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))


# Pengujian tambahan
print("\n--- PENGUJIAN TAMBAHAN ---")

print("Rata-rata [100, 80]:",
      hitung_rata_rata([100, 80]))

print("Status 59:", status(59))

print("Rata-rata data kosong:",
      hitung_rata_rata([]))

print("Nilai tertinggi data kosong:",
      nilai_tertinggi([]))
