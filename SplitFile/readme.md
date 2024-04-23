# Split File Python Program

Program ini memecah file teks menjadi beberapa file kecil dengan jumlah baris tertentu.

## Cara Menggunakan

1. Pastikan Anda memiliki Python diinstal di komputer Anda. Anda dapat mengunduh Python dari situs web resminya: [python.org](https://www.python.org/downloads/).

2. Clone repository ini atau unduh file `app.py` dan letakkan di folder Anda.

3. Letakkan file teks yang ingin Anda pecah di dalam folder yang sama dengan `app.py`.

4. Buka terminal atau command prompt, lalu arahkan ke direktori tempat Anda menyimpan file `app.py`.

5. Jalankan program dengan perintah berikut:

   ```bash
   python app.py
   ```

6. Setelah menjalankan perintah di atas, Anda akan diminta untuk memasukkan path dari file teks dan jumlah baris maksimal. Jika jumlah baris maksimal tidak dimasukkan, maka secara default akan menjadi 100 baris.

7. Program kemudian akan memecah file teks menjadi beberapa file kecil sesuai dengan jumlah baris maksimal yang dimasukkan, dan menyimpannya dalam folder yang baru dibuat bernama `split_files`.

## Contoh Penggunaan

```bash
$ python app.py
Masukkan path dari file teks: rockyou.txt
Masukkan jumlah baris maksimal (default: 100): 100
4 file telah dibuat di folder split_files.
```

## Catatan

Pastikan file teks yang ingin Anda pecah berada dalam format yang dapat dibaca (UTF-8, latin-1, dsb.).
