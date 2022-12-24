import os
from random import choice

kota = ['bandung', 'bekasi', 'depok', 'bogor', 'cimahi', 'cirebon', 'sukabumi', 'solo', 'semarang', 'salatiga', 'magelang', 'pekalongan', 'tegal', 'klaten', 'surabaya', 'malang', 'madiun', 'blitar', 'kediri', 'mojokerto', 'sidoarjo', 'gresik', 'jombang', 'pasuruan']

kata = choice(kota)

Token = 10
Kalah = False
Tebakan = []
hasil = ['*'] * len(kata)

print()
nama = input("Ayok Main Tebak Nama Kota, Siapa Namamu?")
print("Have Fun & Good Luck", nama)
print()

()
print('''
+****************************************+
| SELAMAT DATANG DI GAME TEBAK NAMA KOTA |
+****************************************+
''')

while not Kalah: 

    print("Token : {}".format(u'\U0001f537'*Token))
    print("Huruf Tertebak : {}".format(Tebakan))

    hidden_word = ''.join(hasil)
    print("Tebak Nama Kota Berikut Ini : {}".format(hidden_word))
    print("Ketik 'keluar' untuk berhenti bermain")
    huruf = input("Tebak 1 Huruf : ").lower()


    if huruf == 'keluar':
      print('''
      *-----------------------------------------*
      |       Terima Kasih Telah Bermain        |
      *-----------------------------------------*
      ''')
      Kalah = True
    elif huruf in kata and huruf not in Tebakan:
      print("Tebakan Anda Benar")
      for i in range(len(kata)):
        if kata[i] == huruf:
            hasil[i] = huruf
    elif huruf in Tebakan:
      print("Huruf Sudah Ditebak Sebelumnya, Coba lagi")
    else:
         Token -= 1
         print("Yahh...Tebakan Anda Salah")

    if huruf not in Tebakan:
      Tebakan.append(huruf)

    if Token == 1:
      print("Kesempatan Terakhir")
    elif Token <= 0:
      print("Yahh...Kesempatan Anda Habis, Anda KALAH")
      print("WK"*15+"!!")
      Kalah = True
    elif kata == ''.join(hasil):
       print(" Selamat Kamu Berhasil Menebak Nama Kota : {} ".format(''.join(hasil)))
       Kalah = True
       print('''
       +*******************************************************+
       |   YEAY KAMU TELAH MENYELESAIKAN GAME TEBAK NAMA KOTA  |
       +*******************************************************+
       ''')









