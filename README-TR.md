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

-	Endüstriyel otomasyon firmaları,
-	IOT projeleri geliştiren start-up’lar,
-	Gateway tabanlı proje geliştiren firmalar (RS485 / Ethernet -> Web Service vs.),
-	Hızlı prototipleme ihtiyacı olan kullanıcılar,
-	Gömülü Linux tabanlı uygulama geliştirmek isteyen öğrenciler/akademisyenler,
-	Ve tabiki Hobi kullanıcıları.

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


<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteIcon.jpg" alt="drawing" width="35"/>
**Note** 
Raspberry’yi görüntü işleme veya yoğun process işlemlerde kullanıyor iseniz MiniIOEX üzerinden 24V ile Raspberry’yi beslemeniz önerilir. 
<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteIcon.jpg" alt="drawing" width="35"/>
**Note** 
Raspberry Pi üzerinde çalışacak SD kartı, formatlanmış bir şekilde mağazamızdan satın alabilirsiniz. 

## Raspberry Üzerinde Basit Linux Komutları ## 

SD kartı Raspberry’ye taktıktan sonra Raspberry wireless USB klavye/Mouse bağlayabilir ve HDMI konnektörünü kullanarak monitörünüze Raspberry üzerindeki görüntüyü aktarabilirsiniz. Bu başlık altında Linux/GNU üzerinde çalışabilen komutlar üzerine yoğunlaşacağız. Raspberry’de kullandığımız işletim sistemi Debian tabanlı Raspbian işletim sistemi Linux/GNU çekirdeğini kullandığı için bazı komutları bilmemiz gerekiyor. Bu dokumanı okuyan ve genelde otomasyon sektöründe PLC’ler için kod yazan okuyucular belki zorlanabilir ama temel Linux/GNU terminal komutlarını öğrendiklerinde birçok işlerini çok rahat çözebildiklerini görecekler. 

MiniIOEx’e enerji verdiğinizde Raspberry’ye de çalışma gerilimi için gerekli gerelim regülatörlerden geçecek ve Raspberry çalışmaya başlayacak. Her işletim sistemi gibi Raspberry’nin de bir açılış ekranı var ve ilk açılış ekranında işletim sistemi üzerinde çalışan servislerin açılıp açılmadığını bu ekrandan izleyeyebilirsiniz. Eğer açılış zamanında bir hata ile de karşılaşırsanız yine bu ekran üzerinden görebilirsiniz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/11.jpg)

<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteIcon.jpg" alt="drawing" width="35"/>
**Note**
Raspberry Pi'yi ÇALIŞTIRMAK için fişini takmanız yeterlidir. Üzerinde bir açma-kapama düğmesi mevcut değildir. Çalışan programlarınızı ya da işletim sisteminizi kapattıktan sonra cihazın fişini çekebilirsiniz.


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/12.jpg)

Raspberry’nin internet üzerinden uygulama güncelleştirmelerini yüklemek önemlidir. Bundan dolayı Wireless ayarlarını yaptıktan sonra güncelleştirme yüklenmesi için terminal ekranında komut girmemiz gereklidir. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/13.jpg)

Terminal ekranında güncelleştirmeler için aşağıdaki komutları giriyoruz:

```sh
$ sudo apt update
$ sudo apt upgrade
$ sudo rpi-update
```

Sonrasında güncelleştirmeler başlayacak ve sistem en güncel haline getirilecektir. Bunu yapmak önemlidir. Kütüphane, sistem dosyaları ve eğer varsa güvenlik açıkları bu yolla minimuma indirilebilir. 


Bu Linux komutları, en çok kullanılan Linux komutları arasında olsa da sizin de kullanacağınız birçok Linux komutu olabilir ve bu da Linux işletim sistemi üzerinde yaptığınız işlemlerin hızlanmasına yol açar.  Linux büyük/küçük harf duyarlı olduğu için komutları yazarken buna dikkat etmek gereklidir. 


Raspberry Pi’yi eğer yeniden başlatmak veya kapatmak istiyorsak aşağıdaki komutları uygulamamız yeterlidir. 

| Raspberry Shutdown / Reboot	 | Açıklama |
| ------ | ------ |
|shutdown -h	| Düzgün kapatmak için bu komutu kullanabiliriz. Açık dosyaları kapatır ve işletim sistemi kapanmaya hazır hale gelir. “shutdown -h +1” komutu ile 1dk sonra kapatabilirsiniz. | 
| reboot	| Yeniden başlatma |
| poweroff	| Komutu yazar yazmaz işletim sistemi kapanır. Açık dosyalarınız ve hali hazırda çalışan programlarınız var ise bu komut önerilmez. | 

<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteIcon.jpg" alt="drawing" width="35"/>
**Note**
Raspberry’yi komut ekranından kapattığınızda yeniden açmak için enerjisini kesip tekrar enerjisini vermeniz yeterlidir. 

## Raspbian Konfigürasyon Araçları ##
Linux/GNU işletim sistemleri üzerinde bazı işlemler vakit alır. Örnek olarak ssh servisini açmak istiyorsak bununla ilgili portları açmalıyız ve servislerin işletim sistemleri üzerinde çalışmasına izin vermeliyiz. Üzerlerindeki GPIO’ları kullanmak için bazı izinler de gereklidir. Örnek olarak SPI,i2C portlarını kullanacağımızı işletim sistemine bildirmemiz gereklidir ki işletim sistemi de belirli GPIO’lardan “clock” üretsin veri okusun vs. Raspbian işletim sisteminin “raspi-config” aracıyla bu işlemler basite indirgenmiştir. Bu araçları kullanarak manuel yapılan birçok işlemi otomatik hale getirebiliriz. Bu başlık altında bu aracın nasıl çalıştığı ile özet bilgi verilecektir. İlgili başlıklarda bu servislerin kullanılması ile ilgili ayrıntılı bilgiler mevcuttur. 

### SSH Ayarları ###

Raspberry’yi monitör ve klavye gibi çevre birim elemanları takıp üzerinde çalışmak mümkün ama çoğu zaman yazılımcılar Raspberry’ye uzaktan bağlanmayı tercih ederler. Bu da tabiki sahada çalışan Raspberry’ler içinde büyük bir avantaj olmaktadır. Uzaktan çalışmanın çeşitli yolları olsa da Linux/GNU üzerinde en yaygın kullanılanı Secure Socket Shell (SSH) çözümüdür. Bu bağlantı yöntemiyle güvenli bir bağlantı sağlar ve cihazlarınıza güvenle erişebilirsiniz. SSH Linux/GNU üzerinde çalışan bir servis olduğundan dolayım belirli bir port numarası kullanır. 22 No’lu Port SSH için ayrılmıştır. Raspbian işletim sisteminde SSH servisini **“raspi-config”** üzerinden rahatlıkla aktif edebiliriz.  
Eğer Windows bir işletim sistemi kullanıyorsanız SSH yüklü olarak gelmez. Yardımcı bir programla SSH üzerinden başka bir cihaza bağlanmanız gerekir. 
Windows üzerinde Putty programı ile başka bir cihaza SHH üzerinden bağlanabiliriz.  Putty programını indirmek için bu bağlantıdan bilgi alabilirsiniz: https://www.putty.org/
Hostname kısmına Raspberry’nin IP’sini girebilirsiniz. Sonrasında da gelecek ekranda **“login name”** yani Raspberry kullanıcı adı istenilecektir. Eğer değiştirmediyseniz Raspbian işletim sistemlerinde  hostname / password aşağıda  verilmiştir. 

Default Raspbian Login Ayarları:

- Raspberry Hostname:	pi
- Raspberry Password:	raspberry

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/14.jpg)

Raspberry üzerinde SSH kullanımını aktif etmek için aşağıdaki adımları izlemeniz yeterlidir:
1)	Terminal ekranında “sudo raspi-config” komutunu gir
2)	“Interfacing Options” kısmına git
3)	“SSH” menüsünü seç
4)	Ok-> Enable et
5)	Finish
Kaynak: https://www.raspberrypi.org/documentation/remote-access/ssh/
Bu işlemler bittikten sonra işletim sistemini yeniden başlatarak SSH ile cihaza bağlanabilirsiniz. IP’nizi öğrenmek için terminal ekranında **“ifconfig”** komutunu girebilirsiniz ve buradaki IP numaranızı putty ekranında hostname olarak yazabilirsiniz. 

## Raspbian Üzerinde C/C++/Python Derlenmesi ve Çalıştırılması ##

Raspberry Pi üzerinde yazılım dilleriyle çalışmak oldukça kolaydır. Windows İşletim sistemlerinde herhangi bir .C dosyasını çalıştırmak için birçok program indirilmesi gerekse de Raspbian işletim sistemleri Linux/GNU tabanlı olduğu için buna gerek yoktur. GCC derleyicisi hazır olarak gelmektedir. Yapmamız gereken tek şey terminali açıp, programı yazmak ve derlemektir. Raspberry’de çalışmak bazı durumlarda zor olabilir.  Eğer kendi bilgisiyarımızdan Raspberry’ye bağlanmak istiyorsak Linux üzerinde çalışabilen SSH protokolünü kullanabiliriz. Bu protokel sayesinde kendi kişisel bilgisiyarınızda (Macbook vs.) yerde kodumuzu yazabilir ve Raspberry üzerinde çalıştırabiliriz. Bu başlık altında bu uygulamalara da yer verilecektir. 

<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteIcon.jpg" alt="drawing" width="35"/>
**Note**
Yeni açtığınız dosyalarda veri işlemeye işletim sistemi tarafından izin verilmiyor ise dosyaya veya klasöre bazı haklar vermeniz gerekiyor. Aşağıdaki komut ile bu hakların hepsini vermiş olursunuz. 

'''sh
$ sudo chmod a+w "DOSYA ADI"
'''
### C99 Standartlarına Göre C Programlama Dili ve Derlenmesi ###

Raspbian işletims sistemlerinde C ve C++ kodlarını derlemek için hazır olarak GCC derleyici gelmektedir. Terminali açtıktan sonra “nano” editörü yardımıyla kodumuzu yazabiliriz.  
Terminal ekranında:
```sh
$ nano helloWorld.c
```

**helloWorld.c**
```sh
#include <stdio.h>
void foo(){
    printf("Hello World\n");
}
int main(){
    foo();
    return 0;
}

```
Kayıt etmek için “nano” editörü üzerinde **CTRL + X** ile çıkıp **“Y”** tuşuna basmamız gerekiyor. Bu şekilde dosya ilgili klasörün altında oluşturulacaktır. 
Kodumuzu derlemek için yine terminal ekranında aşağıdaki komut satırını girmemiz gerekiyor:
```sh
$ gcc -o helloWorld helloWorld.c 
```

Eğer kodumuzda bir hata yoksa “mesaj” veya “başarıyla derlendi” mesajı almayız. Terminal ekranında bir alt satıra inilmesi gerekmektedir. Normal şartlar altında bu programın doğru derlenmesi gerekmektedir. Program derlendiğinde aynı zamanda “executable-çalışabilir” bir dosya da oluşturacaktır. Bu dosyanı adı “helloWorld” olmaktadır. Programı derlerken de “helloWorld.c” dosyasının “helloWorld” çalışabilir dosyasını oluşturması komutunu veriyoruz. 

Programı çalıştırmak için ise aşağıdaki komutu çalıştırmamız yeterlidir:
```sh
$ ./helloWorld  
```

Program  “Hello World” çıktısını üretecektir. Ürettimiz **helloWorld** çalışabilir dosya **C99** standartlarına göre üretilmiş bir dosyadır. Eğer C11 standartlarında çalışmak istiyor isek bir parametre daha girmemiz gereklidir. 

### C11 Standartlarına Göre C Programlama Dili ve Derlenmesi ###

Eğer C11 standartlarına göre programın derlenmesini ve çalışabilir bir dosyanın oluşturulmasını istiyor isek **“-std=c11”** komut parametrisini girmemiz gereklidir. 

Aşağıdaki kodu derlemeye çalışalım:

```sh
#include <stdio.h>

int main(){

    for(int i = 0; i < 100; ++i)
        printf("Hello World\n");

    return 0;
} 
```

Normal şartlar altında aşağıdaki gibi derliyorduk:
**C11 Standartları için Hatalı Derleme:**
```sh
$ gcc -o helloWorld helloWorld.c  
```

Bu kodu bu şekilde derlediğimizde hata mesajı ile karşılaşırız: FOR döngüsünün içinde bir değişken ilk defa tanımlandığı için.
Bundan dolayı **“-std=c11”** komut parametresini girmemiz gerekiyor. 

C11 Standartları için Doğru Derleme:
```sh
$ gcc -o helloWorld helloWorld.c -std=c11  
```

Parametreyi eklediğimizden dolayı artık hata mesajı almadan programımızı çalıştırabiliriz: 

```sh
$ ./helloWorld  
```

Ekrana 100 adet “Hello World” yazısı yazdırılacaktır. 

