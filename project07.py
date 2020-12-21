mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',              #ini list data
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',     #ini list data
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']       #ini list data

print("===============================================================")
print("NIM".ljust(10),"Nama Mahasiswa".ljust(26),"Tgl.Lahir".ljust(15),"Tempat Lahir".ljust(15)) #menampilkan string dengan format l.just 
print("---------------------------------------------------------------")
for n in mhs: #untuk variabel n di list data mhs
    data = n.split(":") #split variabel n berdasar tanda (:) dan taruh hasilnya ke variabel data
    a = data[0] #variabel a nilainya adalah data hasil split ke 0 (pertama)
    b = data[1] #variabel a nilainya adalah data hasil split ke 1 (kedua)
    c = data[2] #variabel b nilainya adalah data hasil split ke 2 (ketiga)
    d = c.replace("-","/") #variabel c nilainya adalah variabel b yang direplace 
    e = data[3] #variabel d nilainya adalah data hasil split ke 3 (keempat)

    print(a.ljust(11), b.ljust(25), d.ljust(16), e.ljust(15))
    #tampilkan data dalam list mhs yang telah displit dan direplace, format rata kiri dengan l.just
print("---------------------------------------------------------------")


