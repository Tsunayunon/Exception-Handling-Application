
---

# Hata Ayıklama Programı

Bu Python programı, kullanıcının girdiği iki sayıyı bölerken olası hata durumlarını ele alır ve uygun hata mesajlarını ekrana yazdırır.

## Nasıl Kullanılır

1. `hata_ayiklama.py` dosyasını çalıştırın.
2. Program başlatıldığında, birinci ve ikinci sayıları girin.
3. Program, girdiğiniz sayıları bölmeye çalışacak ve olası hatalar için uygun mesajları ekrana yazdıracaktır.

## Örnek Kullanım

```
$ python hata_ayiklama.py
Birinci sayıyı giriniz: 10
İkinci sayıyı giriniz: 0
hiçbir sayı 0 a bölünemez
Program sonlandı
```

## Desteklenen Hatalar

- ZeroDivisionError: İkinci sayı sıfıra bölünemez.
- ValueError: Girilen değerler sayısal bir formatta değilse.

## Geliştirme

Bu program, basit bir hata ayıklama örneğidir. Geliştirmek için şunları düşünebilirsiniz:

- Farklı hata türlerini ele almak için başka hata işleyicileri ekleyin.
- Kullanıcıya daha fazla geri bildirim sağlamak için hata mesajlarını iyileştirin.
- Programın kullanıcı arayüzünü geliştirerek daha kullanıcı dostu hale getirin.

## Lisans

Bu program MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---
