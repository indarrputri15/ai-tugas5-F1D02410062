# Sistem Pakar Troubleshooting Gangguan Wi-Fi

## 1. Identitas

- **Nama:** Khofipah Indar Putri
- **NIM:** F1D02410062
- **Mata Kuliah:** Kecerdasan Buatan 
- **Tugas:** Tugas 5 — Membuat Sistem Pakar

---

## 2. Topik

Topik yang dipilih adalah **Sistem Pakar Troubleshooting Gangguan Wi-Fi**. Sistem menerima fakta dari pengguna mengenai kondisi koneksi Wi-Fi, kemudian menggunakan aturan IF-THEN untuk menarik kesimpulan. Metode inferensi yang digunakan adalah **Forward Chaining**. Tujuan sistem bukan menggantikan teknisi jaringan, tetapi memberikan saran awal berdasarkan pengetahuan yang telah dimasukkan ke dalam basis aturan.

---

## 3. Cara Menjalankan Program

### Bahasa dan versi

- Python 3.x
- Tidak membutuhkan library eksternal.

## 4. Sumber Pengetahuan

### S1 — Microsoft Support

**Judul:** Memperbaiki masalah koneksi Wi-Fi di Windows  
**Penerbit:** Microsoft Support  
**URL:** https://support.microsoft.com/id-id/windows/experience/connectivity-networking/fix-wi-fi-connection-issues-in-windows  
**Tanggal akses:** 9 November 2026

Sumber ini digunakan untuk aturan tentang Wi-Fi terhubung tetapi tidak ada internet, pengujian pada perangkat lain, sinyal/koneksi, koneksi yang sering terputus, adaptor Wi-Fi, dan langkah troubleshooting lainnya.

### S2 — TP-Link Support

**Judul:** Why cannot I access the Internet after installed the TP-Link router?  
**Penerbit:** TP-Link Support  
**URL:** https://www.tp-link.com/id/support/faq/833/  
**Tanggal akses:** 9 November 2026

Sumber ini digunakan terutama untuk kondisi IP WAN router `0.0.0.0` dan pemeriksaan koneksi modem/router.

### S3 — TP-Link Support

**Judul:** TP-Link Router Not Connecting to Internet: How to Troubleshoot and Fix  
**Penerbit:** TP-Link Support  
**URL:** https://www.tp-link.com/id/support/faq/1556/  
**Tanggal akses:** 9 November 2026

Sumber ini digunakan sebagai referensi tambahan mengenai pemeriksaan koneksi modem/router dan restart perangkat jaringan.

### S4 — Microsoft Support

**Judul:** Wi-Fi dan tata letak rumah Anda  
**Penerbit:** Microsoft Support  
**URL:** https://support.microsoft.com/id-id/windows/experience/connectivity-networking/wi-fi-and-your-home-layout  
**Tanggal akses:** 9 November 2026

Sumber ini digunakan untuk aturan bahwa sinyal Wi-Fi yang lemah dapat ditangani dengan mendekatkan perangkat ke titik akses/router dan mengurangi penghalang.

---

## 5. Basis Aturan IF-THEN

| ID | IF | THEN | Sumber |
|---|---|---|---|
| R1 | Wi-Fi terhubung AND tidak ada internet | koneksi internet bermasalah | S1 |
| R2 | koneksi internet bermasalah AND semua perangkat tidak bisa internet | kemungkinan masalah router atau modem | S1 |
| R3 | kemungkinan masalah router atau modem AND IP router 0.0.0.0 | periksa koneksi modem dan router | S2 |
| R4 | Wi-Fi lambat AND sinyal lemah | kualitas sinyal buruk | S1 |
| R5 | kualitas sinyal buruk | disarankan mendekat ke router | S4 |
| R6 | koneksi sering terputus | koneksi tidak stabil | S1 |
| R7 | koneksi tidak stabil | periksa pengaturan daya adaptor Wi-Fi | S1 |
| R8 | Wi-Fi tidak terdeteksi | periksa adaptor Wi-Fi dan sakelar Wi-Fi | S1 |

### Aturan yang membentuk rantai

R1 menghasilkan:

```text
koneksi internet bermasalah
```

Hasil tersebut digunakan oleh R2:

```text
koneksi internet bermasalah
        +
semua perangkat tidak bisa internet
        ↓
kemungkinan masalah router atau modem
```

Hasil R2 kemudian digunakan oleh R3:

```text
kemungkinan masalah router atau modem
        +
IP router 0.0.0.0
        ↓
periksa koneksi modem dan router
```

Jadi terdapat rantai forward chaining:

```text
Fakta awal
   ↓
R1
   ↓
koneksi internet bermasalah
   ↓
R2
   ↓
kemungkinan masalah router atau modem
   ↓
R3
   ↓
periksa koneksi modem dan router
```

---

## 6. Metode Inferensi: Forward Chaining

