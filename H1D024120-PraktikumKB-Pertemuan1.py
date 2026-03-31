import statistics
from datetime import datetime

# 1. Implementasi Struktur Data (List dan Dictionary)
# List yang berisi kumpulan dictionary (data penjualan produk)
data_penjualan = [
    {"produk": "Laptop", "harga": 15000000, "terjual": 5},
    {"produk": "Mouse", "harga": 250000, "terjual": 20},
    {"produk": "Monitor", "harga": 2000000, "terjual": 8},
    {"produk": "Keyboard", "harga": 500000, "terjual": 12}
]

def main():
    print(f"--- Laporan Penjualan Per Tanggal: {datetime.now().strftime('%Y-%m-%d')} ---")
    
    total_pendapatan_list = []

    # 2. Implementasi Struktur Kontrol (Looping)
    for item in data_penjualan:
        total_item = item["harga"] * item["terjual"]
        total_pendapatan_list.append(total_item)
        
        # 2. Implementasi Struktur Kontrol (Percabangan)
        if total_item > 10000000:
            kategori = "Sangat Tinggi"
        elif total_item > 5000000:
            kategori = "Tinggi"
        else:
            kategori = "Standar"
            
        print(f"Produk: {item['produk']} | Total: Rp{total_item:,} | Kategori: {kategori}")

    # 3. Implementasi Library (Menggunakan library 'statistics')
    rata_rata = statistics.mean(total_pendapatan_list)
    total_seluruh = sum(total_pendapatan_list)

    print("-" * 45)
    print(f"Total Pendapatan Seluruhnya : Rp{total_seluruh:,}")
    print(f"Rata-rata Pendapatan Produk : Rp{rata_rata:,}")
    print("-" * 45)

if __name__ == "__main__":
    main()