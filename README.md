# Studi-Kasus-NIMGanjil-Sistem-Pencatatan-Nilai-Mahasiswa

## Penjelasan Singkat Kode 
### Library

<img width="160" height="48" alt="image" src="https://github.com/user-attachments/assets/ae7e511b-490f-412f-baa3-5c3f10258759" />

Import Library bawaan python. Digunakan untuk mengolah data berformat JSON, OS digunakan untuk mengecek keberadaan file dalam sistem.

### Fungsi Load Data

<img width="542" height="278" alt="image" src="https://github.com/user-attachments/assets/77993953-9b45-45b2-927e-a8a8d13fd2b6" />

Fungsi untuk membaca data dari file data_nilai.json. Fungsi ini mengecek apakah data sudah ada atau belum lewat os.path.exists(). Jika belum ada, file baru dibuat dengan isi list kosong []. Fungsi ini juga dilengkapi penanganan error json.JSONDecodeError agar program tidak crash jika isi file kosong.

### Fungsi Simpan Data

<img width="435" height="75" alt="image" src="https://github.com/user-attachments/assets/13a81c90-49b6-407c-b5cd-40eb41cbf04f" />

Fungsi untuk menuliskan/menyimpan seluruh data mahasiswa yang ada di dalam list data ke file data_nilai.json

### Fungsi Tampil Data

<img width="905" height="320" alt="image" src="https://github.com/user-attachments/assets/f8b9b4ce-8f13-4c45-8bb7-a8c07d9351de" />

Fungsi untuk menampilkan seluruh data nilai mahasiswa yang tersimpan ke dalam tabel, Jika data kosong akan muncul pesan pemberitahuan.

### Fungsi Tambah Nilai

<img width="747" height="527" alt="image" src="https://github.com/user-attachments/assets/fa060869-1977-470a-8f9b-5e3668577585" />

Fungsi untuk menerima input data mahasiswa baru dari pengguna. Fungsi ini dilengkapi validasi try-except agar input nilai harus berupa angka (float). Setelah data baru ditambahkan ke list, fungsi langsung memanggil simpan_data() agar perubahan tersimpan.

### Fungsi Utama (Main)

<img width="700" height="597" alt="image" src="https://github.com/user-attachments/assets/f1dd0ebe-3ae2-4254-99ca-0a72c8997179" />


Fungsi utama yang menjalankan menu dengan perulangan while True. Menu ini terus berjalan sampai pengguna memilih angka 3 untuk keluar.

## Output

<img width="586" height="257" alt="image" src="https://github.com/user-attachments/assets/bb28f846-7d7f-4249-9524-58e1f18a9e8e" />

Output ketika user memilih pilihan 1 (Lihat riwayat nilai). Jika belum ada data yang ditambahkan sebelumnya akan muncuk pesan pemberitahuan seperti yang ada digambar.

<img width="615" height="301" alt="image" src="https://github.com/user-attachments/assets/d0acb89a-3945-41af-82f0-17cfaea304c1" />

Output ketika user memilih pilihan 2 (Tambah nilai baru). User akan diminta untuk menginput NIM, Nama, dan Nilai. Ketika semua data sudah valid maka data berhasil disimpan.

<img width="1473" height="312" alt="image" src="https://github.com/user-attachments/assets/79eb8752-470a-437e-9bca-7824cba2fe4b" />

Ketika user sudah menambahkan data maka data akan muncul otomatis di file JSON

<img width="427" height="308" alt="image" src="https://github.com/user-attachments/assets/1f31e966-3478-4195-b256-f5a0f40bdd12" />

Berikut output ketika user sudah menambahkan data sebelumnya dan memilih pilihan 1(Lihat riwayat data kembali) kembali maka akan muncul tabel beserta data yang sudah diinput sebelumnya.

<img width="193" height="70" alt="image" src="https://github.com/user-attachments/assets/9371aed5-f3a5-420d-a569-5fea57ea15e4" />

Output ketika user memilih pilihan 3, maka program berhenti berjalan dan akan muncul pesan 'Terima Kasih!'







