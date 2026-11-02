
def baca_nilai(nama_file):
    file = open(nama_file, "r", encoding="utf-8")
    data = file.readlines()
    file.close()

    return data


hasil = baca_nilai("data/nilai.txt")

for baris in hasil:
    print(baris.strip())
