print("==========================================================")
data_nama = input("Masukkan nama kamu: ")
data_kelamin = input("L/P: ")
data_kampus = input("Masukkan nama kampus: ")
data_umur = input("Masukkan umur: ")
data_semester = input("Masukkan semester sekarang: ")
print("========================================")
print(f"Biodata akademik dari {data_nama}: ")
print(f"1. Namanya {data_nama}")

# status kelamin
if data_kelamin == "L":
    print(f"2. {data_nama} adalah Laki-laki")
else:
    print(f"2. {data_nama} adalah Perempuan")
    
print(f"3. {data_nama} saat ini berkuliah di {data_kampus}")

# status mahasiswa
if int(data_semester) >= int(1) and int(data_semester) <= int(2):
    print(f"4. {data_nama} termasuk mahasiswa baru karena baru semester {data_semester}")
elif int(data_semester) >= int (3) and int(data_semester) <= int (6):
    print(f"4. {data_nama} termasuk mahasiswa junior karena sudah semester {data_semester}")
elif int(data_semester) >= int (7) and int(data_semester) <= int (8):
    print(f"4. {data_nama} termasuk mahasiswa akhir karena sudah semester {data_semester}")
elif int(data_semester) > int (8):
    print(f"4. {data_nama} termasuk mahasiswa abadi karena sudah semester {data_semester}")
else:
    print(f"4. Data tidak ada!")

# status angkatan
if int(data_semester) == int(1):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2022")
elif int(data_semester) == int (2):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2022")
elif int(data_semester) == int (3):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2021")
elif int(data_semester) == int (4):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2021")
elif int(data_semester) == int (5):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2020")
elif int(data_semester) == int (6):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2020")
elif int(data_semester) == int (7):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2019")  
elif int(data_semester) == int (8):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2019")  
elif int(data_semester) == int (9):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2018")
elif int(data_semester) == int (10):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2018")
elif int(data_semester) == int (11):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2017")
elif int(data_semester) == int (12):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2017")
elif int(data_semester) == int (13):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2016")
elif int(data_semester) == int (14):
    print(f"5. Status {data_nama} adalah mahasiswa angkatan 2016")
else:
    print(f"5. Mahasiswa telah berstatus dikeluarkan / Drop Out (DO)!")

# kategori umur
if int(data_umur) > int(0) and int(data_umur) <= int(10):
    print(f"6. {data_nama} termasuk anak-anak karena masih berusia {data_umur} tahun")
elif int(data_umur) > int (10) and int(data_umur) <= int (17):
    print(f"6. {data_nama} termasuk anak remaja karena sudah berusia {data_umur} tahun")
elif int(data_umur) >= int (18):
    print(f"6. {data_nama} termasuk orang dewasa karena sudah berusia {data_umur} tahun")
else:
    print(f"6. Tidak ada umur kurang dari {data_umur} tahun")

# Tahun kelulusan dimulai dari angkatan 2019 :)
if int(data_semester) == int(1):
    print(f"7. Tahun kelulusan {data_nama} adalah pada tahun 2026")
elif int(data_semester) == int (2):
    print(f"7. Tahun kelulusan {data_nama} adalah pada tahun 2026")
elif int(data_semester) == int (3):
    print(f"7. Tahun kelulusan {data_nama} adalah pada tahun 2025")
elif int(data_semester) == int (4):
    print(f"7. Tahun kelulusan {data_nama} adalah pada tahun 2025")
elif int(data_semester) == int (5):
    print(f"7. Tahun kelulusan {data_nama} adalah pada tahun 2024")
elif int(data_semester) == int (6):
    print(f"7. Tahun kelulusan {data_nama} adalah pada tahun 2024")
elif int(data_semester) == int (7):
    print(f"7. Tahun kelulusan {data_nama} adalah pada tahun 2023")
elif int(data_semester) == int (8):
    print(f"7. Tahun kelulusan {data_nama} adalah pada tahun 2023")
elif int(data_semester) > int (8):
    print(f"7. Tahun kelulusan {data_nama} tidak diketahui karena melebihi 8 semester")
else:
    print("Data tidak valid!")

print(f'\nTerima Kasih sudah mengunjungi Website Akademik {data_kampus}!')
print("==========================================================")