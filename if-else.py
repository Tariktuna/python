def ortalama_hesapla(vize,final):
    if (type(vize) == int and type(final) == int):
        if 0 < vize < 100:
            if 0 < final < 100:
                sonuc = (vize * 40 + final * 60) / 100
                if 0 < sonuc <= 40:
                    print("notunuz dc")
                elif 40 < sonuc <= 60:
                    print("Notunuz cb")
                elif 60 < sonuc <= 80:
                    print("Notunuz bb")
                elif 80 < sonuc <= 100:
                    print("Notunuz aa")
            else:
                print("geçersiz final notu")
        else:
            print("geçersiz vize notu")
ogr1vize=int(input("Birinci öğrencinin vize notunu girin: "))
ogr1final=int(input("Birinci öğrencinin final notunu girin."))
ortalama_hesapla(ogr1vize,ogr1final)