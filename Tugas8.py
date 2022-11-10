# import library
from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# inisialisasi fungsi
def ganjil_genap(i):
   if i % 2 == 0:
      print(i+1, "Genap - ID proses", getpid())
   else:
      print(i+1, "Ganjil - ID proses", getpid())
   sleep(1)

# input
angka = int(input("Input:\n"))

print("\nOutput:")

# Pemrosesan Sekuensial
print("\nSekuensial")
sekuensial_awal = time()

for i in range (angka):
   ganjil_genap(i)

sekuensial_akhir = time()

# Multiprocessing Process
print("\nmultiprocessing.Process")
kumpulan_proses = []

process_awal = time()

for i in range (angka):
   p = Process(target=ganjil_genap, args=(i,))
   kumpulan_proses.append(p)
   p.start()

for i in kumpulan_proses:
   p.join()

process_akhir = time()

# Multiprocessing Pool
print("\nmultiprocessing.Pool")
Pool_awal = time()

Pool = Pool()
Pool.map(ganjil_genap, range(0, 3))
Pool.close

Pool_akhir = time()

# Perbandingan Waktu
print("\nWaktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool :", Pool_akhir - Pool_awal, "detik")
