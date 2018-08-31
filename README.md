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

MiniIOEx-3G has standart **Metal Sheet** to be used in electrical panels and industrial fields. So, you can easily mount it your projects. MiniIOEx-3G has also industrial 2x12 push-in terminal. Because of this feature, you will not worry cable installation time and robustness. For the MiniIOEx Terminal, the reference ground for all inputs is the 0 V power contact. The wires can be connected without tools in the case of solid wires using a direct plug-in technique. 

MiniIOEx terminal features:

| Terminal Features	| Comment |
| ------------- | ------------- |
| Terminal Number	|2x12 |
| Nominal Voltage	| 300V |
| Nominal Current	| 8A |
| Resistance Voltage	| 2000V |
| Max. Cable Size	| 2.5mm2 |
| Working Temperature	| -40C   +105C |


## Who is For MiniIOEx-3G? ##

The Raspberry-based control solutions enable you to run any applications for vaious IOT platforms: building automation, urban automation, smart city applications to operate and monitoring. MiniIOEx significantly reduces hardware and software costs and there is also not any licence prices thanks to Raspberry Pi. 

- Building Automation,
- Urban Automation,
- IOT applications,
- End user,
- Energy Monitoring via seri port, 
- Ship automation,
- Machine Tools,
- Robotics in Handling, Production and Assembly,
- Handling and Assembly Technology,
- Railway applications, 
- AV and Media Technology,
-	Real time data stream,
-	Camera stream via 3G,
- Students/Engineers who aim to develop about Embedded Linux plaftorms. 


## What is in the box ? ##

If you just buy *MiniIOEx* without 3G module :

- MiniIOEx
- MiniIOEx Metal Sheet
- Sheet mount parts

If you buy  *MiniIOEx-3G* with **3G module** :

- MiniIOEx
- Quectel UC20 MiniPCI Express Module
- GPRS Antenna 
- GPRS Antenna Cable
- MiniIOEx Metal Sheet
- Sheet mount parts

## IO Handling ##

MiniIOEx has Digital Input, Digital Output and Analog Input functions for your IOT/IIOT applications. Digital IOs are directly connected Raspberry pin to pin and Analog Input is connected over SPI. So, you will use SPI functions to get Analog Input Data. 

At the below table, you can find which MiniIOEx pins are connected to Raspberry PINs. 

| IO  	| Raspberry GPIO Place |
| ------------- | ------------- |
| Digital Input 1 	| 31 |
| Digital Input 2	| 33 |
| Digital Output Relay 1	| 35 |
| Digital Output Relay 2	| 36 |
| Digital Output  Transistor 1	| 38 |
| Digital Output  Transistor 2	| 40 |
| Digital Output  *RUN* LED	| 37 |


## Digital Input 

We mentioned before MiniIOEx-3G has 2ch Digital Inputs. Digital Input on MiniIOEx has given characteristics at below table:

| Technical Data  	| Digital Input |
| --- | --- |
| Terminal Connection 	| 2 Wire |
| Digital Input Channel	| 2 |
| Nominal Voltage	| 24V |
| “0” Signal Voltage	| 0..3.9V |
| “1” Signal Voltage 	| 4.2V..30V |
| Input Filter	| - |
| Confituration	| GPIO or bcm2835 library install |

| IO  	| Raspberry GPIO Place |
| ------------- | ------------- |
| Digital Input 1 	| 31 |
| Digital Input 2	| 33 |


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/27.jpg)
*MiniIOEx Digital Input Terminal *

Terminal 16 and 18 is Digital Input connection point. You can easily mount your cable with **ground** on terminal. 

Sample connection of buttons:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/28.jpg)
*MiniIOEx Digital Input Connection*

Given in the example code, you can monitor your Digital contacts/switches/buttons etc.
*di_test.py*

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
You can run program with at below command. 

```sh
python3 di_test.py
```


## Digital Output ##

MiniIOEx-3G has 4ch Digital Outputs. 2ch relay and 2ch 24VDC transistor you can use. Load resistors are set up to allow the transistors to draw no more current and a maximum current of 80mA is allowed to be drawn. If you need more load, you can use the relays on MiniIOEX or external relays to connect these transistors.

You can view the Digital Outputs on the MiniIOEx in the following table:

