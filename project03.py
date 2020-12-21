try :   #mulai blok yang akan dicek exception
    a = int(input("Masukkan jumlah baris formasi (ganjil): ")) #ini untuk inputan

    def star(a): #mari deklarasikan function
        for b in range (a): #pengulangan variabel b yang berada di range variabel a
            formasi = "*" + "**"*b #ini rumus formasi yang akan ditampilkan
            print(formasi.center(20, " "))  #tampilkan formasi tadi dengan format center

    def star2(a): #mari deklarasikan function
        c = 0 #ini pendeklarasian nilai awal c
        d = a-1 #ini pendeklarasian nilai awal d
        for b in range (a,0,-1):  #pengulangan variabel b yang berada di range variabel a 
            formasi =  "*" + "**"*(d-c) #ini rumus formasi yang akan ditampilkan
            print(formasi.center(20," "))  #tampilkan formasi tadi dengan format center
            c += 1 #ini increment

    def star3(a): #mari deklarasikan function
        if(a%2 != 0): #pengulangan variabel b yang berada di range variabel a
            star(a//2+1) #panggil function star dan rumuskan parameternya
            star2((a//2)) #panggil function star2 dan rumuskan parameternya
        else:
            print("Maaf, Bilangan anda tidak ganjil !!") #jika angka yang dimasukkan bukan ganjil
                                                          #maka akan ditampilkan pesan tersebut
    star3(a) #panggil function star3

except ValueError: #ini blok jika terdapat error
    print("Maaf, type data yang anda inputkan bukan angka !") #tampilkan pesan error