C koduyla çalışırken genelde başka kütüpnalerden fonksiyonlar da kullanıyoruz. Örnek olarak MedIOEx(http://www.medioex.com) shield ile çalışırken MedIOEx’in C koduyla yazılmış dosyasını aynı klasör altında derlemeye çalışmış olmalısınız. Tüm kodu aynı dosyada yazmak kodun ilerleleyen dönemlerinde okunmasını, bakımını ve modülerliğini azaltmaktadır. Bundan dolayı bu başlık altında birden çok C kütüphanesi ile çalışmayı ve bunların derlenmesi ile ilgili örnekler verebiliriz. 
Kendi kütüphanenizi oluşturmak için yeniden nano editörü ile bir dosya oluşturabilirsiniz. Bu örnekte **pmedex** kütüphasini oluşturacağız ve **test.c** programında bu kütüphanenin örnek fonksiyonunu kullanacağız. 
İlk olarak “pmedex.h” kütüphanesini oluşturuyoruz. 
Sonrasında ise kullanacağımız fonksiyonları ve değişkenleri tanımlıyoruz. 
**pmedex.h**
```sh
#include <stdio.h>
static int myCounter = 0;
void fCounter();
```
Kütüphanemizde sadece fonksiyon ve kullanacağımız standart kütüphane fonksiyonlarını tanımladık. 

Bu fonksiyonların gövdelerini ise **pmedex.c** programına yazıyoruz. 


```sh
#include "pmedex.h"

void fCounter(){
    myCounter++;
    printf("myCounter  = %d \n",myCounter);
}

```

**“pmedex.h”** kütüphanesini oluşturduk ve fonksiyonların yazımını gerçekleştirdik. Bu fonksiyonları “main.c” dosyası altında kullanabiliriz. “main.c” dosyasını oluşturuyoruz ve bu program içinde **“fCounter()”** fonksiyonunu çağırıyoruz. 

```sh
#include <stdio.h>
#include "pmedex.h"
int main(){
    fCounter();
    return 0;
}

```

Derlemek için ise aşağıdaki komut satırını kullanabilirsiniz. 

```sh
$ gcc main main.c pmedex.c -std=gnu11
```

### MiniIOEx Üzerinde C Programlama Dili ile Raspberry Üzerinde LED Kontrolü ###

Genelde Raspberry ile yapılan ilk örnek LED kontrolü olur. Bunun için bir adet transistör, LED ve direnç ile Raspberry üzerindeki ilgili GPIO’ya bağlantı yapılarak LED on/off yaptırılır. Biz de bu geleneği bozmayalım. Yalnız burada transistör, LED, direnç gibi temel elektronik ekipmanlara ihtiyacınız yok. Örneklerin hepsinin MiniIOEx-3G endüstriyel Raspberry Shield üzerinden yapacağımızı belirtmiştik. İlk uygulama örneğimizi de bu shield üzerinden gerçekleştiriyoruz. Önceki başlıklarda bcm2835 kütüphanesinin yüklenmesini ve nasıl derleneceğini öğrenmiştik. Bu örnekte de bcm2835 kütüphanesine ihtiyacımız olacaktır. Bu kütüphaneyi yüklediyseniz ilk örneğimize geçebiliriz. Raspberry üzerindeki GPIO numaraları ile bcm2835 kütüphanesinin GPIO numaraları farklıdır. Bu farklılığın nedeni bcm2835 kütüphanesinin Raspberry A modeli için yazılmış olmasıdır. Sonraki güncelleştirmelerle yeni model Raspberry’lere de uyumlu hale getirilmiştir. Bu nedenlerden dolayı Raspberry üzerindeki kullanacağımız GPIO’yu bcm2835 kütüphanesinin karşılık gelen PIN ile eşleştirmemiz gerekiyor. Programda bcm2835 kütüphanesindeki PIN adresini kullanacağız. Biraz karışık gelse de ilk örnekten sonra daha iyi anlaşabileceğini düşünüyorum. 

Aşağıdaki tabloda Raspberry üzerindeki GPIO’ya bağlı olan LED ve buna karşılık olarak da bu GPIO’ya karşılık gelen bcm2835 PIN numarası görülmektedir. Aşağıda yazacağımız bu basit uygulamada bcm2835 üzerindeki PIN adresini kullanacağız. 


| Raspberry Üzerindeki GPIO	| BCM2835 GPIO |
| ------ | ------ |
| 37	| BCM26 |

Programı aşağıdaki gibi oluşturabiliriz:

```sh
#include <stdio.h>
#include <bcm2835.h>

#define RASP_DIG_tr_LED_1 RPI_V2_GPIO_P1_37 
//miniIOEx RUN LED 
//update 08.2018
int main(){
    
     if (!bcm2835_init())
      return 1;
     // Set the pin to be an output
    bcm2835_gpio_fsel(RASP_DIG_tr_LED_1, BCM2835_GPIO_FSEL_OUTP);
    while (1)
    {
    // Turn it on
    bcm2835_gpio_write(RASP_DIG_tr_LED_1, HIGH);
    // wait a bit
    bcm2835_delay(250);
    // turn it off
    bcm2835_gpio_write(RASP_DIG_tr_LED_1, LOW);
    // wait a bit
    bcm2835_delay(250);
    }
    bcm2835_close();
    return 0;   
}

```
Programı aşağıdaki komutlar ile derleyip/çalıştırabiliriz:

```sh
$ gcc -o led led.c -lbcm2835 -std=gnu11 
$ ./led
```
Sonrasında MiniIOEx-3G üzerindeki LED’in flash yaptığını görebileceksiniz. Bu uygulama sayesinde bcm2835 kütüphanesinin doğru yüklenip yüklenmediğini de görebileceğiz. 

Programı anlamak için öncelikle bunu açıklamak gerekecektir. Her ne kadar basit bir kod gibi görünse de aslında program birçok işlemi gerçekleştirmektedir. Programda ilk olarak Raspberry üzerindeki GPIO kullanacağımız için kullanacağımız PIN tanımlanmıştır. Bu PIN, MiniIOEx üzerinde LED pinidir. Bu pinin Raspberry’nin hangi bacağına bağlı oldu yukarıda verilmişti. 

```sh
$ #define RASP_DIG_tr_LED_1 RPI_V2_GPIO_P1_37 
```

RPI_V2_GPIO_P1_37, bcm2835.h kütüphanesinde tanımlanmıştır. Bunu daha anlaşılır hale gelmesi için kendimiz bu ismi tanımlayacak başka bir isim tanımladık. 

```sh
     if (!bcm2835_init())
      return 1;
```
bcm2835 kütüphanesi bir sebepten doalyı çalışmıyor ise burada hata döndürülecektir. Bu hata yüksek ihtimalle GPIO’ların aynı anda kullanılması gibi sebeplerden olabilir veya memory hatası sık karşılaşılan problemlerdendir. Kütüphane, stabil bir kütüphane olduğundan dolayı eğer bir hata mesajı alıyorsanız yüksek ihtimalle sorun kodunuzdadır. 

```sh
bcm2835_gpio_fsel(RASP_DIG_tr_LED_1, BCM2835_GPIO_FSEL_OUTP);
```
Bu fonksiyon yardımı ile de Raspberry’nin 37. Bacağında olan LED’imizi çıkış olarak tanımlıyoruz. 

```sh
bcm2835_gpio_write(RASP_DIG_tr_LED_1, HIGH);
```
Yukarıdaki fonksiyon yardımıyla da PIN’imizi aktif veya pasif hale getirebiliyoruz. HIGH, konumunu LOW ile değiştirdiğimiz takdirde ise LED’imizin söndüğünü görebiliriz. 

```sh
bcm2835_gpio_write(RASP_DIG_tr_LED_1, LOW);
```
### C++ Programlama Dili ve Derlenmesi: ###

C++ dilini C diline benzer bir şekilde derleyebilir ve çalıştırabiliriz. Komut satırında “.cpp” uzantılı dosya yaratalım. 

```sh
$ sudo nano helloWorld.cpp 
```


```sh
$ #include <iostream>
int main(){
    std::cout<<"Hello World"<<std::endl;
    return 0;
} 
```
Dosyayı kayıt ettiğimizde aşağıdaki komut satırını yazarak programı derleyebiliriz. 
g++ -o helloWorld helloWorld.cpp
```sh
$ sudo g++ -o helloWorld helloWorld.cpp 
```

Programı çalıştırmak için ise aşağıdaki komut satırını terminalde girmemiz gereklidir:
```sh
$ sudo ./helloWorld 
```

Programın çıktısı olarak “Hello World” görmemiz gereklidir. Bu başlık altında çok temel olarak Linux/GNU üzerinde C/C++ programların derlenmesi ve çalıştırabilir dosyaların nasıl oluşturulacağı incelenmiştir. Bu bilgiler kullanılarak en azından temel olarak “nano” editöründe veya başka bir editörde C/C++ dillerinde yazdığımız kodları derleyip/çalıştırabiliriz. 

### QT ile Raspbian Üzerinde Çalışmak  ###

C++ ‘ın geniş kütüphane desteğini kullanarak Raspberry üzerinde çok farklı uygulamalar yapılabilir. Görüntü işleme, yapay zeka gibi birçok popüler yazılım araçlarında da C++ kullanılabilir. C++ ile modern GUI’ler de oluşturulabilir. Bu GUI’lerin hazırlanmasında QT kullanılabilir. QT’yi Raspberry’de çalıştırmanın diğer avantajı da GPIO’lara C++ üzerinden doğrudan erişilebilir ve bu GUI’de GPIO kontrollerini de yapabilirsiniz. 

```sh
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install qt5-default
$ sudo apt-get install qtcreator
```
Yukarıdaki komutlar ile QT programını Raspberry üzerinde çalışabilir hale getirebilirsiniz. Sonrasında QT programında bazır ayarlamalar yapmak durumundasınız. QT default olarak GCC compiler’ı ile gelmiyor. Bundan dolayı QT üzerinde derleyici olarak compiler seçmek zorundasınız. QT üzerinde aşağıdaki adımları takip ederek bu ayarları yapabilirsiniz. 
*Tools->Options->Build & Run* sekmesinde aşağıdaki adımları yapabilirsiniz:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/15.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/16.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/17.jpg)

Kaynak: http://pe2a.com/blog/2017/02/19/qt-ile-basit-masaustu-uygulamasi/

Bu ayarları yaptıktan sonra C++  kodunuzu derleyip çalıştırabilirsiniz. 

## Raspbian OS Üzerinde Python ile Çalışmak  ##

MedIOEx shield’inde birçok örneği C kodu ile anlattık ve kullanıcılar bu koddan yararlanarak kendi kütüphanelerini farklı platformlarda yazmayı başardı. MedIOEx’de birden fazla SPI entegresi olduğundan dolayı GPIO kontrolü MiniIOEx’e göre biraz daha zor olmaktaydı. MiniIOEx Digital Input ve Digital Output’lar Raspberry pinlerine doğrudan “pin-to-pin” bağlantısı olduğundan dolayı IO’ların kontrolü çok daha kolay. Bundan dolayı bu dokumanda da çoğu örneği Python üzerinden verdik. Bu bölümde ilk başta python kodlarımın nasıl çalıştırılacağını görecek sonrasında da MiniIOEx üzerinde bulunan RUN led’i ile ilgili çalışmalar gerçekleştireceğiz. 

Herhangi bir Linux/GNU türevinde Python kodunu çalıştırmak için herhangi bir IDE yüklenmesine gerek yoktur. Terminal ekranında “python” yazarsanız doğrudan python kodlarını çalıştırabilirsiniz. Raspbian işletim sisteminde de hazır olarak Python IDE’leri gelmektedir. Bu IDE’yi kullanılabileceğiniz gibi terminal ekranından da python kodunuzu yazabilirsiniz. Eğer Windows bir bilgisiyardan çalışmak istiyorsanız da Pycharm IDE’sini indirerek kodunuzu Raspbian üzerinde SSH üzerinden bağlanarak çalıştırabilirsiniz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/18.jpg)

Python kodları uzantısı “.py” dir. Bundan dolayı çalıştıracağımız python kodlarına “.py” uzantılı isimler vermemiz gerekmektedir. 
Aşağıda terminalde yazacağımız komut ile ilk python kodumuzu oluşturabiliriz.

**helloWorld.py**
```sh
def myPrint():
    for i in range(0,10):
        print("Hello World")
myPrint()

```
Python bir “script” dili olduğundan dolayı programı “compile” etmeye gerek yoktur. Doğrudan kodunuzu çalıştırabilir ve kodda bir herhangi bir neden ile hata var ise bu da yine “real time” da ortaya çıkmaktadır. 

Python ile dosyayı çalıştırmak için:
```sh
$ sudo python helloWorld.py
```

Python3 ile dosyayı çalıştırmak için:
```sh
$ sudo python3 helloWorld.py
```

Python, script tabanlı bir dil olduğundan kodu derlemeye gerek olmamaktadır. Doğrudan çalışabilen kod, çalışma zamanında derlenecek ve çıktı üretecektir. Eğer herhangi bir hata olmadı ise programınızda, program 10 adet “Hello World” çıktısı verecektir.

**led.py**
```sh
#miniIOEx RUN LED 
#update 08.2018
import RPi.GPIO as GPIO
import time

#definition DIGITAL OUPUT 
RASP_DIG_tr_LED_1 = 26 #Pin P1-37 
#init function
GPIO.setmode(GPIO.BCM) #bcm library
GPIO.setup(RASP_DIG_tr_LED_1,GPIO.OUT)

while 1:
    GPIO.output(RASP_DIG_tr_LED_1, GPIO.HIGH)  # will be ON
    time.sleep(0.25) #250ms
    GPIO.output(RASP_DIG_tr_LED_1, GPIO.LOW)  # will be OFF
    time.sleep(0.25) #250ms

```
Dosyayı çalıştırmak için:

```sh
$ sudo python3 led.py
```

Program çalıştığında RUN Led’inin 250ms aralıklarla yanıp söndüğü(flash) yaptığı görülecektir. RUN led’inin kullanıcıya bilgi vermesi açısından kullanabilirsiniz. Örnek olarak internetten veri kullanıcıya işlerin yolunda gitti belirtilmek isteniyorsa hızlı bir flash yapılabilir. Eğer herhangi bir veri iletişimi koptu ise yüksek aralıklarla flash yaptıralabilir.  
Yukarıdaki led.c programında programın nasıl çalıştığı ana hatlarıyla verilmişti. led.py dosyasında da benzer tanımlamalar ve benzer fonksiyonlar kullanılmıştır. Bu başlıkta C ve Python ile Raspberry üzerinde nasıl kod yazılıp derleneceği ile bilgili verildi. Fiziksel olarak Raspberry üzerindeki bir GPIO’nın nasıl kullanılacağı ile uygulama örneği paylaşıldı. 

### Tkinter ile Raspbian OS Üzerinde Çalışmak   ###

Raspberry üzerinde birçok amaçla GUI tasarlamak ve bunu gerçekleştirmek mümkün. Örnek olarak bir kahve makinesi yaptığınızı düşünün. Suyu ısıtıp, valfleri kontrol ederek sıcak suyu bardağa boşaltacak ve yine valf kontrolü ile sıcak suyun üstüne kahve boşaltacaksınız. Tabi bunları yaparken de ürününüzün modern görünmesini isterseniz ve tabiki daha fazla kullanılmasını isterseniz iyi bir GUI tasarımına ihtiyacınız var demektir. 


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/19.jpg)

Yukarıdaki resimdeki gibi bir kahve makinesi yapmak istersek Raspberry mükemmel bir seçim olabilir. Üzerindeki GPIO’lar ile ısıtma/boşaltma gibi kontakları kontrol edebiliriz. MiniIOEx üzerindeki Analog Input ile de sıcaklık/basınç gibi parametreleri okuyabiliriz/kontrol edebiliriz. Raspberry ve MiniIOEx üzerinde bulunan ethernet/wireless/3G ile de makine kullanılma istatistiklerini merkez sunuculara bildirebilir ve eğer kahve/süt boşaldıysa alarm oluşturabiliriz. Raspberry üzerindeki “Display” çıkışıyla da dokunmatik bir ekranda Tkinter veya QT’de tasarladığımız GUI’yi kullanıcıya gösterebiliriz. Raspberry bu gibi işleri rahatlıkla yapabilir. Hatta programınızı biraz daha geliştirebilir ve kullanıcının kimlik kartıyla kahve almasını sağlayabilirsiniz. Kullanıcı kartını bir yere tanıtır ve üzerindeki TAG MiniIOEx üzerinde bulunan RS232 haberleşme modülü sayesinde Raspberry’nin kullanabileceği bir bilgiye dönüşebilir. 
Bu bilgileri GUI tasarımı ile nasıl bitmiş proje yaratılır bunun örneğini vermek için kullandık. Raspbian işletim sistemlerinde Tkinter hazır yüklü olarak gelmektedir. Python ile çalışan birçok GUI tasarım aracı vardır ama kolay prototip oluşturabileceğiniz ve internette birçok kaynak bulabileceğiniz Tkinter modülü sayesinde yukarıda senaryosunu yazdığımız programı hayata geçirebilirsiniz.
Tkinter, Raspbian ile birlikte beraber gelir. Bundan dolayı herhangi bir yükleme işlemine gerek yoktur. Terminal ekranında “python3” komutu ile gelen ekranda aşağıdaki komutları yazdığımızda Tkinter test ekranı karşımıza gelecektir. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/20.jpg)

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/21.jpg)

İlerleyen bölümlerde Tkinter ile GPIO’ların beraber kullanıldığı örnekler verildi. 

### Python ile Grafik Çizdirme ve Loglama   ###

Python ile rahatlıkla projelerinizdeki input’ların grafiği çizdirilebilir. Analog Input veya buna bağlı Digital Input’ların grafiği çizdirilerek bu mail yoluyla gönderilebilir veya bu bilgiler loglanabilir. Bu başlık altında MiniIOEx’in gerilim değerinin loglanması ve bilgilerin grafiğe dönüştürülmesi ile ilgili temel projeler gerçekleştireceğiz. Özellikle endüstriyel uygulamalarda grafik çizdirilmesi hatanın bulunması açısından önemlidir. Sistemdeki bir hata grafik ile bulunabilir. Örnek olarak bir kontak geldiğinde analog input’dan gelen bir değer aşırı artıyorsa hata arama faaliyetini ilgili kontak üzerinde yoğunlaşabiliriz. Bu geçişler de genel olarak “trigger” olarak adlandırılabilir. 
Python ile grafik çizebilmek için “matplotlib” kütüphanesini kullanıyoruz. Bu kütüphaneyi indirmek için aşağıdaki komutu girmemiz yeterlidir:

```sh
$ sudo apt-get install python3-matplotlib
```
Kaynak: https://matplotlib.org/users/installing.html#installing-an-official-release
“matplotlib” kütüphanesini yükledikten sonra ilk örnek programı çalıştırabiliriz. 
Sonrasında komut satırında “test.py” dosyasını oluşturuyoruz. 

```sh
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.1)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()

ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()

```
![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/22.jpg)

Bu grafiği gerçek değerler ile de çizdirebiliriz. Bunun için kodda ufak tefek bazı değişiklikler yapmamız gerekecektir. 
Grafiğe hazırlanırken random değerler ile 10 adet verinin grafiğini çizdirelim. Sonrasında bu random değerler gerçek gerilim değerleri ile değişecek. 


```sh
import matplotlib.pyplot as plt
import random
import time
# Data for plotting
s = []
counter = 0
while counter < 10:

    s.append(random.random()*10)
    counter+=1
    time.sleep(0.10)
plt.plot(s)
plt.ylabel("Power In Voltage")
plt.show()
```
![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/23.jpg)

