print ("\n")
print ("--------------------------------------")
print ("===PROGRAM MENGHITUNG GAJI KARYAWAN===")
print (">>>>>>>>>>>>> OBP HER-1 <<<<<<<<<<<<<<")
print ("--------------------------------------")

nama = input("Masukkan Nama Anda : ")

print ("     Silahkan Pilih Jabatan Anda  ")
print ("     1. Manager          ")
print ("     2. Kepala Devisi    ")
print ("     3. Karyawan Tetap   ")
print ("     4. Karyawan Kontrak ")
print ("     5. Info Kami        ")

pilihan = int(input("Masukkan Jabatan anda(dengan angka)   : "))
print ("\n")

manager          = 25000000
kepala_divisi    = 12000000
karyawan_tetap   = 6000000
karyawan_kontrak = 4000000

if pilihan == 1:
    print ("Note : Diawali dengan huruf besar! ")
    pilihan2 = input("Apakah Anda mempunyai Istri(Ya/Tidak) : ")
    pilihan3 = input("Apakah anda punya Anak(Ya/Tidak)      : ")
    print ("\n")
    print (" _______________________________________________")
    print ("| ============ Slip Gaji Karyawan ============= |")
    print ("| Nama                        :", nama,      "          |" )
    print ("| Jabatan                     : Manager         |")
    print ("| Gaji Pokok Anda             : Rp. ", manager, "  |")
    pajak = 0.05 * manager
    print ("| Pajak yang harus Anda bayar : Rp. ", pajak,  " |")

    if pilihan2 == "Ya":
        tunjangan2_istri = manager * 0.04
        print ("| Tunjangan untuk istri Anda  : Rp. ", tunjangan2_istri, " |")
    
        if pilihan3 == "Ya" :
            tunjangan3_anak = manager * 0.06
            total = manager - pajak + tunjangan2_istri + tunjangan3_anak
            print ("| Tunjangan untuk anak Anda   : Rp. ", tunjangan3_anak, " |")
            print ("| --------------------------------------------- |")
            print ("| Total Gaji bersih anda     : Rp. ",total, " |" )
        else:
            total = manager - pajak + tunjangan2_istri
            print ("| Total Gaji bersih anda      : Rp. ",total,"|" )
    else:
        total = manager - pajak
        print ("| Total Gaji bersih anda      : Rp. ",total, "|" )

    print ("| (Sudah termasuk pajak dan tunjangan)          |")
    print ("| ----------------------------------------------|")
    print ("| Tanggal Penerimaan Gaji     : 04 Oktober 2021 |")
    print ("|_______________________________________________|")
    print ("\n")


if pilihan == 2:
    print ("Note : Diawali dengan huruf besar! ")
    pilihan2 = input("Apakah Anda mempunyai Istri(Ya/Tidak) : ")
    pilihan3 = input("Apakah anda punya Anak(Ya/Tidak)      : ")
    print ("\n")
    print (" _______________________________________________")
    print ("| ============ Slip Gaji Karyawan ============  |")
    print ("| Nama                        :", nama,      "          |" )
    print ("| Jabatan                     : Kepala Divisi   |")
    print ("| Gaji Pokok Anda             : Rp. ", kepala_divisi, "  |")
    pajak = 0.05 * kepala_divisi
    print ("| Pajak yang harus Anda bayar : Rp. ", pajak,  "  |")

    if pilihan2 == "Ya":
        tunjangan2_istri = kepala_divisi * 0.04
        print ("| Tunjangan untuk istri Anda  : Rp. ", tunjangan2_istri, "  |")
    
        if pilihan3 == "Ya" :
            tunjangan3_anak = kepala_divisi * 0.06
            total = kepala_divisi - pajak + tunjangan2_istri + tunjangan3_anak
            print ("| Tunjangan untuk anak Anda   : Rp. ", tunjangan3_anak, "  |")
            print ("| --------------------------------------------- |")
            print ("| Total Gaji bersih anda     : Rp. ",total," |" )
        else:
            total = kepala_divisi - pajak + tunjangan2_istri
            print ("| Total Gaji bersih anda      : Rp. ",total, "|" )
    else:
        total = kepala_divisi - pajak
        print ("| Total Gaji bersih anda      : Rp. ",total,"|" )

    print ("| (Sudah termasuk pajak dan tunjangan)          |")
    print ("| ----------------------------------------------|")
    print ("| Tanggal Penerimaan Gaji     : 04 Oktober 2021 |")
    print ("|_______________________________________________|")
    print ("\n")


