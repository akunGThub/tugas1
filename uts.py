class barang:

    def barang():
        global totalbarang
        global banyak
        global barang
        print ("\n----------------------- barang -----------------------")
        print ("1. celana levis - Rp 150000")
        print ("2. baju cardinal - Rp 250000")
        print ("3. daster - Rp 100000")
        print ("4. kaos polos - 50000")
        nomor=int(input("masukan pilihan: "))
        banyak=int(input("berapa banyak: "))

        if nomor==1:
            totalbarang=banyak*150000
            print (banyak,"banyak celana levis = Rp", totalbarang)
            barang=("celana levis")
        elif nomor==2:
            totalbarang=banyak*250000
            print (banyak,"banyak baju cardinal = Rp",totalbarang)
            barang=("baju cardinal")
        elif nomor==3:
            totalbarang=banyak*100000
            print (banyak,"banyak daster = Rp", totalbarang)
            barang=("daster")
        elif nomor==4:
            totalbarang=banyak*50000
            print (banyak,"banyak kaos polos = Rp", totalbarang)
            barang=("kaos polos")
        else:
            print("pilihan tidak ada, silahkan masukan lagi!!!")
            barang()

    barang()
    totalsemua=totalbarang

    print("\ntotal harus dibayar:Rp",totalsemua)
    uang=int(input("uang tunai pembeli: Rp "))  
    kembalian=int(uang-totalsemua) 
    print("kembalian :",kembalian)  

    print("\n===============================================")   
    print("\n================ struk beli ===================")
    print("\n===============================================")
    print ("nama\t\t:",barang)
    print ("beli\t\t:",banyak,barang,"(Rp",totalbarang,")")
    print ("tagihan\t\t: Rp",totalsemua)
    print ("dibayar\t\t: Rp",uang)
    print ("kembalian\t\t: Rp",kembalian)
    print("=================================================")
