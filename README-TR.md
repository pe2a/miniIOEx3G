# Giriş

Bu dokuman, kredi kartı büyüklüğündeki yüksek işlem kapasitesine sahip bilgisiyar Raspberry Pi ve işlem gücünün endüstriyel ortamlarda nasıl kullanılabileceği ile ilgilidir. Otomasyon sektöründe çalışan, IOT sektörüne yeni giriş yapan ve makinelerle iletişim sağlamak isteyen mühendisler ve ilgililer için yararlı bilgiler bulunmaktadır. Raspberry Pi’yi bir heves ile alıp çekmecesine yerleştiren ve oradan hiç çıkarmayan kullanıcılar için de bu dokümanlarda anlatılanlar yararlı olabilir. Raspberry Pi’lerin hangi ortamlarda kullanılabileceğini gördükten sonra belki ilgili oldukları bir alanda kullanabilecekleri fikirler gelebilir. Dokumanda sık sık C/C++ ve Python gibi dillerden uygulamalı örnekler de verilmiştir. Bu dilleri kullanarak otomasyon alanında neler yapılabileceği ile de bir fikir oluşturabilir.  Bununla beraber, Raspberry Pi’nin GPIO pinlerinin kontrolü, seri port uygulamaları, sahadan gelen verilerin sunuculara aktarılması, 3G özelliğini kullanarak internete çıkılması, USB portlarının kullanılması, internet hız testleri gibi birçok konu da bu dokumanda bahsedilecektir. Bu bilgileri kullanarak projenizi nasıl geliştirebileceğiniz ve Raspberry Pi’yi hangi alanda kullanabileceğiniz fikri de gelişebilir. 

Raspberry Pi’nin kısaca tarihinden bahsedecek olursak, Bilgisiyar Bilimcisi Eben Upton ve bir grup arkadaşı ile beraber Cambridge Universitesi’nde Raspberry Pi ile ilgili çalışmalara başladı ve birçok prototip Raspberry Pi türevi geliştirdi. Amaçları; çok ucuza bir bilgisiyar geliştirirek bu bilgisiyarın herkes tarafından kullanılabilmesini sağlamalarıydı. İlk resmi Raspberry Pi ise bu çalışmalara başladıktan 6 yıl sonra 2012 yılında “Raspberry Pi A” serisi ile duyruldu. Sonrasında ise müteakip yıllarda “Model B” duyruldu. Şubat 2015’de yeni model Raspberry Pi 2, (şu andaki Raspberry Pi’ler ile aynı GPIO ve boyutlara sahip) mini bilgisiyar geliştirildi. Raspberry Pi A ve Raspberry Pi 2 arasındaki performans farkları, GPIO sayısının artması gibi nedenler ile Raspberry Pi satışları patlamış ve Raspberry Pi’nin bugünkü popülerliğini almasını sağlamıştır. Raspberry Pi ilk modeli ARM tabanlı Broadcom bcm2835 chip’i üzerinde inşaa edilse de yeni çıkan Raspberry Pi 3 Model B+ modelinde bcm2837 chipi kullanılmıştır. Raspberry üzerinde aynı zamanda Video işlemcisi de bulunmaktadır. Bunlara ek olarak Ethernet, 4 adet USB, kamera girişi, HDMI, Audio, ekran çıkışı gibi özellikler de bulunmaktadır. Modelller arasındaki karşılaştırmalar internet üzerinden edinilebilir. Aşağıdaki resimde en son çıkan Raspberry Pi 3 Model B+ modeli bulunmaktadır. Bu model üzerindeki chip’lerde dahili olarak ‘heatsink’ler eklenerek işlemcilerin ısı/işlem performansını arttırmıştır. 

![Image of RPI 3 B+](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/rpi3b.jpg)
Raspberry Pi 3 Model B+’da aşağıdaki özellikler bulunmaktadır:

- BCM2837B0, Cortex-A53 64-bit 1.4GHz işlemci
- 1 GB LPDDR2 SDRAM
- 2.4GHz ve 5GHz IEEE 802.11.b/g/ n/ac kablosuz LAN, Bluetooth 4.2, BLE
- USB 2.0 üzerinden Gigabit Ethernet (maksimum çıkış 300 Mbps)
- Genişletilmiş 40 pinli GPIO başlığı
- HDMI
- 4 USB 2.0 bağlantı noktası
- CSI kamera portu
- DSI dokunmatik ekran portu
- Video ve ses çıkış portu (4’lü jack çıkışı)
- Micro SD Kart girişi 

