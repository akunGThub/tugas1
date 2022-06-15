class rondaposko:

    def rondaposko():
        global jumlahposko
        global banyakorang
        global posko 
        print ("\n----------------------- ronda posko -----------------------")
        print ("1. posko keamanan")
        print ("2. posko putri")
        print ("3. posko balai ")
        print ("4. posko daerah selatan")
        nomor=int(input("masukan pilihan: "))
        banyakorang=int(input("berapa orang: "))

        if nomor==1:
            jumlahposko=banyakorang
            print (banyakorang,"posko keamanan ", jumlahposko)
            posko=("posko keamanan")
        elif nomor==2:
            jumlahposko=banyakorang
            print (banyakorang,"posko putri ", jumlahposko)
            posko=("posko putri")
        elif nomor==3:
            jumlahposko=banyakorang
            print (banyakorang,"posko balai ", jumlahposko)
            posko=("posko balai")
        elif nomor==4:
            jumlahposko=banyakorang
            print (banyakorang,"posko daerah selatan ", jumlahposko)
            posko=("posko daerah selatan")
        else:
            print("pilihan tidak ada, silahkan masukan lagi!!!")
            rondaposko()

    rondaposko()
    jumlahposko=jumlahposko

  

    