| Raspberry Pi Pin 	| MiniIOEx3G | 
| --- | --- |
| 35	| Digital Output Relay - 1 |
| 36	| Digital Output Relay - 2 |
| 37	| Digital Output RUN LED |
| 38	| Digital Output Transistor 2 |
| 40	| Digital Output Transistor 1 |

<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteICON.jpg" alt="drawing" width="35"/>

**Important Note**

If you supply MiniIOEx with 24V, you can use all Digital Output pins. You can only use Relay outputs if you supply directly from Raspberry via 5V USB.

| Technical Data  	| Digital Output | 
| --- | --- |
| Terminal Connection |	2 kablo |
| Digital Output Relay | 	2ch |
| Digital Output Transistor 	| 2ch |
| Relay Switch Current and Volatge	| 1A,24VDC |
| Transistör Switch Current and Voltage	| 80mA, 24VDC |
| Configuration	| GPIO veya bcm28354 kütüphanesinin yüklenmesi |

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/29.jpg)
*Relay Datasheet Informations*

With MiniIOEx, many basic automation operations can be performed. For example, the data can be sent to the central servers from a device via RS485 / RS232 and then the device can be started / stopped / performance monitored with this information. When we look at the whole of document, many examples like this are shared.

Aşağıdaki kodda **MiniIOEx3G** üzerindeki tüm **Digital Çıkışlar** kullanılmıştır. 

## Analog Input ##

The *MiniIOEx-3G* has the *MCP3208* Analog Input integration. With this integration, it is possible to receive voltage / current information from the field at **12bit** resolution and process this data on Raspberry. Raspberry and ADC integration communicate with each other via SPI. Raspberry has 2 Chip Selects. These bus lines can be programmed as desired. The ADC integration is connected to CS0. By default, the SPI bus is 'disabled'. This can be enabled / disabled via "raspi-config" or manually via the "raspi-blacklist.conf" file, depending on the library to be used.

With the MCP3208 ADC integration it is possible to receive ~ 75000 data at the moment. At 3.3V, the ADC integration has ~ 63kSPS. From this value, the value of SCLK is 24bit * 63 000 = 1.5MHz. At 16 μs, the ADC integrate can read / write. If you want to take sampling in such a short interval, it might be a problem for embedded system platforms running on the operating system. Therefore, in our ADC programs on Raspberry ~ 1ms 'delay' data acquisition will be correct in terms of program sustainability. 

We will give some examples of what we can do in our code.

The table below shows which PINs are used on Raspberry:

| PIN Name  	| Raspberry GPIO Place | 
| --- | --- |
| Chip Select |	CS0 - 24 |
| SDO	| 19 |
| SDI	| 21 |
| SCLK	| 23 |
	
According to this table, an external SPI ADC communication library can also be created for MiniIOEx. The following steps must be followed to read the ADC data:
- Installing the SPI library
- Raspberry SPI enable / disable based on installed library
- Terminal cable installation or reading of input supplies

When using SPI libraries in Raspberry, different configuration settings need to be made in different software libraries.

| Library Name	| SPI Enable / Disable | 
| --- | --- |
| bcm2835 (C) 	| **Disable** |
| Wiring Pi  (C) | 	**Enable** |
| SpiDev (Python) |	**Enable** |

When we use the above libraries, we also need to make the necessary settings in Raspberry Pi. So, if you are using the bcm2835 library **SPI -> Disable** 
Otherwise your program will likely get 'fatal error' at 'Run Time' even if it does not get an error in 'Compile Time'. Raspberry's new models  have **BCM2836 ** or **BCM2837** chips are used. So do not think bcm2835's library will not work. The bcm2835 ibrary is compatible with  all bcmXX  models.


## MiniIOEx-3G Analog Input Read ##

MiniIOEx-3G can provide 2ch analog inputs can be received from the field. The MiniIOEx also reads the voltages on the 5V and 24V internal supply. The value of the field shall be max.**33.0V**. Sensors with a **4-20mA** variable current source can also be installed in the MiniIOEx-3G. Be careful with the possibility of damaging the Raspberry or MiniIOEx-3G when you are at higher voltages. 