Forward Chaining adalah metode penalaran yang dimulai dari **fakta awal**, kemudian mencari aturan yang syaratnya terpenuhi. Jika sebuah aturan terpenuhi, bagian THEN ditambahkan sebagai fakta baru. Proses diulangi sampai tidak ada aturan baru yang dapat dijalankan.

Pseudocode sederhana:

```text
memori = fakta awal

ULANGI:
    cari aturan yang semua syaratnya ada di memori
    dan hasilnya belum ada di memori

    jika tidak ada:
        berhenti

    jalankan aturan
    tambahkan hasil THEN ke memori
    catat aturan sebagai alasan
```

### Contoh perhitungan manual

Fakta awal:

```text
wifi terhubung
tidak ada internet
semua perangkat tidak bisa internet
ip router 0.0.0.0
```

#### Siklus 1

R1:

```text
IF wifi terhubung
AND tidak ada internet
THEN koneksi internet bermasalah
```

Karena kedua fakta tersedia, R1 aktif.

Fakta baru:

```text
koneksi internet bermasalah
```

#### Siklus 2

R2:

```text
IF koneksi internet bermasalah
AND semua perangkat tidak bisa internet
THEN kemungkinan masalah router atau modem
```

Kedua syarat tersedia.

Fakta baru:

```text
kemungkinan masalah router atau modem
```

#### Siklus 3

R3:

```text
IF kemungkinan masalah router atau modem
AND ip_router 0.0.0.0
THEN periksa koneksi modem dan router
```

Kedua syarat tersedia.

Fakta baru:

```text
periksa koneksi modem dan router
```

#### Siklus 4

Tidak ada aturan baru yang dapat dijalankan.

Program berhenti.

Kesimpulan:

```text
koneksi internet bermasalah
kemungkinan masalah router atau modem
periksa koneksi modem dan router
```

---

## 7. Kasus Uji

Pengujian dilakukan menggunakan tiga kasus untuk mengetahui apakah sistem dapat menerapkan metode **Forward Chaining** sesuai dengan fakta yang diberikan oleh pengguna. Dua kasus menghasilkan kesimpulan, sedangkan satu kasus tidak menghasilkan kesimpulan karena tidak ada aturan yang terpenuhi.

### Kasus 1 — Gangguan Internet pada Semua Perangkat

[Kasus 1](screenshot/kasus 1.png)

**Deskripsi kasus:**

Pada kasus ini, pengguna mengalami kondisi Wi-Fi terhubung tetapi tidak dapat digunakan untuk mengakses internet. Masalah terjadi pada seluruh perangkat yang terhubung ke jaringan. Pengguna juga mengetahui bahwa alamat IP router menunjukkan `0.0.0.0`.

**Jawaban `ya`:**

```text
- Wi-Fi terhubung
- Tidak ada internet
- Semua perangkat tidak bisa internet
- IP router 0.0.0.0
```

Berdasarkan fakta tersebut, sistem menjalankan aturan secara berurutan menggunakan Forward Chaining.

**Rantai aturan yang diharapkan:**

```text
R1 → koneksi internet bermasalah
R2 → kemungkinan masalah router atau modem
R3 → periksa koneksi modem dan router
```

Penjelasan prosesnya adalah sebagai berikut:

```text
R1:
Wi-Fi terhubung + tidak ada internet
→ koneksi internet bermasalah

R2:
koneksi internet bermasalah + semua perangkat tidak bisa internet
→ kemungkinan masalah router atau modem

R3:
kemungkinan masalah router atau modem + IP router 0.0.0.0
→ periksa koneksi modem dan router
```

Dengan demikian, fakta baru yang dihasilkan oleh R1 digunakan kembali sebagai fakta untuk menjalankan R2. Selanjutnya, hasil dari R2 digunakan untuk menjalankan R3. Hal ini menunjukkan proses **Forward Chaining secara bertahap dari fakta awal menuju kesimpulan**.

**Kesimpulan yang diharapkan:**

```text
- koneksi internet bermasalah
- kemungkinan masalah router atau modem
- periksa koneksi modem dan router
```

Simpan screenshot hasil pengujian sebagai:

```text
screenshot/kasus1.png
```

---

### Kasus 2 — Sinyal Wi-Fi Lemah

[Kasus 2](screenshot/kasus 2.png)

**Deskripsi kasus:**

Pada kasus ini, pengguna mengalami koneksi Wi-Fi yang lambat dan mengetahui bahwa sinyal Wi-Fi yang diterima perangkat tergolong lemah. Fakta tersebut digunakan untuk mengetahui kemungkinan masalah pada kualitas sinyal.

**Jawaban `ya`:**

```text
- Wi-Fi lambat
- Sinyal lemah
```

