## hata ayıklama veya hata yakalama ve verilen hatayı yazdırma
#valueError
#zerodivisionError ##alınan hataların adları deneyıp aldıgımız hataların adları
#valueError
try:                                       
    sayı1= int(input("Birinci sayıyı giriniz: "))
    sayı2= int(input("İkinci sayıyı giriniz: "))
    sonuc= sayı1/sayı2
    print("Bölme işleminin sonucu: ", sonuc)
except ZeroDivisionError:
    print("hiçbir sayı 0 a bölünemez")
except ValueError as e:
    print("Lütfen sadece sayı giriniz")
    print("Sistem mesajı: ", e)
except:
    print("Bir hata oluştu")
else: #hata oluşmama durumunda calısır
    print("işlem başarılı")
finally:
    print("Program sonlandı")
    