In the following image, the Analog Input model between MiniIOEx-3G and Raspberry Pi integration is explained. As seen in this model, the 5V and 24V readings are carried out with the voltage divider on the MiniIOEx and there are 2ch Analog Input inputs that MiniIOEx-3G can read from the field. You can read MiniIOEx-3G input voltages from the relevant library and use them in your operations.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/35.jpg)
*MiniIOEx Analog Input*

The following table contains the terminal numbers for the analog data to be input from the field. 

| Physical Input | MiniIOEx-3G Terminal No | 
| --- | --- |
| Analog Input 1 |	14 |
| Analog Input 2 |	12 |
| Analog Input GND |	13 |
| Analog Input GND |	11 |

You can use the MiniIOEx-3G Analogue Input Module by wiring the following terminals:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/36.jpg)
*MiniIOEx Analog Input Terminal Number*

**IMPORTANT NOTE**
To use the analog input module as a 4-20mA sensor input, the following buttons must be pulled in the direction of ** ON **.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/37.jpg)
*MiniIOEx 4-20mA Selection Button will be pulled in the direction of ON*

In the applications we saw on the field, there was a request to measure Raspberry's input voltage or battery voltage. Therefore, you can measure 5V and 24V power input supplies directly from Raspberry via MiniIOEx without any external cabling.

<img src="https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/myNoteIcon.jpg" alt="drawing" width="35"/>

**Important Note**
There is no need to take any end from your 24V or 5V supply source and enter the MiniIOEx connector. These input feeds are measured internally on MiniIOEx.

To describe with a sample scenario; You feed the MiniIOEx with the battery and the battery voltage is dropping. If this voltage is never tracked, you can only understand it when Raspberry is shut down. If you follow the battery voltage, you may be warned when the battery voltage begins to fall and when it drops below the critical level, you can turn off all files running on the Raspberry.

Sensors used in industrial applications generally have * 0-10V * and * 4-20mA * outputs. As mentioned above, the MiniIOEx allows up to 33V . So you can use these sensors with MiniIOEx you can easily measure.

Everything is measured ** DIGITAL ** when operating in microprocessors. That is, although the outputs of the sensors are voltage, they are reflected in the ADC integrations as ** DIGITAL ** according to the resolution. In MiniIOEx, we also digitally measure the voltage information from the field. If this incoming ** DIGITAL ** value is written we can write simple functions to convert real sensor value. 

The following table shows the voltage limit values for the MiniIOEx Analog Input * read data and the corresponding ** DIGITAL ** values.

| Analog Input Voltage Min. 	| Analog/Digital Circuit(ADC) Min. Digital Value |
| --- | --- |
| 0V	| 0 |


| Analog Input Voltage Max. 	| Analog/Digital Circuit(ADC) Max. Digital Value |
| --- | --- |
| 33.0V	| 4095 |

From there, the necessary functions can be written in the software. In this document, how to read the sensor data and translate it into meaningful values will be explained with examples.

The ADC circuit of MiniIOEx-3G provides data exchange via SPI. Therefore, Raspberry Pi SPI libraries are also used to read from MCP3208. How these libraries are used is also shared in this document with different programming language examples. The MCP3208 circuit 8 channels. Only 4 of these channels are used in MiniIOEx.

| Physical Input	| MCP3208 Channel Name |
| --- | --- |
| Analog Input 1	| 0 .  |
| Analog Input 2	| 1 .  |
| Analog Input 3 (Raspberry Pi Power In - 5V) |	6. |
| Analog Input 4 (MiniIOEx-3G Power In - 24V) |	7. |

As shown in the table above, the 6th and 7th legs of the MCP3208 circuit are used to measure the voltages on the Raspberry Pi and MiniIOEx-3G. When you run the Analog Input test code written in Python, you should see values of ~ 620 on channel 6. This value is the Raspberry Pi feed input voltage given in the above table. With a simple calculator it is possible to transform this digital value into a truly meaningful value.

## Reading Analog Input Value from MiniIOEx-3G ##

The following values are fixed values for MiniIOEx Analogue Reading functions. When you write your own function, you can use the following limit values.

- Digital value read from the Entire (x),
- Max. 12bit ADC Digital Value -> 4095 (2 ^ 12),
- Max. Field Input Voltage -> 33V.

As a result, if we want to find the voltage value of the power supply supplied by Raspberry, we have to solve the following equation:


