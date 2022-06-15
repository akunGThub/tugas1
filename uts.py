class menumakanan:

    def menumakanan():
        global totalmakanan
        global porsi
        global makanan
        print ("\n----------------------- menumakanan -----------------------")
        print ("1. pentol tono - Rp 10000")
        print ("2. pentol kawan - Rp 10000")
        print ("3. telur gulung - Rp 5000")
        nomor=int(input("masukan pilihan: "))
        porsi=int(input("berapa porsi: "))

        if nomor==1:
            totalmakanan=porsi*10000
            print (porsi,"porsi pentol tono = Rp", totalmakanan)
            makanan=("pentol tono")
        elif nomor==2:
            totalmakanan=porsi*10000
            print (porsi,"porsi pentol kawan = Rp",totalmakanan)
            makanan=("pento kawan")
        elif nomor==3:
            totalmakanan=porsi*5000
            print (porsi,"porsi telur gulung = Rp", totalmakanan)
            makanan=("telur gulung")
        else:
            print("pilihan tidak ada, silahkan masukan lagi!!!")
            menumakanan()

    menumakanan()
    totalsemua=totalmakanan

    print("\ntotal harus dibayar:Rp",totalsemua)
    uang=int(input("uang tunai pembeli: Rp "))  
    kembalian=int(uang-totalsemua) 
    print("kembalian :",kembalian)  

    print("\n===============================================")   
    print("\n================ struk beli ===================")
    print("\n===============================================")
    print ("nama\t\t:",menumakanan)
    print ("beli\t\t:",porsi,makanan,"(Rp",totalmakanan,")")
    print ("tagihan\t\t: Rp",totalsemua)
    print ("dibayar\t\t: Rp",uang)
    print ("kembalian\t\t: Rp",kembalian)
    print("=================================================")