Python dosyası 10 adet random değer üretti ve bunun grafiğini çizdik. Analog Input için mcp3208 entegresi kullanıyoruz. Entegre ve Raspberry aralarında SPI haberleşme protokolü ile veri alış verişi sağlanıyor. Raspberry Pi bir master CPU olarak entegreden sorgulama yapıyor ve cevap alıyor.  Analog Input başlığında bu konu detaylıca işlenmiştir. Buradaki amacımız basit bir grafik oluşturmak olduğundan ayrıntıya girilmemiştir. 
Aşağıdaki programı “python3 powerIN.py” komutu ile çalıştırdığımızda 1sn süreyle Raspberry’nin gerilim grafiğini çizecektir. Raspberry üzerinde Analog Input okumak için gerekli PIN’ler yoktur. Bu bilgiyi MiniIOEx üzerindeki SPI entegresi yardımıyla almaktayız. Yani gerilim değerini MiniIOEx üzerindeki entegre okuyor ve SPI haberleşmesiyle Raspberry’nin anlayacağı BIT’e dönüştürüyor. 

```sh
import spidev
import matplotlib.pyplot as plt
import time

#analog input 6 -> Raspberry 5V
#analog input 7 -> Raspberry 24V
def readAI(ch):
        if 7 <= ch <= 0:
            raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

        cmd = 128  # 1000 0000
        cmd += 64  # 1100 0000
        cmd += ((ch & 0x07) << 3)
        ret = spi.xfer2([cmd, 0x0, 0x0])

        # get the 12b out of the return
        val = (ret[0] & 0x01) << 11  
        val |= ret[1] << 3           
        val |= ret[2] >> 5           

        return (val & 0x0FFF)  

def fADCconv(val):
    return val * 33.0 / 4095.0 #Voltage 

#definition SPI parameter
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629
#definition Analog Input Var. 

# Data for plotting
s = []
counter = 0
while counter < 10:

    s.append(fADCconv(readAI(6)))
    counter+=1
    time.sleep(0.10)
plt.plot(s)
plt.ylabel("Power In Voltage")
plt.show()

```
Grafikte dalgalanmalar büyük görünse de aslında max. 30mV civarında seyir ediyor. Bu değerin çok fazla oynanaması normaldir. Bunun nedeni Raspberry’ye gelen gerilimin MiniIOEx üzerindeki lineer regülatörden geçmesidir. Lineer regülatör gerilimi sabit tutmaktadır.  Aşağıdaki grafik daha farklı şekillerde “matplotlib” kütüphanesi yardımıyla da çizilebilir. Threshold değerlerinde farklı gösterimler yapılabilir veya çizgi lineer, logaritmik gibi eğimlerde seçilebilir. Şimdilik en basit haliyle çiziyoruz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/24.jpg)

Gelen değerin grafiğini çizdirdikten sonra değerlerin kayıt edilmesi ile ilgili birkaç program paylaşacağız. Değerlerin grafiğinin çizdirilmesiyle beraber hata durumlarında veya normal durumlarda bu değerlerin gerçek değerlerine erişmek de önemlidir. Bu değerler veritabanına kayıt edilebileceği gibi basit “.csv” formatlı dosyalar da kayıt edilebilir. Bu örnekte Raspberry Pi 5V gerilim değerinin 500ms aralıklarla “.csv” formatında kayıt edilmesi ile ilgili örnek uygulama paylaşılmıştır. 

```sh
import csv
import spidev
from time import sleep, strftime, time

#analog input 6 -> Raspberry 5V
#analog input 7 -> Raspberry 24V
def readAI(ch):
        if 7 <= ch <= 0:
            raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

        cmd = 128  # 1000 0000
        cmd += 64  # 1100 0000
        cmd += ((ch & 0x07) << 3)
        ret = spi.xfer2([cmd, 0x0, 0x0])

        # get the 12b out of the return
        val = (ret[0] & 0x01) << 11  
        val |= ret[1] << 3           
        val |= ret[2] >> 5           

        return (val & 0x0FFF)  

def fADCconv(val):
    return val * 33.0 / 4095.0 #Voltage 

#definition SPI parameter
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629
#definition Analog Input Var. 

counter  = 0
with open("/home/pi/Desktop/rpi_voltage.csv", "a") as log:
    while counter < 10:
        sleep(0.1)
        log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(readAI(6)),str(fADCconv(readAI(6)))))
        counter+=1
```
Programın çıktısı olarak 5V besleme geriliminin zamana bağlı digital ve gerilim değerleri .csv formatında kayıt edilmektedir. .csv uzantılı dosyayı Raspberry’de açmak isterseniz UTF-8 formatında açmanız gerekmektedir. Bunun dışında yazılar anlamsız görülecektir. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/25.jpg)

Yazacağınız basit script’ler ile de bu dosyaları mail ile de hata durumlarında kullanıcılara gönderebilirsiniz. 
Eğer MiniIOEx kullanmıyorsanız ve bu işlemleri gerçek değerler ile yapmak istiyorsanız gpiozero kütüphanesinde bulunan CPU sıcaklık değerini kullanabilirsiniz. Aşağıda bulunan kod ile CPU sıcaklık değerini izleyebilir ve yine üstte yer alan örnekler ile yine değerlerinizi “.csv” formatında kayıt edebilirsiniz. 


```sh
from gpiozero import CPUTemperature
from time import sleep, strftime, time

cpu = CPUTemperature()
temp = cpu.temperature

counter  = 0
while counter < 100:
    print(temp)
    counter+=1
    sleep(0.25)
```


## MiniIOEx için Ek Kütüphaneler ##
Raspberry IO’ların çalışabilmesi için bazı kütüphanelerin yüklenmesi gerekmektedir. Birçok alternatif IO kütüphanesi bulunmasına rağmen bu içerikte [C] programlama dili örneklerinde kullanacağımız bcm2835.h ve [PYTHON] programlama dili üzerindeki örnekler içinde SpiDev ve GPIO kütüphaneleri üzerinden gideceğimiz için bu kütüphanenin öncelikle yüklenmesi gerekmektedir. Çalışmalarımızda aşağıdaki kütüphaneleri yükleyeceğiz:

Kütüphane İsmi	Amaç
bcm2835	IO’ların kullanılması
Tkinter	GUI Tasarımı
Raspbian işletim sisteminde hazır gelmektedir.
Firebase-admin	WEB tabanlı proje geliştirmek
SQLite	Veritabanı kullanımı 
Spidev	Python SPI Kullanımı

*Bağlantılı kütüphaneler listelenmemiştir.* 

### C GPIO/SPI bcm2835 Kütüphanesini Kurulumu ###
Raspberry’de IO’ları (Digital Input / Output /Analog Input vs.) çalıştırabilmek için broadcom çipi üzerinde yazılan bir kütüphaneye ihtiyaç duyarız. Bu kütüphane önceden yazılmış olduğu için bize sadece kurulumu ve yüklemesi kalır. 
“bcm2835.h” kütüphanesinin kurulumu, MedIOEx shield internet sitesinde yer alan dokumanda anlatıldığı gibidir. Bu dokumanda da yine de bilgi olarak verilebilir. 
(Ayrıntılı bilgi: http://pe2a.com/MedIOEx/TR/MedIOEx-Baslangic-TR.html) 

Terminal ekranında aşağıdaki komutları sıralı bir biçimde girmek gereklidir. Bu işlemler yapıldığında internet bağlantısının olduğundan emin olmalısınız. 


```sh
pi@raspberrypi:~ $ sudo su
root@raspberrypi:/home/pi# mkdir medIOEx
root@raspberrypi:/home/pi# cd medIOEx
root@raspberrypi:/home/pi/medIOEx # git clone git://github.com/pe2a/MedIOEx.git
root@raspberrypi:/home/pi/medIOEx /MedIOEx# cd MedIOEx
root@raspberrypi:/home/pi/medIOEx /MedIOEx# tar zxvf bcm2835-1.50.tar.gz
root@raspberrypi:/home/pi/medIOEx /MedIOEx# cd bcm2835-1.50
root@raspberrypi:/home/pi/medIOEx /MedIOEx/bcm2835-1.50# ./configure
root@raspberrypi:/home/pi/medIOEx /MedIOEx/bcm2835-1.50# make
root@raspberrypi:/home/pi/medIOEx /MedIOEx/bcm2835-1.50# make check
root@raspberrypi:/home/pi/medIOEx /MedIOEx/bcm2835-1.50# make install
```

Bu yapılan işlemler sonucunda “bcm2835.h” kütüphanesi *“/usr/lib”* dizini altına yüklendiğinden Raspberry içerisinde herhangi bir dizinde bu kütüphaneyi kullanabilirsiniz. 

### 1.1.2	PYTHON SpiDev Kütüphanesini Kurulumu ###

bcm2835.h kütüphanesinin kurulması yukarıda anlatılmıştı. Eğer projenizde Python ile kod yazmak istiyorsanız ve SPI kullanacaksanız SpiDev kütüphanesini yüklemeniz gerekmektedir. Aşağıdaki adımları gerçekleştirerek SPI kütüphanesini yükleyebilirsiniz. 

**1.    Adım** [PYTHON] için SPI Haberleşme Ayarını Aktif Etme 
```sh
$sudo raspi-config 
INTERFACING Options -> SPI -> “YES”    -> REBOOT
```
**2.	Adım:** [PYTHON] SPIDEV modülünün Raspberry’ye Yüklenmesi
Terminalde aşağıdaki komutları girerek SPIDEV modülünün Raspberry’ye yüklenmesini sağlayabilirsiniz. 
```sh
$sudo apt-get update
$sudo apt-get upgrade
$sudo apt-get install python-dev python3-dev
$cd ~
$sudo git clone https://github.com/doceme/py-spidev.git
$cd py-spidev
$sudo make
$sudo make install
```
**3.	Adım:** [PYTHON] SPIDEV modülünün Testi

```sh
def readAI(ch):
        if 7 <= ch <= 0:
            raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

        cmd = 128  # 1000 0000
        cmd += 64  # 1100 0000
        cmd += ((ch & 0x07) << 3)
        ret = spi.xfer2([cmd, 0x0, 0x0])

        # get the 12b out of the return
        val = (ret[0] & 0x01) << 11  
        val |= ret[1] << 3           
        val |= ret[2] >> 5           

        return (val & 0x0FFF)  

```

Dosya yolunun olduğu dizinde terminalde aşağıdaki komutları girerek programı çalıştırabilirsiniz:


```sh
sudo chmod +x spi-test.py
sudo python3 spi-test.py
```

Sonrasında terminal ekranında MiniIOEx üzerindeki giriş gerilimlerini DIGITAL sayı ve gerilim olarak görebilirsiniz. 


### PYTHON GPIO Kütüphanesinin Kurulumu ### 

Terminal ekranında aşağıdaki komutları girerek bu kütüphaneyi yükleyebilirsiniz.
```sh
sudo apt-get install python-dev python-rpi.gpio 
```

Tüm bu işlemler bittikten sonra aşağıdaki kodu çalıştırarak MiniIOEx3G üzerindeki IO’lara ‘GUI’ ile ulaşabilirsiniz. Bu sayede kartınızı hemen test edebilirsiniz. Programı çalıştırmadan önce aşağıdaki kütüphanelerin yüklendiğinden emin olmanız gerekmektedir:

- GPIO
- Spidev
Eğer bu kütüphaneler yüklü ise aşağıdaki komutu terminal üzerinde çalıştırarak veya python compiler’ı kullanarak GUI’yi kullanabilirsiniz. 

Kodu çalıştırmak aşağıdaki adımları uygulamanız yeterlidir:
```sh
$sudo chmod +x test.py
$sudo python3 test.py
```
Kodu çalıştırdığınızda aşağıdaki gibi bir GUI ekranı karşılamaktadır:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/26.jpg)
*MiniIOEx3G GUI test Ekranı*
**Not**
*Kod revize edildiğinde GUI şekildeki gibi görünmeyebilir.*
Kontrol etmek istediğiniz Digital Çıkışları ‘textbox’ların içerisini ‘1’ yaptıktan  sonra ‘Submit’ tuşuna basarak kontrol edebilirsiniz. Bu sırada da Rölelerin ve Transistor Çıkışların LED’lerinin yandığını görebilirsiniz.  
GUI programın en güncel haline https://github.com/pe2a/MiniIOEx3G klasörünün altında erişebilirsiniz.  

### Raspbian OS Üzerine Firebase Kurulumu ###

Firebase, herhangi bir sunucu programlamaya gerek olmadan Google sunucuları üzerinde ve altyapı desteğinde dinamik bir veritabanı sunar. Bu veritabanına birçok Raspberry tabanlı veya başka IOT cihazlarınız güvenli bir protokolde bağlanabilir ve ilgili veriyi kullanabilir. Örnek olarak bir WEB sitesi uygulaması yapmak istiyorsunuz ve Raspberry’den aldığınız bu verileri bir WEB sunucusunda göstermek istiyorsunuz. Bunu bir sunucu ile yapmaya çalışırsanız sunucu ile ilgili birçok ayar yapmak zorunda ve her kullanıcı için ayrı uğraşmak durumundasınız. Buradaki sunucu programlama ise ayrı bir zor iştir. Her cihazdan veri almak ve bu verilerin çok hızlı bir şekilde işlenmesi, veritabanına kaydı gibi işlemler hem yorucu hem de zahmetli işlerdir. Firebase, bizi bu zor altyapı problemlerinden kurtarmakta ve bunu da hemen hemen bedavaya yapmaktadır. Herhangi bir veritabanı lisans ücreti veya işletim sistemi için ayrıca lisans ücreti ödemenize gerek kalmamaktadır. Google altyapısını kullandığından dolayı da veriler çok hızlı bir biçimde veritabanına işlenmektedir. 

Firebase fiyatları ilgili site üzerinden incelenebilir: https://firebase.google.com/pricing/

Firebase şu anda Raspberry’de sadece Python ile programlamaya destek vermektedir. Bundan dolayı işlenen konular Python üzerinden verilecektir. 

#### Firebase Python Kütüphanesi Yüklenmesi ####

Aşağıdaki komutları terminalde yazmamız gereklidir:

```sh
$sudo pip3 install pyrebase
```
Eğer *‘opentype’* hatası alırsanız aşağıdaki kütüphaneleri de kurmanız gerekecektir:

```sh
$pip3 install pyasn1
$pip3 install pyasn1-modules
$pip3 install –upgrade google-auth-oauthlib
```

Açık kaynak kodlu pyrebase kütüphanesini incelemek için aşağıdaki link incelenebilir:
https://github.com/thisbejim/Pyrebase

Bu aşamadan sonra herhangi bir uygulama oluşturup kütüphanenin yüklenip/yüklenmediği kontrol edilebilir. Konuyla alakalı örnekler sonraki konularda işlenecektir. 

Bu bölümde basit olarak bir Raspberry’yi nasıl kuracağımızı ve gerekli kütüphaneleri yükleyebileceğimizi öğrendik. Bu işlemlerin PLC/Gömülü PC’ye göre çok daha basit olduğunu hatırlatmak isterim. PLC’lerdeki IO atama gibi işlemlerin burada yazılımda hali hazırda rahatlıkla yapılabildiği ve bir GUI’nin çok kısa bir sürede hazırlanabildiği görülmektedir. PLC’lerde bu GUI’yi hazırlamak bile yüksek ihtimalle herhangi bir lisansın (licence price) konusu olabilir. Raspberry’de tüm bu işlemler ücretsizdir ve internet’de bu konularla ilgili yüzlerce örnek kod ve kaynak bulmak olasıdır. Raspberry aynı zamanda güçlü bir bilgisiyar olduğundan dolayı sahadan aldığınız verileri işlemek ve buna göre bir karar almak da oldukça kolaydır. İstenirse hiçbir ayrıca ücret gerektirmeden bu verilerin ‘cloud’a aktarılması da mümkündür. İlerleyen konularda da bununla ilgili basit örnekler paylaşılmıştır. 

# MiniIOEx Üzerinde Fiziksel Giriş/Çıkışların (Digital Input/Output) Kontrolü #

MiniIOEx’de 4 adet Digital Output ve 2 adet Digital Input mevcut bulunmaktadır. Bu Input/Output’lar ile ilgili örnekler verilecek ve nasıl kullanıldığı mevcut dokumanda anlatılacaktır. MiniIOEx, Digital Input ve Output’lar doğrudan Raspberry üzerinden sürülür. Yani herhangi bir haberleşme bağlantısı mevcut değildir. Digital Input/Output için aşağıdaki pinler kullanılmıştır:


| PIN İsmi  	| Raspberry GPIO Yeri | 
| --- | --- |
| Digital Input 1 	| 31 |
| Digital Input 2	| 33 |
| Digital Output Relay 1	| 35 |
| Digital Output Relay 2	| 36 |
| Digital Output Transistor 1	| 38 |
| Digital Output Transistor 2	| 40 |
| Digital Output RUN LED	| 37 |
	
Yukarıdaki tablodaki PIN’leri kullanarak kendi GPIO kütüphanenizi yazabilirsiniz. Bu dokumanda da ayrıntılı olarak bu PIN’lerin nasıl kullanılacağı ile örnekler verilmiştir. 

##Digital Input Kullanımı ##

MiniIOEx’de 2 adet Digital Input olduğundan söz etmiştik. Digital Input ile herhangi bir kontak’dan veri alabilirsiniz. Digital Input çalışma karakteristikleri aşağıda verilmiştir:


| Teknik Data  	| Digital Input |
| --- | --- |
| Konnektör Bağlantısı 	| 2 kablo |
| Digital Input Sayısı	| 2 |
| Nominal Gerilim	| 24V |
| “0” Sinyal Gerilimi	| 0..3.9V |
| “1” Sinyal Gerilimi 	| 4.2V..30V |
| Input Filter	| - |
| Konfigürasyon	| GPIO veya bcm28354 kütüphanesinin yüklenmesi |

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/27.jpg)
*MiniIOEx Digital Input Klemens No*

Buton veya yardımcı kontaktan çıkan sinyal bilgisini MiniIOEx 16 ve 18 No’lu klemenslere girebilirsiniz. 

Raspberry üzerinde 31 ve 33 No’lu pinlerin Digital Input için kullanıldığı yukarıda bahsedilmişti. Bu konuyla ilgili örnek yapalım. Eğer bir butonu (acil stop/start/stop vs.) MiniIOEx bağlarsanız aşağıdaki gibi bu butondan alınan veriyi kontrol edebilirsiniz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/28.jpg)
*MiniIOEx Digital Input Bağlantısı*

Yukarıdaki devreyi gerçekleştirerek GUI üzerinden Digital Input değişkeninin anahtar aç/kapa konumlarında değişip değişmediğine bakabilirsiniz. 

Aşağıdaki yazılım ile Digital Input’lara gelen kontakları izleyebilirsiniz. 

```sh
import RPi.GPIO as GPIO
import time

#definition GPIO
RASP_DIG_IN_1 = 6   #DI_1
RASP_DIG_IN_2 = 13  #DI_2

#init function
GPIO.setmode(GPIO.BCM) #bcm library
#for digital inputs
GPIO.setup(RASP_DIG_IN_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RASP_DIG_IN_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)

while 1:
    DI_In1 = not GPIO.input(RASP_DIG_IN_1)
    DI_In2 = not GPIO.input(RASP_DIG_IN_2)
    
    if  DI_In1:
        print(“DI_IN_1 : True”)
    if DI_In2:
        print(“DI_IN_2 : True”)
    time.sleep(1) #for holding time   
```
Yukarıdaki yazılım ile Digital Input kodunu çalıştırabilirsiniz. İlgili klemens girişlerine gerilim uyguladığınızda *“True”* ifadesinin komut satırında belireceğini görmelisiniz. 

## Digital Output Kullanımı ## 

MiniIOEx’de 4 adet Digital Output mevcut bulunmaktadır. Bununla sahadaki röle ve kontaktörleri anahtarlayabilirsiniz. 4 adet Digital Output’dan 2 adet röle ve 2 adet’de 24VDC çıkşlı transistörlerdir. Transistörlerin fazla akım çekmemesi için yük dirençleri koyulmuştur ve maksimum 80mA akım çekilmesine izin verilmiştir. Eğer daha fazla yük ihtiyacınız var ise MiniIOEX üzerindeki röleleri veya bu transistörlere bağlayacağınız harici röleleri kullanabilirsiniz. 
MiniIOEx üzerinde bulunan Digital Çıkışları aşağıdaki tabloda görebilirsiniz:


| Raspberry Pin Çıkışı	| MiniIOEx3G | 
| --- | --- |
| 35	| Digital Output Röle - 1 |
| 36	| Digital Output Röle - 2 |
| 37	| Digital Output RUN LED |
| 38	| Digital Output Transistor 2 |
| 40	| Digital Output Transistor 1 |


<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteICON.jpg" alt="drawing" width="35"/>
**Not**
MiniIOEx’i 24V ile beslediğiniz takdirde tüm Digital Output pinlerini kullanabilirsiniz. Eğer 5V USB ile doğrudan Raspberry üzerinden beslerseniz sadece Röle çıkışlarını kullanabilirsiniz. 

| Teknik Data  	| Digital Output | 
| --- | --- |
| Konnektör Bağlantısı |	2 kablo |
| Digital Output Röle | 	2ch |
| Digital Output Transistor 	| 2ch |
| Röle Kontak Akımı ve Gerilimi	| 1A,24VDC |
| Transistör Kontak Akımı ve Gerilimi	| 80mA, 24VDC |
| Konfigürasyon	| GPIO veya bcm28354 kütüphanesinin yüklenmesi |

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/29.jpg)
*Röle Datasheet Bilgileri*

Digital Input ve Digital Output kullanılarak aslıdan birçok örnek yapılabilir. Otomasyonun temeli Input ve Output’dur 😊 MiniIOEx ile birçok temel düzeyde otomasyon işlemleri gerçekleştirilebilir. Örnek olarak bir cihazdan/makineden RS485/RS232 üzerinden çalışma verisi alınıp merkez sunuculara gönderilebilir sonrasında da bu bilgiler ile cihaz çalıştırılabilir/durdurulabilir performans takip edilebilir vs. Dokumanın geneline baktığımızda da bunun gibi birçok örnek paylaşılmıştır. 

Aşağıdaki kodda **MiniIOEx3G** üzerindeki tüm **Digital Çıkışlar** kullanılmıştır. 

--asdasdasdasdaBOŞBOŞ******


<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/UYGICON.jpg" alt="drawing" width="35"/>
**Uygulama Örneği #1 – Start/Stop Butonu ile FAN Motoru Kontrolü:**

Aşağıda iki Digital Input ve bir adet Digital Output kullanarak oluşturabileceğimiz güzel bir örnek bulunmaktadır. ‘Start’ ve ‘Stop’ butonlarından veri alınarak ‘FAN’ çalıştırılmaktadır.  Aslında bu FAN büyük bir fan veya asansör motoru da gerçek hayatta olabilirdi. Aşağıdaki resimdeki gibi bu uygulamada küçük bir fan tercih edilmiş ve bu fan çıkışı transistor output çıkışına bağlanarak Transistor’in HIGH durumunda FAN çalıştırılmıştır. 

Bu uygulamada gerekli olan ekipmanlar:

-	1 Adet 24VDC FAN [24VDC 80mA]
-	1 Adet Start Butonu - Normally Open (NO)
-	1 Adet Stop Butonu – Normally Close (NC)
-	24VDC 30W Güç Kaynağı [Phoenix UNO Power tercih edilmiştir]
-	Raspberry Pi 3 
-	Class 10 16GB SD Kart [GPIO ve SpiDev kütüphanesi yüklenmesi]
Senaryo:
*Start butonuna 1sn basılırsa FAN motoru çalışsın; 1sn Stop butonuna basılırsa FAN Motoru dursun.*
Senaryo basit gibi görünse de aslında burada Raspberry ile çalışrken birçok öğrendiğimiz uygulamayı da beraber yapmış olacağız. İlk başta senaryoyu Python ile kodlayıp işin içine WEB de taşıyacağız ve biraz Javascript ekleyerek her yerden ulaşılabilir bir FAN motoru WEB sitesi tasarlayacağız. Böylelikle gerçek bir uygulamayı ‘0’ yazılım maliyeti ile (sunucu kullanım ücreti, Raspberry İşletim sistemi lisans ücreti, WEB ücreti, HMI ücreti vs. olmadan) bir uygulamayı ayağa kaldıracağız. Belki burada hatırlatmakta fayda var birçok PLC üreticisi verilerinizi WEB’e göndermek veya bir GUI uygulaması çalıştırmak için lisans ücreti istiyor. Yani siz bilgisiyar alıyorsunuz ama internete girmek için bilgisayar firmasına para ödemek zorunda kalıyorsunuz 😊 MiniIOEx veya ürettiğimiz diğer shield’lerin en büyük faydası zaten büyük sermayeleri olmayan otomasyon firmalarını bu gibi lisans ücretlerinden kurtarmak oldu. Yani HMI lisans parası yerine 1 adet MiniIOEx alabilir veya WEB lisans ücreti yerine onlarca MiniIOEx alabilirsiniz. Tabi eğer makine üretiyorsanız ürettiğiniz adet kadar bu lisans ücretlerini ödemek zorundasınız. 

Senaryoyu bir grafiğe dökecek olursak aşağıdaki gibi bir grafik elde edebiliriz. Bu grafiğe göre de programlama yapmamız gerekir:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/300.jpg)

Yukarıdaki grafikte de görüleceği üzere Start butonu veya Stop butonuna 1sn süreyle basıldığında FAN motorunun değeri yükselen veya düşen kenar olarak değişmesi gerekiyor. 1sn süresi aslında ‘digital filtre’imkanı da sağlıyor. Yani herhangi bir parazit yüzünden Start butonunun Xms enerjili kalması FAN motorunun harekete geçmesini sağlamıyor. Bu gibi filtreler yazılım uygulamasının donanım ile beraber çalışması açısından önemlidir. Analog Input konusunda da yine başka filtre uygulamalarından bahsedilecektir. 
Bağlantılarda aşağıdaki klemens numaraları kullanılmıştır:


| Klemens No |	Açıklama |
| --- | --- |
| 18 |	Digital Input - 1 | 
| 16 |	Digital Input - 2 |
| 10 | 	Transistor Output 1 |

*Bu uygulamada röle kullanılmamıştır. Bunun nedeni anahtarlanacak yükün yüksek akım gerektirmemesidir.*

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/30.jpg)
*Fan Motoru Çalıştırılması- 1*

Yukarıdaki şekildeki gibi kablolamaları yapabiliriz. FAN GND’si güç kaynağı GND’si ile kısa devre edilmiştir. Gerilimi ise transistor ucundan yazılım tarafından anahtarlanarak verilmiştir. Aşağıdaki resimde kablo uçları paylaşılmıştır:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/31.jpg)
*Fan Motoru Klemens Kablo*


```sh
import RPi.GPIO as GPIO
import time

#definition GPIO
RASP_DIG_IN_1 = 6 #START BUTTON
RASP_DIG_IN_2 = 13  #STOP BUTTON
RASP_DIG_tr_OUT_1 = 21 #TRANSISTOR Output 

#init function
GPIO.setmode(GPIO.BCM) #bcm library
#for digital inputs
GPIO.setup(RASP_DIG_IN_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RASP_DIG_IN_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RASP_DIG_tr_OUT_1,GPIO.OUT)
GPIO.setwarnings(False)

while 1:
    DI_In1 = not GPIO.input(RASP_DIG_IN_1)
    DI_In2 = not GPIO.input(RASP_DIG_IN_2)
    
    if  DI_In1:
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)

    if not DI_In2:
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)
    
    time.sleep(1) #for holding time   

```
Kodu inceleyecek olursak:

```sh
    DI_In1 = not GPIO.input(RASP_DIG_IN_1)
    DI_In2 = not GPIO.input(RASP_DIG_IN_2)
```

Buradaki kodun amacı Digital Input’larımız **PULL_UP** olduğu için Raspberry açılış anında buradaki butonlara basılmasa bile **PULL_UP** ’da olduğu için *1* geldiğini varsayıyor. Biz buradaki inputları *‘değil’*leyerek fiziksel değerine döndürüyoruz. 


```sh
if  DI_In1:
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)

if not DI_In2:
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)
```

Bu yapıda da Start butonuna basılıyor ve FAN motoru çalışmaya başlıyor. Bu çalışmanın kesilmesi için tek koşul : *Stop* butonuna 1sn süreyle basılmasıdır. *Stop* butonu Normally Close(NC) olduğundan dolayı sürekli Input değeri 1'dir. *Stop* butonuna basıldığında PIN kendini 0’a çekiyor. Kodun bunu anlaması için de aşağıdaki gibi fiziksel değişken koşuluna **not** ekliyoruz.
```sh
if not DI_In2:
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)
```
1sn basma ise sıkça kullanılan time.sleep yapısıyla yapıyoruz. Kod büyüdüğünde böyle bir yapı tüm programı bekleteceğinden ayrı thread’ler kullanmamız gerekecek ama ilk aşamada basit olarak bu yapıyı kullanabiliriz. Bu süreyi uzatırsak daha fazla zaman butona basılması gerekecek. 

```sh
    time.sleep(1) #for holding time   
```

### RASPBERRY REBOOT Edildikten Sonra Programın Otomatik Çalıştırılması ###

Yazdığımız otomasyon programlarını Raspberry ‘reboot’ ettikten sonra çalıştırmamız gerekiyor. Yani, Raspberry enerjisi gidip geldiğinde ‘button’ programımız gerekli ayarlamaları yaptığımızda çalışmaya başlayacak. Bunu yapmak oldukça kolaydır. Terminal ekranına girerek ilgili kodumuza çalışma haklarının hepsini vermemiz gerekiyor. Sonrasında da “rc.local” klasöründe dosya yolunu vererek ilgili kodun linkini vermemiz gerekiyor. Hepsi bu kadar :)

```sh
$ sudo chmod +x button.py
$ sudo nano /etc/rc.local
```
**“rc.local”** dosyasının içini açtıktan sonra programımızın PATH’ini girmemiz gerekiyor. Button.py dosyamız masaüstünde olduğu için ilgili PATH: /home/pi/Desktop . Program python3’de çalıştırılmasını istediğimiz içinde parametre olarak ‘python3’ giriyoruz. Raspberry, reboot edildikten sonra artık programımız her Raspberry başlangıcında otomatik olarak çalışacaktır. Yalnız program ‘while 1’ yani sonsuz döngüde çalıştığı için hiçbir şekilde durmayacaktır. Sadece ‘top’ komutu ile ilgili ‘process’i bulup ‘kill -6 “ProcessID”’ komutunu işlememiz gerekmektedir.  

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/32.jpg)
*Auto-Boot Çalıştırma*


Bu uygulamayı öğrendiğimiz konularla beraber daha fazla geliştireceğiz. Dokumanın başında verdiğimiz *‘serverless’* sunucusuz çalıştırma servislerinden **Firebase** kullanarak uygulamamızı internet üzerinden bir uygulama olarak kullanabileceğiz. 

## Uygulama Örneği #2 – Start/Stop Butonu ve WEB Referans Değer ile FAN Motoru Kontrolü ##

Bu uygulamada Start/Stop butonuna ek olarak WEB üzerinden referans bir değer geldiğinde de FAN motorunun çalışma bitinin değiştirilmesi konusu üzerinde duracağız. Bu uygulamada aşağıdaki kütüphanelerin yüklü olması gerekiyor:
-	GPIO
-	Firebase
Bu kütüphaneler yüklü ise uygulamayı ayağa kaldırabiliriz. Senaryomuzda işin içine WEB uygulamada gireceği için ufak tefek değişiklikler olacak. 
Senaryo:
*Start butonuna 1sn basılırsa veya WEB Start butonu aktif edilirse FAN motoru çalışsın; 1sn Stop butonuna basılırsa [VEYA] WEB Stop Butonu aktif edilirse FAN Motoru dursun.*

Firebase üzerinde **WEBSample** adında bir veritabanı ismi oluşturuyoruz ve bunların alt kümesi **“StartButton”** ve **“StopButton”** oluyor. Bu değerler WEB’den geldiği için de programımızı ona göre ayarlamamız gerekiyor. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/33.jpg)
*Firebase WEB Referans Değerleri*

WEB üzerinden gelecek StopButton’da Normalde Kapalı gibi bir özellik olmadığından dolayı bunu normal bir değişken gibi alabiliriz. Firebase’da kayıtlı olan değişkenlerimiz string olduğu için buna göre hareket etmemiz gereklidir. Doğrudan string olarak da kullanabilirsiniz veya int’a çevirebilirsiniz. Web Referansı değeri veya fiziksel buton değeri FAN motorunun çalışması için gerekli olduğundan bu iki değeri **‘OR’**luyoruz. 