- * eq1. * Power Supply Input Voltage = (Digital Data (x) * Max Field Input Voltage) / (Max.Digital Data)
- * eq2. * Power Supply Input Voltage = (620 * 33V) / (4095) = 4.996V

In order to read the digital value from the MCP3208 integration, the code block below is shared and the conversion of this value to voltage and sensor data is detailed in the headers of the document. 

**Important Note**
Since the Python library is used, Raspi-Config -> Interfacing Options -> SPI * enable * is required.


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

The equivalence of the above Python code written in C language is as follows. You can select the code block for which you want to work with the programming language in your work.

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

You can use this function block in your program. You can also check this value with any voltage meter (multimeter).
Since there is no voltage dropping element on the MiniIOEx in the 5V line, this value is the voltage that Raspberry feeds directly. However, you need to add approximately 1.4V (0.7V * 2) to the voltage value that you measure the 24V value because the following bridge diode is on the 24V line. In the illustration below you can see the MiniIOEx-3G power supply input bridge diode connection.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/38.jpg)

## Seri Port ##

Serial communication is a type of communication that operates on software protocols specified in the standard on the physical shell specified in the telecom standards and allows for bi-directional data communication. In industrial systems, RS232 and RS485 protocols generally come to mind in terms of serial communication. MiniIOEx supports RS232 and RS485 physical communication serial paths. RS-232 is a serial communication standard designed for short distance communications. The information transmitted via RX and TX is determined according to the reference level GND. With RS-232, short distances and speeds of 115.2 Kbit / s can be achieved. This standard is not suitable for noisy environments. RS-232 drives are not designed to be able to sustain many receivers at the same time.

UART (*Universal Asynchronous Receiver / Transmitter*) serial bus provides serial communication with two cables on Raspberry as standard. With Raspberry 3, serial port settings can be made on the "raspi-config" screen. Raspberry Pi should be restarted after these changes are made. This document explains how to make these settings. Tx and Rx pins on Raspberry Pi are responsible for serial communication. Raspberry can easily communicate with a device on another serial port hardware. If Raspberry will communicate with another serial port device, "console login" feature should be removed. These changes will also be mentioned.

The RS-485 is a serial transmission developed for use at longer distances, in noisy environments, where higher speeds are required. MiniIOEx-3G also supports these two serial transmission routes.

The serial port PIN table on the MiniIOEx is shared below.

MiniIOEx Seri Port Pin table is given at below:

| Seri Port Pin | MiniIOEx-3G Terminal No | 
| --- | --- |
| RS232RX	| 19 |
| RS232TX	| 20 |
| RS485B	| 19 |
| RS485A	| 20 |
| RS GND	| 17 |

Raspberry’de tek bir UART çıkışı olduğundan dolayı MiniIOEx’de 2 adet seri port converter kullanıyoruz: UART/RS232 ve UART/RS485. Bu iki converter’ı aynı anda kullanamadığımız ziçin seçim yapmamız gereklidir. Aşağıdaki gibi kullanacağınız seri port’a göre seçim yapabilirsiniz: RS485 için yukarı yönde switch’leri ileri itebilir, RS232 için diğer yönde seçim yapabilirsiniz. 

Since Raspberry has a single UART output, we use serial port converters in MiniIOEx: UART / RS232 and UART / RS485. You can control a button on MiniIoEx and you can choose which serial port can be used. 

If we can not use these two converters at the same time, we have to make a choice. You can choose according to the serial port you will use as follows: For RS485, you can push upwards the switches, for RS232 you can choose the other direction.

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


## 3G / GPS ##

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

<span style="color:blue">USB Kabloyu değiştirdikten sonra halen Quectel modulü USB üzerinden görülemiyorsa lütfen tarafımıza bildiriniz! text</span>

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/54.jpg)

*Ekranda görülen diğer USB portları kablosuz klavye/mouse veya taşınabilir USB disk olabilir.*

Fiziksel olarak USB bağlı olduğuna göre minicom üzerinde yapılacak setup ayarları ile ATkomutları modüle gönderebiliriz. Minicom ayrı bir terminalde açılarak aşağıdaki adresten miniIOEx-3G-test.py dosyası çalıştırılarak AT komutları cevapları görülebilir. Bu cevaplar aşağıda açıklanacaktır. AT komutları 3G modül ile haberleşmeden kullanılır. Bu komutlar ile cihaz üzerindeki bilgilerin sorgulanabileceği gibi SMS, Arama gibi özellikler de bu komutlar sayesinde gerçekleştirilebilir.


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/55.jpg)

