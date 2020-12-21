nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},  #ini list data
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},      #ini list data
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},   #ini list data
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},    #ini list data
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]  #ini list data

print("===================================================================================")
print("NIM".ljust(10),"Nama".ljust(15),"N.MID".ljust(15),"N.UAS".ljust(15),"N.AKHIR".ljust(15), "STATUS".ljust(15)) 
#menampilkan string dengan format l.just 
print("====================================================================================")
for a in nilai: #perulangan variabel a di data list nilai
    hasil = (a["mid"]+(2*a["uas"]))/3 #rumus untuk mendapatkan nilai dair variabel hasil
    if(hasil>=60): #jika "hasil" lebih dari sama dengan 60 maka :
        status ="Lulus" #statustnya lulus
    else : #jika tidak memenuhi kondisi if diatas maka
        status ="Tidak Lulus" #statusnya tidak lulus
    print(a["nim"].ljust(10), a["nama"].ljust(15), str(a["mid"]).ljust(15),str(a["uas"]).ljust(15), str(round(hasil,2)).ljust(15), status.ljust(10))
    #tampilkan data a sesuai dengan data yang ada di list nilai (tambah data hasil pengolahan nilai juga :),  format rata kiri dengan l.just
print("====================================================================================")



