
# Pertemuan 13 - Debugging dan Testing

**Nama:** Nailah Nur Fadilah  
**NIM:** 2225250163
**Kelas:** 3E

## 1. Kasus

Praktik ini membahas proses debugging, tracing,
testing, dan test case menggunakan Python.

Program yang diuji merupakan program pengolahan
nilai mahasiswa yang memiliki tiga bug, yaitu:
1. Kesalahan dalam menghitung rata-rata.
2. Kesalahan dalam menentukan status kelulusan.
3. Kesalahan dalam mencari nilai tertinggi.

## 2. Test Case

| ID | Target | Input | Expected | Actual Awal | Retest |
|---|---|---|---|---|---|
| T1 | Rata-rata | [80,60,90,70] | 75.0 | 60.0 | PASS |
| T2 | Rata-rata | [100,80] | 90.0 | 36.0 | PASS |
| T3 | Status | 60 | Lulus | Tidak lulus | PASS |
| T4 | Status | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | Tertinggi | [80,60,90,70] | 90 | 0 | PASS |

## 3. Bug Report

### Bug B01 - Kesalahan Rata-rata
Gejala:
Hasil rata-rata tidak sesuai dengan jumlah data.

Akar penyebab:
Pembagi ditentukan secara tetap menggunakan angka 5.

Perbaikan:
Mengganti pembagi dengan len(nilai).

### Bug B02 - Kesalahan Status Kelulusan
Gejala:
Nilai 60 dinyatakan tidak lulus.

Akar penyebab:
Program menggunakan operator > 60.

Perbaikan:
Mengubah operator menjadi >= 60.

### Bug B03 - Kesalahan Nilai Tertinggi
Gejala:
Program menghasilkan nilai tertinggi 0.

Akar penyebab:
Variabel tertinggi dimulai dari 0 dan kondisi
perbandingan menggunakan operator yang terbalik.

Perbaikan:
Menggunakan elemen pertama list sebagai nilai
tertinggi dan membandingkannya dengan operator >.

## 4. Retest

Setelah dilakukan perbaikan, seluruh lima test case
dijalankan kembali.

Hasil pengujian:
- T1: PASS
- T2: PASS
- T3: PASS
- T4: PASS
- T5: PASS

Seluruh hasil pengujian telah sesuai dengan
expected result dan tidak ditemukan regresi
pada lima test case tersebut.

## 5. Cara Menjalankan

Jalankan melalui terminal VS Code:

python praktik/praktik_4_debugging.py

## 6. Refleksi

Melalui praktik ini, saya memahami bahwa program
yang berhasil dijalankan belum tentu menghasilkan
jawaban yang benar. Kesalahan logika dapat terjadi
meskipun tidak terdapat pesan error.

Teknik debugging membantu saya mengetahui letak
dan penyebab kesalahan. Test case juga membantu
memastikan bahwa program sudah sesuai dengan
hasil yang diharapkan.

Setelah melakukan perbaikan, pengujian ulang perlu
dilakukan agar kesalahan yang sama tidak muncul
kembali dan tidak menimbulkan masalah pada bagian
program lainnya.
