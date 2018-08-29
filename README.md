## An Industrial Raspberry Shield: MiniIOEx-3G ##

MiniIOEx-3G is Raspberry Pi shield that can be used in industrial areas with 3G Module. MiniIOEx-3G has affordable price to use with Raspberry Pi. You can easily commissioning shield and you can easily integrate in your projects.  

MiniIOEx-3G has specifications mentioned at below:

| Technical Data  	| MiniIOEx-3G      |
| ------------- | ------------- |
| Digital Input | 	2ch(<4V FALSE, >4V TRUE ) |
| Digital Output |	4ch (2ch Relay@5V, 2ch transistor@24V) |
| Analog Input	 | 2ch 12bit 0-30V OR 2ch 12 bit 4-20mA |
| SeriPort	| RS232 OR RS485 |
| Power Input 	| 24V on Terminal OR 5V on RPI USB | 
| 3G Module	| QEUCTEL UC20/EC20 MiniPCI  |
| EEPROM	| 32kBit |
| Real Time Clock | 	- |
| Size with Case	| 80x94x42mm(WxLxH)|
| Weight	| ~30gr |

You can easily integrate RS232 / RS485 to communicate with other devices. If you have no Ethernet or Wireless possibility in the fields so MiniIOEx-3G can be used with IO features. If MiniIOEx-3G will be used in industrial area and it is provided 24V DC input on MiniIOEx-3G terminal. Else, you can use 5V on Raspberry Pi USB for boosting MiniIOEx-3G. 

We have some pictures for industrial shields at below:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3369.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3373.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3380.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3383.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3378.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3367.jpg)

MiniIOEx-3G has standart **Metal Sheet** to be used in electrical panels and industrial fields. So, you can easily mount it your projects. MiniIOEx-3G has also industrial 2x12 push-in terminal. Because of this feature, you will not worry cable installation time and 

MiniIOEx üzerinde aşağıdaki tabloda özellikleri verilen 2x12’li bir konnektör bulunmaktadır. Bu konnektör ile zaman kaybetmeden hızlı ve sağlam kablo montajı yapabilirsiniz. 

MiniIOEx Konnektör özellikleri:

| Terminal Features	| Comment |
| ------------- | ------------- |
| Terminal Number	|2x12 |
| Nominal Voltage	| 300V |
| Nominal Current	| 8A |
| Resistance Voltage	| 2000V |
| Max. Cable Size	| 2.5mm2 |
| Working Temperature	| -40C   +105C |

Bu dokumanda Raspberry üzerinde çalışacak MiniIOEx’in nasıl kurulacağı ve Raspberry için gerekli olan SD kart formatı, Linux üzerinde çalışırken bilinmesi gereken temel Linux komutları ve ayarlarından da bahsedilecektir. MiniIOEx ile basit otomasyon uygulamaları da gerçekleştirilerek dokumanda anlatılanların gerçek hayatta da uygulanabilirliği gösterilecektir. 

## Who is For MiniIOEx-3G? ##


## What is in the box ? ##

If you just buy  MiniIOEx without 3G module :

- MiniIOEx
- MiniIOEx Metal Sheet
- Sheet mount parts

If you buy  MiniIOEx-3G with **3G module** :

- MiniIOEx
- Quectel UC20 MiniPCI Express Module
- Antenna 
- Antenna Cable
- MiniIOEx Metal Sheet
- Sheet mount parts



Endüstriyel otomasyon projeleri geliştirirken en çok aradığımız özellik: PLC’de C/C++/Python/JAVA gibi yüksek seviye dillerini kullanmak, internete verileri aktarabilmek, PLC üzerinde local veritabanı kurarak SCADA üzerindeki yükü azaltmaktı. Raspberry Pi ilk çıktığında cihaza biraz mesafeli yaklaşsam da sonradan Raspberry Pi ile birçok endüstriyel otomasyon pprojeleri geliştirdim. Raspberry üzerinde GUI uygulamaları, verilerin seri port üzerinden veya doğrudan IO’lar üzerinden alınması ve bu verilerin bir sunucuya aktarılması/WEB uygulaması oluşturulması gibi işlemler oldukça kolaydır. Bunun nedeni Raspberry’nin üzerinde bir işletim sistemi çalışması ve Linux üzerinden programlama yapabilmemizdir. Bu dokumanda da bu başlığa birçok atıf yapacağız. Neden Linux/GNU kullanmamız gerektiği, PLC üzerinde yapması nerdeyse günler süren ve pahalı çözümlerin burada ne kadar yapılabildiğini de birçok başlık altında görebileceğiz. 

MiniIOEx projelerinde PLC’den Linux/GNU’ya geçmek isteyen kullanıcılar için aslında bire bir. Piyasada birçok Raspberry Pi eğitim kartları bulunmakta ama bu kartların hiçbirini endüstriyel projelerimizde kullanamamaktayız. Bundan dolayı ilk hevesle alınan birçok Raspberry’nin tekrar çekmecelere konduğuna şahidim. Bu dokumanda da aslında Raspberry ile nelerin yapılabileceğini gösteriyoruz. Enerki analizöründen veri okuyoruz, AC motorumuza hız referansı gönderiyoruz, sensörlerden veri okuyoruz ve bunları bir sunucuya göndererek verilerimize dışarıdan erişilmesine fırsat tanıyoruz. Yani tüm bunları özetleyecek olursak MiniIOEx kimin için?

-	Endüstriyel otomasyon firmaları,
-	IOT projeleri geliştiren start-up’lar,
-	Gateway tabanlı proje geliştiren firmalar (RS485 / Ethernet -> Web Service vs.),
-	Hızlı prototipleme ihtiyacı olan kullanıcılar,
-	Gömülü Linux tabanlı uygulama geliştirmek isteyen öğrenciler/akademisyenler,
-	Ve tabiki Hobi kullanıcıları.

## Digital Input 

## Digital Output ##

## Analog Input ##

## Seri Port ##

## 3G / GPS ##

## Other Topics ##
