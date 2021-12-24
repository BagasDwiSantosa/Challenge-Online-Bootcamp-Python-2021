

def menu():
    print("+"+("-"*73)+"+")
    print("|"+("-"*14)+"> PROGRAM MENYIMPAN DAN MENAMPILKAN BIODATA <"+("-"*14)+"|")
    print("+"+("-"*73)+"+")
    print('''Pilihlah salah satu fungsionalitas sebagai berikut :
            1. Menyimpan Identitas dan Pendidikan
            2. Menampilkan Identitas dan Pendidikan
            3. Keluar program\n''')
    pilih = int(input("Masukkan pilihan : "))
    return pilih

def identitas():
    nama = input("Masukkan Nama                 : ")
    ttl = input("Masukkan Tempat Tanggal Lahir : ")
    alamat = input("Masukkan Alamat               : ")
    email = input("Masukkan E-mail               : ")
    no = input("Masukkan No HP                : ")
    simpan = open ("identitas.txt", "a")
    data = """\n    Nama                 : {}
    Tempat Tanggal lahir : {}
    Alamat               : {}
    E-mail               : {}
    No HP                : {}""".format(nama,ttl,alamat,email,no)
    simpan.write(data)
    simpan.close()
    return simpan


def pendidikan():
    universitas = input("\nMasukkan Universitas          : ")
    fakultas = input("Masukkan Fakultas             : ")
    prodi = input("Masukkan Program Studi        : ")
    nim = input("Masukkan NIM                  : ")
    file = open("identitas.txt", "a")
    data = """\n    Universitas          : {} 
    Fakultas             : {}
    Program Studi        : {}
    NIM                  : {}""".format(universitas,fakultas,prodi,nim)
    file.write(data)
    file.close()
    return file

def menampilkan():
    data = open("identitas.txt", "r")
    print("+"+("-"*73)+"+")
    print("|"+"-"*22+" <> Biodata lengkap Anda <> "+"-"*23+"|")
    print("+"+("-"*73)+"+")
    print(data.read())
    data.close()
    return data

pilih = int()

while pilih<3:
    pilih=menu()
    if pilih ==3:
        print("\n+"+("-"*73)+"+")
        print("|"+"-"*14+"<-> Terimakasih sudah mencoba Program kami <->"+"-"*13+"|")
        print("+"+("-"*73)+"+\n")
        break
    else:
        if pilih == 1:
            identitas()
            lanjut = input("\nLanjut menginput data Pendidikan?yes/no : ")
            if lanjut == "yes":
                pendidikan()
            else :
                pass
            print("\n|"+"-"*20+"(: Data Anda telah kami simpan :)"+"-"*20+"|\n")
        else:
            pilih =2
            menampilkan()
            
