try : #mulai blok yang akan dicek exception
    a = int(input("Masukkan jumlah baris formasi : ")) #ini untuk inputan
    def star(a): #mari deklarasikan function
        for b in range (a): #pengulangan variabel b yang berada di range variabel a
            formasi = "*" + "**"*b #ini rumus formasi yang akan ditampilkan
            print(formasi.center(20, " ")) #tampilkan formasi tadi dengan format center

    star(a) #panggil function star
except ValueError: #ini blok jika terdapat error
    print("Maaf type data yang anda masukkan Salah ! Hanya masukkan angka") #tampilkan pesan error


