def ubahHuruf(kata, p, q): #mari desklarasikan function
    listkata = list(kata) #ubah variabel kata menjadi list
    hasil = "" #nilai awal variabel (kosong)
    for huruf in listkata: #perulangan pengecekan tiap variabel di listkata
        if(huruf==p): #jika salah satu variabel dalam list (huruf) sama dengan variabel awal (p) maka:
            huruf=q #huruf yang sama tsb, akan diganti dengan isi variabel (q) diawal tadi
        hasil ="".join([hasil, huruf]) #variabel hasil(kosong), akan diisi dengan gabungan nilai awal(kosong)dengan
                                       #setiap variabel anggota listkata yang telah dicek                                         
    return hasil #mengembalikan nilai untuk menyimpannya
  
print(ubahHuruf("MATEMATIKA", "T", "S")) #panggil function dan tampilan nilai yang dikembalikan