Berdasarkan fakta tersebut, sistem menjalankan aturan R4 terlebih dahulu. Kesimpulan yang diperoleh dari R4 kemudian digunakan sebagai fakta baru untuk menjalankan R5.

**Rantai aturan yang diharapkan:**

```text
R4 → kualitas sinyal buruk
R5 → disarankan mendekat ke router
```

Penjelasan prosesnya adalah sebagai berikut:

```text
R4:
Wi-Fi lambat + sinyal lemah
→ kualitas sinyal buruk

R5:
kualitas sinyal buruk
→ disarankan mendekat ke router
```

Dengan demikian, sistem tidak hanya menggunakan fakta yang diberikan pengguna, tetapi juga menggunakan **kesimpulan dari aturan sebelumnya sebagai fakta baru** untuk menjalankan aturan berikutnya.

**Kesimpulan yang diharapkan:**

```text
- kualitas sinyal buruk
- disarankan mendekat ke router
```

Simpan screenshot hasil pengujian sebagai:

```text
screenshot/kasus 2.png
```

---

### Kasus 3 — Tidak Menghasilkan Kesimpulan

[Kasus 3](screenshot/kasus 3.png)

**Deskripsi kasus:**

Pada kasus ini, pengguna hanya menyatakan bahwa perangkat terhubung ke Wi-Fi. Tidak ada fakta lain yang mendukung kondisi pada aturan yang tersedia.

**Jawaban `ya`:**

```text
- Wi-Fi terhubung
```

Fakta tersebut belum cukup untuk memenuhi kondisi aturan mana pun. Oleh karena itu, sistem tidak dapat menghasilkan fakta baru.

**Proses Forward Chaining yang diharapkan:**

```text
Fakta awal:
Wi-Fi terhubung

Tidak ada aturan yang seluruh kondisinya terpenuhi
→ tidak ada aturan yang dapat dijalankan
→ proses berhenti
```

Sistem kemudian menampilkan bahwa tidak ditemukan kesimpulan berdasarkan fakta yang diberikan.

**Hasil yang diharapkan:**

```text
Tidak ditemukan kesimpulan berdasarkan fakta
yang diberikan dan aturan yang tersedia.
```

Kasus ini digunakan untuk menguji kondisi ketika **tidak terdapat aturan yang dapat dijalankan**, sehingga sistem dapat berhenti dengan benar tanpa menghasilkan diagnosis yang tidak didukung oleh fakta.

Simpan screenshot hasil pengujian sebagai:

```text
screenshot/kasus3.png
```

## 8. Screenshot

Setelah menjalankan program, ambil minimal tiga screenshot:

1. Kasus 1 - menghasilkan kesimpulan.
2. Kasus 2 - menghasilkan kesimpulan.
3. Kasus 3 - tidak menghasilkan kesimpulan.


[Kasus 1](screenshot/kasus1.png)

[Kasus 2](screenshot/kasus2.png)

[Kasus 3](screenshot/kasus3.png)

---

## 9. Batas Keberlakuan

Basis pengetahuan sistem ini dirangkum dari dokumentasi resmi Microsoft Support dan TP-Link Support mengenai troubleshooting Wi-Fi dan router. Sistem ditujukan untuk membantu pengguna Windows atau jaringan Wi-Fi rumah dalam mengidentifikasi beberapa pola gangguan dasar berdasarkan fakta yang diberikan. Sistem tidak mencakup seluruh kemungkinan penyebab gangguan jaringan dan hasilnya hanya merupakan saran awal untuk troubleshooting, bukan diagnosis teknis atau keputusan akhir. Kondisi perangkat, model router, konfigurasi jaringan, dan layanan ISP dapat menyebabkan hasil nyata berbeda dari kesimpulan sistem.

---

## 10. Penggunaan AI

AI digunakan sebagai alat bantu dalam proses pengerjaan tugas, terutama untuk:

- membantu memahami materi sistem pakar dan Forward Chaining;
- membantu melakukan pengecekan logika kode;
- membantu merapikan dokumentasi README.

Basis aturan tetap disusun berdasarkan sumber resmi yang dicantumkan pada bagian sumber. Program kemudian diuji dengan beberapa kasus untuk memastikan proses Forward Chaining berjalan sesuai aturan.

---

## 11. Kesimpulan

Sistem yang dibuat merupakan sistem pakar sederhana berbasis aturan menggunakan metode Forward Chaining. Basis pengetahuan dipisahkan dari mesin inferensi dalam file `kb_wifi.json`. Program membaca aturan tersebut, menerima fakta dari pengguna, menjalankan aturan secara bertahap, menghasilkan fakta baru, dan menampilkan kesimpulan beserta aturan yang menjadi alasannya.

Sistem berhasil menunjukkan proses penalaran berantai, yaitu hasil suatu aturan dapat menjadi kondisi untuk aturan berikutnya. Sistem juga dapat menangani kasus ketika tidak ada aturan yang terpenuhi.
