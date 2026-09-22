# Capstone E-Commerce

Proyek Capstone ini membahas pengumpulan dan pengolahan data pada domain E-Commerce.

## 1. Domain

Domain yang digunakan adalah E-Commerce.

## 2. Sumber Data

Proyek menggunakan dua sumber data CSV dari dataset Brazilian E-Commerce Public Dataset by Olist:

1. `olist_orders_dataset.csv`
   - Berisi informasi pesanan pelanggan.

2. `olist_order_items_dataset.csv`
   - Berisi informasi detail barang pada setiap pesanan.

Kedua dataset memiliki hubungan melalui atribut `order_id`.

## 3. Struktur Directory

Struktur directory proyek adalah sebagai berikut:

- `data/source/`
  - `olist_orders_dataset.csv`
  - `olist_order_items_dataset.csv`
- `data/raw/`
  - `olist_orders_dataset.csv`
  - `olist_order_items_dataset.csv`
- `scripts/`
  - `data_collection.py`
- `README.md`
- `requirements.txt`

## 4. Data Collection

Proses data collection dilakukan menggunakan script `scripts/data_collection.py`.

Script mengambil data dari folder `data/source/` dan melakukan ingestion ke folder `data/raw/`.

Untuk menjalankan proses ingestion, gunakan perintah:

`python scripts/data_collection.py`

Jika proses berhasil, akan muncul status:

`Status: INGESTION BERHASIL`

## 5. Requirements

Dependensi proyek dicatat dalam file `requirements.txt`.

Pada tahap data collection, proses menggunakan library bawaan Python sehingga tidak membutuhkan library eksternal.