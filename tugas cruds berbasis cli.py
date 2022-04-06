#nama   : reza ramadhan
#kelas  : R4
#nim    : 200511078
#tugas  : cruds berbasis cli (tugas 1)

from glob import glob
from operator import truediv
import psycopg2 as db
import os
con = None
connected = None
cursor = None
def connect():
    global connected
    global con
    global cursor
    try:
        con = db.connect(host="localhost",database="sekolah",port=5432,user="reza",password="123")
        cursor = con.cursor()
        connected = True
    except:
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected==True):
        cursor.close()
        con.close
    else:
        con = None
    connected = False

def tampil(sql):
    a = connect()
    a.execute(sql)
    record = a.fetchall()
    return record

sql="select * from mahasiswa"
a = tampil(sql)
print(a)
disconnect

def Entry():
    global connected
    global con
    global cursor
    xnim = input("masukan nim: ")
    xnama = input("masukan nama lengkap: ")
    xidfk = input("masukan ID fakultas (1..5): ")
    xidpr = input("masukan ID prodi (1...10: ")
    a = connect()
    sql = "insert into mahasiswa (nim,nama,idfakultas,idprodi) values ('"+xnim+"','"+xnama+"','"+xidfk+"','"+xidpr+"')"
    a.execute(sql)
    con.commit()
    print("berhasil di tambahkan good job :).")

def Cari():
    global connected
    global con
    global cursor
    xnim = input("masukan nim yang di cari: ")
    a = connect()
    sql = "select * from mahasiswa where nim = '"+xnim+"'"
    a.execute(sql)
    record = a.fetchall()
    print(record)
    print("search berhasil di cari.")

def Ubah():
    global connected
    global con
    global cursor
    xnim = input("masukan Nim yang di cari: ")
    a = connect()
    sql = "select from mahasiswa where nim = '"+xnim+"'"
    a.execute(sql)
    record = a.fetchall()
    print("data saat ini : ")
    print(record)
    row = a.rowcount
    if(row==1):
        print("silahkan untuk mengubah data ..")
        xnama = input("masukan nama lengkap: ")
        xidfk = input("masukan ID fakultas (1..5): ")
        Xidpr = input("masukan ID prodi (1..10):")
        a = connect()
        sql = "update mahasiswa set nama='"+xnama+"', idfakultas='"+xidfk+"',idprodi='"+Xidpr+"'where nim='"+xnim+"'"
        a.execute(sql)
        con.commit()
        print("berhasil di update.")
        sql="select * from mahasiswa where nim='"+xnim+"'"
        a.execute(sql)
        rec = a.fetchall()
        print("data setelah diubah : ")
        print (rec)

    else:
        print("data tidak di temukan")

def hapus():
    global connected
    global con
    global cursor
    xnim = input("masukan Nim yang di cari: ")
    a = connect()
    sql = "select from mahasiswa where nim = '"+xnim+"'"
    a.execute(sql)
    record = a.fetchall()
    print("data saat ini : ")
    print(record)
    row = a.rowcount
    if(row==1):
        jwb=input("apakah ingin menghapus data? (y/t)")
        if(jwb.upper()=="Y"):
            a = connect()
            sql = "delete from mahasiswa where nim='"+xnim+"'"
            a.execute(sql)
            con.commit()
            print("delete is done")

        else:
            print("data batal untuk di hapus")
    
    else:
        print("data tidak ditemukan")
        
def show_menu():
  print("===================================================")
  print("=== APLIKASI DATABASE POSTGRESQL CRUDS BERBASIS CLI ===")
  print("1. tanbahkan data")
  print("2. cari data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    Entry()
  elif menu == "2":
    Cari()
  elif menu == "3":
    Ubah()
  elif menu == "4":
    hapus()
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")

if __name__ == "__main__":
  while(True):
    show_menu()


hapus()