```sh
if (DI_In1 or myConnect.WEB_REF_1 == '1'):
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)
        print("web ref_1")
                    #stop comes from firebase DB
if (not DI_In2 or myConnect.WEB_REF_2 == '1'):
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)
```

Yazılımımız şu anda WEB’den gelen değer ve fiziksel butondan gelen değerlere bağlı olarak çalışıyor. Programımı tekrardan çalıştırdığımızda da iki türlü de çalıştığını görebilirsiniz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/34.jpg)
*Firebase WEB Referans Değerleri*

Firebase console ekranından StarButton’ın değerini değiştirdiğimizde FAN motorunun dönmeye başladığını görebilirsiniz. Tabiki bu yapıyı değiştirip kullanıcıya göre atama da yapılabilir. Yani her kullanıcı kümesi FAN motorunu çalıştırmasın diye bir senaryo da eklenebilir ama bu dokumanın esas mantığından bizi uzaklaştıracağı için bu senaryolara girmiyoruz. 
Programımız artık bir WEB veritabanı üzerinden çalışmaya başlayacak. Bu da bize artık Raspberry’nin dışındaki bir dünyadan Raspberry’ye ulaşmamızı sağlayacak. Örnek olarak bu veritabanına gerekli servisler yazıldığında mobil uygulama üzerinden veya WEB uygulama üzerinden Raspberry’ye erişebilirsiniz. Bir sunucu üzerinden Raspberry’ye erişmek güvenlik zaafiyeti de doğurabilir. Sonuçta güvenlik ayarlamaları ve olası saldıralara karşı sunucunuzun güvenlik yapılandırmasını sizin yapmanız gerekiyor. Firebase gibi servislerde ise böyle bir sorun ile karşılaşma olasılığınız çok düşüktür. 

Aşağıda Firebase üzerinden de FAN motorunu kontrol edebileceğiniz uygulama mevcuttur. Burada Firebase üzerinden gelecek bazı parametrelere ihtiyaç bulunmaktadır. Firebase’e giriş yaptıktan sonra bu bilgileri ana sayfadan rahatlıkla alabilirsiniz. Yazdığınız uygulamalarda bu parametreleri kullanmanız gerekmektedir. 
Bu parametrelerin neler olduğu aşağıda belirtilmiştir:

```sh
myFirebaseConfig = {
              "apiKey": "",
              "authDomain": "",
              "databaseURL": "",
              "projectId": "",
              "storageBucket": "",
              "messagingSenderId": "",
        }
```

```sh
import RPi.GPIO as GPIO
import time
import spidev
import pyrebase

RASP_DIG_IN_1 = 6 #START BUTTON
RASP_DIG_IN_2 = 13  #STOP BUTTON
RASP_DIG_tr_OUT_1 = 21 #RPI PIN: 40

#init function
GPIO.setmode(GPIO.BCM) #bcm library
#for digital inputs
GPIO.setup(RASP_DIG_IN_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RASP_DIG_IN_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#transistor output definition
GPIO.setup(RASP_DIG_tr_OUT_1,GPIO.OUT)
GPIO.setwarnings(False)

#firebase connection 
class connectCloudPolly():
    
    def __init__(self,myConfig):
        
        self.myCloudConfig = myConfig
        self.cloud = pyrebase.initialize_app(self.myCloudConfig)
        self.db = self.cloud.database()
       
       
    
    def ReadButtonInf(self):
        self.WEB_REF_1 = self.db.child("/WEBSample/StartButton/").get().val()
        self.WEB_REF_2 = self.db.child("/WEBSample/StopButton/").get().val()
        
        print(bWEB_REF_1,bWEB_REF_2)
        
#firebase connection struct 
#you can easily get the values from firebase console
myFirebaseConfig = {
              "apiKey": "",
              "authDomain": "",
              "databaseURL": "",
              "projectId": "",
              "storageBucket": "",
              "messagingSenderId": "",
        }
#firebase connection
myConnect = connectCloudPolly(myFirebaseConfig)

while 1:
    DI_In1 = not GPIO.input(RASP_DIG_IN_1)
    DI_In2 = not GPIO.input(RASP_DIG_IN_2)
    
    myConnect.ReadButtonInf()
                #start comes from firebase DB
    if (DI_In1 or myConnect.WEB_REF_1 == '1'):
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.HIGH)
        print("web ref_1")
                    #stop comes from firebase DB
    if (not DI_In2 or myConnect.WEB_REF_2 == '1'):
        GPIO.output(RASP_DIG_tr_OUT_1, GPIO.LOW)
    
    time.sleep(1) #for holding time

```

# MiniIOEx3G Analog Giriş (Analog Input) Kontrolü #

MiniIOEx’de mcp3208-Analog Input entegresi bulunur. Bu entegre ile sahadan gerilim/akım bilgisini 12bit çözünürlüğünde almak ve Raspberry üzerinde bu verileri işlemek mümkündür. Raspberry ve ADC entegresi birbirleriyle SPI üzerinden haberleşmektedir. Raspberry 2 adet Chip Select barındırmaktadır. Bu bus hatlarında istenildiği gibi programlama yapılabilmektedir. ADC entegresi CS0’a bağlıdır. Default olarak SPI bus ‘disable’ edilmiştir. Kullanılacak kütüphaneye göre “raspi-config” veya manuel olarak “raspi-blacklist.conf” dosyası üzerinden bu enable/disable edilebilir. 

MCP3208 ADC entegresi ile saniyede ~75000 data almak mümkündür. 3.3V’da ADC entegresi ~63kSPS kapasitesine sahiptir. Bu değer üzerinden de SCLK değeri 24bits * 63 000 = 1.5MHz bir değer çıkmaktadır. 16 us’de ADC entegresi okuma/yazma yapabilmektedir. eğer bu kadar kısa aralıkta örnekleme almak istiyorsanız üzerinde işletim sistemi çalışan gömülü sistem platformları için sorun olabilir. Bundan dolayı Raspberry üzerindeki ADC programlarımızda ~1ms ‘delay’  ile verileri alma programın sürdürülebilirliği açısından doğru olacaktır. Konu ile ilgili kodumuzda ne gibi değişiklikler yapabiliriz örnekler verilecektir. 

Aşağıdaki tabloda Raspberry üzerindeki hangi PIN’lerin kullanıldığı verilmiştir:

| PIN İsmi  	| Raspberry GPIO Yeri | 
| --- | --- |
| Chip Select |	CS0 - 24 |
| SDO	| 19 |
| SDI	| 21 |
| SCLK	| 23 |
	
Tablodaki bu verilere göre harici bir SPI ADC haberleşme kütüphanesi de MiniIOEx için oluşturulabilir. ADC verilerini okuyabilmek için aşağıdaki adımlar takip edilmelidir:
-	SPI kütüphanesi yükleme 
-	Yüklenen kütüphaneye göre Raspberry SPI enable/disable 
-	Klemense kablo montajı veya giriş beslemelerin okunması 

Raspberry’de SPI kütüphaneleri kullanırken farklı yazılım kütüphanelerinde farklı konfigürasyon ayarları yapılması gerekmektedir. 

| Kütüphane İsmi	| SPI Enable / Disable | 
| --- | --- |
| bcm2835 (C) 	| Disable |
| Wiring Pi  (C) | 	Enable |
| SpiDev (Python) |	Disable |

Yukarıdaki kütüphaneleri kullandığımızda Raspberry’de de o gerekli ayarları yapmamız gerekmektedir. Yani eğer bcm2835 kütüphanesi kullanıyor isek **SPI -> Disable** olmalı. Aksi takdirde programınız ‘Compile Time’da bir hata almasa bile ‘Run Time’da ‘fatal error’ almanız muhtemeldir. 
Raspberry’nin yeni modellerinde *BCM2836* ve *BCM2837* chip’leri kullanılıyor. Bundan dolayı bcm2835 kütüphanesinin çalışmayacağını düşünmeyin. Kütüphane, *bcmXX* modelleri ile uyumlu çalışıyor. 


## MiniIOEx Analog Giriş Okuma ##

MiniIOEx üzerinde bulunan entegre ile sahadan 2 adet analog giriş alınabilir. MiniIOEx dahili olarak 5V ve 24V besleme taraflarındaki gerilimleri de okumaktadır. Sahadan gelecek gerilim değeri max. 33V olmalıdır. MiniIOEx’e 4-20mA değişken akım kaynağı bulunan sensörler de montaj edilebilir. Daha yüksek gerilimlere çıktığınızda Raspberry’nin veya MiniIOEx’in zarar görme ihtimaline karşı dikkatli olmak gerekmektedir. Aşağıdaki görselde MiniIOEx ve Raspberrya arasındaki Analog Input modeli anlatılmaktadır. Bu modelde de görüleceği gibi 5V ve 24V okunması MiniIOEx üzerinde bulunan gerilim bölücülerle gerçekleşmekte ve sahadan da MiniIOEx’in okuyabileceği 2 adet Analog Input girişi bulunmaktadır. MiniIOEx giriş gerilimlerini ilgili kütüphaneden okuyabilirsiniz ve işlemlerinizde kullanabilirsiniz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/35.jpg)
*MiniIOEx Analog Giriş*

Aşağıdaki tabloda sahadan gelecek analog verilerin girmesi gereken klemens numaraları bulunmaktadır. 


| Fiziksel Input | MiniIOEx Klemens No | 
| --- | --- |
| Analog Input 1 |	14 |
| Analog Input 2 |	12 |
| Analog Input GND |	13 |
| Analog Input GND |	11 |

MiniIOEx Analog Giriş modülünü aşağıdaki klemenslere kablo girişi yaparak kullanabilirsiniz:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/36.jpg)
*MiniIOEx Analog Input Klemens Numaraları*

Analog Input modülünü 4-20mA sensör girişi olarak kullanabilmek için aşağıdaki butonları **ON** yönüne doğru çekilmesi gerekmektedir. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/37.jpg)
*MiniIOEx 4-20mA Seçim Butonu ON yönüne doğru çekilecektir*

Sahada gördüğümüz uygulamalarda Raspberry’nin giriş gerilimini veya batarya gerilimi ölçme isteği bulunmaktaydı. Bundan dolayı 5V ve 24V güç giriş beslemelerini harici herhangi bir kablolamaya ihtiyaç duymadan doğrudan Raspberry üzerinden MiniIOEx üzerinden ölçebilirsiniz. 

<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteIcon.jpg" alt="drawing" width="35"/>
**Not**
24V veya 5V besleme kaynağınızdan herhangi bir uç alıp MiniIOEX konnektörüne girmenize gerek yoktur. Bu giriş beslemeleri dahili olarak MiniIOEx üzerinde ölçülmektedir. 

Örnek bir senaryo ile anlatmak gerekirse; sahada MiniIOEx’i batarya ile beslediniz ve batarya gerilimi düşüyor. Eğer bu gerilim hiç takip edilmez ise Raspberry kapandığında sadece bunu anlayabilirsiniz. Batarya gerilimini takip ettiğiniz takdirde ise batarya gerilimi düşmeye başladığında uyarı verebilir ve kritik seviyenin altına indiğinde ise Raspberry üzerinde çalışan tüm dosyaları kayıt ederek kapatabilirsiniz. 

Endüstride kullanılan sensörlerin genelde çıkışları *0-10V* ve *4-20mA*’dir. Yukarıda da bahsedildiği gibi batarya giriş gerilimlerin ölçülmesi için MiniIOEX 33V’a kadar müsaade ediyor. Bundan dolayı satın alacağınız Analog Çıkışlı sensörleri MiniIOEx ile rahatlıkla ölçebilirsiniz. 

Mikroişlemcilerde işlem yaparken herşeyin değeri **DİGİTAL** olarak ölçülür. Yani sensörlerin çıkışları gerilim olsa da bu ADC entegrelerine, çözünürlüğüne göre **DİGİTAL** değer olarak yansır.  Raspberry’de de yazdığımız fonksiyonlarda sahadan gelen gerilim bilgisini digital olarak ölçüyoruz. Bu gelen **DİGİTAL** değeri ise yazacağımız basit fonksiyonlar ile öncelikle gerilim/akım değerine sonra da sensörlerin anlamlı verisine (*Basınç, Sıcaklık, CO2*) bilgilere dönüştürebiliriz. 

Aşağıdaki tabloda *MiniIOEx Analog Input* okuma verisi için gerilim sınır değerleri ve bunlara karşılık gelen **DİGİTAL** değerler bulunmaktadır. 


| Analog Giriş Gerilimi Min. 	| Analog Digital Engtegre(ADC) Sayısal Değer |
| --- | --- |
| 0V	| 0 |


| Analog Giriş Gerilimi Max. 	| Analog Digital Engtegre(ADC) Sayısal Değer |
| --- | --- |
| 33V	| 4095 |

Buradan yola çıkarak yazılımda gerekli fonksiyonlar yazılabilir. Bu dokumanda sensör verisi nasıl okunur ve anlamlı değerlere çevrilir örneklerle anlatılacaktır. 

ADC entegresi MiniIOEx ile SPI üzerinden veri alışverişini sağlamaktadır. Bundan dolayı mcp3208 kütüphanesinde Raspberry SPI kütüphaneleri de kullanılmıştır. Bu kütüphanelerin nasıl kullanıldığı da farklı programlama dili örnekleriyle yine bu dokumanda paylaşılmıştır. MCP3208 entegresi 8 adet kanalı ölçmektedir. MiniIOEx’de bu kanalların sadece 4’ü kullanılmıştır. 

| Fiziksel Giriş	| Mcp3208 Kanal İsmi |
| --- | --- |
| Analog Input 1	| 0 .  |
| Analog Input 2	| 1 .  |
| Analog Input 3 (Raspberry Besleme - 5V) |	6. |
| Analog Input 4 (MiniIOEx Besleme - 24V) |	7. |


Yukarıdaki tabloda görüleceği gibi MCP3208 entegresinin 6. ve 7. Bacakları Raspberry üzerindeki gerilimleri ölçmek için kullanılmıştır. MiniIOEx konnektörlerine hiçbirşey bağlamasanız bile 24V veya 5V gerilim bağladıysanız Raspberry üzerindeki gerilimi görmeniz gerekmektedir.

Python’da yazılmış Analog Input test kodunu çalıştırdığınızda 6.kanalda yaklaşık ~620 değerlerini görmeniz gerekir. Bu değer yukarıdaki tabloda verilen Raspberry besleme giriş gerilimidir. Basit bir hesap ile bu digital değeri gerçek anlamlı bir değere dönüştürmek mümkündür. 

## Analog Giriş Okuma Fonksiyon Ayarlarının Yapılması ##

Aşağıdaki değerler MiniIOEx Analog Okuma fonksiyonları için sabit değerlerdir. Siz de kendi fonksiyonunuzu yazdığınızda aşağıdaki sınır değerlerini kullanabilirsiniz. 

-	Entegre’den Okunan Digital Değer (x), 
-	Max. 12bit ADC Digital Değer -> 4095 (2^12),
-	Max. Saha Giriş Gerilimi -> 33V .

Sonuç olarak Raspberry’nin beslendiği güç kaynağının gerilim değerini bulmak ister isek aşağıdaki denklemi çözmemiz gerekiyor:


-	*eq1.* Güç Kaynağı Giriş Gerilimi = (Okunan Digital Data(x) * Max.  Saha Giriş Gerilimi)/ (Max.Digital Data )
-	*eq2.* Güç Kaynağı Giriş Gerilimi =(620 * 33V)/(4095 ) = 4.996V 

MCP3208 entegresinden digital değer okumak için aşağıda kod bloğu paylaşılmış ve dokumanın ilerleyen başlıklarında ise bu değerin gerilim ve sensör datalarına çevirme işlemleri ayrıntılı olarak işlenmiştir.


```sh
def readAI(ch):
        if 7 <= ch <= 0:
            raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

        cmd = 128  # 1000 0000
        cmd += 64  # 1100 0000
        cmd += ((ch & 0x07) << 3)
        ret = spi.xfer2([cmd, 0x0, 0x0])

        # get the 12b out of the return
        val = (ret[0] & 0x01) << 11  
        val |= ret[1] << 3           
        val |= ret[2] >> 5           

        return (val & 0x0FFF)  
```
Yukarıda karşılığı verilen Python kodunun C dilinde yazılmış eşdeğeri aşağıdaki gibidir. Çalışmalarınızda hangi programlama dili ile çalışacaksanız ilgili kod bloğunu seçebilirsiniz.  

