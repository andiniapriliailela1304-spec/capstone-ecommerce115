import os
import shutil
from datetime import datetime

# Folder sumber dan tujuan
SOURCE_FOLDER = "data/source"
RAW_FOLDER = "data/raw"

# Daftar file yang akan di-ingest
FILES = [
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv"
]


def collect_data():
    print("======================================")
    print("       DATA COLLECTION CAPSTONE")
    print("======================================")

    # Membuat folder raw jika belum ada
    os.makedirs(RAW_FOLDER, exist_ok=True)

    success = True

    for file_name in FILES:

        source_path = os.path.join(SOURCE_FOLDER, file_name)
        raw_path = os.path.join(RAW_FOLDER, file_name)

        # Mengecek apakah file sumber tersedia
        if os.path.exists(source_path):

            # Menyalin data dari source ke raw
            shutil.copy2(source_path, raw_path)

            print(f"[OK] {file_name}")
            print("     Data berhasil di-ingest ke data/raw/")

        else:

            print(f"[ERROR] {file_name} tidak ditemukan di data/source/")
            success = False

    print("\nWaktu ingestion:")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if success:
        print("\nStatus: INGESTION BERHASIL")
    else:
        print("\nStatus: INGESTION GAGAL")

    print("======================================")


if __name__ == "__main__":
    collect_data()