if pilihan == 3:
    print ("Note : Diawali dengan huruf besar! ")
    pilihan2 = input("Apakah Anda mempunyai Istri(Ya/Tidak) : ")
    pilihan3 = input("Apakah anda punya Anak(Ya/Tidak)      : ")
    print ("\n")
    print (" ______________________________________________")
    print ("| ============ Slip Gaji Karyawan ============ |")
    print ("| Nama                        :", nama,      "         |" )
    print ("| Jabatan                     : Karyawan Tetap |")
    print ("| Gaji Pokok Anda             : Rp. ", karyawan_tetap, "  |")
    pajak = 0.05 * karyawan_tetap
    print ("| Pajak yang harus Anda bayar : Rp. ", pajak,  " |")

    if pilihan2 == "Ya":
        tunjangan2_istri = karyawan_tetap * 0.04
        print ("| Tunjangan untuk istri Anda  : Rp. ", tunjangan2_istri, " |")
    
        if pilihan3 == "Ya" :
            tunjangan3_anak = karyawan_tetap * 0.06
            total = karyawan_tetap - pajak + tunjangan2_istri + tunjangan3_anak
            print ("| Tunjangan untuk anak Anda   : Rp. ", tunjangan3_anak, " |")
            print ("| -------------------------------------------- |")
            print ("| Total Gaji bersih anda     : Rp. ",total," |" )
        else:
            total = karyawan_tetap - pajak + tunjangan2_istri
            print ("| Total Gaji bersih anda      : Rp. ",total, "|" )
    else:
        total = karyawan_tetap - pajak
        print ("| Total Gaji bersih anda      : Rp. ",total,"|" )

    print ("| (Sudah termasuk pajak dan tunjangan)         |")
    print ("| ---------------------------------------------|")
    print ("| Tanggal Penerimaan Gaji     : 04 Oktober 2021|")
    print ("|______________________________________________|")
    print ("\n")


if pilihan == 4:
    print ("Note : Diawali dengan huruf besar! ")
    pilihan2 = input("Apakah Anda mempunyai Istri(Ya/Tidak) : ")
    pilihan3 = input("Apakah anda punya Anak(Ya/Tidak)      : ")
    print ("\n")
    print (" _______________________________________________")
    print ("| ============ Slip Gaji Karyawan ============  |")
    print ("| Nama                        :", nama,      "          |" )
    print ("| Jabatan                     : Karyawan Kontrak|")
    print ("| Gaji Pokok Anda             : Rp. ", karyawan_kontrak, "   |")
    pajak = 0.05 * karyawan_kontrak
    print ("| Pajak yang harus Anda bayar : Rp. ", pajak,  "  |")

    if pilihan2 == "Ya":
        tunjangan2_istri = karyawan_kontrak * 0.04
        print ("| Tunjangan untuk istri Anda  : Rp. ", tunjangan2_istri, "  |")
    
        if pilihan3 == "Ya" :
            tunjangan3_anak = karyawan_kontrak * 0.06
            total = karyawan_kontrak - pajak + tunjangan2_istri + tunjangan3_anak
            print ("| Tunjangan untuk anak Anda   : Rp. ", tunjangan3_anak, "  |")
            print ("| --------------------------------------------- |")
            print ("| Total Gaji bersih anda      : Rp. ",total," |" )
        else:
            total = karyawan_kontrak - pajak + tunjangan2_istri
            print ("| Total Gaji bersih anda      : Rp. ",total, " |" )
    else:
        total = karyawan_kontrak - pajak
        print ("| Total Gaji bersih anda      : Rp. ",total," |" )

    print ("| (Sudah termasuk pajak dan tunjangan)          |")
    print ("| ----------------------------------------------|")
    print ("| Tanggal Penerimaan Gaji     : 04 Oktober 2021 |")
    print ("|_______________________________________________|")
    print ("\n")


if pilihan == 5 :
    print ("\n")
    print ("|---------------------------------------|")
    print ("|<<<<<<<<<<<<<< OBP HER-1 >>>>>>>>>>>>>>|")
    print ("|============ Heri Gunawan =============|")
    print ("|---------------------------------------|")
    print ("\n")
    print (" __________________ 1 __________________ ")
    print ("|========== Bagas Dwi Santosa ==========|")
    print ("|************** 212103006 **************|")
    print ("|~~~~~~~~~~~~ Angkatan 2021 ~~~~~~~~~~~~|")
    print ("|__________________ 2 __________________|")
    print ("|========= Meiri Fauziah yusuf =========|")
    print ("|************** 212103010 **************|")
    print ("|~~~~~~~~~~~~ Angkatan 2021 ~~~~~~~~~~~~|")
    print ("|_______________________________________|")
    print ("\n")
    print ("|---------------------------------------|")
    print ("|>>>>>>>> SISTEM INFORMASI 2021 <<<<<<<<|")
    print ("|---------------------------------------|")
    print ("\n")