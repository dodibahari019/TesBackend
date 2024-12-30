print(f"{'='*50}")
print(f"{'HITUNG GAJI KARYAWAN':^100}")
print(f"{'='*50}")

def hitung_gaji(jamKerja, tarifPerJam):
  if jamKerja > 40:
    jamLembur = jamKerja - 40
    gajiLembur = jamLembur * (1.5 * tarifPerJam)
    gajiTotal = (40 * tarifPerJam) + gajiLembur
  else:
    gajiTotal = jamKerja * tarifPerJam

  return gajiTotal

try:
  jamKerja = float(input("Masukkan jumlah jam kerja: "))
  tarifPerJam = float(input("Masukkan tarif per jam: "))

  gaji = hitung_gaji(jamKerja, tarifPerJam)
  print(f"Gaji total karyawan adalah: Rp {gaji:,.2f}")
except ValueError:
  print("Masukkan angka yang sesuai ya!")
