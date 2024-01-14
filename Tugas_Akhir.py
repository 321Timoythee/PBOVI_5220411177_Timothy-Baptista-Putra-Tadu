import mysql.connector
from prettytable import PrettyTable
import os


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PBO_Akhir"
)

cur = conn.cursor()

class shush:
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan

class starting(shush):
    def __init__(self, pelanggan, gender):
        super().__init__(pelanggan)
        self.gender = gender

    def beli_sepatu(self):
        pelanggan = input("Masukkan nama anda (Jika sudah pernah mendaftar, ketik s): ")

        if pelanggan.lower() == "s":
            os.system('cls')
            pilihan_pelanggan = """
            1.) Alexander dengan gender Pria
            2.) Alexandra dengan gender Wanita
            3.) Poppy dengan gender Waria
            4.) Donny dengan gender Pria
            """
            print (pilihan_pelanggan)
            pilih_pelanggan = int(input("Masukkan pilihan yang merupakan anda sendiri: "))
            os.system('cls')

            if pilih_pelanggan == 1:
                pelanggan = "Alexander"
                gender = "Pria"
            
            elif pilih_pelanggan == 2:
                pelanggan = "Alexandra"
                gender = "Wanita"

            elif pilih_pelanggan == 3:
                pelanggan = "Poppy"
                gender = "Waria"
            
            elif pilih_pelanggan == 2:
                pelanggan = "Donny"
                gender = "Pria"
        else:
            os.system('cls')
            pilihan_gender = """
            1.) Pria
            2.) Wanita
            3.) Waria
                """
            
            print (pilihan_gender)
            pilih_gender = int(input("Silahkan pilih gender anda: "))
            os.system('cls')

            if pilih_gender == 1:
                gender = "Pria"
            elif pilih_gender == 2:
                gender = "Wanita"
            elif pilih_gender == 3:
                gender = "Waria"
            else:
                print ("ERROR")

        menu_sepatu = "SELECT * FROM sepatu"
        cur.execute(menu_sepatu)
        result_sepatu = cur.fetchall()
        self.tabel_untuk_sepatu(result_sepatu)

        pilih_sepatu = int(input("Silahkan memilih sepatu yang ingin di beli: "))
        nama_sepatu = ("SELECT nama FROM sepatu WHERE id=%s" % pilih_sepatu)
        
        cur.execute(nama_sepatu)
        nama_sepatu_jadi = cur.fetchone()
        result_nama_sepatu = nama_sepatu_jadi[0]
        os.system('cls')


        if pilih_sepatu == 1:
            jumlah_beli_sepatu = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sepatu = ("SELECT harga FROM sepatu WHERE id=%s" % pilih_sepatu)
            cur.execute(harga_sepatu)
            result_harga_sepatu = cur.fetchone()

            harga_sepatu_new = result_harga_sepatu[0]
            total_harga_sepatu = harga_sepatu_new * jumlah_beli_sepatu

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sepatu, jumlah_beli_sepatu, total_harga_sepatu)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")
        
        elif pilih_sepatu == 2:
            jumlah_beli_sepatu = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sepatu = ("SELECT harga FROM sepatu WHERE id=%s" % pilih_sepatu)
            cur.execute(harga_sepatu)
            result_harga_sepatu = cur.fetchone()

            harga_sepatu_new = result_harga_sepatu[0]
            total_harga_sepatu = harga_sepatu_new * jumlah_beli_sepatu

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sepatu, jumlah_beli_sepatu, total_harga_sepatu)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")
        
        elif pilih_sepatu == 3:
            jumlah_beli_sepatu = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sepatu = ("SELECT harga FROM sepatu WHERE id=%s" % pilih_sepatu)
            cur.execute(harga_sepatu)
            result_harga_sepatu = cur.fetchone()

            harga_sepatu_new = result_harga_sepatu[0]
            total_harga_sepatu = harga_sepatu_new * jumlah_beli_sepatu

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sepatu, jumlah_beli_sepatu, total_harga_sepatu)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")

        elif pilih_sepatu == 4:
            jumlah_beli_sepatu = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sepatu = ("SELECT harga FROM sepatu WHERE id=%s" % pilih_sepatu)
            cur.execute(harga_sepatu)
            result_harga_sepatu = cur.fetchone()

            harga_sepatu_new = result_harga_sepatu[0]
            total_harga_sepatu = harga_sepatu_new * jumlah_beli_sepatu

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sepatu, jumlah_beli_sepatu, total_harga_sepatu)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")

        elif pilih_sepatu == 5:
            jumlah_beli_sepatu = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sepatu = ("SELECT harga FROM sepatu WHERE id=%s" % pilih_sepatu)
            cur.execute(harga_sepatu)
            result_harga_sepatu = cur.fetchone()

            harga_sepatu_new = result_harga_sepatu[0]
            total_harga_sepatu = harga_sepatu_new * jumlah_beli_sepatu

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sepatu, jumlah_beli_sepatu, total_harga_sepatu)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")

        else:
            print("ERROR")
        
        os.system('pause')
        os.system('cls')
        return result_sepatu

    def beli_sandal(self):
        pelanggan = input("Masukkan nama anda (Jika sudah pernah mendaftar, ketik s): ")

        if pelanggan.lower() == "s":
            os.system('cls')
            pilihan_pelanggan = """
            1.) Alexander dengan gender Pria
            2.) Alexandra dengan gender Wanita
            3.) Poppy dengan gender Waria
            4.) Donny dengan gender Pria
            """
            print (pilihan_pelanggan)
            pilih_pelanggan = int(input("Masukkan pilihan yang merupakan anda sendiri: "))

            if pilih_pelanggan == 1:
                pelanggan = "Alexander"
                gender = "Pria"
            
            elif pilih_pelanggan == 2:
                pelanggan = "Alexandra"
                gender = "Wanita"

            elif pilih_pelanggan == 3:
                pelanggan = "Poppy"
                gender = "Waria"
            
            elif pilih_pelanggan == 2:
                pelanggan = "Donny"
                gender = "Pria"
        else:
            os.system('cls')
            pilihan_gender = """
            1.) Pria
            2.) Wanita
            3.) Waria
                """
            
            print (pilihan_gender)
            pilih_gender = int(input("Silahkan pilih gender anda: "))
            os.system('cls')

            if pilih_gender == 1:
                gender = "Pria"
            elif pilih_gender == 2:
                gender = "Wanita"
            elif pilih_gender == 3:
                gender = "Waria"
            else:
                print ("ERROR")

        menu_sandal = "SELECT * FROM sendal"
        cur.execute(menu_sandal)
        result_sandal = cur.fetchall()
        self.tabel_untuk_sandal(result_sandal)

        pilih_sandal = int(input("Silahkan memilih sandal yang ingin di beli: "))
        nama_sandal = ("SELECT nama FROM sendal WHERE id=%s" % pilih_sandal)
        
        cur.execute(nama_sandal)
        nama_sandal_jadi = cur.fetchone()
        result_nama_sandal = nama_sandal_jadi[0]
        os.system('cls')

        if pilih_sandal == 1:
            jumlah_beli_sandal = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sandal = ("SELECT harga FROM sendal WHERE id=%s" % pilih_sandal)
            cur.execute(harga_sandal)
            result_harga_sandal = cur.fetchone()

            harga_sandal_new = result_harga_sandal[0]
            total_harga_sandal = harga_sandal_new * jumlah_beli_sandal

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sandal, jumlah_beli_sandal, total_harga_sandal)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")

        elif pilih_sandal == 2:
            jumlah_beli_sandal = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sandal = ("SELECT harga FROM sendal WHERE id=%s" % pilih_sandal)
            cur.execute(harga_sandal)
            result_harga_sandal = cur.fetchone()

            harga_sandal_new = result_harga_sandal[0]
            total_harga_sandal = harga_sandal_new * jumlah_beli_sandal

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sandal, jumlah_beli_sandal, total_harga_sandal)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")

        elif pilih_sandal == 3:
            jumlah_beli_sandal = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sandal = ("SELECT harga FROM sendal WHERE id=%s" % pilih_sandal)
            cur.execute(harga_sandal)
            result_harga_sandal = cur.fetchone()

            harga_sandal_new = result_harga_sandal[0]
            total_harga_sandal = harga_sandal_new * jumlah_beli_sandal

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sandal, jumlah_beli_sandal, total_harga_sandal)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")

        elif pilih_sandal == 4:
            jumlah_beli_sandal = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sandal = ("SELECT harga FROM sendal WHERE id=%s" % pilih_sandal)
            cur.execute(harga_sandal)
            result_harga_sandal = cur.fetchone()

            harga_sandal_new = result_harga_sandal[0]
            total_harga_sandal = harga_sandal_new * jumlah_beli_sandal

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sandal, jumlah_beli_sandal, total_harga_sandal)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")

        elif pilih_sandal == 5:
            jumlah_beli_sandal = int(input("Masukkan jumlah barang yang ingin di beli : "))
            harga_sandal = ("SELECT harga FROM sendal WHERE id=%s" % pilih_sandal)
            cur.execute(harga_sandal)
            result_harga_sandal = cur.fetchone()

            harga_sandal_new = result_harga_sandal[0]
            total_harga_sandal = harga_sandal_new * jumlah_beli_sandal

            input_ke_keranjang = """INSERT INTO keranjang (id, nama_pelanggan, gender_pelanggan, 
            nama_produk, jumlah_produk, total_harga_produk) VALUES (NULL, %s, %s, %s, %s, %s)
            """
            value_input_ke_keranjang = (pelanggan, gender, result_nama_sandal, jumlah_beli_sandal, total_harga_sandal)
            cur.execute(input_ke_keranjang, value_input_ke_keranjang)
            conn.commit()

            print("Berhasil ditambahkan ke keranjang!!!")

        else:
            print("ERROR")
        
        os.system('pause')
        os.system('cls')
        return result_sandal

    def tabel_untuk_sandal(self, data):
        tabel = PrettyTable()
        tabel.field_names = ["id", "nama", "harga"]
        for row in data:
            tabel.add_row(row)
        print(tabel)
        return tabel

    def tabel_untuk_sepatu(self, data):
        tabel = PrettyTable()
        tabel.field_names = ["id", "nama", "harga"]
        for row in data:
            tabel.add_row(row)
        print(tabel)
        return tabel
    
    def tabel_untuk_keranjang(self, data):
        tabel = PrettyTable()
        tabel.field_names = ["id", "nama_pelanggan", "gender_pelanggan", "nama_produk", "jumlah_produk", "total_harga_produk"]
        for row in data:
            tabel.add_row(row)
        print(tabel)
        return tabel

    def menu_keranjang(self):
        tampil_keranjang = "SELECT * FROM keranjang"
        cur.execute(tampil_keranjang)
        result_tampil_keranjang = cur.fetchall()
        self.tabel_untuk_keranjang(result_tampil_keranjang)
        pilih_keranjang = int(input("Silahkan pilih nama anda untuk membayar produk yang sudah masuk ke dalam keranjang: "))
        os.system('cls')

        if pilih_keranjang == 1:
            harga_produk = ("SELECT total_harga_produk FROM keranjang WHERE id=%s" % pilih_keranjang)
            cur.execute(harga_produk)
            result_harga_produk = cur.fetchone()

            harga_produk_new = result_harga_produk[0]
            print(f"Harga yang perlu dibayar ialah {harga_produk_new} rupiah")
            uang_pelanggan = int(input("Silahkan masukkan jumlah uang anda: "))

            if uang_pelanggan >= harga_produk_new:
                kembalian = uang_pelanggan - harga_produk_new
                print("Pembelian berhasil!")

                hapus_isi_data_tabel = ("DELETE FROM keranjang WHERE id=%s" % pilih_keranjang)
                cur.execute(hapus_isi_data_tabel)
                conn.commit()

                return kembalian, harga_produk
            elif uang_pelanggan <= harga_produk_new:
                print ("Uang anda tidak cukup pembelian dibatalkan")
        
        elif pilih_keranjang == 2:
            harga_produk = ("SELECT total_harga_produk FROM keranjang WHERE id=%s" % pilih_keranjang)
            cur.execute(harga_produk)
            result_harga_produk = cur.fetchone()

            harga_produk_new = result_harga_produk[0]
            print(f"Harga yang perlu dibayar ialah {harga_produk_new} rupiah")
            uang_pelanggan = int(input("Silahkan masukkan jumlah uang anda: "))

            if uang_pelanggan >= harga_produk_new:
                kembalian = uang_pelanggan - harga_produk_new
                print("Pembelianberhasil!")

                hapus_isi_data_tabel = ("DELETE FROM keranjang WHERE id=%s" % pilih_keranjang)
                cur.execute(hapus_isi_data_tabel)
                conn.commit()

                return kembalian, harga_produk
            elif uang_pelanggan <= harga_produk_new:
                print ("Uang anda tidak cukup pembelian dibatalkan")
        
        elif pilih_keranjang == 3:
            harga_produk = ("SELECT total_harga_produk FROM keranjang WHERE id=%s" % pilih_keranjang)
            cur.execute(harga_produk)
            result_harga_produk = cur.fetchone()

            harga_produk_new = result_harga_produk[0]
            print(f"Harga yang perlu dibayar ialah {harga_produk_new} rupiah")
            uang_pelanggan = int(input("Silahkan masukkan jumlah uang anda: "))

            if uang_pelanggan >= harga_produk_new:
                kembalian = uang_pelanggan - harga_produk_new
                print("Pembelian berhasil!")

                hapus_isi_data_tabel = ("DELETE FROM keranjang WHERE id=%s" % pilih_keranjang)
                cur.execute(hapus_isi_data_tabel)
                conn.commit()

                return kembalian, harga_produk
            elif uang_pelanggan <= harga_produk_new:
                print ("Uang anda tidak cukup pembelian dibatalkan")
        
        elif pilih_keranjang == 4:
            harga_produk = ("SELECT total_harga_produk FROM keranjang WHERE id=%s" % pilih_keranjang)
            cur.execute(harga_produk)
            result_harga_produk = cur.fetchone()

            harga_produk_new = result_harga_produk[0]
            print(f"Harga yang perlu dibayar ialah {harga_produk_new} rupiah")
            uang_pelanggan = int(input("Silahkan masukkan jumlah uang anda: "))

            if uang_pelanggan >= harga_produk_new:
                kembalian = uang_pelanggan - harga_produk_new
                print("Pembelian berhasil!")

                hapus_isi_data_tabel = ("DELETE FROM keranjang WHERE id=%s" % pilih_keranjang)
                cur.execute(hapus_isi_data_tabel)
                conn.commit()

                return kembalian, harga_produk
            elif uang_pelanggan <= harga_produk_new:
                print ("Uang anda tidak cukup pembelian dibatalkan")
        
        elif pilih_keranjang == 5:
            harga_produk = ("SELECT total_harga_produk FROM keranjang WHERE id=%s" % pilih_keranjang)
            cur.execute(harga_produk)
            result_harga_produk = cur.fetchone()

            harga_produk_new = result_harga_produk[0]
            print(f"Harga yang perlu dibayar ialah {harga_produk_new} rupiah")
            uang_pelanggan = int(input("Silahkan masukkan jumlah uang anda: "))

            if uang_pelanggan >= harga_produk_new:
                kembalian = uang_pelanggan - harga_produk_new
                print("Pembelian berhasil!")

                hapus_isi_data_tabel = ("DELETE FROM keranjang WHERE id=%s" % pilih_keranjang)
                cur.execute(hapus_isi_data_tabel)
                conn.commit()
                
                return kembalian, harga_produk
            elif uang_pelanggan <= harga_produk_new:
                print ("Uang anda tidak cukup pembelian dibatalkan")
        
        else:
            print("ERROR")
        os.system('pause')
        os.system('cls')

    def mengubah_isi_tabel(self):
        menu_rahasia = """
        ==========================
        |     Welcome Admin!!    |
        ==========================
        1.) Ubah isi tabel sepatu
        2.) Ubah isi tabel sendal
        """
        print(menu_rahasia)
        pilih_admin = int(input("Masukkan pilihan anda: "))
        os.system('cls')

        if pilih_admin == 1:
            tabel_sepatu = "SELECT * FROM sepatu"
            cur.execute(tabel_sepatu)
            result_tabel_sepatu = cur.fetchall()
            self.tabel_untuk_sepatu(result_tabel_sepatu)
            pilih_admin_sepatu = int(input("Masukkan id data yang ingin diubah: "))
            os.system('cls')
            
            if pilih_admin_sepatu == 1:
                tabel_yang_diubah = ("SELECT * FROM sepatu WHERE id=%s" % pilih_admin_sepatu)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sepatu(result_tabel_yang_diubah)

                nama_sepatu_baru = input("Masukkan nama sepatu yang baru: ")
                harga_sepatu_baru = int(input("Masukkan harga sepatu yang baru: "))

                pengubahan_data_sepatu = "UPDATE sepatu SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sepatu = (nama_sepatu_baru, harga_sepatu_baru, pilih_admin_sepatu)

                cur.execute(pengubahan_data_sepatu,value_pengubahan_data_sepatu)
                conn.commit()

                print("Pengubahan data berhasil!")

            elif pilih_admin_sepatu == 2:
                tabel_yang_diubah = ("SELECT * FROM sepatu WHERE id=%s" % pilih_admin_sepatu)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sepatu(result_tabel_yang_diubah)

                nama_sepatu_baru = input("Masukkan nama sepatu yang baru: ")
                harga_sepatu_baru = int(input("Masukkan harga sepatu yang baru: "))

                pengubahan_data_sepatu = "UPDATE sepatu SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sepatu = (nama_sepatu_baru, harga_sepatu_baru, pilih_admin_sepatu)

                cur.execute(pengubahan_data_sepatu,value_pengubahan_data_sepatu)
                conn.commit()

                print("Pengubahan data berhasil!")

            elif pilih_admin_sepatu == 3:
                tabel_yang_diubah = ("SELECT * FROM sepatu WHERE id=%s" % pilih_admin_sepatu)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sepatu(result_tabel_yang_diubah)

                nama_sepatu_baru = input("Masukkan nama sepatu yang baru: ")
                harga_sepatu_baru = int(input("Masukkan harga sepatu yang baru: "))

                pengubahan_data_sepatu = "UPDATE sepatu SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sepatu = (nama_sepatu_baru, harga_sepatu_baru, pilih_admin_sepatu)

                cur.execute(pengubahan_data_sepatu,value_pengubahan_data_sepatu)
                conn.commit()

                print("Pengubahan data berhasil!")

            elif pilih_admin_sepatu == 4:
                tabel_yang_diubah = ("SELECT * FROM sepatu WHERE id=%s" % pilih_admin_sepatu)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sepatu(result_tabel_yang_diubah)

                nama_sepatu_baru = input("Masukkan nama sepatu yang baru: ")
                harga_sepatu_baru = int(input("Masukkan harga sepatu yang baru: "))

                pengubahan_data_sepatu = "UPDATE sepatu SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sepatu = (nama_sepatu_baru, harga_sepatu_baru, pilih_admin_sepatu)

                cur.execute(pengubahan_data_sepatu,value_pengubahan_data_sepatu)
                conn.commit()

                print("Pengubahan data berhasil!")

            elif pilih_admin_sepatu == 5:
                tabel_yang_diubah = ("SELECT * FROM sepatu WHERE id=%s" % pilih_admin_sepatu)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sepatu(result_tabel_yang_diubah)

                nama_sepatu_baru = input("Masukkan nama sepatu yang baru: ")
                harga_sepatu_baru = int(input("Masukkan harga sepatu yang baru: "))

                pengubahan_data_sepatu = "UPDATE sepatu SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sepatu = (nama_sepatu_baru, harga_sepatu_baru, pilih_admin_sepatu)

                cur.execute(pengubahan_data_sepatu,value_pengubahan_data_sepatu)
                conn.commit()

                print("Pengubahan data berhasil!")
        if pilih_admin == 2:
            tabel_sandal = "SELECT * FROM sendal"
            cur.execute(tabel_sandal)
            result_tabel_sandal = cur.fetchall()
            self.tabel_untuk_sandal(result_tabel_sandal)
            pilih_admin_sandal = int(input("Masukkan id data yang ingin diubah: "))
            os.system('cls')

            if pilih_admin_sandal == 1:
                tabel_yang_diubah = ("SELECT * FROM sendal WHERE id=%s" % pilih_admin_sandal)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sandal(result_tabel_yang_diubah)

                nama_sandal_baru = input("Masukkan nama sandal yang baru: ")
                harga_sandal_baru = int(input("Masukkan harga sandal yang baru: "))

                pengubahan_data_sandal = "UPDATE sandal SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sandal = (nama_sandal_baru, harga_sandal_baru, pilih_admin_sandal)

                cur.execute(pengubahan_data_sandal,value_pengubahan_data_sandal)
                conn.commit()

            elif pilih_admin_sandal == 2:
                tabel_yang_diubah = ("SELECT * FROM sendal WHERE id=%s" % pilih_admin_sandal)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sandal(result_tabel_yang_diubah)

                nama_sandal_baru = input("Masukkan nama sandal yang baru: ")
                harga_sandal_baru = int(input("Masukkan harga sandal yang baru: "))

                pengubahan_data_sandal = "UPDATE sandal SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sandal = (nama_sandal_baru, harga_sandal_baru, pilih_admin_sandal)

                cur.execute(pengubahan_data_sandal,value_pengubahan_data_sandal)
                conn.commit()

            elif pilih_admin_sandal == 3:
                tabel_yang_diubah = ("SELECT * FROM sendal WHERE id=%s" % pilih_admin_sandal)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sandal(result_tabel_yang_diubah)

                nama_sandal_baru = input("Masukkan nama sandal yang baru: ")
                harga_sandal_baru = int(input("Masukkan harga sandal yang baru: "))

                pengubahan_data_sandal = "UPDATE sandal SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sandal = (nama_sandal_baru, harga_sandal_baru, pilih_admin_sandal)

                cur.execute(pengubahan_data_sandal,value_pengubahan_data_sandal)
                conn.commit()

            elif pilih_admin_sandal == 4:
                tabel_yang_diubah = ("SELECT * FROM sendal WHERE id=%s" % pilih_admin_sandal)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sandal(result_tabel_yang_diubah)

                nama_sandal_baru = input("Masukkan nama sandal yang baru: ")
                harga_sandal_baru = int(input("Masukkan harga sandal yang baru: "))

                pengubahan_data_sandal = "UPDATE sandal SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sandal = (nama_sandal_baru, harga_sandal_baru, pilih_admin_sandal)

                cur.execute(pengubahan_data_sandal,value_pengubahan_data_sandal)
                conn.commit()

            elif pilih_admin_sandal == 5:
                tabel_yang_diubah = ("SELECT * FROM sendal WHERE id=%s" % pilih_admin_sandal)
                cur.execute(tabel_yang_diubah)
                result_tabel_yang_diubah = cur.fetchall()
                self.tabel_untuk_sandal(result_tabel_yang_diubah)

                nama_sandal_baru = input("Masukkan nama sandal yang baru: ")
                harga_sandal_baru = int(input("Masukkan harga sandal yang baru: "))

                pengubahan_data_sandal = "UPDATE sandal SET nama=%s, harga=%s WHERE id=%s"
                value_pengubahan_data_sandal = (nama_sandal_baru, harga_sandal_baru, pilih_admin_sandal)

                cur.execute(pengubahan_data_sandal,value_pengubahan_data_sandal)
                conn.commit()
            else:
                print("ERROR")

        else:
            print("ERROR")
        os.system('pause')
        os.system('cls')
        


    def menu(self):
        while True:
            menu = """
            ==================================
            |      Welcome to AKI - AKI      |
            |      tempat terbaik untuk      |
            |            alas kaki           |
            ==================================
            1.) Beli sepatu
            2.) Beli sandal
            3.) Keranjang
            0.) Keluar

            """
            print(menu)
            pilih = int(input("Masukan pilihan anda: "))
            os.system('cls')

            if pilih == 1:
                self.beli_sepatu()
            elif pilih == 2:
                self.beli_sandal()  
            elif pilih == 3:
                self.menu_keranjang()
            elif pilih == 0:
                break
            elif pilih == 8888:
                self.mengubah_isi_tabel()


start = starting(pelanggan="", gender="")
start.menu()