Çalıştırılan python scripti sonrasında minicom ekranında yukarıdaki gibi bir çıktı elde edilir. Kırmızı blok içine alınmış script’lerin açıklaması aşağıda verilmiştir.

1-) Quectel cihaz seri no numarası -> **ATI**

2-) Cihaz üzerinde Sim Kilidi ile ilgili bir sıkıntı yoksa Sim kartının kullanıma hazır olduğunu belirtir. Sim kartı yeni aldı iseniz herhangi bir cep telefonunda Sim kartı PIN özelliğini devreden çıkartabilirsiniz: **AT+CPIN?**

3-) Şebekenin hazır olup olmadığını belirtir. Eğer şebeke hazır değil ise CME Error hatası döndürür ve ekteki dokumandan hangi hata olduğunu inceleyebilirsiniz: **AT+CREG?**

4-) Şebekenin çekim kapasitesidir. Antenin kalitesi, baz istasyonun yakınlığı ve çevresel faktörlere göre bu oran değişir. 30‘un aşağısı kabul edilebilir değerdir. 99,99 şebeke çekiminin olmadığını gösterir: **AT+CSQ**

5-) Kart üzerindeki SIM kartının operatörünü gösterir. Testler sırasında Vodafone SIM kartı kullanılmıştır. Türk Telekom veya Turkcell‘de IOT uygunluğu olan SIM kartı üretmektedir. Eğer burada SIM kartı yeri boş veya şebeke bağlantısı 99 gösteriyorsa SIM kartında veya servis sağlayıcısında bir problem olabilir. Lütfen başka bir SIM kartıyla aynı işlemleri tekrardan deneyin: **AT+COPS?**

Satın aldığınız cihazın IMEI numarasını ise edevlet üzerinden sorgulayabilirsiniz. (https://www.turkiye.gov.tr/imei-sorgulama ) Bu sorgulama sadece Türkiye için geçerlidir. **IMEI** kayıtlı değil ise lütfen modülleri satın aldığınız firma ile iletişim kurunuz.


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/56.jpg)

Eğer modulün IMEI numarası kayıtlı ise yukarıdaki gibi bir cevap almamız gereklidir.

**Not : Cihaz yurtdışında kullanılacak ise lütfen tarafımıza bildiriniz.**

SIM kartı ve USB testleri bitirildikten sonra aşağıdaki script çalıştırılarak shield ile internete çıkabilirsiniz.



```sh
sudo chmod +x ./pe2a_miniIOEx.sh
sudo ./pe2a_miniIOEx.sh internet ttyUSB3
```

ttyUSB2, Raspberry’nin üzerindeki USB’lerden hangisine bağladığınıza göre değişecektir. ttyUSB’nin yanlış seçilmesi durumunda cihaz internete çıkmayacaktır. Genellikle, Vodafone için default APN **‘internet’** dir. Bulunan ülkeye göre ve servis aldığınız operatöre göre bu değişir. Yanlış APN’de cihaz internete bağlanamaz. Turkcell için APN "mgbs" 'dir. Ayrıntılı bilgiye ekte ulaşılabilir: https://www.turkcell.com.tr/kurumsal/kurumsal-cozumler/statik-ip/sikca-sorulan-sorular

Bu işlemlerden sonra internet bağlantılarını kapatmayı unutmayınız:

```sh
sudo ifconfig eth0 down
sudo ifconfig wlan0 down
```

APN ayarlarından sonra ise aşağıdaki komut ile internete çıkabilirsiniz:

```sh
sudo pppd call gprs
```
Komutun arka planda çalışmasını istiyorsanız aşağıdaki gibi ‘&’ karakterini komut satırına ek yapabilirsiniz. 

```sh
sudo pppd call gprs&
```

**“sudo pppd call gprs”** komutundan sonra aşağıdaki gibi bir ekranla karşılaşmamız gerekmektedir:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/57.jpg)