```sh
//AI reading channel val
int smallex_getVal(const int channel){
    char tbuf[3]; //transmitting values to mcp3208
    char rbuf[3]; //reading value from mcp3208
    
    int adc = 0;
    int adcDigNumber = 0;
    
    if(channel == 0){
        
        //ch0
        tbuf[0] = 0b00000110;
        tbuf[1] = 0b00000000;
        tbuf[2] = 0b00000000;
        
    }
    if(channel == 1){
        //ch1
        tbuf[0] = 0b00000110;
        tbuf[1] = 0b01000000;
        tbuf[2] = 0b00000000;  
    }
                    
    if(channel == 6){
        
        //ch6
        tbuf[0] = 0b00000111;
        tbuf[1] = 0b10000000;
        tbuf[2] = 0b00000000;
            
    }
    
    if(channel == 7){
        
        //ch7
        tbuf[0] = 0b00000111;
        tbuf[1] = 0b11000000;
        tbuf[2] = 0b00000000;
        
    }
    
    bcm2835_spi_transfernb(tbuf, rbuf,sizeof(tbuf));
    adcDigNumber = (rbuf[1] << 8) + rbuf[2];
    adcDigNumber &= 0xFFF;
    
    return adcDigNumber; //should be 0 - 4095
```

Bu fonksiyon bloğunu programınızda kullanabilirsiniz. Herhangi bir gerilim ölçüm aleti (multimetre) ile de bu değeri kontrol edebilirsiniz. 
5V hattında MiniIOEx üzerinde herhangi bir gerilim düşürücü eleman bulunmadığı için bu değer doğrudan Raspberry’nin beslendiği gerilimdir. 24V değerini ölçtüğünüzde bulunan gerilim değerine yaklaşık olarak 1.4V (0.7V * 2) eklemeniz gerekmektedir 24V hattında aşağıdaki köprü diyot olduğundan dolayı. Aşağıdaki resimde MiniIOEx güç besleme girişi köprü diyot bağlantısını görebilirsiniz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/38.jpg)

Bu yapılan hesaplarının benzerlerini sensörlerin çıkış gerilim değerlerinin anlamlı datalara dönüştürülmesinde de kullanabiliriz. Elimizde bir basınç sensörü olduğunu düşünelim. Basınç sensörünün değerleri belirtilmiş olur. Örnek bir basınç sensörü için aşağıdaki bilgiler ışığında bir örnek çözelim.


Basınç sensörü değerleri:
-	Basınç Min. Değer = 0 Bar
-	Basınç Max. Değer = 16 Bar

**Not**
Bu sensör değerleri sensörün çeşidine göre farklılık gösterebilir. Her basınç sensörü aynı başlangıç değerlerine sahip olmamaktadır.  

Bu ifadelere göre sensör gerilim çıkışını anlamlı sensör datasına dönüştürmek için aşağıdaki gibi formalize edebiliriz: 

### Analog Gerilim Çıkışlı Sensör Örneği: ###
Output  =(Input-0V) * ((Basınç Max.  - Basınç Min.)/(10V-0V )) + Basınç Min. 

Sensörden aşağıdaki değerlere geldiğini varsayar isek ilgili basınç değerlerini bulabiliriz. 

Input = 0V: 	Output=  (0V-0V) * ((16Bar  -(0)Bar )/(10V-0V )) + (0)Bar   = 0 Bar

Input = 6V: 	Output=  (6V-0V) * ((16Bar  -(0)Bar )/(10V-0V )) + (0)Bar   =  9.6 Bar

Input = 9.9V: 	Output =  (9.9V-0V) * ((16Bar  -(0)Bar )/(10V-0V )) + (0)Bar =  15.84 Bar


MiniIOEx, Analog Input modülüne girecek 33V modülün entegrede digital olarak 4095 değerini vereceğinden bahsetmiştik. Bu bilgiye göre aşağıdaki referans gerilim noktalarında ilgili digital değerleri hesaplanmıştır. 

0V   ->  0 
6V   -> 4095 * 6V/33V = 745 
10V -> 4095 * 10V/33V = 1241 

Yukarıdaki orantı orantıyı ADC/gerilim fonksiyonuna çevirmeye çalıştığımızda aşağıdaki gibi bir fonksiyona çevirebiliriz. 

```sh
def fADCconv(val):
    return val * 33.0 / 4095.0 #Voltage 
```

Bu fonksiyonun ürettiği değerler artık anlamlı gerilim datasıdır. val değeri, ADC’den gelen digital değerdir. return fonksiyonu ile de  val  değeri üzerinde basit bir çevirme işlemi uyguladık. Yukarıda yapılan çözümleri herhangi bir gerilim çıkışı veren sensör datası üzerinden uygulama yapmak da mümkündür. 24V ve 5V giriş beslemeleri bu basit fonksiyon ile ölçebilirsiniz. Sensör dataları okunurken aşağıdaki adımların yapılması sensör okumayı kolaylaştırır:

-	Entegreden okunan digital değer anlamlı gerilim değerine dönüştürülür
-	Anlamlı gerilim değeri sensörün min./max. sınırları çerçevesinde gerçek dataya dönüştürülür. 


Gerilim çıkışlı sensörlerin MiniIOEx’de kullanılması ile ilgili örnekler verildi. Bu başlık altında **“Akım Çıkışlı”** sensörlerin hesaplamasında uygulanacak yöntemlerden bahsedilecektir.

### Analog Akım Ölçüm Örneği ###

4-20mA veya 0-20mA akım çıkışlı sensörler genelde gerilim hattında gürültü bulunan sistemlerde kullanılır. Örnek olarak; güçlü bir pompaya sahip sistem çalışmaya başlarken sensör dataları üzerinde parazitler oluşturabilir. Eğer gerilim çıkışlı bir sensör tercih edilirse gerilimde oluşacak oynamalar daha fazla olacağı için gelen dataların ölçümünde sorun yaşanabilir. Bu dokumanda kablolaların yerleşimleri, seçilmesi gereken kablo ve tesisat bu dokumanın konusu olmadığından sadece hesaplamaların nasıl yapılacağı anlatılacaktır. 

Basınç sensörü sınır değerleri:
-	Basınç Min. Değer = 0 Bar
-	Basınç Max. Değer = 16Bar

Analog Akım Çıkışlı Sensör Ölçüm Örneği:
 
Output  =(Input-4mA) * ((Basınç Max.  - Basınç Min.)/(20mA-4mA )) + Basınç Min. 


Input = *0mA*: 	Output=  (0mA-4mA) * ((16Bar  -(0)Bar )/(20mA-4mA )) + (0)Bar   = 0 Bar


Input = *12mA*: 	Output=  (12mA-4mA) * ((16Bar  -(0)Bar )/(20mA-4mA)) + (0)Bar   =  8 Bar


Input = *20mA*: 	Output =  (20mA-4mA) * ((16Bar  -(0)Bar )/(20mA-4mA )) + (0)Bar =  16 Bar


### CO2 Sensörü İle Yapılmış Gerçek Bir Uygulama ###

Bu başlıkta “Siemens QPA2002” CO2 / Hava kalitesi sensöründen gelen veri işlenecektir. Böylelikle anlatılan işlemler gerçek bir sistem ile karşılaştırılacaktır. 

•	Test sırasında sensör ve MiniIOEX beslemesi 24V’dur. Gerekli kablolamalar da buna göre yapılmıştır. 
•	Sensör, gerilim çıkışlı (U1) 0-10V modeli tercih edilmiştir.
Siemens QPA2002 Sensör bilgileri:
*Min. CO2*  = (0) ppm
*Max. CO2* = 2000 ppm  
-	3 No’lu Pin : G
-	4 No’lu Pin : G0
-	5 No’lu Pin:  U1
U1 No’lu pin çıkışı sensör gerilim çıkışıdır. 
Sensörün çıkış gerilimini aşağıdaki gibi formalize edebiliriz:

Output  =(Input-0V) * ((CO2 ppm max.  - CO2ppm min.)/(10V-0V )) + CO2 ppm Min. 

Output  =(Input) * ((2000ppm - 0ppm)/(10V-0V )) + 0ppm

Yukarıdaki denkleme bağlı olarak da CO2 sensörünün fonksiyonunu aşağıdaki gibi gerçekleştirebiliriz:

```sh
def co2_sensor_converter(val):
    return val * 200.0
```

Sensör datası ile ilgili fonksiyon yazıldıktan sonra ise kodun tamamını yukarıdaki örneklerde de verildiği gibi gerçekleştirebiliriz. 

**Not:**
İç mekanlarda hava kalitesinin iyi olması için 1000ppm’i aşmaması önerilir. Siz de yazacağınız program bu değerlerle ilgili histerisiz eğrileri oluşturabilir ve buna göre havalandırma fanını *ON/OFF* kontrol edebilirsiniz.

Aşağıda bu sensör ile ilgili yazılmış örnek bir kod bloğu bulunmaktadır. CO2 sensörü, MiniIOEx J2:12 nolu pine takılmış ve GND’ler birbirine kısa devre yapılmıştır. Eğer hava kalitesi sensörünün içerisine üflerseniz de nefesinizdeki CO2 den dolayı sensörün ürettiği ‘ppm’ datasının değiştiğini görebilirsiniz. Üflemeden sonra bu değer artacaktır. 

```sh
import spidev
import time

#definition SPI parameter
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 7629
#definition Analog Input Var. 
AI_ANIN2 = 0 #J2, pin:12 and always GND is common with sensor
#definition co2 sensor data
co2SensorData = 0
#mcp3208 ADC
def readAI(ch):
        if 7 <= ch <= 0:
            raise Exception('MCP3208 channel must be 0-7: ' + str(ch))

        cmd = 128  # 1000 0000
        cmd += 64  # 1100 0000
        cmd += ((ch & 0x07) << 3)
        ret = spi.xfer2([cmd, 0x0, 0x0])

        # get the 12b out of the return
        val = (ret[0] & 0x01) << 11  
        val |= ret[1] << 3           
        val |= ret[2] >> 5           

        return (val & 0x0FFF)  

#converts digital number to voltage
def dig_vol_converter(val):
    return val*33.0/4095.0

#0 ppm -> 0V 2000ppm -> 10V
#Siemens QPA2002
#assume val is co2sensor voltage output : (val-0V) *[(2000ppm-0ppm / 10V-0V) + 0V]
def co2_sensor_converter(val):
    return val * 200
    
print('-' * 55)
# Main program loop.
while True:
    print('\n')
    print('{} | {} '.format('Sensor Voltage[V]','Sensor Data[ppm]'))
   
    # The read_adc function
    AI_ANIN2 = dig_vol_converter(readAI(1)) #Voltage
    #lets convert co2 value
    co2SensorData = round(co2_sensor_converter(AI_ANIN2),1) #ppm
    
    print('{:6f}  {:21f} '.format(AI_ANIN2,co2SensorData))
    time.sleep(1)
```

Şu ana kadar verilen örneklerin hepsi sensörlerin lineer olma koşulu ile ilgiliydi ama bazı sensörler lineer olmayabilir. Yani gerilim ve sensör değeri lineer orantılı olmayabilir. Bu tarz durumlarda sensör değerlerini kayıt ederek değerleri lineerleştirebiliriz. Değerleri kayıt ettikten sonra http://www.wolframalpha.com/  sitesinde hesaplayabiliriz. 

Bir örnekle bu durumu daha net açıklayabiliriz. Örnek değerler, **“Exploring Raspberry Pi, M. Derek, 2016”** kitabından alınmıştır. 
3925 digital değerine karşılık 10cm, 2790 digital değerine karşı 15cm geldiğini varsayalım. Burada değerlerde lineer bir azalma olmadığı görülüyor. Lineer olmayan bir denklemi ise Raspebrry üzerinde kullanamayız. Bundan dolayı bu değeri lineerleştirmeye yaklaştırmak için çeşitli teoremler üretilmiştir. (Marquardt-Levenberg) Wolfram programı bu değeri otomatik olarak lineerleştirecektir. Tek yapmamız gereken aşağıdaki denklem setini Wolfram programına yazmamız:

*exponential fit {3925,10}, {2790,15}, {2200,20}, {1755,25}, {1528,30},{1273,40}, {851,50}, {726,60}, {620,70}, {528,80}*

Bu program sonucunda aşağıdaki gibi bir grafik ve denklem elde edebiliriz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/39.jpg)

Eğer bu tarz bir nonlineer çıkışlı bir sensör setine sahip olursanız bu teoremden faydalanabilirsiniz. 

## Seri Port Kullanımı ve RS485/RS232 Protokolleri #

Seri haberleşme, telekom standartlarında belirtilmiş fiziksel kabuk üzerinde standartlarda belirtilmiş yazılım protokelleriyle çalışan ve çift taraflı veri iletişimine imkân veren bir haberleşme çeşididir. Endüstriyel sistemlerde seri haberleşme denilince genel olarak RS232 ve RS485 protokelleri akla gelir. MiniIOEx, RS232 ve RS485 fiziksel haberleşme seri yollarını destekler. RS-232 kısa mesafeli iletişim için tasarlanmış bir seri iletişim standardıdır. RX ve TX üzerinden iletilen bilgiler referans seviyesi olan GND’ye göre belirlenmektedir. RS-232 ile kısa mesafeli ve 115.2 Kbit/sn gibi hızlara ulaşılabilmektedir. Bu standart gürültülü ortamlar için uygun değildir. RS-232 sürücüleri birçok alıcıyı aynı anda sürebilecek şekilde tasarlanmamıştır.

UART (*Universal Asynchronous Receiver/Transmitter*) seri bus standart olarak Raspberry üzerinde iki kablo ile seri haberleşmeyi sağlar. cmdline.txt’de seri port değişkenleri görülebilir. Raspberry 3 ile beraber seri port ayarları “raspi-config”ekranında yapılabilir. Bu değişiklikler yapıldıktan sonra Raspberry yeniden başlatılmalıdır. Bu dokumanda bu ayarların nasıl yapılabileceği anlatılmıştır. Raspberry Pi üzerindeki Tx ve Rx pinleri seri haberleşmeden sorumludur. Başka bir seri port donanımı üzerinde bulunan bir cihaz ile raspberry kolaylıkla haberleşebilir.  Eğer Raspberry başka bir seri port cihazı ile haberleşecekse “console login” özelliği kaldırılmalıdır. Bu değişlikliklerden de bahsedilecektir. 

RS-485 daha uzun mesafelerde, gürültülü ortamlarda, daha yüksek hız gerektiren yerlerde, daha çok alıcı vericinin gerektiği yerlerde kullanılmak üzere geliştirilmiş bir seri iletim ortamıdır. MiniIOEx bu iki seri iletim yolunu da destekler. 
Aşağıda MiniIOEx üzerinde bulunan seri port pin tablosu paylaşılmıştır:
MiniIOEx Seri Port Pin Tablosu:


| Seri Port Pin | MiniIOEx Klemens No | 
| --- | --- |
| RS232RX	| 19 |
| RS232TX	| 20 |
| RS485B	| 19 |
| RS485A	| 20 |
| RS GND	| 17 |

Raspberry’de tek bir UART çıkışı olduğundan dolayı MiniIOEx’de 2 adet seri port converter kullanıyoruz: UART/RS232 ve UART/RS485. Bu iki converter’ı aynı anda kullanamadığımız ziçin seçim yapmamız gereklidir. Aşağıdaki gibi kullanacağınız seri port’a göre seçim yapabilirsiniz: RS485 için yukarı yönde switch’leri ileri itebilir, RS232 için diğer yönde seçim yapabilirsiniz. 


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/40.jpg)
*RS485 Seçimi*

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/41.jpg)
*RS232 Seçimi*

Seri port klemens uçları bir cihaza takılı iken seri port seçim butonları ile değişim yapmak: MiniIOex üzerindeki entegreleri bozabilir. Bundan dolayı hangi seri port seçimi yapılacaksa cihaza takılmadan önce butonların o yönde ayarlanması gereklidir. 

Terminal ekranında daha önceden de kullandığımız **“raspi-config”** komutunu terminale girmemiz gerekiyor. 

```sh
$raspi-config > Interfacing Options > Serial 
```

Bu menüye girildiğinde ise **“Serial”** menüsünde “enter”tuşuna basıldıktan sonra aşağıdaki adımların takip edilmesi gereklidir. 