Otomasyon ve IOT/IIOT sektöründe gelişen ihtiyaçlar internet bağlantısının olmadığı yerlerde, GPRS sistemler üzerinden haberleşmeyi mecbur bırakmıştır. Cep telefonu operatörlerin kapsama alanlarını genişletmesi, internet altyapısının ulaşamadığı yerlerde SIM kartı üzerinden endüstriyel cihazların internete bağlanması için gerekli cihazların üretilmesine yol açmıştır. Türkiye’de de birçok yerde 4.5G bağlantısının olması veri iletişimini oldukça hızlandırmıştır. Raspberry’nin sahip olduğu yüksek işleme kapasitesi, kamera girişi, video oynatma ve kolay programlanabilir IO pinlerinin olması dolayısıyla shield üzerinde rahatlıkla birçok endüstriyel uygulamalar geliştirilebilir. Kullandığınız program ne ise Raspberry üzerinde de bu programlama dilini kullanabilirsiniz. 

Javascript, Python, C/C++, JAVA gibi programlama dilleri Raspberry üzerinde sorunsuz çalışmaktadır. Bundan dolayı PLC’lerde olduğu gibi IO programlamada farklı; sunucu programlamada farklı bir programlama dili kullanmanıza gerek yoktur. Raspberry’nin bu işlem gücünün ve Linux üzerinde çalışması dolayısıyla altyapı esnekliğinin otomasyon alanında keşfedilmesiyle beraber endüstriyel shield’ler üretilmeye başlanmıştır. Türkiye’de bunun ilk örneğini **MedIOEx - Endüstriyel Raspberry Pi Shield** ile beraber gördük. Otomasyon sektörünün birçok alanında bu kart kullanılmış ve olumlu geri bildirimler alınmıştır. MedIOEx üzerinde 40’dan fazla IO mevcuttur. Bazı IOT uygulamalarında az IO ve 3G bağlantısı ihtiyacı olmamaktadır. Bundan dolayı da MiniIOEx-3G geliştirilmiştir. Dokumanın devamında da sık sık bu kart ile yapılmış uygulama örneklerinden bahsedilecektir.  Kullandığınız programlama dili ne ise rahatlıkla **MiniIOEx** üzerinden fabrikanızdaki enerji analizörlerinden RS485 üzerinden veri alabilir aynı seri portu kullanarak motor sürücülerine referens gönderebilir ve pano üzerindeki ana kontaklarını kontrol edebilirsiniz. Bütün bunları yaparken de anlık Analog sensörlerinizden gelen datayı SD karta kayıt edebilir bu verileri internet üzerinden sunucularınıza göndererek kullanıcının bu bilgilere WEB veya mobil üzerinden ulaşmasını sağlayabilirsiniz. Bu uygulama aslında fabrikalarda var olan ama binlerce EUR’ya mal edilen sistemlerdendir. Raspberry Pi ve üretilen endüstriyel shield’ler bu maliyetler minimuma inmekte ve popüler yazılım dilleriyle ve halihazırda önceden yazılmış kütüphanelerle çalışma imkanı verdiği için en basit sıcaklık sensöründen gelen veriyi bile “Yapay Zeka” kullanarak işleyebilirsiniz. (**Python TensorFlow Kütüphanesi**)

![Image of Populer Diller](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/PopulerDiller.jpg)

Yukarıdaki grafikte 2017 yılında en popüler programlama dilleri yer almaktadır. Bu dişllerden ilk 4’ü Raspberry Pi tarafından doğrudan desteklenmekte ve Raspberry Pi üzerinde çalışan birçok uygulamaları mevcuttur. Bu doğal dillerin hiçbiri doğrudan bir PLC veya gömülü PC üzerinde çalışmadığından kaynak bulmak zor olmakta ve popüler yazılım kütüphaneleri kullanılamamaktadır. Okuyucunun aklına hemen ama bu diller Raspberry Pi üzerinde “Real Time” programlama yapmaya izin vermez gibi bir düşünce gelebilir. Evet! Raspberry Pi üzerinde gerçek zamanlı uygulama yapılamamaktadır. Peki, bu gerçek zamanlı uygulamalar bir otelin lambalarını kontrol ederken veya bir şebekenin enerji bilgilerini kontrol ederken ne kadar işe yarayabilir? Yani eğer CNC gibi yüksek hassasiyet ve doğruluk gerektiren bir iş yapmıyor iseniz Raspberry ve endüstriyel shield’ler rahatlıkla kullanılabilir. 1ms delay çoğu uygulamalarda önemsiz olmaktadır. Örnek olarak bir lamba komut’dan 50ms sonra çalışması bile bir kullanıcı tarafından zaten algılanamamaktadır. Raspberry Pi kullandıkça yapılan işlerin kalitesinin arttığı da görülecektir. 

