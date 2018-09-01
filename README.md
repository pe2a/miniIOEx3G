
##Table of Contents##

[An Industrial Raspberry Shield: MiniIOEx-3G] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#an-industrial-raspberry-shield-miniioex-3g)

[Who is for MiniIOEx-3G?] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#who-is-for-miniioex-3g)

[What is in the box?] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#what-is-in-the-box-)

[IO Handling] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#io-handling)

[Digital Input] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#digital-input)

[Digital Output] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#digital-output)

[Analog Input] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#analog-input)

[Reading Analog Input Values ]https://github.com/pe2a/miniIOEx3G/blob/master/README.md#miniioex-3g-analog-input-read

[Serial Port] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#seri-port)

[3G / GPS] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#3g--gps)

[GPS Commissioning] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#gps-commissioning)

[RTC and EEPROM Usage] (https://github.com/pe2a/miniIOEx3G/blob/master/README.md#real-time-clock-and-eeprom)




# An Industrial Raspberry Shield: MiniIOEx-3G #

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
- Real time data stream,
- Camera stream via 3G,
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

# IO Handling #

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


## Digital Input ##

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

```python
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

**Important Note**
**If you supply MiniIOEx with 24V, you can use all Digital Output pins. You can only use Relay outputs if you supply directly from Raspberry via 5V USB.**

| Technical Data  	| Digital Output | 
| --- | --- |
| Terminal Connection |	2 kablo |
| Digital Output Relay | 	2ch |
| Digital Output Transistor 	| 2ch |
| Relay Switch Current and Volatge	| 1A,24VDC |
| Transistor Switch Current and Voltage	| 80mA, 24VDC |
| Configuration	| GPIO or bcm2835 library install |

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
**To use the analog input module as a 4-20mA sensor input, the following buttons must be pulled in the direction of ** ON **.**

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
Since the Python library is used, **Raspi-Config -> Interfacing Options -> SPI** *enable* is required.

```python
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

```c
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

## Serial Port ##

Serial communication is a type of communication that operates on software protocols specified in the standard on the physical shell specified in the telecom standards and allows for bi-directional data communication. In industrial systems, RS232 and RS485 protocols generally come to mind in terms of serial communication. MiniIOEx supports RS232 and RS485 physical communication serial paths. RS-232 is a serial communication standard designed for short distance communications. The information transmitted via RX and TX is determined according to the reference level GND. With RS-232, short distances and speeds of 115.2 Kbit / s can be achieved. This standard is not suitable for noisy environments. RS-232 drives are not designed to be able to sustain many receivers at the same time.

UART (*Universal Asynchronous Receiver / Transmitter*) serial bus provides serial communication with two cables on Raspberry as standard. With Raspberry 3, serial port settings can be made on the "raspi-config" screen. Raspberry Pi should be restarted after these changes are made. This document explains how to make these settings. Tx and Rx pins on Raspberry Pi are responsible for serial communication. Raspberry can easily communicate with a device on another serial port hardware. If Raspberry will communicate with another serial port device, "console login" feature should be removed. These changes will also be mentioned.

The RS-485 is a serial transmission developed for use at longer distances, in noisy environments, where higher speeds are required. MiniIOEx-3G also supports these two serial transmission routes.

The serial port PIN table on the MiniIOEx is shared below.

MiniIOEx Seri Port Pin table is given at below:

| Serial Port Pin | MiniIOEx-3G Terminal No | 
| --- | --- |
| RS232-RX	| 19 |
| RS232-TX	| 20 |
| RS485-B	| 19 |
| RS485-A	| 20 |
| Serial GND	| 17 |

Since Raspberry has a single UART output, we use serial port converters in MiniIOEx: UART / RS232 and UART / RS485. You can control a button on MiniIoEx and you can choose which serial port can be used. It should be known RS232 uses three cables and RS485 uses two cables. 

If we can not use these two converters at the same time, we have to make a choice. You can choose according to the serial port you will use as follows: For RS485, you can push upwards the switches, for RS232 you can choose the other direction.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/40.jpg)
*RS485 Selection*

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/41.jpg)
*RS232 Selection*

To change the serial port selection buttons while the serial port terminal is plugged into a device: It may break the integrations on MiniIOex. Therefore, if any serial port is selected, the buttons need to be adjusted in that direction before connecting to the device.

We need to use the Raspberry Pi configuration tool to configure the serial ports. In the terminal, we write ** "raspi-config" **.

```sh
$raspi-config > Interfacing Options > Serial 
```
After pressing the "enter" key on the **"Serial"** menu, follow the steps below.

**On the Login menu, use Serial Port> Off (No)**

If this menu is missed, the program using the serial port will fail when it starts to work. Therefore, in order to use Login, serial port must be closed.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/42.jpg)
*Serial Port Using Login Shell*

**Serial Port Hardware Use -> On / (Yes)**

This menu makes the Raspberry Pi serial port terminals programmable.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/43.jpg)
*Serial Port Hardware Usage*

When all the processes are finished, we need to see a screen like this:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/44.jpg)
*Serial Port Usage Informations*

With the "minicom" program that can run on Raspberry, you can see the variables coming from Raspberry via serial port or give any reference through this program.

If you want to install the Minicom program, you can follow the steps below:

**1. Minicom Install:**

```sh
$sudo apt-get install minicom 
```

**2. Minicom Starting Program**

If you use before Raspberry Pi 3 version, you need to use port adress as being "ttyAMA0". 

```sh
$sudo minicom -b 9600 -o -D /dev/ttyAMA0 
```
If you use  Raspberry Pi 3 version and the others, you need to use port adress as being "ttyS0". 

```sh
$sudo minicom -b 9600 -o -D /dev/ttyS0

```
The 9600 number entered in the parameter is the baudrate rate. You can change this speed according to the standard speeds. Usually this value is also used in 115200. After this process, you can send or receive data to Raspberry by using serial port from any PC or any other device. You can change these settings with the ** "minicom -s" ** parameter.

In this document we will illustrate with practical examples how we can obtain data via **"Entes MPR63 Energy Analyzer"** using RS485 as an example.


## 3G / GPS ##

One of the most important and basic features of the MiniIOEx is that it has a structure that is compatible with 3G and 4G communication. So if you are in a place where Wireless and Ethernet are not available or if work is being done on site, data communication with 3G is the most convenient method. This communication can be fully exploited from the data exchange capacity of 3G since it is realized via USB rather than through serial port. 3G services have been added to the MiniIOEx because some service providers can not provide full performance on 3G services. It is compatible with MiniIOEx-3G, Raspberry V2, V3, Zero devices and software tests have been tested on Jessie and later operating systems. Quectel 3G Module can provide 14.4 Mbps downlink and 5.76 Mbps uplink service. Due to its compact and modular structure, it can be easily used in projects with MiniIOEx-3G. If you did not purchase the MiniIOEx with the 3G module, it will be enough to place only 3G module in your plans in the future.
Where MiniIOEx-3G is available:

- IOT applications,
- Exporting data from another PLC or PC,
- Remote monitoring of industrial machines,
- Real Time Data stream operations,
- Camera stream operations,
- Transferring images via camera etc.

The fact that the MiniIOEx can be fed with 24V is a very useful feature for industrial environments. For an application that consumes too much power and draws instantaneous pulsating currents like 3G, it is very important for the continuity of communication that there is a 24V supply alternative. Many tests and studies have been conducted on this subject. Below are 2 oscilloscope screenshots. These are the graphs of voltage the 3G modem tries to connect to the first internete. As you can see in this chart, there is a voltage drop due to the flow in the red box. This voltage drop has been tried to be kept at the lowest voltage possible. The module does not operate by resetting the module itself at any serious voltage drop because it operates with 3.3V precision supply voltage. Therefore, it was tried to obtain a linear voltage graph at the module feed.


![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/52.jpg)

*Voltage Graph during 3G Module Connection*

As shown in the oscilloscope screen image below, the voltage is steady state even though the data download / upload operations after connecting the internet.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/53.jpg)

*After 3G connection Voltage Graph*

As a result of this work MiniIOEx and 3G module works synchronously and efficiently. In the following chapters, the commissioning of the 3G module is shown. The products listed below are needed to perform these operations.
- USB Cable
- Antenna
- Antenna cable

These products are shipped in the product package when you buy MiniIOEx-3G. There is no need to buy an external material.

## 3G Connection Configuration ##

We can test the Quectel 3G module using the following steps:
1- Fitting on Quectel Modul Shield,
2- Placement of the SIM card on the module,
3- Installation of Raspberry on Shield,
4- Installation of USB cable to Raspberry Pi,
5- Installation of 3G antenna on Quectel UC20 module.
Once the physical module and the Raspberry have been installed, the corresponding 'scripts' can be activated to activate the 3G module. As expected, the 3G module requires a high current source in the internete coupling stage. If this current is not met, the voltage drops and the module resets itself. This topic is about sahada and lab. We did a lot of research / development in our tests. In MiniIOEX and similar 3G products, we have also ensured that this voltage regulator protects our 3G connection more stable.
6- It is recommended to operate the latest operating system on the operating system. The Minicom program displays the data received from the serial port sockets for SIM card and the Module tests. For **speedtest-cli**, you can also use the device's internete connection speed for testing purposes.

Relevant examples are given in the text.

- sudo apt-get update
- sudo apt-get minicom
- sudo apt-get speedtest-cli
- sudo apt-get rpi-update
- sudo apt-get upgrade
- sudo reboot
- git clone git: //github.com/pe2a/miniIOEx3G.git

After the installation is finished, the terminal is opened and the **lsusb** command is executed. This command then shows the devices connected to the USB. If there is no situation, you should see a screen like below. If we can not see Quectel UC20 Module, it could be the Quectel UC20 module or the USB cable itself. For this situation, It may be beneficial to insert and remove the module. 

**Important Note**
**Installation work on the module should be done without energy**

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/54.jpg)

*Ekranda görülen diğer USB portları kablosuz klavye/mouse veya taşınabilir USB disk olabilir.*

Fiziksel olarak USB bağlı olduğuna göre minicom üzerinde yapılacak setup ayarları ile ATkomutları modüle gönderebiliriz. Minicom ayrı bir terminalde açılarak aşağıdaki adresten miniIOEx-3G-test.py dosyası çalıştırılarak AT komutları cevapları görülebilir. Bu cevaplar aşağıda açıklanacaktır. AT komutları 3G modül ile haberleşmeden kullanılır. Bu komutlar ile cihaz üzerindeki bilgilerin sorgulanabileceği gibi SMS, Arama gibi özellikler de bu komutlar sayesinde gerçekleştirilebilir.

* Other USB ports on the screen can be wireless keyboard / mouse or portable USB disk. *

Since MiniIOEx-3G physically connected to USB, we can send the **AT** commands.  AT commands can be used communicating with the 3G module. With these commands, the information on the device can be queried as well as features such as SMS and Search can be performed by these commands. Just write these commands on the Minicom. 

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/55.jpg)

The description of the basic AT commands in the red block is given below:

1-) Quectel device serial number -> ** ATI **

2-) Indicates that the Sim card is ready for use if there is no problem with Sim Lock on the device. You can disable the SIM card PIN feature on any mobile phone if you have just bought a SIM card: **AT + CPIN?**

3-) Indicates whether the network is ready or not. If the network is not ready, you can return the CME Error  and see what error it is on the following document: **AT + CREG?**

4-) The net capacity of the net. This ratio changes according to the quality of the antenna, the proximity of the base station and the environmental factors. Below 30 is acceptable. 99.99 indicates no network capture: **AT + CSQ**

5-) Shows the operator of the SIM card on the card. Vodafone SIM card was used during the tests. Turk Telekom or Turkcell'te IOT compatible SIM card is produced. If the SIM card is empty or shows the network connection 99 here, there may be a problem on the SIM card or the service provider. Please try the same process again with another SIM card: **AT + COPS?**

You can also inquire about the IMEI number of the device you have purchased through the municipality. **This question applies only to Turkey.** If IMEI is not registered, please contact the company where you purchased the modules.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/56.jpg)

If the module's IMEI number is registered, we need to get an answer as above.

**Important Note: Please inform us if the device will be used abroad.**

After completing the SIM card and USB tests, you can connect to the internet by running the following script.

```sh
sudo chmod +x ./pe2a_miniIOEx.sh
sudo ./pe2a_miniIOEx.sh internet ttyUSB3
```
The **ttyUSB3** address will change according to what you connect to the USB on Raspberry. If ttyUSB is incorrectly selected, the device will not be connect internet. Usually, the default APN for Vodafone is **'internet'**. This depends on the country you are located in and the operator you are servicing. The device can not connect internet on the wrong APN. For Turkcell, the APN may be **"mgbs"**. Detailed information can be reached at: https://www.turkcell.com.tr/kurumsal/kurumsal-cozumler/statik-ip/sikca-sorulan-sorular

Do not forget to close the internet connections after this:

```sh
sudo ifconfig eth0 down
sudo ifconfig wlan0 down
```
After the APN settings, you can connect to the internet with the following command:

```sh
sudo pppd call gprs
```
If you want the program backplane to work, you can add '&' to the command line as follows.

```sh
sudo pppd call gprs&
```

After the **"sudo pppd call gprs"** command, you should see a screen like this:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/57.jpg)

If the device does not connect internet, it will give a "script failed" error. The most common problems are that the APN address of the SIM card is incorrect, the PIN code is insufficient, etc. You can access the IP of the device by executing the following command on the device internete.

```sh
sudo ifconfig
```
If you want to see internet speed, ** speedtest-cli ** program should be installed. Through this program, we can see the speed of the international exit. Below is a sample screenshot of the relevant topic:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/58.jpg)

## GPS Commissioning ##

The MiniIOEx can be used for GPRS-based applications as well as for GPRS connectivity. Location data from GPS satellites and hours from GPS can be used in applications. It is possible to encounter many applications in the related market. Since the antennas used in GPS and GPRS are different, using the same antennas will result in incorrect reception or no data at all.

Be sure to connect to the module MiniIOEx and Raspberry via the **"lsusb"** command. Some of the most common mistakes are misdirecting the USB address path. You can also see this in detail via the **"lsusb-v"** command which USB devices are connected to which USB.

In this section, the data from the GPS data will be examined and the sample code will be shared. You can then perform your actions accordingly. **The GPS antenna needs to be connected to the Quentel UC20 modular GNSS connector.** You need to download and run MiniIOEx-gps.py from GitHub. You can revise the "AT" commands sent in UC20 mode through the program according to the commands you need from the link on the right.

Quectel UC20 GNSS AT Commands Document link:
http://www.quectel.com/UploadImage/Downlad/Quectel_UC20_GNSS_AT_Commands_Manual_V1.1.pdf

The output of the program will be as follows:

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/59.jpg)

*GNSS Outputs*

Functions that come after the program has been run: UTC Clock, Date, Coordinate, etc. can be used on Raspberry Pi. As you can see above, the coordinates change often. Therefore, users need to use functions such as optimizing coordinates on the ground for more accurate calculation of coordinate data. It is possible to get a more accurate result on this view. When you do the GOOGLE MAPS data entry in the location coordinate data, the place you are about will appear. UTC clock data also can be used with RTC as Raspberry Pi CPU clock and of course you can write that UTC Clock to EEPROM on MiniIOEx. 

## Real Time Clock and EEPROM  ##

In microprocessors, it is important that the clock is continuous. Since the Raspberry Pi does not have a Real Time Clock, your clock can start at 'fake' one hour or the last one you have when the energy of Raspberry Pi goes out. This leads to time-consuming changes in automation. For example, if you need to start an engine every day at 13:00, you can operate this pump at 18:00 after 5 hours of normal time. For such reasons we have integrated the real time clock into the MiniIOEx-3G. To use the time clock, you can follow the steps below. 

EEPROM and RTC communicate with MiniIOEx-3G via i2C. i2C is a popular communication protocol for receiving and sending data from many devices. It is possible to send / receive data at high speed with only 2 wires. The module that controls I2C devices is called 'master' and the module that is controlled is called 'slave'. Each i2c slave device has a unique address. Each i2C device communicates over the same serial clock (SCL) and serial data (SDA). The i2c protocol includes the states **START** and **STOP** to inform the master device whether the data starts or ends.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/60.jpg)

In the picture below, you can find the BIT chart of SCL and SDA. SCL is a clock, consecutive reference signals; SDA produced the data of the slave device.

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/61.jpg)

In the terminal **raspi-config-> Interface Options-> i2c-> Enable** then it is recommended to start Raspberry Pi reboot. To access the I2C devices, you can run terminal command that **i2cdetect -y 1**. For older Raspberry Pi version, it shall be **i2cdetect -y 0**

![Image of MiniIOEx-3G](https://github.com/pe2a/miniIOEx3G/blob/master/doc/images/62.jpg)

The ** EEPROM ** on MiniIOEx **(24LC512)** unique address is **0x50**. We also need to use this unique address in the software. If RTC data is written to EEPROM and Raspberry Pi is restarted, RTC data can be read from EEPROM, or some 'secret' passwords can be written to EEPROM. 

Below is a sample program written in *.c*. In this code, clock data from RTC is printed on EEPROM and this data is read through EEPROM.

```c
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