**Login menüsünde Seri Port kullanımını > Kapalı (No) **

Bu menü eğer gözden kaçırılırsa seri port kullanan program çalışmaya başladığında hata verecektir. Bundan dolayı Login kullanımı için seri port’un kapalı olması gereklidir. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/42.jpg)
*Seri Port Kullanımı Login Shell*

**Seri Port Donanım Kullanımı -> Açık /(Yes)**

Raspberry seri port uçlarının programlanabilir hale getirmektedir. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/43.jpg)
*Seri Port Kullanımı Donanım*

Tüm işlemler bittiğinde ise aşağıdaki gibi bir ekranla karşılaşmamız gerekmektedir:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/44.jpg)
*Seri Port Kullanım Bilgileri*

Raspberry üzerinde çalışabilen “minicom” programı ile Raspberry’ye seri port üzerinden gelen değişkenleri görebilir veya bu program üzerinden herhangi bir referans verebilirsiniz. 

Minicom programı yüklemek istiyorsanız aşağıdaki adımları takip edebilirsiniz:

**1. Minicom Yükleme:**

```sh
$sudo apt-get install minicom 
```

**2. Minicom Programını Başlatma**
Eğer Raspberry Pi 3’den önce çıkmış bir Raspberry serisini kullanıyor iseniz port adresiniz: “ttyAMA0” olmalıdır. 

```sh
$sudo minicom -b 9600 -o -D /dev/ttyAMA0 
```

Raspberry Pi 3 ve sonrası için ise seri port “ttys0” olarak değişmiştir. Aşağıdaki komutu girmemiz gereklidir:

```sh
$sudo minicom -b 9600 -o -D /dev/ttyS0

```
Parametreye girilen 9600 sayısı baudrate hızıdır. Bu hızı standart hızlara göre değiştirebilirsiniz. Genelllikle bu değer 115200’de  de kullanılır. Bu işlemler sonrasında ise herhangi bir PC’den veya başka bir cihazdan seri port kullanarak Raspberry’ye veri gönderebilir veya veri alabilirsiniz.  Bu dokumanda örnek olarak RS485 kullanarak **“Entes MPR63 Enerji Analizörü”** vasıtasıyla veri alabildiğimizi uygulamalı örneklerle anlatacağız. 

## RS485 Üzerinden Entes Enerji Analizöründen Veri Okuma  ##

RS485 sayesinde birçok cihaza bağlanabilir ve bunlardan veri okuyabiliriz.  Raspberry ve MiniIOEx ile bu verileri 3G veya Ethernet/Wireless üzerinden merkeze gönderebilir, bu verilerin sayesinde IO’ları kullanarak eyleme geçebilir veya bu verileri yüksek çözünürlükte depolayabiliriz. Bu tarz bir işlem kolay gibi görünse de PLC veya gömülü PC’lerde oldukça yüksek maliyetler çıkmaktadır. 
Aşağıda sistemde kullandığımız topoloji gözükmektedir. Topolojide harici bir bilgisayar da gözükmektedir. Bilgisayarı kullanmamızdaki amaç RS485 fiziksel seri yolu üzerinden MODBUS RTU protokolü ile veri alış/verişi yaptığımız için bu verileri nasıl aldığımızı göstermektir. Yani enerji analizöründen veri alırken hangi sorgularla aslında bu verileri alıyoruz bunu harici bir bilgisayar üzerinden rahatlıkla görebileceğiz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/45.jpg)
*RS485 Cihaz Topoloji*

Yukarıdaki sistemde Bilgisiyar master/slave , MiniIOEx master ve Analizör slave ‘dir. RS485, *A* ve *B* uçları sistemde kısa devredir. Bilgisiyar’da kurulu olan **“Modbus Master”** ve **“Terminal v1.9b”** programları sayesinde Entes Analizör’den veri okumak için gitmesi gereken referans kodları görebiliyoruz. Tabi bunu yapmadan önce Analizör’ün hangi register’larında hangi bilgiler var bunları bilmemiz gereklidir. Bunu da Entes Analizör’ün analizör dokuman internet sayfasında bulunan **“Data Mapping”** dokümanından çıkartabiliriz.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/46.jpg)
*Entes Analizör Register Tablosu*

Buradaki tabloda görüldüğü gibi *cosq* değerleri *19,20,21* nolu register’larında yer almaktadır. (Register tablosunda ilk değerin 0’dan başladığı görülmektedir.) cosq değeri için çözünürlük 1000 olduğu için gelen değerin gerçek cosq değerinde olması için 1000’e bölünmesi gereklidir. Örnek olarak 999 değeri geldiğinde bu değerin cosq = 999/1000 = 0.99 olması gerekmektedir. Entes analizöre herhangi Akım/Gerilim uçları bağlanmadığı için arada faz farkı oluşmamakta ve bundan dolayı cosq = 1 değeri görmemiz gereklidir. Sahada uygulama yapıldığında bu dokuman kullanarak diğer bilgiler (gerilim, akım vs.) de alınabilir. 
Analizörü bilgisiyar ve MiniIOEx klemens uçlarına bağladığımızda veri okuma işlemlerine geçebiliriz. 


| MiniIOEx Klemens Ucu |MPBR63 Analizör Haberleşme Klemens Ucu | 
| --- | --- |
| RS485-B, 19	| RS485-B, 15 |
| RS485-A, 20	| RS485-A, 14 |

İlk olarak bilgisayarda kurulu olan **MODBUS MASTER** programında kaç adet register okumak istediğimizi, node/slave adresi gibi temel bilgileri yazmamız gerekiyor. Aşağıdaki ekran görüntüsünden de örnek bilgiler edinilebilir:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/47.jpg)
*HEX Formatında Analizör Sorgu ve Cevap*

Bilgisayarın gönderdiği sorgu : **01 03 00 00 1E C5 C2** şeklindedir. Bu sorguya göre ise Analizör uzun bir cevap vermiştir. Rx, bilgisiyarın gönderdiği sorgu; Tx ise analizörden gelen cevaptır. RS485 üzerinde sorgulamadan veri alınamaz. RS232 ile bu yönde de ayrılırlar. Bu uzun cevaplar aslında Analizörün ölçtüğü Gerilim/Akım/Frekans/Güç faktörü gibi parametrelerdir. Biz bu parametrelerden cosq’yu kullanacağımız için ilk başta Analizörün gönderdiği sorguyu inceleyelim. Analizör bize sıralı olarak 03 E8 cevaplarını göndermiştir. Bu cevap aslında HEX 0x3E8 ‘dir. Ondalık sayı sisteminde ise “1000” ile ifade edilir. Yani analizöre yaptığımız sorgu sonucunda cosq register’ında 1000 ifademiz ise 1000/1000 = 1 olarak ifade edilir. Eğer 999(0x3E7) değeri gelseydi 999 / 1000 = 0.99 olacaktı. Bu yapılan işlemler en temel düzeyde RS485 seri yolunda gerçekleşen olaylardır. Biz protokoller kullanarak bu işlemleri basit hale getiriyoruz. Eğer Raspberry’den bilgisiyar gibi bir sorgu yapmak istersek aşağıdaki kodu kullanabiliriz. Aşağıdaki kodda “python serial” kütüphanesi olduğu görülmektedir. Bu kütüphaneyi terminalde aşağıdaki komutu yazarak kurabilirsiniz.

```sh
$sudo apt-get install python-serial
```
Kütüphaneyi yükledikten sonra ilgili sorguyu aşağıdaki programı çalıştırarak gönderebiliriz. 

```sh
import os,time
import serial
      
ser = serial.Serial(
              
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
            )

ser.write(serial.to_bytes([0x01,0x03,0x00,0x00,0x00,0x1E,0xC5,0xC2]))

```

Analizörden veri almamız için analizöre ilgili parametreyi göndermemiz gerektiğini yukarıda belirtmiştik: 01 03 00 00 1E C5 C2 bu parametreyi seri port üzerinden Analizör’e gönderdiğimizde ise bize yine HEX olarak üzerindeki parametreleri döndürmektedir. Bunu da yine bilgisayar üzerinden **“Terminal v1.9b”** programı sayesinde görebilmekteyiz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/48.jpg)
*RS485 Sorgu ve Cevabı*

Yukarıdaki resimde, Analizör’e giden sorgu **( 01 03 00 00 1E C5 C2 )** ve analizörden gelen sorgu ve bu sorguya göre de analizörden gelen cevaplar yer almaktadır. Bu sorguda aslında çok da karışık değildir. Örnek olarak “01” Node adresini tanımlar; “1E”’de kaç adet register tanımlanmış onu gösterir. RS485 protokolünde ilk sorgu sonra da onun cevabı yer alır. RS485 seri port üzerinden Yazma ve Okuma ikisi senkronize bir şekilde sorgulanamaz. Bu durum hataya sebep verir. 
Bu temel kodu çalıştırdığımızda Analizör yukarıdaki gibi bir sonuç verecektir. Bu kodu ModbusRTU protokolü ile yazdığımızda parametrelerin anlaşılması, Check-Sum hesapları, CRC hesapları daha rahat olmaktadır. 
Raspberry’de çalışan birçok açık kaynaklı ModbusRTU kütüphanesi mevcut bulunmaktadır. İnternette bu konuyla ilgili birçok dokuman da bulunmaktadır. ModbusRTU, bir protokol olduğundan isterseniz bu protokolü siz de oluşturabilirsiniz ama yazılım gibi çoğu alanda da geçerli olan “tekerliği yeniden icat etme” ye burada da gerek yoktur.  Bu dokumanda “pymodbus” kütüphanesi kullanılmıştır. Pymodbus kütüphanesini aşağıdaki terminale komutu girerek yükleyebilirsiniz. 


```sh
$sudo pip install  -U pymodbus
```

**“pymodbus”** kütüphanesi yüklendiğinde ise ModbusRTU protokolünü kullanarak Analizörden sahadan aldığı parametreleri çekebiliriz. Buradaki örnekte kullanılan analizöre hiçbir gerilim veya akım kaynağı bağlanmamıştır. Bundan dolayı sadece “cosq” verisini sorgulayabileceğiz. “cosq” verisini alabilmek demek zaten diğer verilere de rahatlıkla ulaşılabileceği anlamına gelmektedir. Diğer bilgileri alabilmek için sadece doğru “register” adreslerini bilmek gereklidir. 


```sh
import serial
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
import time

client = ModbusClient(method = 'rtu', port = '/dev/ttyS0',baudrate = 9600,timeout = 1, parity = 'N')
client.connect()

while 1:

    try:
        result = client.read_holding_registers(0x00,40,unit = 0x01)
        #print(result.registers)
        print("cosqL1 : {}, cosqL2 : {}, cosqL3 : {}".format(result.registers[19]/1000.0,result.registers[20]/1000.0,result.registers[21]/1000.0))
    except:
        pass
    time.sleep(1)

```

Programın içerisindeki *read_holding_registers* kullanımı:

```sh
result = client.read_holding_registers(0x00,40,unit = 0x01)
```

Yukarıdaki yazılım örneğinde analizörün üzerindeki 0 ve 40. Register’lar arasındaki register’lar sorgulanıyor. Yukarıda da register tablosu verilmişti ve bu register’lar arasında birçok parametrenin olduğunu görmüştük. Analizörün haberleşme node “1” olduğu için “client.read_holding_registers” fonksiyonun  parametresine de “0x01” veya sadece “1” ID sorgu parametresini de ekliyoruz. Yani aslında unit ID’si 1 olan analizör, 0 ve 40. Registerlar arasındaki paramatrelerini göndermesini istiyoruz. Bu parametreler arasında agerilim, akım, cosq, enerji gibi değerler de mevcut. Eğer bu ID numaralı bir analizör yoksa *timeout*’da sistem bekleyecektir. 

Kodun çıktısı ise faz Aktif Güçlerindeki cosq’ların değeri olmaktadır. Eğer gerilim/akım gibi bilgiler alınacaksa ilgili Register tablosundan sorgulama yapılmalıdır. Cosq’ları Analizörden aldığımız diğer bilgiler vasıtasıyla da hesaplayabiliriz.

-	P = VIcosq  == cosq=P/VI
 
-	Örnek P = 3.4kW, V=400V, I=10A

-	Cosq = 3400W / (400Vx10A)

-	Cosq = 0.85

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/49.jpg)


Buradan cosq’yu *0.85* olarak hesaplayabiliriz. Tabiki cosq’nun her zaman 1’e yakın olmasını isteriz. Analizörden Gerilim, Akım, Aktif Güç değerlerini de alabildiğimiz için cosq’yu ve buna bağlı olarak açı hesaplarını yapabiliriz. Eğer sistemde cosq 1 olmuyorsa Reaktif Kullanım yüğzünden para cezası ödenebilir. Bundan dolayı güç faktörü hesaplarının takibinin iyi yapılması gerekmekte ve böyle bir durumda Reaktör veya Kapasite bankaları ile cosq’yu 1(>0.98) ’e çekmemiz gerekmektedir. Kullanıcı bilgilendirme gibi işlemleri Raspberry yüzünden rahatça yapılabilir. Yazacağınız koda birkaç satır ekleyerek mail atma, “push-in notification” gibi özellikleri ekleyebilirsiniz.  

Analizörden Tüketilen enerji ve Üretilen enerjiyi de görebilirsiniz. Eğer bir güneş santraliniz var ise Harcanan ve Üretilen Enerji bilgilerini de alabilir ve günlük/haftalık/aylık bazda veritabına kayıt edebilir ve sunucunuza MiniIOEx üzerindeki 3G module’i da kullanarak herhangi bir internet servis sağlayıcı olmaksızın verilerinizi gönderebilirsiniz. Enerji üretimi olduğunda Akım’ın işareti değişecektir. Buna dikklat edilmelidir. 

## RS485 Üzerinden Modbus RTU Protokolünü Kullanarak ABB Motor Sürücüsü Kontrolü  ##

MiniIOEx ile Analizörden veri okumayı rahatlıkla yapabildiğimizi bir önceki bölümde gördük. MiniIOEx endüstriyel bir geliştirme kartı olduğundan dolayı endüstriyel ortamlarda da kullanılması için tasarlandı. Endüstriyel ortamlar denilince de akla tabiki motor kontrolü ve uygulamaları ilk sıralarda geliyor. Bu uygulamamızda herhangi bir PWM üreterek motor kontrolünden ziyade motor sürücülerine RS485 üzerinden referans değerlerini vererek motor sürmeye çalışacağız. Bu çalışmada da yine RS485 kullanılacak. Bundan dolayı aşağıdaki kütüphanelerin yüklü olduğunu varsayıyoruz:
-	serial
-	pymodbus
Eğer bu kütüphaneleri yüklemediyseniz bir önceki örneğe bakarak yükleyebilirsiniz. “raspi-config” seri port ayarlarının açık olduğu kontrol edilmelidir. Buradaki amacımız motor sürücüsüne hız referansı vermek ve bu hızı Raspberry üzerinden kontrol etmek olacaktır. Bu çalışmada aşağıdaki ekipmanlar kullanılmıştır:

-	ABB ACH550 3P 400V 7.5kW Motor Sürücü
-	Siemens 2kW 3P 400V 1500rpm AC Motor 
-	Raspberry Pi 3 B+
-	MiniIOEx-3G 
-	Phoenix Contact UNO Power 230V/24V Güç Kaynağı

**Motorun ve sürücünün bağlantılarını deneyimli bir elektrik teknisyeni yardımıyla gerçekleştirin. 400V’da ölüm tehlikesi bulunduğu unutulmamalıdır.**

ABB Sürücünün motor parametrelerini ayarlarını gerçekleştirdikten sonra “Haberleşme Parametre” ayarlarını girmemiz gereklidir. İlgili parametre ayarı sürücü klavuzunda mevcuttur. Parametreleri ayarladıktan sonra, MiniIOEx’in RS485 uçlarını ABB Motor Sürücüsüne montajını gerçekleştiriyoruz. 
Terminal ekranında “abb.py” adında bir dosya oluşturuyoruz ve bu dosyada seri port ve IO işlemleri kullanılacağı için tüm hakları vermemiz gerekiyor. Terminalde yazacağımız “chmod +x abb.py” komutuyla bu hakları verebiliriz. Sürücünün motor bağlantıları ve haberleşme bağlantıları tamam ise ilgili yazılımımıza geçebiliriz. Sürücünün manuel sayfasını okuduğumuzda ilgili register’ları ediyoruz ve bu registerlarda ne bilgiler yer alıyor bunları kontrol etmemiz gerekiyor.  Sürücü tüketilen enerjiden, tasarruf edilen enerjiye kadar birçok bilgi verse de biz sadece aşağıdaki parametreleri kullanacağız:


-	Motor Hızı[rpm]
-	Motor Akımı[A]
-	Motor Gücü[W]
-	Sürücü DC Bara Gerilimi[V]
-	Sürücü Sıcaklığı [Celcius]

Bu değerleri ilgili registerları sorgulayarak alabiliriz. Örnek yazılımızda sadece Motor Hızı değişkenini kullandık. Koda bakılarak diğer bilgiler de alınabilir. Bu bilgilerden Motor Sıcaklığı parametresi önemlidir. Genelde motor sürücüleri belirli bir sıcaklıkta sadece belirli bir süre çalışabilir. İstemsiz duruşlar için bu değer sürekli kontrol edilmeli ve sıcaklık çok yüksek ise (çalışma sıcaklıklığı genellikle max. 400C )  sürücü bakıma alınabilir veya çevre koşulları değiştirilebilir. 
Analizör ile RS485 üzerinden veri okuduk ama herhangi bir veri analizör üzerine yazmamıştık. Bu örnekte Modbus üzerinden nasıl veri yazılacağı da bulunmakta. 

```sh
client = ModbusClient(method = 'rtu', port = '/dev/ttyS0',baudrate = 9600,timeout = 1, parity = 'N')
client.connect()

try:
    result = client.read_holding_registers(100,20,unit = 0x01)
    print("Motor Speed : {}".format(result.registers[2]))

```

Analizör üzerinde veri okuması yaparken ‘0’ register’ı sorgulamıştık ama ACH550 sürücü bize 100. Register’ından itibaren okuma yapabileceğimizi söylediğinden dolayı 100. register’dan itibaren 20 adetlik register’ın sorgulamasını yaptık. “.read_holding_registers” fonksiyonun geri dönüş değeri ‘result’ dizisinde yukarıda bahsedilen tüm değişkenler yer almaktadır. 100.register’da ise Hız Değişkeni olduğundan dolayı bundan sonraki sorgulamalarda result[0] bize anlık hız değişkenini verecektir. 
İlk sorgulamadan sonra değişkenlere bakarak motora ‘start’ verilip verilmeyeceği program tarafından karar verilir. Buradaki basit bir örnek olduğundan dolayı buı değişkenleri kontrol etmedik. Örnek olarak motorun başlangıç sıcaklığı, DC bara gerilimi kontrol edilebilir ve bu değerler istenilen değer aralıklarında değil ise motora start verilmemelidir. 

Programın genel akış diyagramı:
-	Motor ve sürücü parametrelerini oku
-	“Sürücü start” ilk koşulların referansı ver
-	“Sürücü start” 
-	Sürücü motor hız referansı gönderilmesi [Hz] tipinde 
-	Motor hız referansını arttır 
-	Motor hız referansını 0 Hz’e çek 
-	Sürücü start durumundan stop durumuna getir 

İlk aşamada motor ve sürücü parametrelerini okuduk. Şimdi ise sürücüye start vermemiz gerekiyor. Sürücü manuelinde aşağıdaki şekilde devreye alınabileceği belirtilmektedir. 

Analizör’de sadece okuma yaptığımızı burada ise yazma yapacağımızdan da bahsetmiştik. Aşağıdaki fonksiyonu kullanarak yaza işlemini gerçekleştirebiliriz:

```sh
result = client.write_registers(REGISTER_ADRESS,REGISTER_REF,unit = UNITID)
```

Bu fonksiyon sayesinde istediğimiz yazma işlemini gerçekleştirebiliriz. İlk önce 0. Register’daki Sürücü Start işlemini gerçekleştirmemiz sonrasında ise motora hız referansı göndermemiz gerekiyor. Tüm bunları **“write_registers”** fonksiyonu sayesinde yapabiliyoruz. 

Sürücü Start Bit Referans Değerleri İlk Durum:

| ACH550 Motor Sürücü Register Değeri[0]	| Bit Değeri |
| --- | --- |
| [0].1	| True |
| [0].2	| True |
| [0].3	| True |
| [0].4	| True |
| [0].5	| True |
| [0].6	| True |
| [0].7	| True |
| [0].10 | True |
| [0].0	| **False (Start Biti)** |

İlk olarak tabloda yer alan refaransların gönderilmesi gerekiyor. Referansları DECIMAL türden gönderdiğimiz için bu tablodaki yer alan değerin DECIMAL karşılığı 1278 ‘dir.

```sh
result = client.write_registers(0,1278,unit = 1)
```
Sonrasında ise Start Biti’ini True yaparak motor sürücüyü **“HABERLEŞME”** üzerinden çalışır hale getireceğiz. 

Sürücü Start Bit Referans Değerleri İkinci Durum:

| ACH550 Motor Sürücü Register Değeri[0]	| Bit Değeri |
| --- | --- |
| [0].1	| True |
| [0].2	| True |
| [0].3	| True |
| [0].4	| True |
| [0].5	| True |
| [0].6	| True |
| [0].7	| True |
| [0].10 | True |
| [0].0	| **False (Start Biti)** |

**[0].0** start bitinin değeri değiştiğinden dolayı register’a göndereceğimiz referans değeri artacaktır. 

```sh
result = client.write_registers(0,1279,unit = 1)
```

Bu referans değerinden sonra motor sürücü dışarıdan refarans almaya hazır hale gelecektir. Sürücü üzerinde de bir röle çekerek sürücü motor fanını açacaktır. İlk olarak 1279 değerini vermemiz istenmiyor. Bundan dolayı motor sürücüsünü kademeli olarak devreye aldık. Şimdi yeniden “write_registers” fonksiyonunu kullanarak motora hız referansını gönderelim. 

```sh
result = client.write_registers(1,speedRef,unit = 1)
```

ABB Motor Sürücü manuelinde 1 No’lu register’da “Hız Referansı” register’ının olduğunu belirtmektedir. “speedRef” değişkenini arttırarak motorun hızlanmasını sağlayabiliriz. AC Motor sürücünün hız referansı parametresi “Hz” olduğunu belirtmiştik. 

| Referans Değeri(Decimal) | Hz Karşılığı |
| --- | --- |
| 0	| 0 Hz |
| 10000	| 25Hz |
| 20000	| 50Hz |

*speedRef* değerini her cycle’da 10.000 arttırarak motorun hızlanmasını sağlıyoruz. 

```sh
myCounter = 5
speedRef = 0
    while myCounter:
        
        result = client.write_registers(1,speedRef,unit = 1)
        time.sleep(1)
        result = client.read_holding_registers(100,20,unit = 0x01)
        print("Motor Speed : {} ".format(result.registers[0]))
        myCounter = myCounter - 1 
        speedRef = speedRef + 10000
        time.sleep(10)
```
Programı çalıştırdığımızda aşağıdaki gibi hız değerlerini elde ediyoruz:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/50.jpg)

*ABB Sürücü Hız Referansı*


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/51.jpg)

*Tam Hızda Sürücü Kullanıcı Paneli [AUTO] Modda *

Yukarıdaki ekran görüntüsünde görüldüğü gibi Hız rpm cinsinden kademeli olarak artmış ve sonrasında kademeli olarak azalmıştır. Motor üzerindeki kaymadan dolayı maksimum 1476rpm’e yükselmiştir. Bölüm başında hedeflediğimiz gibi ABB sürücü hız referansı verilerek motor İLERİ yönde döndürülmüş ve durdurulmuştur. Bütün bunları PYTHON dilini kullanarak rahatlıkla yapabilmek mümkün. Program geliştirilerek çok güzel grafikler çıkartılabilir, WEB’e veriler gönderilebilir veya çeşitli durumlarda WEB’den program çalıştırılabilir. Tabiki bütün bunlar yapılırken motorun dönme kuvvetinden dolayı herhangi bir canlıya zarar verilebileceği unutulmamlı ve sadece yazılım ile değil donanım ile de motorun dönmesi istendiğinde durdurulacak tesisatların yapılması gerekmektedir. Aşağıda ABB ACH550 Motor sürücüsünü kontrol etmek için gerekli kodu bulabilirsiniz.

```sh
client.close()
```
Modbus haberleşmesi “.close()” fonksiyonu ile kapatılabilir. 

**abb.py**

```sh
import serial
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
import time

client = ModbusClient(method = 'rtu', port = '/dev/ttyS0',baudrate = 9600,timeout = 1, parity = 'N')
client.connect()

try:
    result = client.read_holding_registers(100,20,unit = 0x01)
    print("Motor Speed : {}".format(result.registers[2]))
    time.sleep(1)
    #start bit  0       
    result = client.write_registers(0,1278,unit = 1)
    time.sleep(1)
    #start bit  1
    result = client.write_registers(0,1279,unit = 1)
    time.sleep(1) 
    #after start operation 
    print("operation starts:")
    myCounter = 5
    speedRef = 0
    while myCounter:
        
        result = client.write_registers(1,speedRef,unit = 1)
        time.sleep(1)
        result = client.read_holding_registers(100,20,unit = 0x01)
        print("Motor Speed : {} ".format(result.registers[0]))
        myCounter = myCounter - 1 
        speedRef = speedRef + 10000
        time.sleep(10)
    #Stop Operation
    #speed ref will be 0 rpm
    time.sleep(5)
    result = client.write_registers(1,0,unit = 1)
    time.sleep(20)
    result = client.read_holding_registers(100,20,unit = 0x01)
    print("Motor Speed : {}".format(result.registers[0]))
    #driver start bit will be 0 and driver will stop
    result = client.write_registers(0,0,unit = 1)
    result = client.read_holding_registers(100,20,unit = 0x01)
    print("Motor Speed : {}".format(result.registers[0]))

except:
    pass
    
time.sleep(1)
client.close()

```

# 3G ve GPS Bağlantı Ayarları #

MiniIOEx’in en önemli ve temel özelliklerinden birisi 3G ve 4G haberleşmeye uyumlu bir yapıya sahip olmasıdır. Yani eğer Wireless ve Ethernet imkanı olmayan bir yerdeyseniz veya sahada çalışmalar gerçekleştiriliyorsa 3G ile data haberleşmesi en uygun yöntemdir. Bu haberleşme seri port üzerinden değil USB üzerinden gerçekleştiğinden dolayı da 3G’nin data alış-veriş kapasitesinden tam olarak yararlanılabilir. Bazı servis sağlayacılarının 3G modemleri endüstriyel sahada tam performans veremediklerinden dolayı MiniIOEx’e 3G uyumluluğu eklenmiştir. MiniIOEx-3G, Raspberry V2, V3, Zero cihazlarla uyumludur ve yazılım testleri Jessie ve sonrası işletim sistemleri üzerinde test edilmiştir.  Quectel 3G Module 14.4 Mbps downlink ve 5.76 Mbps uplink hizmeti sağlayabilir. Küçük ve modüler yapısından dolayı MiniIOEx-3G ile beraber projelerinizde rahatlıkla kullanılabilir.  Eğer MiniIOEx’i 3G modül ile beraber almadıysanız ileride planlarınız dahilinde sadece 3G modül siparişi vermeniz yeterli olacaktır. 
MiniIOEx-3G nerelerde kullanılabilir:

-	IOT uygulamaları,
-	HDMI üzerinden görüntü aktarma işlemler,
-	Başka bir PLC veya PC’den verilerin dışarı aktarılması,
-	Endüstriyel makinelerin uzaktan izlenmesi,
-	Real Time Data stream işlemleri,
-	Camera stream işlemleri vb.

MiniIOEx’in 24V ile beslenebiliyor olması endüstriyel ortamlar için oldukça faydalı bir özelliktir. 3G gibi çok fazla güç harcayan ve anlık darbe akımları çeken bir uygulama için de 24V besleme alternatifinin olması haberleşmenin devamlılığı açısından oldukça önemlidir. Bu konu ile ilgili birçok test ve çalışma gerçekleştirilmiştir. Aşağıda 2 adet osiloskop ekran görüntüsü paylaşılmıştır. Bunlardan ilki 3G modemin ilk internete bağlanmaya çalıştığındaki gerilim grafiğidir. Bu grafikte de görülebileceği gibi kırmızı kutu içerisinde kalan kısımda akıma bağlı olarak gerilim düşmesi görülmektedir. Bu gerilim düşmesini mümkün olan en düşük gerilimde tutulmaya çalışılmıştır. Modül 3.3V hassas besleme gerilimi ile çalıştığından dolayı herhangi ciddi bir gerilim düşmesinde modül kendisini resetlyerek çalışmamaktadır. Bundan dolayı modül beslemesinde lineer bir gerilim grafiği elde edilmeye çalışılmıştır. 


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/52.jpg)

*3G Modül Bağlantı Esnasında Akım Darbeleri Gerilim Grafiği*

Aşağıda verilen osiloskop ekran görüntüsünde de görüleceği gibi internete bağlandıktan sonra veri indirme/yükleme işleri olsa bile gerilim “steady state” karakteri göstermektedir. 


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/53.jpg)

*3G Bağlantıdan Sonraki Durumda Gerilim Grafiği*


Bu yapılan çalışmalar sonucunda MiniIOEx ve 3G modül senkronize verimli bir şekilde çalışmaktadır. İlerleyen başlıklarda 3G modülün devreye alma işlemleri gösterilmiştir. Bu işlemleri gerçekleştirebilmek için aşağıdaki tabloda yer alan ürünlere ihtiyaç vardır.
-	USB Kablo
-	Anten
-	Anten kablosu 

Bu ürünler, MiniIOEx-3G aldığınızda ürün paketi içerisinde yollanmaktadır. Harici bir malzeme  alınmasına gerek yoktur. 

## 3G Bağlantı Ayarları ##

Quectel 3G modülü aşağıdaki adımları kullanarak test edebiliriz:
1- Quectel modulün Shield üzerine takılması,
2- Sim kartının modül üzerine yerleştirilmesi,
3- Raspberry’nin Shield üzerine montajı,
4- USB kablonun Raspberry’ye montajı,
5- 3G antenin Quectel UC20 modulünün üzerine takılması.
Fiziksel olarak modülün ve Raspberry’nin montajı yapıldıktan sonra ilgili ‘script’ler çalıştırılarak 3G modül devreye alınabilir. 3G modül beklenildiği gibi internete bağlanma aşamasında yüksek bir akım kaynağına ihtiyaç duymaktadır. Eğer bu akım karşılanmadığında gerilim düşerek modül kendini resetliyor. Bu konuyla ilgili sahada ve lab. Testlerinde birçok araştırma/geliştirme yaptık. MiniIOEX ve benzeri 3G ürünlerimizde de bu gerilim regülatör yapımızı koruyarak 3G bağlantısının daha stabil hale gelmesini sağladık. 
6- İşletim sistemi üzerinde son güncel işletim sistemi çalıştırılması önerilir. Minicom programı, seri port soketlerinden alınan veriyi gösterir. RS232 ve USB bağlantısı için kullanabiliriz. SIM kartı ve Modül testleri için minicom oldukça kullanışlı bir programdır. Speedtest-cli programını ise cihazın internete bağlantı hızını test amacıyla kullanabilirsiniz.
İlgili örnekler, dokuman devamında verilmiştir.

-	sudo apt-get update
-	sudo apt-get minicom
-	sudo apt-get speedtest-cli
-	sudo apt-get rpi-update
-	sudo apt-get upgrade
-	sudo reboot
-	git clone git://github.com/pe2a/miniIOEx3G.git

Yükleme işlemleri bittikten sonra terminal açılır ve **lsusb** komutu işletilir. Bu komut o anda USB’ye bağlı cihazları gösterir. Eğer herhangi bir durum yoksa aşağıdaki gibi bir ekranla karşılaşmanız gerekir. Quectel’i göremiyorsak bunun nedeni Quectel UC20 modulü veya USB kablonun kendisinden olabilir. Quectel 3G modulünü terminal ekranından göremiyorsanız modulü takıp çıkartmanız yarar sağlayabilir. **Modül üzerinde montaj işlemleri yaparken enerjisiz çalışmaya özen gösterilmesi gerekmektedir.**

<font color="red">USB Kabloyu değiştirdikten sonra halen Quectel modulü USB üzerinden görülemiyorsa lütfen tarafımıza bildiriniz!</font>