Raspberry Pi ve endüstriyel shield’lerin kullanılma alanları ve tarihlerinden kısaca bahsettik.  Sırada artık bu dokumanın konusu olan MiniIIOEx-3G var. Aşağıdaki başlıklarda bu konuyla ilgili uygulama örnekleri ve Raspberry kurulumlarını bulabilirsiniz. 

## Endustriyel Raspberry Shield: MiniIOEx3G ##

Bu dokuman, otomasyon sektöründe uzun yıllar tecrübe etmiş PLC kullanmış ve Raspberry Pi’ye geçmek isteyen kullanıcılar için olduğundan temel elektrik ve otomasyon bilgileri çoğu zaman kullanıcı tarafından biliniyor kabul edilmiştir. 

Raspberry ve MiniIOEx-3G shield ile çok daha uygun fiyata ve Raspberry’nin geniş kullanıcı desteği, kolay programlanabilir yapısıyla düşündüğünüz uygulamaları rahatlıkla hayata geçirebileceksiniz.

MiniIOEx-3G özellikleri aşağıda belirtilmiştir:

| Teknik Data  	| Açıklama      |
| ------------- | ------------- |
| Digital Input | 	2ch(<4V FALSE, >4V TRUE ) |
| Digital Output |	4ch (2ch Relay@5V, 2ch transistor@24V) |
| Analog Input	 | 2ch 12bit 0-30V veya 2ch 12 bit 4-20mA |
| SeriPort	| RS232 veya RS485 |
| Giriş Beslemesi	| 24V klemens üzerinden veya 5V RPI USB | 
| 3G/4.5G Modül	| QEUCTEL UC20/EC20 MiniPCI Uyumlu |
| EEPROM	| 32kBit |
| Real Time Clock | 	- |
| Güç Girişi	| 24V veya 5V USB | 
| Boyut	| 80x94x42mm(ExBxY) |
| Ağırlık	| 30gr |



RS232/RS485 portunu sahadaki diğer cihazlarla haberleşmek için kullanabilirsiniz. Eğer ethernet veya wireless imkanına sahip olan bir yerde iseniz 3G modulü satın almadan da shield üzerinde bulunan IO’ların hepsini kullanabilirsiniz. MiniIOEx, çalışması için gerekli olan gerilimi Raspberry 5V pinlerinden almaktadır. Bundan dolayı Raspberry’yi 5V USB ile besleyerek aynı zamanda MiniIOEx’i de beslemiş olursunuz.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3369.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3373.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3369.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/IMG_3380.jpg)

MiniIOEx3G endüstriyel ortamlar göz önüne alınarak üretildiği için Metal Sac kutu içerisinde gelmektedir. metal Sac Kutu, DIN Rayı ile beraber geldiği için elektrik panolarında montaja uygundur. Eğer DIN Rayı dışında bir yere montaj etmek istenirse 3 adet M2.5 kulakçıklar akıllı vida ile montaj edilebilir. 


MiniIOEx üzerinde aşağıdaki tabloda özellikleri verilen 2x12’li bir konnektör bulunmaktadır. Bu konnektör ile zaman kaybetmeden hızlı ve sağlam kablo montajı yapabilirsiniz. 

MiniIOEx Konnektör özellikleri:

| Konnektör Özellikleri	| Açıklama |
| ------------- | ------------- |
| Konnektör Sayısı	|12x2 |
| Nominal Gerilim	| 300V |
| Nominal Akım	| 8A |
| Dayanma/Atlama Gerilimi	| 2000V |
| Max. Kablo Kalınlığı	| 2.5mm2 |
| Çalışma Sıcaklığı	| -400C   +1050C |

Bu dokumanda Raspberry üzerinde çalışacak MiniIOEx’in nasıl kurulacağı ve Raspberry için gerekli olan SD kart formatı, Linux üzerinde çalışırken bilinmesi gereken temel Linux komutları ve ayarlarından da bahsedilecektir. MiniIOEx ile basit otomasyon uygulamaları da gerçekleştirilerek dokumanda anlatılanların gerçek hayatta da uygulanabilirliği gösterilecektir. 

### MiniIOEx-3G Kimin İçin ###


Endüstriyel otomasyon projeleri geliştirirken en çok aradığımız özellik: PLC’de C/C++/Python/JAVA gibi yüksek seviye dillerini kullanmak, internete verileri aktarabilmek, PLC üzerinde local veritabanı kurarak SCADA üzerindeki yükü azaltmaktı. Raspberry Pi ilk çıktığında cihaza biraz mesafeli yaklaşsam da sonradan Raspberry Pi ile birçok endüstriyel otomasyon pprojeleri geliştirdim. Raspberry üzerinde GUI uygulamaları, verilerin seri port üzerinden veya doğrudan IO’lar üzerinden alınması ve bu verilerin bir sunucuya aktarılması/WEB uygulaması oluşturulması gibi işlemler oldukça kolaydır. Bunun nedeni Raspberry’nin üzerinde bir işletim sistemi çalışması ve Linux üzerinden programlama yapabilmemizdir. Bu dokumanda da bu başlığa birçok atıf yapacağız. Neden Linux/GNU kullanmamız gerektiği, PLC üzerinde yapması nerdeyse günler süren ve pahalı çözümlerin burada ne kadar yapılabildiğini de birçok başlık altında görebileceğiz. 