Eğer cihaz internete çıkmıyorsa “script failed” hatası verecektir. En çok karşılaşılan problemler SIM kartı APN adresinin yanlış olması, PIN kodu, SIM kartın internete çıkmaması, SIM kartın internet hakkının olmaması vs. Dokuman başlarında anlatılan USB testleri ve SIM kart testleri başarılı ise fiziksel olarak modülde bir sıkıntı olmaması gerekir. 
Cihaz internete çıktığında aşağıdaki komutu işleyerek cihazın IP’sine erişebilirsiniz. 

```sh
sudo ifconfig
```

Cihaz internete çıktığında ise eğer internet hızını görmek istiyorsak **speedtest-cli** programı yüklememiz gereklidir. Bu program üzerinden internete çıkış hızımızı görebiliriz. Aşağıda konuyla ilgili örnek ekran görüntüsü bulunmaktadır:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/58.jpg)

## GPS Commissioning ##

MiniIOEx, GPRS bağlantısının yanı sıra GPS konum tabanlı uygulamalar için de kullanılabilir. GPS uydularından alınan konum verisi ve GPS’den gelecek saat uygulamalarda kullanılabilir. Bununla ilgili piyasada birçok uygulamaya rastlamak mümkündür. GPS ve GPRS’de kullanılan antenler farklı olduğundan dolayı aynı antenlerin kullanılması verilerin düzgün alınmamasına veya hiç veri gelmemesine yol açacaktır.

UC20 shield’i üzerinden GPS verileri alındığı için Bölüm 2.1.’de gerçekleştirilen uygulamaların da GPS verilerini alınması için yüklenmesi ve çalıştırılması tavsiye edilir. Özellikle
“lsusb” komutuyla modulün MiniIOEx’e ve Raspberry’ye bağlandığından emin olunmalıdır. En sık karşılaşılan hatalardan bazıları USB adres yolunun yanlış verilmesidir. Bunu da yine “lsusb-v” komutuyla ayrıntılı olarak USB cihazların hangi USB’lere bağlandığını görebilirsiniz.

Bu bölümde GPS verilerinden gelen datalar incelenecektir ve örnek kod paylaşılacaktır. Buna göre işlemlerinizi gerçekleştirebilirsiniz.
GPS antenini Quectel UC20 modulün GNSS konnektörüne bağlanması gerekmektedir. GitHub’dan MiniIOEx-gps.py kodu indirilmesi ve çalıştırılması gerekmektedir. UC20 modüle gönderilen “AT” komutlarını ekteki linkten ihtiyacınıza uygun komutları program üzerinden revize edebilirsiniz. 

Quectel UC20 GNSS AT Komutları Dokuman Linki:
http://www.quectel.com/UploadImage/Downlad/Quectel_UC20_GNSS_AT_Commands_Manual_V1.1.pdf

Program çıktısı aşağıdaki gibi olacaktır:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/59.jpg)

*GNSS Çıktıları*

Program çalıştırıldıktan sonra gelen dataların: UTC Clock,Date,Coordinate gibi işlevleri Raspberry üzerinde kullanılabilir. Yukarıdaki şekilde de görüldüğü üzere koordinat sık sık yer değiştirmektedir. Bundan dolayı kullanıcıların koordinat verilerin daha doğru hesaplanması için bulunan yer üzerindeki koordinatların optimizasyonu gibi fonksiyonları kullanması gerekmektedir. Bu sayede daha kesin sonuç alınması mümkündür. Location coordinate verisini GOOGLE MAPS veri girişini yaptığımızda bulunduğunuz yer yaklaşık olarak ortaya çıkacaktır. UTC clock verisini ise Raspberry CPU saati olarak RTC ile beraber kullanabilirsiniz.

## Real Time Clock and EEPROM  ##

