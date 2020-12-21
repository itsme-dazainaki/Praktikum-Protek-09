import random
def shuffle(a,b): #mari deklarasikan function
    liststring = [] #ubah listring menjadi list
    i = 0 #ini pendeklarasian nilai awal
    while i < b: #pengulangan menggunakan while, selama i lebih kecil dari parameter b
        acak = "".join(random.sample(a,len(a))) #ini rumus untuk mendapatkan hasil yg diminta (acak huruf)
        if(acak not in liststring): #pengecekan menggunakan perulangan apabila variabel acak tidak berada di list
            liststring += [acak]    #maka akan ditambahkan ke list 
            i += 1 #ini increment
    print(liststring) #tampilan list hasil pengacakan parameter a

shuffle("aku",3) #panggil function, dan isikan parameternya