MiniIOEx projelerinde PLC’den Linux/GNU’ya geçmek isteyen kullanıcılar için aslında bire bir. Piyasada birçok Raspberry Pi eğitim kartları bulunmakta ama bu kartların hiçbirini endüstriyel projelerimizde kullanamamaktayız. Bundan dolayı ilk hevesle alınan birçok Raspberry’nin tekrar çekmecelere konduğuna şahidim. Bu dokumanda da aslında Raspberry ile nelerin yapılabileceğini gösteriyoruz. Enerki analizöründen veri okuyoruz, AC motorumuza hız referansı gönderiyoruz, sensörlerden veri okuyoruz ve bunları bir sunucuya göndererek verilerimize dışarıdan erişilmesine fırsat tanıyoruz. Yani tüm bunları özetleyecek olursak MiniIOEx kimin için?

Endüstriyel otomasyon firmaları,
IOT projeleri geliştiren start-up’lar,
Gateway tabanlı proje geliştiren firmalar (RS485 / Ethernet -> Web Service vs.),
Hızlı prototipleme ihtiyacı olan kullanıcılar,
Gömülü Linux tabanlı uygulama geliştirmek isteyen öğrenciler/akademisyenler,
Ve tabiki Hobi kullanıcıları.

## Raspbian İşletim Sistemi Kurulumu ##

Raspberry, üzerindeki SD kartı üzerinden işletim sistemini çalıştırmaktadır. Bundan dolayı kaliteli ve hızlı bir SD kart (class 10 önerilir) ve üzerinde çalışacak işletim sistemini doğru formatta yüklemek için bir “Disk Image” programı olması gerekmektedir. 
Aşağıdaki adımları takip ederek Windows’da “Win32 Disk Imager” ile bu işlemleri gerçekleştirebilirsiniz:
Win32 Disk Imager Programı: https://sourceforge.net/projects/win32diskimager/

Eğer GPIO’ları yoğun bir şekilde kullanıyor iseniz Raspbian tabanlı bir işletim sistemini kurmak önemlidir. Diğer işletim sistemleri Raspbian gibi Raspberry üzerinde stabil bir çalışma yapısına sahip değildir. Raspberry Vakfı yılın belli dönemlerinde işletim sistemini güncellemektedir. En güncel Raspbian işletim  sistemine ise aşağıdaki linkten ulaşabilirsiniz. 

Raspberry ISO Link: https://www.raspberrypi.org/downloads/raspbian/

İlgili linkte iki adet ISO formatında Raspbian OS bulunmaktadır. “Raspbian Lite” sadece terminal ekranı açılır. Herhangi bir GUI barındırmaz. Bundan dolayı eğer programınız GPIO kullanıyor ve bu verielri örnek olarak bir sunucuya gönderiyor yani herhangi bir GUI işleminin kullanmıyor iseniz ‘Lite’ versiyonu yükleyebilirsiniz. Böylelikle işletim sistemi de kullanmadığınız birçok programın yükünden kurtulacaktır. Eğer Raspbian üzerinde uygulama geliştiriyorsanız, Office gibi programlarını da kullanmak istiyorsanız ‘with Desktop’ en uygun seçim olacaktır. Böylelikle normal bir ‘Windows’ kullanıyor gibi Raspberry’yi kullanabilirsiniz. 

İstenilen işletim sistemi indirildikten sonra ‘Disk Imager’ programınızı açarak ve SD kartını formatlanması için SD kartı bilgisayarınıza yerleştirerek aşağıdaki işlemlere başlayabilirsiniz. 

1)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/RPI1OS.jpg)

2)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/RPI2OS.jpg)

3)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/RPI3OS.jpg)


## MiniIOEx-3G İlk Enerji Verilmesi ##

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/RPI4OS.jpg)

![Image of Note](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteIcon.jpg = 20x)

Note__ Raspberry’yi görüntü işleme veya yoğun process işlemlerde kullanıyor iseniz MiniIOEX üzerinden 24V ile Raspberry’yi beslemeniz önerilir. 

![Image of Note](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteIcon.jpg = 20x)

Note__ Raspberry Pi üzerinde çalışacak SD kartı, formatlanmış bir şekilde mağazamızdan satın alabilirsiniz. 