Mikroişlemcilerde yapılan işlemlerde saatin devamlılığı önemlidir. Raspberry’de Real Time Clock (Gerçek Zaman Saati) bulunmadığından dolayı Raspberry’nin enerjisi gittiğinde saatiniz ‘fake’ bir saatte veya en son kaldığınız bir saatte başlayabilir. Bu da yapılacak otomasyon işlerinin zamanın değişmesine yol açar. Örnek olarak her gün 13:00’da bir pompayı çalıştırmanız gerekirse siz bu pompayı normal saatinden 5 saat sonra 18:00’da çalıştırabilirsiniz. Bu gibi sebeplerden dolayı MiniIOEx’e gerçek zaman saati entegre ettik. Zaman saatini kullanabilmek için aşağıdaki adımları takip edebilirsiniz. EEPROM ve RTC i2c üzerinden MiniIOEx ile haberleşmektedir. i2c, birçok cihazdan veri almak ve veri göndermek için oldukça popüler bir haberleşme protokolüdür. Sadece 2 kablo ile yüksek hızlarda veri alıp/göndermek mümkündür. i2c cihazlarını kontrol eden modüle ‘master’, kontrol edilen modüle ise ‘slave’ denir. Her i2c slave cihazın benzersiz bir adresi mevcuttur. Her i2c cihazı aynı SCL(serial clock) ve SDA(serial data) üzerinden haberleşir. i2c protokolü **START** ve **STOP** durumları içererek datanın başlayıp/bittiğini de master cihaza haber verir.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/60.jpg)

Aşağıdaki resimde ise SCL ve SDA’nın BIT tablosunu bulabilirsiniz. SCL, clock olduğu için birbirini takip eden referans sinyaller; SDA ise slave cihazın verisini üretmiştir. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/61.jpg)


Terminalde **raspi-config-> Interface Options-> i2c->Enable** edildikten sonra Raspberry’yi tekrardan başlatmanız önerilir. 

Bu adımları geçtikten sonra terminalde i2cdetect -y 1 veya eski bir Raspberry sürümü kullanıyorsanız i2cdetect -y 0 (en kısa zamanda yeni bir işletim sistemini yüklemeniz önerilir) ile sistemde bulunan i2c cihazlarını görebilirsiniz. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/62.jpg)

MiniIOEx üzerindeki **EEPROM** entegresinin **(24LC512)** unique adresi **0x50**’dir. Bu unique adresi yazılımda da kullanmamız gerekiyor. EEPROM’a, RTC verisi yazılıp Raspberry yeniden başladığında ise buradan RTC verisi okuması yapılabilir veya programınızın kopyalanmasını önleyecek bazı ‘gizli’ şifreler buraya yazılabilir ve yazdığınız program buradan aldığı bilgi ile çalışmaya başlar. Yani bir şekilde Raspberry’nin SD kartı üzerindeki işletim sistemi imaj’ı kopyalansa bile program kullanılamaz olacaktır. 

Aşağıda *.c* koduyla yazılmış örnek program mevcuttur. Bu kodda EEPROM üzerine RTC’den alınan saat verisi yazdırılıp bu veri EEPROM üzerinden okunmuştur. 


```sh
#include <stdio.h>
#include <sys/ioctl.h> // ioctl
#include <fcntl.h>     // open
#include <unistd.h>    // read/write usleep
#include <time.h>
#include <netinet/in.h> // htons
#include <linux/i2c-dev.h>

#pragma pack(1)

#define PAGESIZE 32
#define NPAGES  128
#define NBYTES (NPAGES*PAGESIZE)

#define ADDRESS 0x50  //  24LC512's address on I2C bus 

typedef struct {
    ushort AW;
    char  buf[PAGESIZE+2];
}WRITE;

static WRITE AT = {0};

int main() {
  int fd;
  char bufIN[180] = {0};
  time_t clock=time(NULL);

  snprintf(AT.buf, PAGESIZE+1, "%s: my first attempt to write", ctime(&clock)); //  the buffer to write, cut to 32 bytes

  if ((fd = open("/dev/i2c-1", O_RDWR)) < 0) {  printf("Couldn't open device! %d\n", fd); return 1; }

  if (ioctl(fd, I2C_SLAVE, ADDRESS) < 0)     { printf("Couldn't find device on address!\n"); return 1; }

  AT.AW = htons(32);    //  I will write to start from byte 0 of page 1 ( 32nd byte of eeprom )

  if (write(fd, &AT, PAGESIZE+2) != (PAGESIZE+2)) { perror("Write error !");    return 1; }
  while (1) { char ap[4];  if (read(fd,&ap,1) != 1) usleep(500); else break; } //   wait on write's end 

  if (write(fd, &AT, 2) != 2) {  perror("Error in sending the reading address");    return 1;  }

  if (read(fd,bufIN,PAGESIZE) != PAGESIZE) { perror("reading error\n"); return 1;}
  printf ("\n%s\n", bufIN);

  close(fd);
  return 0;
}


```

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/63.jpg)


