# Pengolahan Citra Project UTS dan UAS

## Anggota Kelompok:

| No  | Nama                      | NIM       | Kelas     | Akun Github                                                  |
| --- | ------------------------- | --------- | --------- | ------------------------------------------------------------ |
| 1   | Anggita Risqi Nur Clarita | 312210450 | TI.22.A.4 | [@AnggitaRisqiNC](https://github.com/AnggitaRisqiNC)         |
| 2   | Faizah Via Fadhillah      | 312210460 | TI.22.A.4 | [@FaizahviaFadhillah](https://github.com/FaizahviaFadhillah) |
| 3   | Zahra Nurhaliza           | 312210364 | TI.22.A.4 | [@ZahraNurhaliza](https://github.com/ZahraNurhaliza)         |

## Daftar Isi

| No  | Description             | Link                                                                                       |
| --- | ----------------------- | ------------------------------------------------------------------------------------------ |
| 1   | Script Code Project UTS | [Click Here](https://github.com/AnggitaRisqiNC/PengolahanCitra/blob/main/ProjectUTS.py)    |
| 2   | Project UTS             | [Click Here](#project-uts)                                                                 |
| 3   | Script Code Project UAS | [Click Here](https://github.com/AnggitaRisqiNC/PengolahanCitra/blob/main/ProjectUAS.ipynb) |
| 4   | Project UAS             | [Click Here](#project-uas)                                                                 |

## Paper Pengolahan Citra
> **Jurnal:** [Penerapan Algoritma _K-Means Clustering_ dan _Elbow Method_ untuk Segmentasi Citra Digital pada Berbagai Jenis Gambar](https://docs.google.com/document/d/1ZGCDCNelKymmnbvPHMWHaNhUQwwNXcfH1jZPuTMdp1c/edit?usp=sharing)

## Project UTS

Kode ini ditulis dengan Python dan menggunakan library Streamlit untuk membuat aplikasi web sederhana. Aplikasi ini difungsikan untuk manajemen citra warna, dimana kita bisa mengunggah gambar atau menggunakan kamera untuk mengambil gambar, kemudian melakukan berbagai operasi pemrosesan gambar.

- **Fungsi-fungsi pada source code kami:**
  - `adjust_brightness_contrast`: Fungsi untuk mengatur kecerahan dan kontras gambar.
  - `detect_contours`: Fungsi untuk mendeteksi kontur objek dalam gambar (garis tepi).
  - `detect_faces`: Fungsi untuk mendeteksi wajah dalam gambar.
  - `detect_eyes`: Fungsi untuk mendeteksi mata dalam gambar.
  - Bagian ini juga menangani pengunggahan gambar dan penggunaan kamera.
  - `convert_to_hsv`: Fungsi untuk mengubah format warna gambar dari BGR ke HSV.
  - `calculate_histogram`: Fungsi untuk menghitung histogram warna gambar (distribusi intensitas warna).
  - Bagian ini juga menyediakan pilihan operasi yang bisa dilakukan pada gambar yang diunggah/dicapture.

### Tutorial Menjalankan Aplikasi:

#### Persiapan:

1. Pastikan kalian sudah memiliki Python terinstall di komputer kalian. [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Install library Streamlit menggunakan pip: `pip install streamlit`
3. Download file kode tersebut dan simpan dengan nama `app.py`.

#### Menjalankan Aplikasi:

1. Buka Command Prompt (CMD) atau Terminal.
2. Arahkan direktori ke folder tempat kalian menyimpan file `app.py`. kalian bisa menggunakan perintah `cd` diikuti dengan path direktori. Contoh: `cd Desktop/image-processing`.
3. Ketikkan perintah berikut untuk menjalankan aplikasi: `streamlit run app.py`
4. Tunggu hingga Streamlit membuka aplikasi pada web browser secara otomatis (biasanya di http://localhost:8501/).

#### Mengenal Aplikasi:

- Kalian akan melihat tampilan awal dengan judul "Aplikasi Manajemen Citra Warna".
- Di sebelah kanan terdapat bagian untuk mengunggah gambar ( tombol "Upload Gambar") atau menggunakan kamera (tombol "Ambil Gambar dari Kamera").
- Ketika gambar sudah diunggah/dicapture, kalian bisa mengatur kecerahan dan kontras menggunakan slider yang tersedia.
- Tombol-tombol di bawah slider digunakan untuk melakukan operasi tertentu pada gambar, seperti:
  - Atur Kecerahan dan Kontras : Menyesuaikan kecerahan dan kontras sesuai pengaturan slider.
  - Deteksi Kontur : Mendeteksi dan menampilkan kontur objek pada gambar.
  - Deteksi Wajah : Mendeteksi dan menghitung jumlah wajah yang ditemukan pada gambar.
  - Deteksi Mata ️: Mendeteksi dan menghitung jumlah mata yang ditemukan pada gambar.
- Di sebelah kiri terdapat pilihan operasi warna:
  - Ubah ke HSV: Mengubah format warna gambar menjadi HSV dan menampilkannya.
  - Hitung Histogram: Menghitung histogram warna gambar dan menampilkannya dalam bentuk grafik batang.

#### Tampilan Aplikasi:

![1](https://github.com/AnggitaRisqiNC/PengolahanCitra/assets/115614419/9adf77ba-4be7-4643-9fe4-05ce3ae0700e)
![2](https://github.com/AnggitaRisqiNC/PengolahanCitra/assets/115614419/aff2e83e-c586-4e56-ade7-8d46571ead6e)
![3](https://github.com/AnggitaRisqiNC/PengolahanCitra/assets/115614419/2ba0af09-7b25-4173-aec8-097b51b572b5)
![4](https://github.com/AnggitaRisqiNC/PengolahanCitra/assets/115614419/c66f686e-67e9-467d-a3b1-9b616c9f4d4f)
![5](https://github.com/AnggitaRisqiNC/PengolahanCitra/assets/115614419/2178ed72-9985-472b-853f-33831368ba8f)
![6](https://github.com/AnggitaRisqiNC/PengolahanCitra/assets/115614419/f9a68a1f-3262-4c9a-9b5c-b80e4f18e71c)

## Project UAS

Berikut adalah langkah-langkah segmentasi gambar berwarna menggunakan algoritma K-means clustering di Google Notebook. Algoritma ini mengelompokkan piksel gambar dengan warna yang mirip ke dalam cluster yang berbeda, menghasilkan gambar yang tersegmentasi berdasarkan warna.

- **Fungsi-fungsi pada source code kami:**
  - **`import numpy as np`:** Mengimpor library NumPy untuk operasi matematika dan manipulasi array.
  - **`import matplotlib.pyplot as plt`:** Mengimpor library Matplotlib untuk visualisasi data dan pembuatan grafik.
  - **`import cv2`:** Mengimpor library OpenCV untuk pemrosesan gambar dan algoritma K-means clustering.
  - **`pixel_vals = image.reshape((-1, 3))`:** Mengubah bentuk array gambar menjadi matriks 2 dimensi dengan 1 baris dan 3 kolom, di mana setiap baris mewakili piksel dan 3 kolom mewakili nilai warna RGB (Red, Green, Blue).
  - **`pixel_vals = np.float32(pixel_vals)`:** Mengubah tipe data nilai piksel menjadi float32 untuk kompatibilitas dengan algoritma K-means.
  - **`k = int(input("Masukkan jumlah cluster (k): "))`:** Meminta pengguna untuk memasukkan jumlah cluster (k) yang diinginkan. Nilai k ini menentukan berapa banyak kelompok warna yang ingin dibuat dari gambar.
  - **`retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)`:** Melakukan algoritma K-means clustering:
    - `pixel_vals`: Matriks nilai piksel gambar.
    - `k`: Jumlah cluster yang ditentukan oleh pengguna.
    - `None`: Nilai awal pusat cluster tidak ditentukan.
    - `criteria`: Kriteria untuk menghentikan algoritma.
    - `10`: Jumlah percobaan untuk menemukan pusat cluster yang optimal.
    - `cv2.KMEANS_RANDOM_CENTERS`: Metode inisialisasi pusat cluster secara acak.
  - **`segmented_data = centers[labels.flatten()]`:** Mengambil nilai pusat cluster dari setiap piksel berdasarkan label clusternya.
  - **`ax[1].imshow(segmented_image)`:** Menampilkan gambar yang telah di-segmentasi di subplot kedua.

### Tutorial Menjalankan Aplikasi:

#### Persiapan:

1. **Membuka Google Colab:** Buka browser Kalian dan akses [https://colab.research.google.com/](https://colab.research.google.com/). Masuk menggunakan akun Google Kalian.
2. **Membuat Notebook Baru:** Klik tombol "New Notebook" di sebelah kiri atas. Kalian akan diarahkan ke notebook baru.
3. **Siapkan Kode:** Siapkan kode yang kita sediakan dari github kami. Pastikan lagi kode benar tanpa kesalahan.
4. Pastikan Kalian sudah menginstal library NumPy, Matplotlib, dan OpenCV di Google Colab. Kalian dapat menginstalnya dengan perintah `!pip install numpy matplotlib opencv-python` di dalam notebook Kalian.

#### Langkah-langkah:

1. **Buka Google Colab:** Buka browser Kalian dan akses [https://colab.research.google.com/](https://colab.research.google.com/).
2. **Buat Notebook Baru:** Klik tombol "New Notebook" di sebelah kiri atas.
3. **Salin Kode:** Salin semua kode yang disediakan di atas ke dalam notebook Kalian.
4. **Upload Gambar:** Klik "Upload" di sebelah kiri atas notebook Kalian. Pilih gambar yang ingin Kalian segmentasi dan unggah.
5. **Ganti Path Gambar:** Pada baris kode `image_path = 'kamboja.jpg'`, ubah path 'kamboja.jpg' menjadi path gambar yang Kalian unggah.
6. **Run Kode:** Klik tombol "Run" di sebelah kiri atas notebook Kalian.
7. **Masukkan Nilai k:** Pada baris kode `k = int(input("Masukkan jumlah cluster (k): "))`, masukkan nilai k yang Kalian inginkan (jumlah cluster warna).
8. **Hasil:** Tunggu hingga kode selesai dijalankan. Kalian akan melihat hasil segmentasi gambar dengan cluster warna dan detail gambar seperti dimensi, jumlah kanal warna, ukuran, tipe data, dan resolusi.

#### Tampilan Aplikasi:

![7](https://github.com/AnggitaRisqiNC/PengolahanCitra/assets/115614419/0e5b1967-978d-442f-ac0c-adca0c91f979)

## Finish

**Terima kasih telah membaca penjelasan project UTS dan UAS kami!**

Kami ingin mengucapkan terima kasih yang sebesar-besarnya kepada semua pihak yang telah membantu kami dalam menyelesaikan project ini. Project ini merupakan hasil kerja keras dan dedikasi dari tim kami, dan kami sangat senang dapat membagikannya.

Kami ingin mengucapkan terima kasih juga kepada dosen pengampu mata kuliah Pengolahan Citra, **Pak Muhammad Fatchan, S.Kom., M.Kom., MTCNA**, yang telah membantu kami dalam memahami konsep-konsep penting dalam pengolahan citra.

- **Manajemen Citra Warna:** Project ini memungkinkan pengguna untuk mengunggah gambar atau menggunakan kamera untuk mengambil gambar, kemudian melakukan berbagai operasi pemrosesan gambar menggunakan Streamlit. Kami berharap project ini dapat membantu pengguna dalam mengelola dan memodifikasi gambar dengan mudah dan efisien serta melakukan berbagai operasi pemrosesan gambar.

- **Segmentasi Gambar Warna dengan K-means Clustering:** Project ini memandu pengguna dalam melakukan segmentasi gambar berwarna menggunakan algoritma K-means clustering di Google Notebook. Kami berharap project ini dapat membantu pengguna dalam memahami konsep segmentasi gambar dan menerapkannya pada gambar yang berbeda.

**Sekali lagi, terima kasih telah membaca!**

Terima kasih juga kepada [@FaizahviaFadhillah](https://github.com/FaizahviaFadhillah) dan [@ZahraNurhaliza](https://github.com/ZahraNurhaliza) atas kontribusinya dalam menyelesaikan project ini.
